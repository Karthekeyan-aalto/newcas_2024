"""
Created by Karthekeyan Periasamy
Created on Jan 18 09:21 AM
"""
from Operators.Port.Port import Port
from HWDescription.Operators.LUTs.LUTVHDLDescription import LUTVHDLDescription 

class LUT ():
    """
    This class is the base class for any type of LUT that will be constructed
    The purpose of this class is to hold the basic properties of any LUT including the HWDescription and HW Simulation object
    For now, the HWSimulation object will not be implemented in the coming versions it will be implemented
    As LUT is an opertor and is part of AutoPC, it will follow the connect, configure, perform or process, reset process
    The idea of the four step process may not be intiutive, but it allows any package and its associated modules to be configured
    separately and tested accordingly.

    **However many other packages and modules in AutoPC are not made based on the four step process. Its lack of thought process which
    went through while desgning those modules. So, it will be changed in the future and is recommended to follow the four step process
    """

    def __init__(self):
        # connect the necessary packages
        self.connectHWDescriptionPackage()

        # dictionary to store the configuration details, which then will be used by the configure function to set the
        # properties of the LUT
        self.configurationDetailsOfLUT = dict()

        # property to store the number system
        # the number system property will be used the HW Description objects to generate appropriate VHDL syntax
        self.numberSytem = None

        # property to store the name of the LUT
        self.name = None

        # property to store the number system name
        # the name of the number system will be retreived from the configuration details
        # the custom getter and setters are used to use the number system name and set the corresponding number system
        self._numberSystemName = None

        # an array to store the number of input data ports of the LUT
        # for the current LUT, our requriement is only input data port
        # this data port list or array will have port objects that
        self.inputDataPorts = None

        # property to store the clock port
        self.clockPort = None

        # property to store the reset port
        self.resetPort = None

        # property to store the output data port
        # this property is an array that will store the number of output ports for a HW entity
        # for now the LUT will have only one output port
        # the output port will be a bus
        self.outputPorts = None

        # operational frequency of the LUT
        # for now, the LUT is not clock synchornised
        # its just a combinational block.
        self.frequency = None

        # property to store the numberOfBits
        # the number of bits will be used to configure the LUT numberOfBits
        # for an LUT the number of bits would be appropriate based on the input and output ports
        # the input port and output port number of bits will be configured using the configuration details
        self.numberOfBits = None

        # property to store the software map of the LUT in the form of a dictionary
        # the key is the input and the value is the output
        self.pythonLUT = None

        # proeprty to store the required mantissaBits if the numberSystem is of Float
        self.mantissaBits = None

        # property to store the required exponent Bits if the number system is of Float
        self.exponentBits = None

        
    @property
    def numberSystemName(self):
        return self._numberSystemName

    @numberSystemName.setter
    def numberSystemName(self,value):
        self._numberSystemName = value
        # check the name and set the number system number accordingly
        # 0 is the integer for Fixed system
        # 1 is the integer for Float System
        # 2 is the integer for Posit System
        if self._numberSystemName == "Fixed":
            self.numberSystem = 0
        elif self._numberSystemName == "Float":
            self.numberSystem = 1
        elif self._numberSystemName == "Posit":
            self._numberSystem = 2
        elif self._numberSystemName == None:
            # when the numberSystemName is none, it means the numberSystem cannot be set
            # and is invalid.
            self._numberSystem = -1


    
    def generateLUT(self):
        """
        Function to generate a LUT based on the number of bits set
        The number of bits of input data ports will be mapped
        with number of bits of the output port. Here the top input port
        and top output port from the ports array will be used to generate the LUT
        
        Return: The function will return a dictionary which then can be used by the
        HWDescription package to generate appropriate HW architecture using the behaviour dictionary

        *For now, we have generation of LUT when the input is one bit (either 0 or 1) and the output LUT or dictionary can only represent 0 and not 1
        """
        #print("LUT generateLUT function")
        inputPort = None
        outputPort = None

        # check whether there is a top input port 
        if self.inputDataPorts[0] != None:
            # access the top input port
            port = self.inputDataPorts[0]
            # set the port to the inputPort
            inputPort = port

        outputPort = None
        # check whether there is a top output port 
        if self.outputPorts[0] != None:
            # access the top output port
            port = self.outputPorts[0]
            # set the port to the inputPort
            outputPort = port

        # access the number of bits of the inputPort
        numberOfBits = inputPort.numberOfBits

        # check if the numberOfBits is 1 or not
        if numberOfBits == 1:
            # access the output port bits
            outputPortBits = outputPort.numberOfBits
            if outputPortBits == self.numberOfBits:
                # generate zero string for the number of bits
                zeroString = self.generateZeroString()
                # update the python LUT
                self.pythonLUT["0"] = zeroString
                self.pythonLUT["OTHERS"] = self.generateHyphenString()
        else:
             return
    
    
    def generateZeroString(self):
        """
        Function to generate a 4 bit zero 
        """
        zeroString = str()
        for zero in range(0,self.numberOfBits):
            zeroString = zeroString + "0"
            
        return zeroString
        
    def generateHyphenString(self):
        """
        Function to generate hyphen string based on the number of bits 
        """
        hyphenString = str()
        for hyphen in range(0,self.numberOfBits):
            hyphenString = hyphenString + "-"
            
        return hyphenString

    def connectHWDescriptionPackage(self):
        # connect the HWDescription Package
        self.hwDescription = LUTVHDLDescription()
    
    def configure(self):
        """
        This function will be called from outside of the class itself.
        The main purpose of this funciton to receive information via the configuraiton dictionary
        Use the information from the configurartion dictionary to set the properties of the LUT object or configuring itself.
        """
        if self.configurationDetailsOfLUT == None:
            print("The object is not configured and the behaviour of the object cannot be guaranteed")
            return

        configurationDetails = self.configurationDetailsOfLUT
        print("LUT configurationDetails", configurationDetails)

        # initialise the software LUT dictionary
        self.pythonLUT = dict()
        # intialise the inputDataPorts array
        self.inputDataPorts = list()
        # intialise the outputPorts array
        self.outputPorts = list()

        # check the configuration details has number system key or not
        if "NumberSystem" in configurationDetails:
            # access the number system information
            # set it to the number system variable
            self.numberSystemName = configurationDetails["NumberSystem"]
            
        # check the configuration details of the number of bits
        if "NumberOfBits" in configurationDetails:
            self.numberOfBits = configurationDetails["NumberOfBits"]
            

        # check the configuration details of the name
        if "Name" in configurationDetails:
            self.name = configurationDetails["Name"]

        # check the configuration details contains input data ports
        if "InputDataPorts" in configurationDetails:

            # access the ports and set the details of the port
            # the value of the key is expected to be an array
            portDetails = configurationDetails["InputDataPorts"]
            #print("LUT InputDataPorts", portDetails)
            for portDetail in portDetails:
                # access the information about the port or use the configuration details property to configure itself
                newPort = Port()
                newPort.configurationDetails = portDetail
                # configure the port
                newPort.configure()
                # process the port
                newPort.process()
                # once the port is configured, add the port to the InputDataPorts array
                self.inputDataPorts.append(newPort)


        # check the configuration details contains output port details
        if "OutputPorts" in configurationDetails:
            # access the ports and set the details of the port
            # the value of the key is expected to be an array
            portDetails = configurationDetails["OutputPorts"]
            for portDetail in portDetails:
                # access the information about the port or use the configuration details property to configure itself
                newPort = Port()
                newPort.configurationDetails = portDetail
                # configure the port
                newPort.configure()
                # process the port
                newPort.process()
                print("Add the output port")
                # once the port is configured, add the port to the output array
                self.outputPorts.append(newPort)
            
        
        # check the configuration details contains clock port details
        if "InputClockPort" in configurationDetails:
            # access the ports and set the details of the port
            # the value of the key is expected to be a dict
            clockPortDetail = configurationDetails["InputClockPort"]
            # access the portDetail frequency
            # it is expected to have single frequency for the clock port
            # also, only one clock port is possible
            # access the information about the port or use the configuration details property to configure itself'
            newPort = Port()
            newPort.configurationDetails = clockPortDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            # once the port is configured, set the port
            self.clockPort = newPort
            
        
        
        # check the configuration details contains reset port or not
        if "InputResetPort" in configurationDetails:
            # access the ports and set the details of the port
            # the value of the key is expected to be a dict
            resetPortDetail = configurationDetails["InputResetPort"]
            # access the reset port detail
            # only one reset port is possible
            # access the information about the port or use the configuration details property to configure itself'
            newPort = Port()
            newPort.configurationDetails = resetPortDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            # once the port is configured, set the port
            self.resetPort = newPort

                
    def process(self):
        # process the input based on the LUT definition by calling the __generateLUT function
        self.generateLUT()

        # configure the HWDescription package
        self.configureHWDescriptionPackage()

        # process the HWDescription package
        self.processHWDescriptionPackage()

            

    def configureHWDescriptionPackage(self):
        # set the luts generics of the hwDescription of LUT
        lutGenerics = dict()
        if self.numberOfBits != None:
            lutGenerics["numberOfBits"] = self.numberOfBits

        # set the lut generics
        self.hwDescription.configurationDetailsOfHWGenerics = lutGenerics

        # changing the configuration of LUT based on the new HW Description

        configurationDetailsOfHW = dict()
        configurationDetailsOfHW = {"Name":self.__class__.__name__,"PythonHWEntity":{"Name":self.__class__.__name__,"InputDataPorts":[self.inputDataPorts],"OutputPorts":[self.outputPorts],"InputClockPort":self.clockPort,"InputResetPort":self.resetPort},"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":lutGenerics},"PythonHWArchitecture":{"Name":self.__class__.__name__,"HWArchitectureTypeName":"RTL","InputDataPorts":[inputPort], "OutputDataPorts":[outputPort], "InputClockPort":clockPort, "InputResetPort":resetPort},"PythonHW":self.pythonLUT}
        
        self.hwDescription.configurationDetailsOfHW = configurationDetailsOfHW

        # generate HW description of LUT using the hwDescription object
        self.hwDescription.configure()
        
    
    def processHWDescriptionPackage(self):
        # process hwDescription
        self.hwDescription.process()

    def reset(self):
        # reset the hwDescription package
        self.hwDescription = None
        # reset the inputDataPorts
        self.inputDataPorts = None
        # reset the output ports
        self.outputPorts = None
        # reset the clock port
        self.clockPort = None
        # reset the reset port
        self.resetPort = None

    def main(self):
        # process the LUT
        self.process()


    def run(self):
        self.main()

