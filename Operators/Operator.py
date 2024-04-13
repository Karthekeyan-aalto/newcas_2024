"""
Created by Karthekeyan Periasamy
Edited on Mar21 13:29 AM
"""

from SWOperators.SWOperator import SWOperator
from Operators.Port.Port import Port

class Operator ():
    """
    This class is the base class for any type of Operator that will be constructed
    The purpose of this class is to hold the basic properties of any Operator but not including the HWDescription and HW Simulation object
    
    As Operator is part of AutoPC, it will follow the connect, configure, perform or process, reset process
    The idea of the four step process may not be intiutive, but it allows any package and its associated modules to be configured
    separately and tested accordingly.

    **However many other packages and modules in AutoPC are not made based on the four step process. Its lack of thought process which
    led that disaster happen while desgning those modules. So, it will be changed in the future and is recommended to follow the four step process
    """

    def __init__(self):
        self.connect()
        
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
    def isOperatorNameModified(self):
        return self._isOperatorNameModified
    
    @isOperatorNameModified.setter
    def isOperatorNameModified(self,value):
        self._isOperatorNameModified = value

        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator

    @property
    def isOperatorNumberModified(self):
        return self._isOperatorNumberModified
    
    @isOperatorNumberModified.setter
    def isOperatorNumberModified(self,value):
        self._isOperatorNumberModified = value

        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator

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
    def pythonHWOperatorGeneric(self):
        if self._pythonHWOperatorGeneric == None:
            self._pythonHWOperatorGeneric = dict()
            if self.numberSystem > -1 :
                if self.numberSystem == 0:
                    self._pythonHWOperatorGeneric["NumberOfBits"] = self.numberOfBits
                elif self.numberSystem == 1:
                    self._pythonHWOperatorGeneric["MantissaBits"] = self.mantissaBits
                    self._pythonHWOperatorGeneric["ExponentBits"] = self.exponentBits
                    self._pythonHWOperatorGeneric["NumberOfBits"] = self.numberOfBits
                    self._pythonHWOperatorGeneric["FlopocoBits"] = self.flopocoBits
                elif self.numberSystem == 2:
                    self._pythonHWOperatorGeneric["NumberOfBits"] = self.numberOfBits
                    self._pythonHWOperatorGeneric["EsBits"] = self.esBits
        return self._pythonHWOperatorGeneric

    @pythonHWOperatorGeneric.setter
    def pythonHWOperatorGeneric(self,value):
        self._pythonHWOperatorGeneric = value
    
    @property
    def swOperator(self):
        return self._swOperator

    @swOperator.setter
    def swOperator(self,value):
        self._swOperator = value
    
    
    @property
    def input1(self):
        return self._input1

    @input1.setter
    def input1(self,value):
        self._input1 = value
        
        
    @property
    def input2(self):
        return self._input2

    @input2.setter
    def input2(self,value):
        self._input2 = value
    
    @property
    def output(self):
        return self._output

    @output.setter
    def output(self,value):
        self._output = value
    
    
    @property
    def shouldAShiftRegisterBeAddedToInput1(self):
        return self._shouldAShiftRegisterBeAddedToInput1
    
    @shouldAShiftRegisterBeAddedToInput1.setter
    def shouldAShiftRegisterBeAddedToInput1(self,value):
        self._shouldAShiftRegisterBeAddedToInput1 = value
    
    @property
    def shouldAShiftRegisterBeAddedToInput2(self): 
        return self._shouldAShiftRegisterBeAddedToInput2
    
    @shouldAShiftRegisterBeAddedToInput2.setter
    def shouldAShiftRegisterBeAddedToInput2(self,value):
        self._shouldAShiftRegisterBeAddedToInput2 = value    
    
    @property
    def shouldAShiftRegisterBeAddedToInput1AndInput2(self):
        return self._shouldAShiftRegisterBeAddedToInput1AndInput2
    
    
    @shouldAShiftRegisterBeAddedToInput1AndInput2.setter
    def shouldAShiftRegisterBeAddedToInput1AndInput2(self,value):
        self._shouldAShiftRegisterBeAddedToInput1AndInput2 = value
    
    def configure(self):
        """
        This function will be called from outside of the class itself.
        The main purpose of this funciton to receive information via the configuraiton dictionary
        Use the information from the configurartion dictionary to set the properties of the object or configuring itself.
        """
        if self.configurationDetailsOfOperator == None:
            #print("The object is not configured and the behaviour of the object cannot be guaranteed")
            return

        configurationDetails = self.configurationDetailsOfOperator
        #print("Operator configurationDetails", configurationDetails)

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

        # check the configuration details of the name
        if "Name" in configurationDetails:
            self.name = configurationDetails["Name"]

        # check if the configuration details contains frequency
        if "Frequency" in configurationDetails:
            self.frequency = configurationDetails["Frequency"]


        # check the configuration Details for the property arithmeticNode number
        if "ArithmeticNodeNumber" in configurationDetails:
            self.arithmeticNodeNumber = configurationDetails["ArithmeticNodeNumber"]

        # check the configuration details contains input data ports
        if "InputDataPorts" in configurationDetails:

            # access the ports and set the details of the port
            # the value of the key is expected to be an array
            portDetails = configurationDetails["InputDataPorts"]
            #print("Operator InputDataPorts", portDetails)
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


    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        # dictionary to store the configuration details, which then will be used by the configure function to set the
        # properties of the Logic
        self.configurationDetailsOfOperator = dict()
        
        # property to store the number system
        # the number system property will be used the HW Description objects to generate appropriate VHDL syntax
        self._numberSystem = None

        #property to store the number or identity number of the operator
        self._number = None

        # property to store the name of the LUT
        self._name = None

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

        # when the operator name is modified update the hardware description
        self._isOperatorNameModified = False
        
        # when the operator number is modified update the hardware description
        self._isOperatorNumberModified = False


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
        

        #property to store the required es bits if the number system is posit
        self.esBits = None
        
        #property to store the configuration details of hw operator
        self.configurationDetailsOfHWOperator = None


        # property to store the pythonHW that contains the core process or architecture description of the operator
        self.pythonHWOperator = None

        # property to store the pythonHW generics dictionary for the operator
        self._pythonHWOperatorGeneric = None

        # property to store info of the inputDataPorts as dictionary
        self.inputDataPortsInfo = dict()


        # property to store the info of the output ports as dictionary
        self.outputPortsInfo = dict()

        # property to store teh swOperator
        self._swOperator = None
        
        # property to be used by optimisers, where input1 represents the multiplicand property
        self._input1 = None

        #property to be used by optimisers, where input2 represents the multiplier property
        self._input2 = None

        #property to mask the product
        self._output = None

        # property to know whether to attach a shiftRegister is needed to input1 or not
        self._shouldAShiftRegisterBeAddedToInput1 = False
        
        # property to know whether to attach a shiftRegister is needed to input2 or not
        self._shouldAShiftRegisterBeAddedToInput2 = False
        
        # property to know whether to attach a shiftRegister to both input1 and input2
        self._shouldAShiftRegisterBeAddedToInput1AndInput2 = False
        
        # property to know whether the input1 is pipelined with registers or not
        self.isInput1PipelinedWithRegisters = False
        
        # property to know whether the input1 is pipelined with registers or not
        self.isInput2PipelinedWithRegisters = False
        
        # property to store the input shift registers
        self.inputRegisters = dict()

        # property to store the output shift registers
        self.outputRegisters = dict()

        self.flopocoBits = 2





    def resetProperties(self):
        # dictionary to store the configuration details, which then will be used by the configure function to set the
        # properties of the Logic
        self.configurationDetailsOfOperator = dict()

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
        self.configurationDetailsOfHWOperator = None
        
        # property to know that input data ports are updated or not
        # this property can be used to achieve the event driven architectures
        # however, for now, as the inputDataPorts property is not observable, we use this set and update mechanisms to update the inputdataports of an operator is updated
        # the vhdl description of the operator should be updated
        self._isInputDataPortsModified = False


        # like the input data ports, output port when set to that it is modified.
        # Should be used to updated the VHDL Description of the operator itself
        # the outputPorts property is not observable for now, and it will updated by the object whoever modifies the output ports information
        self._isOutputPortsModified = False

        # when the operator name is modified update the hardware description
        self._isOperatorNameModified = False
        
        # when the operator number is modified update the hardware description
        self._isOperatorNumberModified = False

        
        # property to store the pythonHW that contains the core process or architecture description of the operator
        self.pythonHWOperator = None
        
        # property to store the pythonHW generics dictionary for the operator
        self._pythonHWOperatorGeneric = None
        
        # property to store info of the inputDataPorts as dictionary
        self.inputDataPortsInfo = dict()


        # property to store the info of the output ports as dictionary
        self.outputPortsInfo = dict()
        
        # property to store the swOperator
        self._swOperator = None
        
        # property to be used by optimisers, where input1 represents the multiplicand property
        self._input1 = None

        #property to be used by optimisers, where input2 represents the multiplier property
        self._input2 = None

        #property to mask the product
        self._output = None
        
        # property to know whether to attach a shiftRegister is needed to input1 or not
        self._shouldAShiftRegisterBeAddedToInput1 = False
        
        # property to know whether to attach a shiftRegister is needed to input2 or not
        self._shouldAShiftRegisterBeAddedToInput2 = False
        
        # property to know whether to attach a shiftRegister to both input1 and input2
        self._shouldAShiftRegisterBeAddedToInput1AndInput2 = False
        
        # property to know whether the input1 is pipelined with registers or not
        self.isInput1PipelinedWithRegisters = False
        
        # property to know whether the input1 is pipelined with registers or not
        self.isInput2PipelinedWithRegisters = False

        # property to store the input shift registers
        self.inputRegisters = dict()
        
        # property to store the output shift registers
        self.outputRegisters = dict()

        self.flopocoBits = 2




        

    def process(self):
        self.processHWOperatorConfigurationDetails()
        self.processHWGeneration()
    
    def processHWOperatorConfigurationDetails(self):
        self.configurationDetailsOfHWOperator = {"Name":self.name,"PythonHWEntity":{"Name":self.name,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":self.pythonHWOperatorGeneric},"InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort},"PythonHWArchitecture":{"Name":self.name,"HWArchitectureTypeName":"RTL","InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"PythonHWProcess":{"SensitivityList":[self.clockPort.name,self.resetPort.name]}}
            ,"PythonHW":{self.pythonHWOperator}}
    

    def performHWGeneration(self):
        pass

    def processHWGeneration(self):
        pass

    def perform(self):
        self.performHWGeneration()

    def reset(self):
        self.resetProperties()        

    def main(self):
        # process the operator
        self.process()
        self.perform()


    def run(self):
        self.main()

