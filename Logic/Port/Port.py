"""
Created by Karthekeyan Periasamy
Created on Jan 18 15:47
"""

from HWDescription.Logic.Port.PortVHDLDescription import PortVHDLDescription

class Port ():
    """
    This class will be the new sample Port class
    The older Ports on Operations and PCSystem are not really serving the purpose as the system became complex
    This new port class will redefine the attributes of the Port and even support its own HW Description
    Ofcourse, Port object cannot be siumulated and so it cannot support HWSimulation
    """

    def __init__(self):
        # connect the necessary packages
        self.connect()

    """
    Custom Getters and Setters for object attributes
    """

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if self._name != value:
            # there is a name change happeining
            if self._name != None:
                #name is updated, but if value is set to none
                if value == None:
                    # reset the HW Description of the port
                    self.resetHWDescriptionPackage()
                    self._name = value
                else:
                    # reset the HW Description of the port
                    self.resetHWDescriptionPackage()
                    # set the new name or the updated name
                    #print("HW Port Name Being Updated")
                    self._name = value
                    # update the name in the configuration details dictionary
                    self.configurationDetails["Name"] = self._name
                    # process HWDescription Package 
                    self.processHWGeneration()
                    # perform HWDescription package
                    self.performHWGeneration()

            
            elif self._name == None:
                # name is being set
                self._name = value

        self._name = value


    @property
    def portTypeName(self):
        return self._portTypeName

    @portTypeName.setter
    def portTypeName(self,value):
        """
        The setter of PortTypeName is customised, so using the portTypeName property
        We can set the portType accordingly
        """
        self._portTypeName = value
        # check the portType name is Input or Output
        if self._portTypeName == "Input":
            self._portType = 1
        elif self._portTypeName == "Output":
            self._portType = 2
        elif self._portTypeName == "Weight":
            self._portType = 3

       
    @property
    def isPortABus(self):
        return self._isPortABus

    @isPortABus.setter
    def isPortABus(self,value):
        self._isPortABus = value

    @property
    def numberOfBits(self):
        return self._numberOfBits

    @numberOfBits.setter
    def numberOfBits(self,value):
        self._numberOfBits = value
        # check if the number of bits are greater than 1 or not
        if self._numberOfBits > 1:
            #set if the vhdlPort is a bus or not
            self.isPortABus = True
        elif self._numberOfBits == 1:
            self.isPortABus = False
        else:
            self.isPortABus = False
    
    @property
    def portType(self):
        return self._portType

    @portType.setter
    def portType(self,value):
        self._portType = value

    """
    Object Function Definitions
    """
    def connect(self):
        self.connectProperties()
        self.connectHWDescriptionPackage()
        
    
    def connectProperties(self):
        
        # property to store the configuraiton details of the port
        self.configurationDetails = None

        # property to store the name of the port
        self._name = None

        # property to know whether the port is input or output
        # 1. port is a input type port
        # 2. port is a output type port
        # by default the portType is 1
        self._portType = 1

        # property to store the portType name
        # using the we can override the setters of portType name and set the port type accordingly
        self._portTypeName = None

        # number of bits the port will take as input or output based on the port type
        self._numberOfBits = None
        
        # property to store the expectedPort Data
        # this expectedPort Data is set only for weight based ports, where the weights are not transferred from memories
        self.portData = None
        
        # property to store the mantissa bits
        self.mantissaBits = None

        # property to store the es bits
        self.esBits = None

        # property to store the exponentBits
        self.exponentBits = None

        # property to store the flopocoBits
        self.flopocoBits = None
        
        # property to know whether the port in HW is a bus or not
        self.isPortABus = None
        
        #property to store the port constant data
        self.portConstantData = None




    def connectHWDescriptionPackage(self):
        # connect the hwDescription package to generate VHDL definitions of a port
        self.hwDescription = PortVHDLDescription()


    def configure(self):
        #  check is there any configuration details to set the properties of the port
        if self.configurationDetails == None:
            return

        # set the configuration details to a local variable
        configurationDetails = self.configurationDetails
        #print("Port ConfigurationDetails", configurationDetails)
        
        # check the name of the port is in configuration details
        if "Name" in configurationDetails:
            self.name = configurationDetails["Name"]

        if "PortType" in configurationDetails:
            self.portTypeName = configurationDetails["PortType"]

        # check the number of bits is available in configuration details
        if "NumberOfBits" in configurationDetails:
            self.numberOfBits = configurationDetails["NumberOfBits"]


        if "MantissaBits" in configurationDetails:
            self.mantissaBits = configurationDetails["MantissaBits"]


        if "ExponentBits" in configurationDetails:
            self.exponentBits = configurationDetails["ExponentBits"]

        if "EsBits" in configurationDetails:
            self.esBits = configurationDetails["EsBits"]
                        
        if "SignalData" in configurationDetails:
            # extract the data value and set it as portData
            self.portData =  configurationDetails["SignalData"]
            
        if "ConstantSignalValue" in configurationDetails:
            # extract the data value and set it as portData
            self.portConstantData =  configurationDetails["ConstantSignalValue"]


    def processHWGeneration(self):
        # configure the hwDescription object
        self.hwDescription.configurationDetailsOfHWPort = self.configurationDetails
        # configure the hwDescription
        self.hwDescription.configure()
        # configure the hwDescription object
        self.hwDescription.process() 

            
    def process(self):
        """
        Process function of a port is mostly to generate VHDL Description
        In future we can also generate Verilog Description
        """
        # process the HWGeneration
        self.processHWGeneration()

    def perform(self):
        self.performHWGeneration()

    def performHWGeneration(self):
        self.hwDescription.perform()

    def reset(self):
        self.resetProperties()
        self.resetHWDescriptionPackage()

    
    
    def resetProperties(self):        
        # property to store the configuraiton details of the port
        self.configurationDetails = None

        # property to store the name of the port
        self._name = None

        # property to know whether the port is input or output
        # 1. port is a input type port
        # 2. port is a output type port
        # by default the portType is 1
        self._portType = 1

        # property to store the portType name
        # using the we can override the setters of portType name and set the port type accordingly
        self._portTypeName = None

        # number of bits the port will take as input or output based on the port type
        self._numberOfBits = None

        # property to store hwLanguageName which the port needs to be described
        self._hwLanguageName = None

        # property to store the hwlanauge type
        # the default value is -1, meaning no hw language support
        self.hwLanguageType = -1
        
        # property to store the expectedPort Data
        # this expectedPort Data is set only for weight based ports, where the weights are not transferred from memories
        self.portData = None
        
        # property to store the mantissa bits
        self.mantissaBits = None

        # property to store the es bits
        self.esBits = None

        # property to store the exponentBits
        self.exponentBits = None
        
        # property to store the flopocoBits
        self.flopocoBits = None
        
        # property to know whether the port in HW is a bus or not
        self.isPortABus = None

        #property to store the port constant data
        self.portConstantData = None


    
    def resetHWDescriptionPackage(self):
        # connect the hwDescription package to generate VHDL definitions of a port
        self.hwDescription = PortVHDLDescription()



    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()
