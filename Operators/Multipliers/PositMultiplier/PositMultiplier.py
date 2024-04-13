"""
Created by Karthekeyan Peirasamy
Edited on Jan 30 12:10
"""
from Operators.Multipliers.Multiplier import Multiplier
from Operators.Port.Port.Port import Port
from Logic.FF.MB_D_FF.MB_D_FF import MB_D_FF
from HWDescription.Operators.Multipliers.PositMultiplier.PositMultiplierVHDLDescription import PositMultiplierVHDLDescription

class PositMultiplier(Multiplier):

    def __init__(self):
        super().__init__()

    def connect(self):
        self.connectProperties()
        self.connectHWDescriptionPackage()
    
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
            self._positName = ("PositMult" + "_" + str(self.numberOfBits) + "_" + str(self.esBits) \
                              + "_" + "F" + str(self.frequency) + "_" + "uid"+ "2")
        return self._positName

    @positName.setter
    def positName(self,value):
        self._positName = value
    
        
    @property
    def multiplicand(self):
        return self._multiplicand

    @multiplicand.setter
    def multiplicand(self,value):
        if self.swMultiplier.multiplicand == None:
            self.swMultiplier.multiplicand = value
        if self.swMultiplier.multiplicandDriver.isDriverAPort == True:
            self._multiplicand = value
            # make a new port with configuration details
            portDetail = {"Name":self._multiplicand,"NumberOfBits":self.numberOfBits,"PortType":"Input", "ConstantSignalValue":0}
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
        elif self.swMultiplier.multiplicandDriver.isDriverAWeight == True:
            #print("Multiplicand", value)
            #print("Multiplicand Input is a weight with", value)
            if value == self.swMultiplier.weight.name:
                #print("Multiplicand is a float", value)
                self._multiplicand = self.name + str(self.number) + "Weight"
            else:
                #print("Multiplicand is a string", value)
                self._multiplicand = value

            #self._multiplicand = self.name + str(self.number) + "Weight"
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
        if self.swMultiplier.multiplier == None:
            self.swMultiplier.multiplier = value
        if self.swMultiplier.multiplierDriver.isDriverAPort == True:
            # once the port is configured, add the port to the InputDataPorts array
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
        elif self.swMultiplier.multiplierDriver.isDriverAWeight == True:
            #print("Multiplier Input is a weight with value", value)
            # the below check is made to support updation of input ports while generating vhdl
            if value == self.swMultiplier.weight.name:
                #print("Multiplier is a float", value)
                self._multiplier = self.name + str(self.number) + "Weight"
            else:
                #print("Multiplier is a string", value)
                self._multiplier = value

            #self._multiplier = self.name + str(self.number) + "Weight"
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
                portDetail = {"Name":(self.name + str(self.number) + "_" + "Output" + "_" + str(self.arithmeticNodeNumber)),"NumberOfBits":self.numberOfBits,"PortType":"Output", "ConstantSignalValue":0}                
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
        if self._input1 != None:
            if self.isInputDataPortsModified == False:
                # remove the multiplicand port from the inputDataPorts
                multiplicandPort = self.inputDataPortsInfo[self.multiplicand]
                # remove the multiplicand port from the inputDataPorts
                self.inputDataPorts.remove(multiplicandPort)

        self._input1 = value
        self.multiplicand = value
        
    @property
    def input2(self):
        self._input2 = self.multiplier
        return self._input2

    @input2.setter
    def input2(self,value):
        if self._input2 != None:
            if self.isInputDataPortsModified == False:
                #print("Original Input2", self._input2)
                # remove the multiplier port from the inputDataPorts
                multiplierPort = self.inputDataPortsInfo[self.multiplier]
                #print("Multiplier Port Name that will be removed", multiplierPort.name)
                # remove the multiplierPort from the inputDataPorts
                self.inputDataPorts.remove(multiplierPort)
                
        self._input2 = value
        self.multiplier = value
        #print("Multiplier Name", self.multiplier)
    
    @property
    def output(self):
        self._output = self.product
        return self._output

    @output.setter
    def output(self,value):
        self._output = value
        self.product = value
    
    
    def connectProperties(self):
        super().connectProperties()

        # property to store the flpFlopocoName
        self._positName = None

    def connectSWMultiplier(self):
        self.swMultiplier = SWMultiplier()

    def connectHWDescriptionPackage(self):
        self.hwDescription = PositMultiplierVHDLDescription()
   
    def configure(self):
        super().configure()            
                    
    def processHWOperatorConfigurationDetails(self):
        extraOutputSignals = list()
        extraInputSignals = list()
        weightSignals = list()
        stage1ProcessString = list()
        stage2ProcessString = list()
        hwProcessInfo = dict()
        
        if (len(self.inputRegisters.keys()) > 0):
            
            if self.swOperator.multiplicand in self.inputRegisters:
                # access the input Registers using the multiplicand key
                inputRegisters = self.inputRegisters[self.swOperator.multiplicand]
                stage1Register = inputRegisters["Stage1Register"]
                stage2Register = inputRegisters["Stage2Register"]
                extraOutputSignals = extraOutputSignals + stage1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                extraOutputSignals = extraOutputSignals + stage2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                extraInputSignals = extraInputSignals + stage1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals
                extraInputSignals = extraInputSignals + stage2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals
                
                #print("Extra VHDL Output Signals HW Description After extracting information from multiplicand ",extraOutputSignals)
                #print("Extra VHDL Input Signals HW Description After extracting information from multiplicand ",extraInputSignals)
                
            
            if self.swOperator.multiplier in self.inputRegisters:
                # access the inputRegister using the multiplicand key
                inputRegisters = self.inputRegisters[self.swOperator.multiplier]
                stage1Register = inputRegisters["Stage1Register"]
                stage2Register = inputRegisters["Stage2Register"]
               
                extraOutputSignals = extraOutputSignals + stage1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                extraOutputSignals = extraOutputSignals + stage2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                extraInputSignals = extraInputSignals + stage1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals
                extraInputSignals = extraInputSignals + stage2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals
                
                #print("Extra VHDL Output Signals HW Description After extracting information from multiplier converter",extraOutputSignals)
                #print("Extra VHDL Input Signals HW Description After extracting information from multiplier converter",extraInputSignals)
                
            
            multiplicandStage1InputMBDFFInputPort = self.inputRegisters[self.swOperator.multiplicand]["Stage1Register"].inputDataPorts[0]
            multiplierStage1InputMBDFFInputPort = self.inputRegisters[self.swOperator.multiplier]["Stage1Register"].inputDataPorts[0]
            #print("Addend Stage1 Input MBDFF Input port", addendStage1InputMBDFFInputPort)
        
            multiplicandStage1InputMBDFFOutputPort = self.inputRegisters[self.swOperator.multiplicand]["Stage1Register"].outputPorts[0]
            multiplierStage1InputMBDFFOutputPort = self.inputRegisters[self.swOperator.multiplier]["Stage1Register"].outputPorts[0]
        
            multiplicandStage2InputMBDFFInputPort = self.inputRegisters[self.swOperator.multiplicand]["Stage2Register"].inputDataPorts[0]
            multiplierStage2InputMBDFFInputPort = self.inputRegisters[self.swOperator.multiplier]["Stage2Register"].inputDataPorts[0]

            stage1ProcessString.append(multiplicandStage1InputMBDFFInputPort.name + " " + "<=" +  " " + self.multiplicand + "\n")
            stage1ProcessString.append(multiplierStage1InputMBDFFInputPort.name + " " + "<=" + " " +  self.multiplier + "\n")
        
            stage2ProcessString.append(multiplicandStage2InputMBDFFInputPort.name + " " + "<=" +  " " + multiplicandStage1InputMBDFFOutputPort.name + "\n")
            stage2ProcessString.append(multiplierStage2InputMBDFFInputPort.name + " " + "<=" + " " +  multiplierStage1InputMBDFFOutputPort.name + "\n")
                
            hwProcessInfo["1"] = stage1ProcessString    
            hwProcessInfo["2"] = stage2ProcessString


                

        # generate the python hw process info

        #print("Extra OutputSignals", extraOutputSignals)
        self.configurationDetailsOfHWOperator = {"Name":self.name,"NumberSystem":"Posit","Number":self.number,"PythonHWEntity":{"Name":self.name,"NumberSystem":"Posit","Number":self.number,"FLPFlopocoName":self.positName,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":self.pythonHWOperatorGeneric},"InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort},"PythonHWArchitecture":{"Name":self.positName,"HWArchitectureTypeName":"RTL","InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort, "ExtraOutputSignals":extraOutputSignals,"ExtraInputSignals":extraInputSignals,"WeightSignal":weightSignals},"PythonHWProcess":{"SensitivityList":[self.clockPort.name,self.resetPort.name],"PythonHWProcessInfo":None,"PythonHWPipelineStagesInfo":hwProcessInfo,"NumberOfPipelineStages":2,"PythonHWClockProcessInfo":{"Frequency":self.frequency, "ClockPortName":self.clockPort.name,"ClockStimulusName":(self.clockPort.name + "Stimulus")},"PythonHWResetInfo":{"ResetPortName":self.resetPort.name},"PythonHWIOStimulusProcessInfo":{"PythonHWProcessVariablesInfo":[{"Name":"fileline","Type":"line","NumberOfBits":None},{"NumberOfBits":self.numberOfBits,"Name":"inputBuffer","Type":"std_logic_vector"},{"Name":"commaBuffer","Type":"character","NumberOfBits":None}],"PythonHWProcessFileInfo":[{"Mode":"write_mode","Type":"text","Name":"outputfile","FileName":("Output" + "_" + self.name + "_" + str(self.numberOfBits)),"FileExtension":"txt"},{"Mode":"read_mode","Type":"text","Name":"inputfile","FileName":("Input" + "_" + self.name + "_" + str(self.numberOfBits)),"FileExtension":"txt"}],"InputDataPorts":self.inputDataPorts,"OutputDataPorts":self.outputPorts}}}
        #print(self.configurationDetailsOfHWOperator)
        self.hwDescription.configurationDetailsOfHW = self.configurationDetailsOfHWOperator
        self.hwDescription.configure()
    
    def processHWGeneration(self):

        # check whether the multiplier has driver weight or not
        #if self.swMultiplier.multiplicandDriver.isDriverAWeight == True:
        
        # add D_FF to multiplier input
        multiplier_D_FF = MB_D_FF()
        multiplier_D_FF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(self.arithmeticNodeNumber) + "_" + "MultiplierStage1Register"), "InputDataPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "MultiplierStage1Input"),"NumberOfBits":self.numberOfBits,"PortType":"Input", "ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "MultiplierStage1Output"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":self.numberOfBits,"ShiftDirection":"Right","NumberOfBits":self.numberOfBits, "EsBits":self.esBits}
        multiplier_D_FF.configure()
        multiplier_D_FF.process()
        multiplier_D_FF.perform()

        if self.swOperator.multiplier not in self.inputRegisters:
            inputRegisters = dict()
            inputRegisters["Stage1Register"] = multiplier_D_FF
            self.inputRegisters[self.swOperator.multiplier] = inputRegisters
        else:
            inputRegisters = self.inputRegisters[self.swOperator.multiplier]
            inputRegisters["Stage1Register"] = multiplier_D_FF
            self.inputRegisters[self.swOperator.multiplier] = inputRegisters
            
        # add D_FF to multiplier input
        multiplier_D_FF = MB_D_FF()
        multiplier_D_FF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(self.arithmeticNodeNumber)+ "_" + "MultiplierStage2Register"), "InputDataPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "MultiplierStage2Input"),"NumberOfBits":self.numberOfBits,"PortType":"Input", "ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "MultiplierStage2Output"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":self.numberOfBits,"ShiftDirection":"Right","NumberOfBits":self.numberOfBits, "EsBits":self.esBits}
        multiplier_D_FF.configure()
        multiplier_D_FF.process()
        multiplier_D_FF.perform()
        
        if self.swOperator.multiplier not in self.inputRegisters:
            inputRegisters = dict()
            inputRegisters["Stage2Register"] = multiplier_D_FF
            self.inputRegisters[self.swOperator.multiplier] = inputRegisters
        else:
            inputRegisters = self.inputRegisters[self.swOperator.multiplier]
            inputRegisters["Stage2Register"] = multiplier_D_FF
            self.inputRegisters[self.swOperator.multiplier] = inputRegisters

        #elif self.swMultiplier.multiplierDriver.isDriverAWeight == True:
            
        # add D_FF to multiplicand input
        multiplicand_D_FF = MB_D_FF()
        multiplicand_D_FF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(self.arithmeticNodeNumber) + "_" + "MultiplicandStage1Register"), "InputDataPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "MultiplicandStage1Input"),"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "MultiplicandStage1Output"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":self.numberOfBits,"ShiftDirection":"Right","NumberOfBits":self.numberOfBits, "EsBits":self.esBits,"ExponentBits":self.exponentBits}
        multiplicand_D_FF.configure()
        multiplicand_D_FF.process()
        multiplicand_D_FF.perform()
            
        if self.swOperator.multiplicand not in self.inputRegisters:
            inputRegisters = dict()
            inputRegisters["Stage1Register"] = multiplicand_D_FF
            self.inputRegisters[self.swOperator.multiplicand] = inputRegisters
        else:
            inputRegisters = self.inputRegisters[self.swOperator.multiplicand]
            inputRegisters["Stage1Register"] = multiplicand_D_FF
            self.inputRegisters[self.swOperator.multiplicand] = inputRegisters
            
        # add D_FF to multiplicand input
        multiplicand_D_FF = MB_D_FF()
        multiplicand_D_FF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(self.arithmeticNodeNumber) + "_" + "MultiplicandStage2Register"), "InputDataPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "MultiplicandStage2Input"),"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(self.arithmeticNodeNumber)) + "MultiplicandStage2Output"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":self.numberOfBits,"ShiftDirection":"Right","NumberOfBits":self.numberOfBits, "EsBits":self.esBits}

        multiplicand_D_FF.configure()
        multiplicand_D_FF.process()
        multiplicand_D_FF.perform()
            
            
        if self.swOperator.multiplicand not in self.inputRegisters:
            inputRegisters = dict()
            inputRegisters["Stage2Register"] = multiplicand_D_FF
            self.inputRegisters[self.swOperator.multiplicand] = inputRegisters
        else:
            inputRegisters = self.inputRegisters[self.swOperator.multiplicand]
            inputRegisters["Stage2Register"] = multiplicand_D_FF
            self.inputRegisters[self.swOperator.multiplicand] = inputRegisters
      
    def reset(self):
        self.resetProperties()
        self.resetHWDescriptionPackage()
    
    def resetHWDescriptionPackage(self):
        super().resetHWDescriptionPackage()

    def resetProperties(self):
        super().resetProperties()
        
        # property to store the flpFlopocoName
        self._positName = None
    
    
    def main(self):
        self.process()
        self.perform()
    

    def performHWGeneration(self):
        self.hwDescription.process()
        self.hwDescription.perform()


    def process(self):
        product = self.product
        # print the output of the FLPMultiplier
        #print("Product of FLPMultiplier", self.product)
        # print the equation of the FLPMultiplier
        #print("Equation of the FLPMultiplier", self.equation)
        self.processHWGeneration()
        self.processHWOperatorConfigurationDetails()
     
    def perform(self):
        super().perform()
        #print("FLPMultiplier VHDLInstance", self.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)

        #for inputPort in self.inputDataPorts:
            #print("FLPMultiplier inputPort VHDL Signal", inputPort.hwDescription.vhdlPortSignal)

    def run(self):
        self.main()
