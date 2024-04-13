"""
Created by Karthekeyan Periasamy
Edited on Jan 23 =8:15
Rewriting the product node code
"""

from Operators.Operator import Operator
from SWOperators.Multipliers.SWMultiplier import SWMultiplier
from Operators.Port.Port import Port
from SWOperators.Multipliers.Driver.Driver import Driver
from SWLogic.Memory.Weight.Weight import Weight
from HWDescription.Operators.Multipliers.MultiplierVHDLDescription import MultiplierVHDLDescription
#from HWSimulation.Operators.OperatorVHDLSimulation import OperatorVHDLSimulation

class Multiplier(Operator):

    """
    Class to have blueprint of the different types of multipliers
    In general a multiplier will have a LUT, Input Converter, A Multiplier, Output Converter.
    Based on the number systems, we may or may not have the converters, but for sure we will have LUTs.
    """

    def __init__(self):
        self.connect()    
    
    
    @property
    def inputShiftRegisters(self):
        return self._inputShiftRegisters

    @inputShiftRegisters.setter
    def inputShiftRegisters(self,value):
        self._inputShiftRegisters = value

    @property
    def swOperator(self):
        if self._swOperator == None:
            self._swOperator = self.swMultiplier
        return self._swOperator

    @swOperator.setter
    def swOperator(self,value):
        self._swOperator = value
    
    @property
    def isInputDataPortsModified(self):
        return self._isInputDataPortsModified
    
    @isInputDataPortsModified.setter
    def isInputDataPortsModified(self,value):
        self._isInputDataPortsModified = value
        #print("Input Data Ports Modified", self._isInputDataPortsModified)
        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
        if self._isInputDataPortsModified == True:
            # reset the HWDescription package
            self.resetHWDescriptionPackage()
            # process the HWOperatorsConfiguration details
            self.process()
            self.perform()
            # set the input data port modified to false
            self._isInputDataPortsModified = False
    
    @property
    def isOutputPortsModified(self):
        return self._isOutputPortsModified
    
    @isOutputPortsModified.setter
    def isOutputPortsModified(self,value):
        self._isOutputPortsModified = value

        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
        
        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
        if self._isOutputPortsModified == True:
            # reset the HWDescription package
            self.resetHWDescriptionPackage()
            # process the HWOperatorsConfiguration details
            self.process()
            self.perform()
            # set the output port modified to false
            self._isOutputPortsModified = False


    @property
    def equation(self):
        if self._equation == None:
            #print("SWMultiplier", self.swMultiplier.product)
            if self.swMultiplier.product != None:
                if self.swMultiplier.equation != None:
                    self._equation = self.swMultiplier.equation
                    
        return self._equation
    
    
    @equation.setter
    def equation(self,value):
        self._equation = value
    
    
    @property
    def multiplicand(self):
        return self._multiplicand

    @multiplicand.setter
    def multiplicand(self,value):
        self.swMultiplier.multiplicand = value
        if self.swMultiplier.multiplicandDriver.isDriverAPort == True:
            self._multiplicand = value
            # make a new port with configuration details
            portDetail = {"Name":self._multiplicand,"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}
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
            self._multiplicand = value
        elif self.swMultiplier.multiplicandDriver.isDriverAWeight == True:
            self._multiplicand = self.name + str(self.number) + "Weight"
            # make a new port with configuration details
            portDetail = {"Name":self._multiplicand,"NumberOfBits":self.numberOfBits,"PortType":"Weight","SignalData":self.swMultiplier.weight.name}
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
        elif self.swMultiplier.multiplicandDriver.isDriverAnArithmeticNode == True:
            self._multiplicand = value
            # make a new port with configuration details
            portDetail = {"Name":self._multiplicand,"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}
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
            

        
    @property
    def multiplier(self):
        return self._multiplier

    @multiplier.setter
    def multiplier(self,value):
        self.swMultiplier.multiplier = value
        if self.swMultiplier.multiplierDriver.isDriverAPort == True:
            # make a new port with configuration details
            portDetail = {"Name":self._multiplier,"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}
            # access the information about the port or use the configuration details property to configure itself
            newPort = Port()
            newPort.configurationDetails = portDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            newPort.perform()
            self.inputDataPorts.append(newPort)
            self.inputDataPortsInfo[newPort.name] = newPort
            # once the port is configured, add the port to the InputDataPorts array
            self._multiplier = value
        elif self.swMultiplier.multiplierDriver.isDriverAWeight == True:
            self._multiplier = self.name + str(self.number) + "Weight"
            # make a new port with configuration details
            portDetail = {"Name":self._multiplier,"NumberOfBits":self.numberOfBits,"PortType":"Weight","SignalData":self.swMultiplier.weight.name}
            # access the information about the port or use the configuration details property to configure itself
            newPort = Port()
            newPort.configurationDetails = portDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            newPort.perform()
            self.inputDataPorts.append(newPort)
            self.inputDataPortsInfo[newPort.name] = newPort
        elif self.swMultiplier.multiplierDriver.isDriverAnArithmeticNode == True:
            self._multiplier = value
            # make a new port with configuration details
            portDetail = {"Name":self._multiplier,"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}
            # access the information about the port or use the configuration details property to configure itself
            newPort = Port()
            newPort.configurationDetails = portDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            newPort.perform()
            self.inputDataPorts.append(newPort)
            self.inputDataPortsInfo[newPort.name] = newPort
    
    @property
    def product(self):
        if self._product == None:
            if (self.swMultiplier.multiplicandDriver and self.swMultiplier.multiplierDriver) != None:
                outputPort = Port()
                portDetail = {"Name":(self.name + str(self.number) + "_" + "Output" + "_" + str(self.arithmeticNodeNumber)),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}                
                # generate the output port using the configuration details
                outputPort.configurationDetails = portDetail
                # configure the port
                outputPort.configure()
                # process the port
                outputPort.process()
                outputPort.perform()
                # once the port is configured, add the port to the outputdata array
                self.outputPorts.append(outputPort)
                # form the outputPorts Info
                self.outputPortsInfo[outputPort.name] = outputPort
                # set the product expression with the equation
                self._product = outputPort.name
            else:
                self._product = None

        return self._product

    @product.setter
    def product(self,value):
        self._product = value  
   
    @property
    def input1(self):
        self._input1 = self.multiplicand
        return self._input1

    @input1.setter
    def input1(self,value):
        self._input1 = value
        self.multiplicand = value
        
    @property
    def input2(self):
        self._input2 = self.multiplier
        return self._input2

    @input2.setter
    def input2(self,value):
        self._input2 = value
        self.multiplier = value
    
    @property
    def output(self):
        self._output = self.product
        return self._output

    @output.setter
    def output(self,value):
        self._output = value
        self.product = value
    
    @property
    def shiftRegisterDelay(self):
        return self._shiftRegisterDelay

    @shiftRegisterDelay.setter
    def shiftRegisterDelay(self,value):
        self._shiftRegisterDelay = value

    @property
    def shouldShiftRegisterBeAddedToMultiplicand(self):
        return self._shouldShiftRegisterBeAddedToMultiplicand

    
    @shouldShiftRegisterBeAddedToMultiplicand.setter
    def shouldShiftRegisterBeAddedToMultiplicand(self,value):
        self._shouldShiftRegisterBeAddedToMultiplicand = value
        if self._shouldShiftRegisterBeAddedToMultiplicand == True:
            self.isMultiplicandPipelinedWithRegisters = False
            self.isInput1PipelinedWithRegisters = False
        # set the swOperator input1 balanced
        self.swOperator.shouldInput1BeBalanced = value 
    
    @property
    def shouldShiftRegisterBeAddedToMultiplier(self):
        return self._shouldShiftRegisterBeAddedToMultiplier

    
    @shouldShiftRegisterBeAddedToMultiplier.setter
    def shouldShiftRegisterBeAddedToMultiplier(self,value):
        self._shouldShiftRegisterBeAddedToMultiplier = value
        # check if the shiftRegisterBeAddedToMultiplier is true or not
        if self._shouldShiftRegisterBeAddedToMultiplier == True:
            self.isMultiplierPipelinedWithRegisters = False
            self.isInput2PipelinedWithRegisters = False

        # set the swOperator input2 balanced
        self.swOperator.shouldInput2BeBalanced = value 
    
    
    @property
    def shouldShiftRegisterBeAddedToMultiplicandAndMultiplier(self):
        return self._shouldShiftRegisterBeAddedToMultiplicandAndMultiplier

    
    @shouldShiftRegisterBeAddedToMultiplicandAndMultiplier.setter
    def shouldShiftRegisterBeAddedToMultiplicandAndMultiplier(self,value):
        self._shouldShiftRegisterBeAddedToMultiplicandAndMultiplier = value
        # set the swOperator input1 and input2 balanced
        self.swOperator.shouldInput1AndInput2BeBalanced = value 

    
    @property
    def shouldAShiftRegisterBeAddedToInput1(self):
        self._shouldAShiftRegisterBeAddedToInput1 = self.shouldShiftRegisterBeAddedToMultiplicand
        return self._shouldAShiftRegisterBeAddedToInput1
    
    @shouldAShiftRegisterBeAddedToInput1.setter
    def shouldAShiftRegisterBeAddedToInput1(self,value):
        self._shouldAShiftRegisterBeAddedToInput1 = value
        self.shouldShiftRegisterBeAddedToMultiplicand = value

    
    @property
    def shouldAShiftRegisterBeAddedToInput2(self): 
        self._shouldAShiftRegisterBeAddedToInput2 = self.shouldShiftRegisterBeAddedToMultiplier
        return self._shouldAShiftRegisterBeAddedToInput2
    
    @shouldAShiftRegisterBeAddedToInput2.setter
    def shouldAShiftRegisterBeAddedToInput2(self,value):
        self._shouldAShiftRegisterBeAddedToInput2 = value
        self.shouldShiftRegisterBeAddedToMultiplier = value
    
    
    @property
    def shouldAShiftRegisterBeAddedToInput1AndInput2(self):
        self._shouldAShiftRegisterBeAddedToInput1AndInput2 = self.shouldShiftRegisterBeAddedToMultiplicandAndMultiplier
        return self._shouldAShiftRegisterBeAddedToInput1AndInput2
    
    
    @shouldAShiftRegisterBeAddedToInput1AndInput2.setter
    def shouldAShiftRegisterBeAddedToInput1AndInput2(self,value):
        self._shouldAShiftRegisterBeAddedToInput1AndInput2 = value
        self.shouldShiftRegisterBeAddedToMultiplicandAndMultiplier = value

    
    def connect(self):
        self.connectProperties()
        self.connectHWDescriptionPackage()


    def connectHWDescriptionPackage(self):
        self.hwDescription = MultiplierVHDLDescription()

    def connectProperties(self):
        super().connectProperties()
       
        #property to store the arithemetic number
        # the arithmetic number property is the number of current multiplier based on the arithmeticNode Number
        # assigned by any PCOperation
        self.arithmeticNodeNumber = 0
        
        # the below two properties will be useful when the Multiplier has a memory embedded in it

        # property to store the weightReadEnable port of the multiplier
        # when this port is enable, we will read the weight from the memory
        self.weightReadEnable = None

        # property to store the weightWrite enable of the multiplier
        # when this port is enable, we will write the weight to the memory
        self.weightWriteEnable = None

        # property to store the port inputDataSelector
        # inour design the input select is a 2 bit selector of MUX that selects the input to the components of the Multiplier
        # Yet to be confirmed, so the above sentence may not be right
        self.inputDataSelectPort = None

        # input1 of the hw multiplier
        self._multiplicand = None
        # input2 of the hw multiplier
        self._multiplier = None
        
        # property to store the HW drivers like FFs and Converters for the multipliers
        self._drivers = None

        self._product = None

        self._equation = None

        # property to connect the SW multiplier
        # sw multiplier are used to process multiplier sw operations including balancing multiplier node in the whole tree structure
        self.swMultiplier = SWMultiplier()

        # property to know whether to attach a shiftRegister is needed to input1 or not
        self._shouldAShiftRegisterBeAddedToInput1 = False
        
        # property to know whether to attach a shiftRegister is needed to input2 or not
        self._shouldAShiftRegisterBeAddedToInput2 = False
        
        # property to know whether to attach a shiftRegister to both input1 and input2
        self._shouldAShiftRegisterBeAddedToInput1AndInput2 = False

        #property to know whether shift register should be added to multiplier
        self._shouldShiftRegisterBeAddedToMultiplier = False

        #property to know whether shift register should be augend to multiplier and multiplicand
        self._shouldShiftRegisterBeAddedToMultiplicandAndMultiplier = False

        self._shouldShiftRegisterBeAddedToMultiplicand = False
        
        # property to store the multiplicand is pipelined with registers or not
        self.isMultiplicandPipelinedWithRegisters = False

        # property to know whether the input1 is pipelined with registers or not
        self.isInput1PipelinedWithRegisters = False
        
        # property to store the multiplicand is pipelined with registers or not
        self.isMultiplierPipelinedWithRegisters = False

        # property to know whether the input1 is pipelined with registers or not
        self.isInput2PipelinedWithRegisters = False


        # property to store the input shift registers
        self.inputRegisters = dict()
        
        # property to stor ethe shift register delay
        self._shiftRegisterDelay = 0



    def configure(self):
        super().configure()
        # check if the configuration details of the multiplier is set or not
        if self.configurationDetailsOfOperator == None:
            return
            
        configurationDetails = self.configurationDetailsOfOperator
        
        # check the configuration Details for the property arithmeticNode number
        if "ArithmeticNodeNumber" in configurationDetails:
            self.arithmeticNodeNumber = configurationDetails["ArithmeticNodeNumber"]


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
                self.inputDataPortsInfo[newPort.name] = newPort
                
            
        elif "Multiplicand" in configurationDetails:
            self.multiplicand = configurationDetails["Multiplicand"]
            if "Multiplier" in configurationDetails:
                self.multiplier = configurationDetails["Multiplier"]
        
        if "ArithmeticNodeNumber" in configurationDetails:
            self.arithmeticNodeNumber = configurationDetails["ArithmeticNodeNumber"]

    def reset(self):
        self.resetProperties()
        self.resetHWDescriptionPackage()

    
    def resetHWDescriptionPackage(self):
        self.connectHWDescriptionPackage()
    
    def resetProperties(self):
        super().resetProperties()
        #property to store the arithemetic number
        # the arithmetic number property is the number of current multiplier based on the arithmeticNode Number
        # assigned by any PCOperation
        self.arithmeticNodeNumber = 0

        # the below two properties will be useful when the Multiplier has a memory embedded in it

        # property to store the weightReadEnable port of the multiplier
        # when this port is enable, we will read the weight from the memory
        self.weightReadEnable = None

        # property to store the weightWrite enable of the multiplier
        # when this port is enable, we will write the weight to the memory
        self.weightWriteEnable = None

        # property to store the port inputDataSelector
        # inour design the input select is a 2 bit selector of MUX that selects the input to the components of the Multiplier
        # Yet to be confirmed, so the above sentence may not be right
        self.inputDataSelectPort = None
        
        # input1 of the hw multiplier
        self._multiplicand = None
        # input2 of the hw multiplier
        self._multiplier = None
        
        # property to store the HW drivers like FFs and Converters for the multipliers
        self._drivers = None

        self._product = None

        self._equation = None

        # property to connect the SW multiplier
        # sw multiplier are used to process multiplier sw operations including balancing multiplier node in the whole tree structure
        self.swMultiplier = SWMultiplier()
        
        # property to know whether to attach a shiftRegister is needed to input1 or not
        self._shouldAShiftRegisterBeAddedToInput1 = False
        
        # property to know whether to attach a shiftRegister is needed to input2 or not
        self._shouldAShiftRegisterBeAddedToInput2 = False
        
        # property to know whether to attach a shiftRegister to both input1 and input2
        self._shouldAShiftRegisterBeAddedToInput1AndInput2 = False
        
        #property to know whether shift register should be added to multiplier
        self._shouldShiftRegisterBeAddedToMultiplier = False

        #property to know whether shift register should be augend to multiplier and multiplicand
        self._shouldShiftRegisterBeAddedToMultiplicandAndMultiplier = False

        self._shouldShiftRegisterBeAddedToMultiplicand = False
        
        # property to store the multiplicand is pipelined with registers or not
        self.isMultiplicandPipelinedWithRegisters = False

        # property to know whether the input1 is pipelined with registers or not
        self.isInput1PipelinedWithRegisters = False
        
        # property to store the multiplicand is pipelined with registers or not
        self.isMultiplierPipelinedWithRegisters = False

        # property to know whether the input1 is pipelined with registers or not
        self.isInput2PipelinedWithRegisters = False
        
        # property to store the input shift registers
        self.inputRegisters = dict()
       
        # property to stor ethe shift register delay
        self._shiftRegisterDelay = 1


    def process(self):
        self.swMultiplier.process()
        super().process()

   
    def perform(self):
        super().perform()
  
    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()




