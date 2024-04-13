"""
Created by Karthekeyan Peirasamy
Edited on July 10 12:48
"""
from Operators.Adders.Adder import Adder
from Operators.Port.Port import Port
from Logic.FF.MB_D_FF.MB_D_FF import MB_D_FF
from HWDescription.Operators.Adders.PositAdder.PositAdderVHDLDescription import PositAdderVHDLDescription

class PositAdder(Adder):

    def __init__(self):
        super().__init__()


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
            self.processHWOperatorConfigurationDetails()
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
            self.processHWOperatorConfigurationDetails()
            self.perform()
            # set the output port modified to false
            self._isOutputPortsModified = False

    @property
    def positName(self):
        if self._positName == None:
            self._positName = ("PositAdd" + "_" + str(self.exponentBits) + "_" \
                                    + str(self.mantissaBits-1) + "_" + "Freq" + str(self.frequency) + "_" + "uid" + "2")

        return self._positName

    @positName.setter
    def positName(self,value):
        self._positName = value
    
        
    @property
    def augend(self):
        return self._augend

    @augend.setter
    def augend(self,value):
        if self.swAdder.augend == None:
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
            portDetail = {"Name":self._augend,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Input","ConstantSignalValue":0}
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
        if self.swAdder.addend == None:
            self.swAdder.addend = value
        if self.swAdder.addendDriver.isDriverAPort == True:
            self._addend = value
            # make a new port with configuration details
            portDetail = {"Name":self._addend,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Input","ConstantSignalValue":0}
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
            #print("Addend", self._addend)
            # make a new port with configuration details
            portDetail = {"Name":self._addend,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Input","ConstantSignalValue":0}
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
            #print(self.inputDataPortsInfo)
            
    
    @property
    def summation(self):
        if self._summation == None:
            if (self.swAdder.augendDriver and self.swAdder.addendDriver) != None:
                outputPort = Port()
                portDetail = {"Name":(self.name + str(self.number) + "_" + "Output" + "_" + str(self.arithmeticNodeNumber)),"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Output", "ConstantSignalValue":0}                
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
        #print("To be Updated Input1", value)
        if self._input1 != None:
            #print("Original Ports", self.inputDataPorts)
            #print("Original Ports Info", self.inputDataPortsInfo)
            #print("Original Input1", self._input1)
            if self.isInputDataPortsModified == False:
                # remove the augend port from the inputDataPorts
                augendPort = self.inputDataPortsInfo[self.augend]
                #print("To be removed Augend Port", augendPort.name)
                # remove the augend from the inputDataPorts
                self.inputDataPorts.remove(augendPort)
                # remove augend inputRegisters
        
        self._input1 = value
        self.augend = value

        
        
    @property
    def input2(self):
        self._input2 = self.addend
        return self._input2

    @input2.setter
    def input2(self,value):
        #print("To be Updated Input2", value)
        if self._input2 != None:
            #print("Original Ports", self.inputDataPorts)
            #print("Original Ports Info", self.inputDataPortsInfo)
            #print("Original Input2", self._input2)
            if self.isInputDataPortsModified == False:
                # remove the addend port from the inputDataPorts
                addendPort = self.inputDataPortsInfo[self.addend]
                #print("To be removed Addend Port", addendPort.name)
                # remove the addendPort from the inputDataPorts
                self.inputDataPorts.remove(addendPort)
        
        self._input2 = value
        self.addend = value
    
    @property
    def output(self):
        self._output = self.summation
        return self._output

    @output.setter
    def output(self,value):
        self._output = value
    
    
    def connect(self):
        self.connectProperties()
        self.connectHWDescriptionPackage()
     
    def connectProperties(self):
        super().connectProperties()
        # property to store the flpFlopocoName
        self._positName = None
        # property to store the output registers
        self.outputRegisters = dict()


    def connectHWDescriptionPackage(self):
        self.hwDescription = PositAdderVHDLDescription()
    
    def main(self):
        self.process()
        self.perform()
    

    def processHWOperatorConfigurationDetails(self):
        stage1ProcessString = list()
        stage2ProcessString = list()
        hwProcessInfo = dict()

        extraOutputSignals = list()
        extraInputSignals = list()
        
        if (len(self.inputRegisters.keys()) > 0):
            # check whether the multiplier or multiplicand is there as part of the input converters
            if self.swOperator.augend in self.inputRegisters:
               
                # access the input Registers using the multiplier key
                inputRegisters = self.inputRegisters[self.swOperator.augend]
                stage1Register = inputRegisters["Stage1Register"]
                stage2Register = inputRegisters["Stage2Register"]
                extraOutputSignals = extraOutputSignals + stage1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                extraOutputSignals = extraOutputSignals + stage2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                extraInputSignals = extraInputSignals + stage1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals
                extraInputSignals = extraInputSignals + stage2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals
                
                #print("Extra VHDL Output Signals HW Description After extracting information from augend converter",extraOutputSignals)
                #print("Extra VHDL Input Signals HW Description After extracting information from augend converter",extraInputSignals)


            if self.swOperator.addend in self.inputRegisters:
                
                # access the inputRegister using the multiplicand key
                inputRegisters = self.inputRegisters[self.swOperator.addend]
                stage1Register = inputRegisters["Stage1Register"]
                stage2Register = inputRegisters["Stage2Register"]
               
                extraOutputSignals = extraOutputSignals + stage1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                extraOutputSignals = extraOutputSignals + stage2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                extraInputSignals = extraInputSignals + stage1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals
                extraInputSignals = extraInputSignals + stage2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals
                
                #print("Extra VHDL Output Signals HW Description After extracting information from addend converter",extraOutputSignals)
                #print("Extra VHDL Input Signals HW Description After extracting information from addend converter",extraInputSignals)


        augendStage1InputMBDFFInputPort = self.inputRegisters[self.swOperator.augend]["Stage1Register"].inputDataPorts[0]
        addendStage1InputMBDFFInputPort = self.inputRegisters[self.swOperator.addend]["Stage1Register"].inputDataPorts[0]
        #print("Addend Stage1 Input MBDFF Input port", addendStage1InputMBDFFInputPort)
        
        augendStage1InputMBDFFOutputPort = self.inputRegisters[self.swOperator.augend]["Stage1Register"].outputPorts[0]
        addendStage1InputMBDFFOutputPort = self.inputRegisters[self.swOperator.addend]["Stage1Register"].outputPorts[0]
        
        augendStage2InputMBDFFInputPort = self.inputRegisters[self.swOperator.augend]["Stage2Register"].inputDataPorts[0]
        addendStage2InputMBDFFInputPort = self.inputRegisters[self.swOperator.addend]["Stage2Register"].inputDataPorts[0]

        stage1ProcessString.append(augendStage1InputMBDFFInputPort.name + " " + "<=" +  " " + self.augend + "\n")
        stage1ProcessString.append(addendStage1InputMBDFFInputPort.name + " " + "<=" + " " +  self.addend + "\n")
        
        stage2ProcessString.append(augendStage2InputMBDFFInputPort.name + " " + "<=" +  " " + augendStage1InputMBDFFOutputPort.name + "\n")
        stage2ProcessString.append(addendStage2InputMBDFFInputPort.name + " " + "<=" + " " +  addendStage1InputMBDFFOutputPort.name + "\n")
                
        hwProcessInfo["1"] = stage1ProcessString    
        hwProcessInfo["2"] = stage2ProcessString

        self.configurationDetailsOfHWOperator = {"Number":self.number,"Name":self.name,"NumberSystem":"Float","PythonHWEntity":{"Name":self.name,"NumberSystem":"Float","Number":self.number,"FLPFlopocoName":self.positName,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":self.pythonHWOperatorGeneric},"InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts,"InputClockPort":self.clockPort, "InputResetPort":self.resetPort},"PythonHWArchitecture":{"Name":self.name + "_" + str(self.number),"HWArchitectureTypeName":"RTL","InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort, "ExtraOutputSignals":extraOutputSignals,"ExtraInputSignals":extraInputSignals},"PythonHWProcess":{"SensitivityList":[self.clockPort.name,self.resetPort.name],"PythonHWProcessInfo":None,"PythonHWPipelineStagesInfo":hwProcessInfo,"NumberOfPipelineStages":2,"PythonHWClockProcessInfo":{"Frequency":self.frequency, "ClockPortName":self.clockPort.name,"ClockStimulusName":(self.clockPort.name + "Stimulus")},"PythonHWResetInfo":{"ResetPortName":self.resetPort.name},"PythonHWIOStimulusProcessInfo":{"PythonHWProcessVariablesInfo":[{"Name":"fileline","Type":"line","NumberOfBits":None},{"NumberOfBits":self.numberOfBits,"Name":"inputBuffer","Type":"std_logic_vector"},{"Name":"commaBuffer","Type":"character","NumberOfBits":None}],"PythonHWProcessFileInfo":[{"Mode":"write_mode","Type":"text","Name":"outputfile","FileName":("Output" + "_" + self.name + "_" + str(self.numberOfBits)),"FileExtension":"txt"},{"Mode":"read_mode","Type":"text","Name":"inputfile","FileName":("Input" + "_" + self.name + "_" + str(self.numberOfBits)),"FileExtension":"txt"}],"InputDataPorts":self.inputDataPorts,"OutputDataPorts":self.outputPorts}}}

        self.hwDescription.configurationDetailsOfHW = self.configurationDetailsOfHWOperator
        self.hwDescription.configure()

    def process(self):
        summation = self.summation
        # print the output of the FLPAdder
        #print("Summation of FLPAdder", self.summation)
        # print the equation of the FLPAdder
        #print("Equation of the FLPAdder", self.equation)
        self.processHWGeneration()
        self.processHWOperatorConfigurationDetails()

    
    def processHWGeneration(self):
        # add the FLPMB_D_FF to the two inputs of the FLPAdders
         
        # add D_FF to augend input
        augend_D_FF = MB_D_FF()
        augend_D_FF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(self.arithmeticNodeNumber) + "_" + "AugendStage1Register"), "InputDataPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "AugendStage1Input"),"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "AugendStage1Output"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":self.numberOfBits,"ShiftDirection":"Right","NumberOfBits":self.numberOfBits, "EsBits":self.esBits}
        augend_D_FF.configure()
        augend_D_FF.process()
        augend_D_FF.perform()

            
        if self.swOperator.augend not in self.inputRegisters:
            inputRegisters = dict()
            inputRegisters["Stage1Register"] = augend_D_FF
            self.inputRegisters[self.swOperator.augend] = inputRegisters
        else:
            inputRegisters = self.inputRegisters[self.swOperator.augend]
            inputRegisters["Stage1Register"] = augend_D_FF
            self.inputRegisters[self.swOperator.augend] = inputRegisters
            
        
        # add D_FF to augend input
        augend_D_FF = MB_D_FF()
        augend_D_FF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(self.arithmeticNodeNumber) + "_" + "AugendStage2Register"), "InputDataPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "AugendStage2Input"),"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "AugendStage2Output"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":self.numberOfBits,"ShiftDirection":"Right","NumberOfBits":self.numberOfBits, "EsBits":self.esBits}
        augend_D_FF.configure()
        augend_D_FF.process()
        augend_D_FF.perform()
        
        if self.swOperator.augend not in self.inputRegisters:
            inputRegisters = dict()
            inputRegisters["Stage2Register"] = augend_D_FF
            self.inputRegisters[self.swOperator.augend] = inputRegisters
        else:
            inputRegisters = self.inputRegisters[self.swOperator.augend]
            inputRegisters["Stage2Register"] = augend_D_FF
            self.inputRegisters[self.swOperator.augend] = inputRegisters
        
        
        
        # add D_FF to addend input
        addend_D_FF = MB_D_FF()
        addend_D_FF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(self.arithmeticNodeNumber) + "_" + "AddendStage1Register"), "InputDataPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "AddendStage1Input"),"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "AddendStage1Output"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":self.numberOfBits,"ShiftDirection":"Right","NumberOfBits":self.numberOfBits, "EsBits":self.esBits}
        addend_D_FF.configure()
        addend_D_FF.process()
        addend_D_FF.perform()
        
        if self.swOperator.addend not in self.inputRegisters:
            inputRegisters = dict()
            inputRegisters["Stage1Register"] = addend_D_FF
            self.inputRegisters[self.swOperator.addend] = inputRegisters
        else:
            inputRegisters = self.inputRegisters[self.swOperator.addend]
            inputRegisters["Stage1Register"] = addend_D_FF
            self.inputRegisters[self.swOperator.addend] = inputRegisters
            
        
        # add D_FF to addend input
        addend_D_FF = MB_D_FF()
        addend_D_FF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(self.arithmeticNodeNumber) + "_" + "AddendStage2Register"), "InputDataPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "AddendStage2Input"),"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "AddendStage2Output"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":self.numberOfBits,"ShiftDirection":"Right","NumberOfBits":self.numberOfBits, "EsBits":self.esBits}
        addend_D_FF.configure()
        addend_D_FF.process()
        addend_D_FF.perform()
        
        if self.swOperator.addend not in self.inputRegisters:
            inputRegisters = dict()
            inputRegisters["Stage2Register"] = addend_D_FF
            self.inputRegisters[self.swOperator.addend] = inputRegisters
        else:
            inputRegisters = self.inputRegisters[self.swOperator.addend]
            inputRegisters["Stage2Register"] = addend_D_FF
            self.inputRegisters[self.swOperator.addend] = inputRegisters
        
        # check whether the adder has augend driver
        if self.swAdder.summation != None:
            # add FlopocoToIEEE Converter along with inputMBDFF and OutputMBDFF for the FlopocoToIEEE to summation output
            
            outputStage1Register = MB_D_FF()
            outputStage1Register.configurationDetailsOfLogic ={"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(self.arithmeticNodeNumber)), "InputDataPorts":[{"Name":str(self.summation),"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":(str(self.summation)+"Output"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":self.numberOfBits,"ShiftDirection":"Right","NumberOfBits":self.numberOfBits, "MantissaBits":self.mantissaBits,"ExponentBits":self.exponentBits}
            
            outputStage2Register = MB_D_FF()
            outputStage2Register.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(self.arithmeticNodeNumber)), "InputDataPorts":[{"Name":("posit" + self.summation + "Output"),"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("posit" + self.summation + "Input"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":self.numberOfBits,"ShiftDirection":"Right","NumberOfBits":self.numberOfBits, "MantissaBits":self.mantissaBits,"ExponentBits":self.exponentBits}}
            
            self.outputRegisters["Stage1Register"] = outputStage1Register
            self.outputRegisters["Stage2Register"] = outputStage2Register



    def perform(self):
        super().perform()
        #print("FLPAdder VHDLInstance", self.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
        # print the D_FF and other things
    
    
    def performHWGeneration(self):
        self.hwDescription.process()
        self.hwDescription.perform()

    def configure(self):
        super().configure()
    
    def reset(self):
        self.resetProperties()
        self.resetHWDescriptionPackage()
    
    def resetHWDescriptionPackage(self):
        super().resetHWDescriptionPackage()

    def resetProperties(self):
        # property to store the flpFlopocoName
        self._positName = None
        # property to store the output registers
        self.outputRegisters = dict()
