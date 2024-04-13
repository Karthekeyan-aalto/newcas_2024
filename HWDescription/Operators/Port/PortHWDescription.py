"""
Created by Karthekeyan Periasamy
Edited on Jan 20, 09:52
"""

class PortHWDescription():

    def __init__(self):
        self.connect()
    
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
    def hwLanguageName(self):
        return self._hwLanguageName

    @hwLanguageName.setter
    def hwLanguageName(self,value):
        """
        The setter of hwLanguageName is customised, so using the hwLangageName property
        We can set the hwLanguageType accordingly
        """
        self._hwLanguageName = value
        # check the hwLanguage name is VHDL or Verilog
        if self._hwLanguageName == "VHDL":
            self._hwLanguageType = 1
        elif self._hwLanguageName == "Verilog":
            self._hwLanguageType = 2

    @property
    def portType(self):
        return self._portType

    @portType.setter
    def portType(self,value):
        self._portType = value
    
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
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
            self.portType = 1
        elif self._portTypeName == "Output":
            self.portType = 2
        elif self._portTypeName == "Weight":
            self.portType = 3

    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        # property to store the name
        self._name = None
        # property to store the porty type
        self._portType = None
        # property to store the port type name
        self._portTypeName = None
        # property to store the configurationDetails of HW Port
        self.configurationDetailsOfHWPort = None
        
        # property to store hwLanguageName which the port needs to be described
        self._hwLanguageName = None

        # property to store the hwlanauge type
        # the default value is -1, meaning no hw language support
        self.hwLanguageType = -1
        
        # number of bits the port will take as input or output based on the port type
        self._numberOfBits = None
                
        # property to store the mantissa bits
        self.mantissaBits = None

        # property to store the es bits
        self.esBits = None

        # property to store the exponentBits
        self.exponentBits = None

        # property to store the flopocoBits
        self.flopocoBits = None
        
        self.constantSignalValue = None

        # property to store the expectedPort Data
        # this expectedPort Data is set only for weight based ports, where the weights are not transferred from memories
        self.signalData = None




    def configure(self):
        #  check is there any configuration details to set the properties of the port
        if self.configurationDetailsOfHWPort == None:
            return

        # set the configuration details to a local variable
        configurationDetails = self.configurationDetailsOfHWPort
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
        
        if "FlopocoBits" in configurationDetails:
            self.flopocoBits = configurationDetails["FlopocoBits"]

        if "ConstantSignalValue" in configurationDetails:
            self.constantSignalValue = configurationDetails["ConstantSignalValue"]
        
        if "SignalData" in configurationDetails:
            # extract the data value and set it as portData
            self.signalData =  configurationDetails["SignalData"]

        # check the number of bits is available in configuration details
        if "HWLanguageName" in configurationDetails:
            self.hwLanguageName = configurationDetails["HWLanguageName"]
        

    def reset(self):
        self.resetProperties()
    
    def resetProperties(self):
        # property to store the name
        self._name = None
        # property to store the porty type
        self._portType = None
        # property to store the port type name
        self._portTypeName = None

        # property to store the configurationDetails of HW Port
        self.configurationDetailsOfHWPort = None
        
        # property to store hwLanguageName which the port needs to be described
        self._hwLanguageName = None

        # property to store the hwlanauge type
        # the default value is -1, meaning no hw language support
        self.hwLanguageType = -1
        
        # number of bits the port will take as input or output based on the port type
        self._numberOfBits = None
                
        # property to store the mantissa bits
        self.mantissaBits = None

        # property to store the es bits
        self.esBits = None

        # property to store the exponentBits
        self.exponentBits = None
        
        # property to store the flopocoBits
        self.flopocoBits = None

        self.constantSignalValue = None

        # property to store the expectedPort Data
        # this expectedPort Data is set only for weight based ports, where the weights are not transferred from memories
        self.signalData = None
        
        # property to know whether the port in HW is a bus or not
        self.isPortABus = None

    
    def process(self):
        pass

    def perform(self):
        pass

    def main (self):
        pass

    def run(self):
        pass

