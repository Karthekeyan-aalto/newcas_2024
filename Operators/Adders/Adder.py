"""
Created by Karthekeyan Periasamy
Edited on July 13 08:26
Rewriting the sum node code as Adder
"""

from Operators.Operator import Operator
from Operators.Port.Port import Port
from SWOperators.Adders.SWAdder import SWAdder
from SWOperators.Adders.Driver.Driver import Driver
from HWDescription.Operators.Adders.AdderVHDLDescription import AdderVHDLDescription
#from HWSimulation.Operators.OperatorVHDLSimulation import OperatorVHDLSimulation

class Adder(Operator):

    """
    Class to have blueprint of the different types of Adders
    """

    def __init__(self):
        super().__init__()   
    
    
    @property
    def swOperator(self):
        if self._swOperator == None:
            self._swOperator = self.swAdder
        return self._swOperator

    @swOperator.setter
    def swOperator(self,value):
        self._swOperator = value
    
    @property
    def inputShiftRegisters(self):
        return self._inputShiftRegisters

    @inputShiftRegisters.setter
    def inputShiftRegisters(self,value):
        self._inputShiftRegisters = value

    @property
    def isInputDataPortsModified(self):
        return self._isInputDataPortsModified
    
    @isInputDataPortsModified.setter
    def isInputDataPortsModified(self,value):
        self._isInputDataPortsModified = value

        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
        if self._isInputDataPortsModified == True:
            # reset the HWDescription package
            self.resetHWDescriptionPackage()
            # process the HWOperatorsConfiguration details
            self.process()
            self.perform()
            # set the output port modified to false
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
            #print("SWAdder", self.swAdder.summation)
            if self.swAdder.summation != None:
                #print("SWAdder Summation",self.swAdder.summation)
                if self.swAdder.equation != None:
                    self._equation = self.swAdder.equation
                    #print("Adder Equation",self._equation)
        return self._equation
    
    
    @equation.setter
    def equation(self,value):
        self._equation = value
    
    @property
    def drivers(self):
        if self._drivers == None:
            self._drivers = list()

        return self._drivers


    @drivers.setter
    def drivers(self,value):
        self._drivers = value

    @property
    def augend(self):
        return self._augend

    @augend.setter
    def augend(self,value):
        self.swAdder.augend = value
        if self.swAdder.augendDriver.isDriverAPort == True:
            self._augend = value
            # make a new port with configuration details
            portDetail = {"Name":self._augend,"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}
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
            # store the port info 
            self.inputDataPortsInfo[newPort.name] = newPort
        elif self.swAdder.augendDriver.isDriverAnArithmeticNode == True:
            self._augend = value
            # make a new port with configuration details
            portDetail = {"Name":self._augend,"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}
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
            # store the port info 
            self.inputDataPortsInfo[newPort.name] = newPort

        
    @property
    def addend(self):
        return self._addend

    @addend.setter
    def addend(self,value):
        self.swAdder.addend = value
        if self.swAdder.addendDriver.isDriverAPort == True:
            self._addend = value
            # make a new port with configuration details
            portDetail = {"Name":self._addend,"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}
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
            # store the port info 
            self.inputDataPortsInfo[newPort.name] = newPort
        elif self.swAdder.addendDriver.isDriverAnArithmeticNode == True:
            self._addend = value
            # make a new port with configuration details
            portDetail = {"Name":self._addend,"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}
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
            # store the port info 
            self.inputDataPortsInfo[newPort.name] = newPort
            
    
    @property
    def summation(self):
        if self._summation == None:
            if (self.swAdder.augendDriver and self.swAdder.addendDriver) != None:
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
                self.outputPortsInfo[outputPort.name] = outputPort
                # set the product expression with the equation
                self._summation = outputPort.name
            else:
                self._summation = None

        return self._summation

    @summation.setter
    def summation(self,value):
        self._summation = value
            
    @property
    def input1(self):
        self._input1 = self.augend
        return self._input1

    @input1.setter
    def input1(self,value):
        self._input1 = value
        
        
    @property
    def input2(self):
        self._input2 = self.addend
        return self._input2

    @input2.setter
    def input2(self,value):
        self._input2 = value
    
    @property
    def output(self):
        self._output = self.summation
        return self._output

    @output.setter
    def output(self,value):
        self._output = value
        
    @property
    def shouldShiftRegisterBeAddedToAugend(self):
        return self._shouldShiftRegisterBeAddedToAugend

    
    @shouldShiftRegisterBeAddedToAugend.setter
    def shouldShiftRegisterBeAddedToAugend(self,value):
        self._shouldShiftRegisterBeAddedToAugend = value
        if self._shouldShiftRegisterBeAddedToAugend == True:
            self.isAugendPipelinedWithRegisters = False
            self.isInput1PipelinedWithRegisters = False

        # set the swOperator input1 balanced
        self.swOperator.isInput1Balanced = value 

    
    @property
    def shouldShiftRegisterBeAddedToAddend(self):
        return self._shouldShiftRegisterBeAddedToAddend

    
    @shouldShiftRegisterBeAddedToAddend.setter
    def shouldShiftRegisterBeAddedToAddend(self,value):
        self._shouldShiftRegisterBeAddedToAddend = value
        # check if the shiftRegisterBeAddedToMultiplier is true or not
        if self._shouldShiftRegisterBeAddedToAddend == True:
            self.isAddendPipelinedWithRegisters = False
            self.isInput2PipelinedWithRegisters = False
        # set the swOperator input2 balanced
        self.swOperator.isInput2Balanced = value 

    
    
    @property
    def shouldShiftRegisterBeAddedToAugendAndAddend(self):
        return self._shouldShiftRegisterBeAddedToAugendAndAddend

    
    @shouldShiftRegisterBeAddedToAugendAndAddend.setter
    def shouldShiftRegisterBeAddedToAugendAndAddend(self,value):
        self._shouldShiftRegisterBeAddedToAugendAndAddend = value
        # set the swOperator input1 and input2 balanced
        self.swOperator.isInput1AndInput2Balanced = value 


    
    @property
    def shouldAShiftRegisterBeAddedToInput1(self): 
        return self._shouldAShiftRegisterBeAddedToInput1
    
    @shouldAShiftRegisterBeAddedToInput1.setter
    def shouldAShiftRegisterBeAddedToInput1(self,value):
        self._shouldAShiftRegisterBeAddedToInput1 = value
        self._shouldAShiftRegisterBeAddedToInput1 = self.shouldShiftRegisterBeAddedToAugend

    
    @property
    def shouldAShiftRegisterBeAddedToInput2(self): 
        return self._shouldAShiftRegisterBeAddedToInput2
    
    @shouldAShiftRegisterBeAddedToInput2.setter
    def shouldAShiftRegisterBeAddedToInput2(self,value):
        self._shouldAShiftRegisterBeAddedToInput2 = value
        self._shouldAShiftRegisterBeAddedToInput2 = self._shouldShiftRegisterBeAddedToAugendAndAddend
    
    
    @property
    def shouldAShiftRegisterBeAddedToInput1AndInput2(self):
        return self._shouldAShiftRegisterBeAddedToInput1AndInput2
    
    
    @shouldAShiftRegisterBeAddedToInput1AndInput2.setter
    def shouldAShiftRegisterBeAddedToInput1AndInput2(self,value):
        self._shouldAShiftRegisterBeAddedToInput1AndInput2 = value
        self._shouldAShiftRegisterBeAddedToInput1AndInput2 = self._shouldShiftRegisterBeAddedToAugendAndAddend
    

    @property
    def shiftRegisterDelay(self):
        return self._shiftRegisterDelay

    @shiftRegisterDelay.setter
    def shiftRegisterDelay(self,value):
        self._shiftRegisterDelay = value


    def connect(self):
        self.connectProperties()
        self.connectHWDescriptionPackage()

    def connectHWDescriptionPackage(self):
        self.hwDescription = AdderVHDLDescription()

    def connectProperties(self):
        super().connectProperties()
        
        #property to store the arithemetic number
        # the arithmetic number property is the number of current multiplier based on the arithmeticNode Number
        # assigned by any PCOperation
        self.arithmeticNodeNumber = 0
        
        # property to store the augend
        # this is equivalent of inpu1 of the two port adder
        self._augend = None

        # property to store the addend
        # the property to store the second input of the two port adder
        self._addend = None

        # property to store the product of the augend and the addend
        # the property to store the summation of the output
        self._summation = None

        # property to store the dictionary info of the drivers of multiplier
        # Multiplier can be driven at both the ends or one of the input is driven by a memory which gives information about weight
        self.drivers = None
        
        self._equation = None
        
        
        # property to connect the SW multiplier
        # sw multiplier are used to process multiplier sw operations including balancing multiplier node in the whole tree structure
        self.swAdder = SWAdder()
        
        # property to know whether to attach a shiftRegister is needed to input1 or not
        self._shouldAShiftRegisterBeAddedToInput1 = False
        
        # property to know whether to attach a shiftRegister is needed to input2 or not
        self._shouldAShiftRegisterBeAddedToInput2 = False
        
        # property to know whether to attach a shiftRegister to both input1 and input2
        self._shouldAShiftRegisterBeAddedToInput1AndInput2 = False
        
        self._shouldShiftRegisterBeAddedToAugendAndAddend = False

        self._shouldShiftRegisterBeAddedToAddend = False

        self._shouldShiftRegisterBeAddedToAugend = False
        
        # property to store the augend is pipelined with registers or not
        self.isAugendPipelinedWithRegisters = False


        # property to know whether the input1 is pipelined with registers or not
        self.isInput1PipelinedWithRegisters = False
        
        # property to store the addend is pipelined with registers or not
        self.isAddendPipelinedWithRegisters = False

        # property to know whether the input1 is pipelined with registers or not
        self.isInput2PipelinedWithRegisters = False

        
        # property to stor ethe shift register delay
        self._shiftRegisterDelay = 0


        

    def configure(self):
        super().configure()            
        
        configurationDetails = self.configurationDetailsOfOperator
        
        # check the configuration Details for the property arithmeticNode number
        if "ArithmeticNodeNumber" in configurationDetails:
            self.arithmeticNodeNumber = configurationDetails["ArithmeticNodeNumber"]

        # check the configuration details contains input data ports
        if "InputDataPorts" in configurationDetails:

            # access the ports and set the details of the port
            # the value of the key is expected to be an array
            portDetails = config_producturationDetails["InputDataPorts"]
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
                
            
        elif "Augend" in configurationDetails:
            self.augend = configurationDetails["Augend"]
            if "Addend" in configurationDetails:
                self.addend = configurationDetails["Addend"]
       

    
    def reset(self):
        self.resetProperties()
        self.resetHWDescriptionPackage()

    
    def resetProperties(self):
        super().resetProperties()

        #property to store the arithemetic number
        # the arithmetic number property is the number of current multiplier based on the arithmeticNode Number
        # assigned by any PCOperation
        self.arithmeticNodeNumber = 0
        
        # property to store the augend
        # this is equivalent of inpu1 of the two port adder
        self._augend = None

        # property to store the addend
        # the property to store the second input of the two port adder
        self._addend = None

        # property to store the product of the augend and the addend
        # the property to store the summation of the output
        self._summation = None

        # this equation represents the equation of the mutiplier, that is formed based on the given input
        # or combining the driver equations would give the equation a value that can be used
        # the equation will be used by the receiver (or whichever node the current produt node drives)
        self._equation = None

        # property to connect the SW Adder
        # sw Adder are used to process adder sw operations including balancing adder node in the whole tree structure
        self.swAdder = SWAdder()
        
        # property to know whether to attach a shiftRegister is needed to input1 or not
        self._shouldAShiftRegisterBeAddedToInput1 = False
        
        # property to know whether to attach a shiftRegister is needed to input2 or not
        self._shouldAShiftRegisterBeAddedToInput2 = False
        
        # property to know whether to attach a shiftRegister to both input1 and input2
        self._shouldAShiftRegisterBeAddedToInput1AndInput2 = False
        
        self._shouldShiftRegisterBeAddedToAugendAndAddend = False

        self._shouldShiftRegisterBeAddedToAddend = False

        self._shouldShiftRegisterBeAddedToAugend = False
        
        # property to store the augend is pipelined with registers or not
        self.isAugendPipelinedWithRegisters = False

        # property to know whether the input1 is pipelined with registers or not
        self.isInput1PipelinedWithRegisters = False
        
        # property to store the addend is pipelined with registers or not
        self.isAddendPipelinedWithRegisters = False

        # property to know whether the input1 is pipelined with registers or not
        self.isInput2PipelinedWithRegisters = False
        
        # property to stor ethe shift register delay
        self._shiftRegisterDelay = 1



    
    
    def resetHWDescriptionPackage(self):
        self.connectHWDescriptionPackage()
    

    def processHWGeneration(self):
        pass

    def performHWGeneration(self):
        pass


    def process(self):
        super().process()

    def perform(self):
        super().perform()
  
    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()




