"""
Created by Karthekeyan Periasamy
Edited on Mar14 18 16:47 AM
"""
from Logic.Port.Port import Port

class Logic ():
    """
    This class is the base class for any type of Logic that will be constructed
    The purpose of this class is to hold the basic properties of any Logic but not including the HWDescription and HW Simulation object
    
    As Logic is part of AutoPC, it will follow the connect, configure, perform or process, reset process
    The idea of the four step process may not be intiutive, but it allows any package and its associated modules to be configured
    separately and tested accordingly.

    **However many other packages and modules in AutoPC are not made based on the four step process. Its lack of thought process which
    led that disaster happen while desgning those modules. So, it will be changed in the future and is recommended to follow the four step process
    """

    def __init__(self):
        self.connect()
    

    def connect(self):
        self.connectProperties()


    def connectProperties(self):
        # dictionary to store the configuration details, which then will be used by the configure function to set the
        # properties of the Logic
        self.configurationDetailsOfLogic = dict()

        # property to store the number system
        # the number system property will be used the HW Description objects to generate appropriate VHDL syntax
        self._numberSytem = None

        # property to store the name of the LUT
        self.name = None
        
        #property to store the number or identity number of the operator
        self._number = None

        self._numberSystem = None

        # property to store the number system name
        # the name of the number system will be retreived from the configuration details
        # the custom getter and setters are used to use the number system name and set the corresponding number system
        self._numberSystemName = None

        # an array to store the number of input data ports of the LUT
        # for the current LUT, our requriement is only input data port
        # this data port list or array will have port objects that
        self.inputDataPorts = None
        
        # property to know that input data ports are updated or not
        # this property can be used to achieve the event driven architectures
        # however, for now, as the inputDataPorts property is not observable, we use this set and update mechanisms to update the inputdataports of an operator is updated
        # the vhdl description of the operator should be updated
        self._isInputDataPortsModified = False


        # like the input data ports, output port when set to that it is modified.
        # Should be used to updated the VHDL Description of the operator itself
        # the outputPorts property is not observable for now, and it will updated by the object whoever modifies the output ports information
        self._isOutputPortsModified = False

        # property to store the clock port
        self.clockPort = None

        # property to store the reset port
        self.resetPort = None

        #property to store the enable port
        self.enablePort = None


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

        # proeprty to store the required mantissaBits if the numberSystem is of Float
        self.mantissaBits = None

        # property to store the required exponent Bits if the number system is of Float
        self.exponentBits = None

        # property to store the required es Bits if the number system is posit
        self.esBits = None

        # property to store the pythonHW that contains the core process or architecture description of the logic
        self.pythonHWLogic = None
        
        # property to store the pythonHW generics dictionary for the logic
        self._pythonHWLogicGeneric = None

        # property to store info of the inputDataPorts as dictionary
        self.inputDataPortsInfo = dict()


        # property to store the info of the output ports as dictionary
        self.outputPortsInfo = dict()

        self.flopocoBits = 2




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
            self.numberSystem = 2
        elif self._numberSystemName == None:
            # when the numberSystemName is none, it means the numberSystem cannot be set
            # and is invalid.
            self.numberSystem = -1
            return
        
        # check if the name of the operator is set or not
        # if yes, append the name of the operator
        #if self.name != None:
            #self.name = self.name + self._numberSystemName

    @property
    def numberSystem(self):
        return self._numberSystem

    @numberSystem.setter
    def numberSystem(self,value):
        self._numberSystem = value
        # check the number system name, if its present or not 
        # 0 is the integer for Fixed system
        # 1 is the integer for Float System
        # 2 is the integer for Posit System
        if self._numberSystemName == None:
            if self._numberSystem == 0:
                self._numberSystemName = "Fixed"
            elif self._numberSystem == 1:
                self._numberSystemName = "Float"
            elif self._numberSystem == 2:
                self._numberSystemName = "Posit"
            
            # check if the name of the operator is set or not
            # if yes, append the name of the operator
            if self.name != None:
                self.name = self.name + self._numberSystemName

    
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self,value):
        self._number = value
        
        # check if the name of the operator is set or not
        # if yes, append the name of the operator
        #if self.name != None:
            #self.name = self.name + "_" + str(self.number)
    
    @property
    def isInputDataPortsModified(self):
        return self._isInputDataPortsModified
    
    @isInputDataPortsModified.setter
    def isInputDataPortsModified(self,value):
        self._isInputDataPortsModified = value

        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
    
    
    
    @property
    def isOutputPortsModified(self):
        return self._isOutputPortsModified
    
    @isOutputPortsModified.setter
    def isOutputPortsModified(self,value):
        self._isOutputPortsModified = value

        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
    
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value
        
        # check if the name 
        #if self.numberSystemName != None:
            #self._name = self._name + self.numberSystemName

        # check if the number is not none
        #if self.number != None:
            #self._name = self._name + "_" + str(self.number)
        
      
    @property
    def pythonHWLogicGeneric(self):
        if self._pythonHWLogicGeneric == None:
            self._pythonHWLogicGeneric = dict()
            if self.numberSystem > -1 :
                if self.numberSystem == 0:
                    self._pythonHWLogicGeneric["NumberOfBits"] = self.numberOfBits
                elif self.numberSystem == 1:
                    self._pythonHWLogicGeneric["MantissaBits"] = self.mantissaBits
                    self._pythonHWLogicGeneric["ExponentBits"] = self.exponentBits
                    self._pythonHWLogicGeneric["FlopocoBits"] = self.flopocoBits
                elif self.numberSystem == 2:
                    self._pythonHWLogicGeneric["NumberOfBits"] = self.numberOfBits
                    self._pythonHWLogicGeneric["EsBits"] = self.esBits
        return self._pythonHWLogicGeneric

    @pythonHWLogicGeneric.setter
    def pythonHWLogicGeneric(self,value):
        self._pythonHWLogicGeneric = value


        
    def configure(self):
        """
        This function will be called from outside of the class itself.
        The main purpose of this funciton to receive information via the configuraiton dictionary
        Use the information from the configurartion dictionary to set the properties of the object or configuring itself.
        """
        if self.configurationDetailsOfLogic == None:
            print("The object is not configured and the behaviour of the object cannot be guaranteed")
            return

        configurationDetails = self.configurationDetailsOfLogic
        #print("Logic configurationDetails", configurationDetails)

         # intialise the inputDataPorts array
        self.inputDataPorts = list()
        # intialise the outputPorts array
        self.outputPorts = list()

        # check whether a number is given for the operator or not
        if "Number" in configurationDetails:
            self.number = configurationDetails["Number"]

        # check the configuration details has number system key or not
        if "NumberSystem" in configurationDetails:
            # access the number system information
            # check whether the number system value is a string or int
            if type(configurationDetails["NumberSystem"]) == int:

                # set it to the number system variable
                self.numberSystem = configurationDetails["NumberSystem"]
            elif type(configurationDetails["NumberSystem"]) == str:
                # set it to the number system variable
                self.numberSystemName = configurationDetails["NumberSystem"]
            
        # check the configuration details of the number of bits
        if "NumberOfBits" in configurationDetails:
            self.numberOfBits = configurationDetails["NumberOfBits"]
            
        if "MantissaBits" in configurationDetails:
            self.mantissaBits = configurationDetails["MantissaBits"]

        if "ExponentBits" in configurationDetails:
            self.exponentBits = configurationDetails["ExponentBits"]

        if "EsBits" in configurationDetails:
            self.esBits = configurationDetails["EsBits"]
        
        # check if the configuration details contains frequency
        if "Frequency" in configurationDetails:
            self.frequency = configurationDetails["Frequency"]
        
        # check the configuration details of the name
        if "Name" in configurationDetails:
            self.name = configurationDetails["Name"]

        # check the configuration details contains input data ports
        if "InputDataPorts" in configurationDetails:

            # access the ports and set the details of the port
            # the value of the key is expected to be an array
            portDetails = configurationDetails["InputDataPorts"]
            #print("Logic InputDataPorts", portDetails)
            for portDetail in portDetails:
                # access the information about the port or use the configuration details property to configure itself
                newPort = Port()
                newPort.configurationDetails = portDetail
                # configure the port
                newPort.configure()
                # process the port
                newPort.process()
                newPort.perform()
                # once the port is configured, add the port to the InputDataPorts array
                self.inputDataPorts.append(newPort)
                self.inputDataPortsInfo[newPort.name] = newPort



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
                newPort.perform()
                # once the port is configured, add the port to the output array
                self.outputPorts.append(newPort)
                self.outputPortsInfo[newPort.name] = newPort
            
        
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
            newPort.perform()
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
            newPort.perform()
            # once the port is configured, set the port
            self.resetPort = newPort
            
            
        # check the configuration details contains enable port or not
        if "InputEnablePort" in configurationDetails:
            # access the enable port and set the details of the port
            # the value of the key is expected to be a dict
            enablePortDetail = configurationDetails["InputEnablePort"]
            # access the enable port detail
            # only one enable port is possible
            # access the information about the port or use the configuration details property to configure itself'
            newPort = Port()
            newPort.configurationDetails = resetPortDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            newPort.perform()
            # once the port is configured, set the port
            self.enablePort = newPort
    
   
    def resetProperties(self):
        # dictionary to store the configuration details, which then will be used by the configure function to set the
        # properties of the Logic
        self.configurationDetailsOfLogic = dict()

        # property to store the number system
        # the number system property will be used the HW Description objects to generate appropriate VHDL syntax
        self._numberSystem = None
        
        #property to store the number or identity number of the operator
        self._number = None

        # property to store the name of the operator
        self._name = None

        # property to store the number system name
        # the name of the number system will be retreived from the configuration details
        # the custom getter and setters are used to use the number system name and set the corresponding number system
        self._numberSystemName = None
        
        
        # property to know that input data ports are updated or not
        # this property can be used to achieve the event driven architectures
        # however, for now, as the inputDataPorts property is not observable, we use this set and update mechanisms to update the inputdataports of an operator is updated
        # the vhdl description of the operator should be updated
        self._isInputDataPortsModified = False


        # like the input data ports, output port when set to that it is modified.
        # Should be used to updated the VHDL Description of the operator itself
        # the outputPorts property is not observable for now, and it will updated by the object whoever modifies the output ports information
        self._isOutputPortsModified = False

        # an array to store the number of input data ports of the LUT
        # for the current LUT, our requriement is only input data port
        # this data port list or array will have port objects that
        self.inputDataPorts = None

        # property to store the clock port
        self.clockPort = None

        # property to store the reset port
        self.resetPort = None

        # property to store the enable port
        self.enablePort = None

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

        # proeprty to store the required mantissaBits if the numberSystem is of Float
        self.mantissaBits = None

        # property to store the required exponent Bits if the number system is of Float
        self.exponentBits = None
        
        #property to store the required es bits if the number system is posit
        self.esBits = None
        
        #property to store the configuration details of hw operator
        self.configurationDetailsOfHWLogic = None

        
        # property to store the pythonHW that contains the core process or architecture description of the operator
        self.pythonHWLogic = None
        
        # property to store the pythonHW generics dictionary for the operator
        self._pythonHWLogicGeneric = None

        # property to store info of the inputDataPorts as dictionary
        self.inputDataPortsInfo = dict()


        # property to store the info of the output ports as dictionary
        self.outputPortsInfo = dict()

        self.flopocoBits = 2

        
    def process(self):
        self.processHWLogicConfigurationDetails()
    
    def processHWLogicConfigurationDetails(self):
        self.configurationDetailsOfHWLogic = {"Name":self.name,"PythonHWEntity":{"Name":self.name,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":self.pythonHWLogicGeneric},"InputDataPorts":[self.inputDataPorts], "OutputDataPorts":[self.outputPorts], "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort},"PythonHWArchitecture":{"Name":self.name,"HWArchitectureTypeName":"RTL","InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"PythonHWProcess":{"SensitivityList":[self.clockPort.name,self.resetPort.name]}},"PythonHW":{self.pythonHWLogic}}  
    
    def performHWGeneration(self):
        pass

    def perform(self):
        self.performHWGeneration

    def reset(self):
        self.resetProperties()        

    def main(self):
        # process the operator
        self.process()
        self.perform()


    def run(self):
        self.main()

