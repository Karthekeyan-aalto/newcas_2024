"""
Created by Karthekeyan Periasamy
Edited on December 31 10:42 AM
"""

from HWDescription.HWVHDLDescription import HWVHDLDescription
from HWDescription.Architecture.Systems.PCSystem.PCSystemArchitectureVHDLDescription import PCSystemArchitectureVHDLDescription
from Operators.ShiftRegisters.MBRightSHR.MBRightSHR import MBRightSHR
from Logic.FF.MB_D_FF.MB_D_FF import MB_D_FF
from Logic.FF.Cascaded_MB_D_FF.Cascaded_MB_D_FF import Cascaded_MB_D_FF

class PCSystemVHDLDescription(HWVHDLDescription):


    def __init__(self):
        super().__init__()

    @property
    def childrenOfEachLevelOfPCTree(self):
        return self._childrenOfEachLevelOfPCTree

    @childrenOfEachLevelOfPCTree.setter
    def childrenOfEachLevelOfPCTree(self,value):
        self._childrenOfEachLevelOfPCTree = value
        self.updatePCTreeArithmeticNodesUsingChildrenOfEachLevelOfPCTree()

    
    
    def configure(self):
        
        # store the configuraiton details to a local variable
        configurationDetails = self.configurationDetailsOfHW
        #print("Configuration Details of HW", configurationDetails)

        if "PythonHWArchitecture" in configurationDetails:
            architectureConfigurationDetails = configurationDetails["PythonHWArchitecture"]
            self.arithmeticNodes = architectureConfigurationDetails["ArithmeticNodes"]
            self.childrenOfEachLevelOfPCTree = architectureConfigurationDetails["ChildrenOfEachLevelOfPCTree"]
                    
        else:
            return
        super().configure()  
           
          
    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        # connect the hw architecture packages
        self.vhdlEntityArchitectureDescription = PCSystemArchitectureVHDLDescription()


    def connect(self):
        super().connect()

    def connectProperties(self):
        self.numberOfPipelineStages = 0
        self._childrenOfEachLevelOfPCTree = None
        self.arithmeticNodes = None
        self.pythonHWPipelineStagesOfPCTree = None
 
    
    def createHWMBRightSHR(self):
        mbRightSHR = MBRightSHR()
        return mbRightSHR

    def createHWCascadedMB_D_FF(self):
        cascaded_MB_D_FF = Cascaded_MB_D_FF()
        return cascaded_MB_D_FF

    def createHWMB_D_FF(self):
        mb_d_ff = MB_D_FF()
        return mb_d_ff

    """
    # Start: updatePCTreeArithmeticNodesUsingChildrenOfEachLevelOfPCTree
    """

    def updatePCTreeArithmeticNodesUsingChildrenOfEachLevelOfPCTree(self):        
        levels = self.childrenOfEachLevelOfPCTree.keys()
        self.arithmeticNodes = list()
        for level in levels:
            # extract the arithmetic nodes
            children = self.childrenOfEachLevelOfPCTree[level]
                        
            self.arithmeticNodes = self.arithmeticNodes + children
    """
    # End: updatePCTreeArithmeticNodesUsingChildrenOfEachLevelOfPCTree
    """    
    
    def processHWPipelineStagesForPCTree(self):
        # print the dictionary of the PCTree children levels
        #print("Children of Each Level of PCTree Dictionary", self.childrenOfEachLevelOfPCTree)
        # access the number of levels
        pcTreeLevels = self.childrenOfEachLevelOfPCTree.keys()
        #print("PCTree Levels", pcTreeLevels)

        # dictionary to hold the VHDL process information for every level
        # this python pipeline stages info, will have levels as its key and value would be string which will have the 
        # connection information for every level
        pythonHWPipelineStagesInfo = dict()

        # generate number of pipeline stages for every level of childrens of PCTree
        for level in pcTreeLevels:
            #print("PCTree Level", level)
            # make a new array to hold the cascaded registers array
            # this array will be processed to obtain the connnections
            shiftRegistersInfo = dict()
            # access the number of arithmetic nodes for a given level
            for arithmeticNode in self.childrenOfEachLevelOfPCTree[level]:
                #print("Arithmetic Node Input1:",arithmeticNode.input1)
                #print("Arithmetic Node Input2:", arithmeticNode.input2)
                # arithmetic nodes needs to be tested
                if arithmeticNode.swOperator.shouldInput1AndInput2BeBalanced == True:
                    # check the register depth to know which level the arithmeticNode 
                    #print("ArithmeticNode Both the inputs needs to be balanced and its Shift Register Depth",arithmeticNode.shiftRegisterDelay)
                    # print the input 1 and inptu2 of the arithmetic node
                    #print("Arithmetic Node Input1:",arithmeticNode.input1)
                    #print("Arithmetic Node Input2:", arithmeticNode.input2)
                    #print("Arithmetic Node Depth:", arithmeticNode.shiftRegisterDelay)
                    
                    # check whether the input1 is a weight or port
                    if arithmeticNode.swOperator.input1Driver.isDriverAWeight == True:
                        
                        # input1 is a weight and as input1 needs balance, Multi bit delay register needs to be added to the input1 port
                        # form the necessary input port details
                        inputPortDetails = [{"Name":arithmeticNode.input1,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                        
                        # attach the pipeline registers built to the input port of the arithmetic node
                        mbRightSHR = MBRightSHR()
                        mbRightSHR.configurationDetailsOfOperator = {"Name":"MBRightSHR","Frequency":arithmeticNode.frequency,"NumberSystem":arithmeticNode.numberSystem,"Number":(str(arithmeticNode.number) + "_" +"Input1"+ str(arithmeticNode.arithmeticNodeNumber)), "InputDataPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + "Input1"+ "_"+str(arithmeticNode.arithmeticNodeNumber)) + "Input"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_"+"Input1"+ "_"+ str(arithmeticNode.arithmeticNodeNumber)) + "Output"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":arithmeticNode.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "ShiftRegisterResetType":"ASYNC","Depth":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages, "Width":1,"ShiftDirection":"Right","NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}

                        mbRightSHR.configure()
                        mbRightSHR.process()
                        mbRightSHR.perform()
                        
                        shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input1,"ShiftRegister":mbRightSHR}
                        
                        # check whether the level exists or not
                        if level in pythonHWPipelineStagesInfo:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            oldSHRInfo = pythonHWPipelineStagesInfo[level]
                            oldSHRInfo.append(shiftRegistersInfo)
                            pythonHWPipelineStagesInfo[level] = oldSHRInfo
                        else:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]
                            
                    elif arithmeticNode.swOperator.input1Driver.isDriverAPort == True:
                        # input1 is a port and input1 needs balance, Multi bit delay register needs to be added to the input1 port
                        # form the necessary input port details
                        inputPortDetails = [{"Name":arithmeticNode.input1,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input"}]
                        
                        # attach the pipeline registers built to the input port of the arithmetic node
                        mbRightSHR = MBRightSHR()
                        mbRightSHR.configurationDetailsOfOperator = {"Name":"MBRightSHR","Frequency":arithmeticNode.frequency,"NumberSystem":arithmeticNode.numberSystem,"Number":(str(arithmeticNode.number) + "_"+"Input1"+ "_"+str(arithmeticNode.arithmeticNodeNumber)), "InputDataPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" +"Input1"+ "_"+str(arithmeticNode.arithmeticNodeNumber)) + "Input"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_"+"Input1"+ "_"+ str(arithmeticNode.arithmeticNodeNumber)) + "Output"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Output", "ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":arithmeticNode.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages, "Width":1,"ShiftDirection":"Right","NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                        
                        mbRightSHR.configure()
                        mbRightSHR.process()
                        mbRightSHR.perform()
                        
                        shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input1,"ShiftRegister":mbRightSHR}
                        
                        # check whether the level exists or not
                        if level in pythonHWPipelineStagesInfo:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            oldSHRInfo = pythonHWPipelineStagesInfo[level]
                            oldSHRInfo.append(shiftRegistersInfo)
                            pythonHWPipelineStagesInfo[level] = oldSHRInfo
                        else:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]
                        
                    if arithmeticNode.swOperator.input2Driver.isDriverAPort == True:
                        # input2 is a port and input2 needs balance, Multi bit delay register needs to be added to the input1 port
                        # form the necessary input port details
                        inputPortDetails = [{"Name":arithmeticNode.input2,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                        
                        # attach the pipeline registers built to the input port of the arithmetic node
                        mbRightSHR = MBRightSHR()
                        mbRightSHR.configurationDetailsOfOperator = {"Name":"MBRightSHR","Frequency":arithmeticNode.frequency,"NumberSystem":arithmeticNode.numberSystem,"Number":(str(arithmeticNode.number) + "_"+"Input2"+ "_" +str(arithmeticNode.arithmeticNodeNumber)), "InputDataPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + "Input2"+ "_"+str(arithmeticNode.arithmeticNodeNumber)) + "Input"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_"+"Input2"+ "_"+str(arithmeticNode.arithmeticNodeNumber)) + "Output"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":arithmeticNode.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages, "Width":1,"ShiftDirection":"Right","NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}

                        mbRightSHR.configure()
                        mbRightSHR.process()
                        mbRightSHR.perform()
                        
                        shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input2,"ShiftRegister":mbRightSHR}
                        
                        # check whether the level exists or not
                        if level in pythonHWPipelineStagesInfo:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            oldSHRInfo = pythonHWPipelineStagesInfo[level]
                            oldSHRInfo.append(shiftRegistersInfo)
                            pythonHWPipelineStagesInfo[level] = oldSHRInfo
                        else:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]

                    # check whether the balancing input is a weight or port
                    elif arithmeticNode.swOperator.input2Driver.isDriverAWeight == True:
                        
                        # input2 is a weight and as input2 needs balance, Multi bit delay register needs to be added to the input1 port
                        # form the necessary input port details
                        inputPortDetails = [{"Name":arithmeticNode.input2,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                        
                        # attach the pipeline registers built to the input port of the arithmetic node
                        mbRightSHR = MBRightSHR()
                        mbRightSHR.configurationDetailsOfOperator = {"Name":"MBRightSHR","Frequency":arithmeticNode.frequency,"NumberSystem":arithmeticNode.numberSystem,"Number":(str(arithmeticNode.number) + "_"+"Input2"+"_"+str(arithmeticNode.arithmeticNodeNumber)), "InputDataPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" +"Input2"+"_"+str(arithmeticNode.arithmeticNodeNumber)) + "Input"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" +"Input2"+"_"+ str(arithmeticNode.arithmeticNodeNumber)) + "Output"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":arithmeticNode.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages, "Width":1,"ShiftDirection":"Right","NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                        
                        mbRightSHR.configure()
                        mbRightSHR.process()
                        mbRightSHR.perform()
                        
                        shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input2,"ShiftRegister":mbRightSHR}
                        
                        # check whether the level exists or not
                        if level in pythonHWPipelineStagesInfo:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            oldSHRInfo = pythonHWPipelineStagesInfo[level]
                            oldSHRInfo.append(shiftRegistersInfo)
                            pythonHWPipelineStagesInfo[level] = oldSHRInfo
                        else:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]
                        
                elif arithmeticNode.swOperator.shouldInput1BeBalanced == True:
                
                    # as input2 is already balanced we can directly add the cascaded shift registers to that input
                    # form the necessary input port details
                    inputPortDetails = [{"Name":arithmeticNode.input2,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                    
                    # attach the pipeline d flipflops built to the port of the arithmetic node
                    cascaded_MB_D_FF = Cascaded_MB_D_FF()
                    cascaded_MB_D_FF.configurationDetailsOfLogic = {"Name":"Cascaded_MB_D_FF","Frequency":arithmeticNode.frequency,"InputDataPorts":inputPortDetails,"Number":(level+"_"+str(arithmeticNode.number)),"CascadeRegisters":True,"NumberSystem":"Posit","NumberOfCascadeStages":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages,"FFResetType":"ASYNC","Width":arithmeticNode.numberOfBits,"NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                    cascaded_MB_D_FF.configure()
                    cascaded_MB_D_FF.process()
                    cascaded_MB_D_FF.perform()

                                         
                    shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input2,"CascadedRegisters":cascaded_MB_D_FF}
                            
                    # check whether the level exists or not
                    if level in pythonHWPipelineStagesInfo:
                        # access the level using it as key and update the value object with shiftRegisterInfo
                        oldSHRInfo = pythonHWPipelineStagesInfo[level]
                        oldSHRInfo.append(shiftRegistersInfo)
                        pythonHWPipelineStagesInfo[level] = oldSHRInfo
                    else:
                        # access the level using it as key and update the value object with shiftRegisterInfo
                        pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]
                        
                    
                    # check whether the balancing input is a weight or port
                    if arithmeticNode.swOperator.input1Driver.isDriverAWeight == True:
                        
                        # input1 is a weight and as input1 needs balance, Multi bit delay register needs to be added to the input1 port
                        # form the necessary input port details
                        inputPortDetails = [{"Name":arithmeticNode.input1,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                        
                        # attach the pipeline registers built to the input port of the arithmetic node
                        mbRightSHR = MBRightSHR()
                        mbRightSHR.configurationDetailsOfOperator = {"Name":"MBRightSHR","Frequency":arithmeticNode.frequency,"NumberSystem":arithmeticNode.numberSystem,"Number":(str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)), "InputDataPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Input"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Output"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":arithmeticNode.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "ShiftRegisterResetType":"ASYNC","Depth":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages, "Width":1,"ShiftDirection":"Right","NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}

                        mbRightSHR.configure()
                        mbRightSHR.process()
                        mbRightSHR.perform()
                        
                        shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input1,"ShiftRegister":mbRightSHR}
                        
                        # check whether the level exists or not
                        if level in pythonHWPipelineStagesInfo:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            oldSHRInfo = pythonHWPipelineStagesInfo[level]
                            oldSHRInfo.append(shiftRegistersInfo)
                            pythonHWPipelineStagesInfo[level] = oldSHRInfo
                        else:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]

                    elif  arithmeticNode.swOperator.input1Driver.isDriverAPort:
                        # input1 is a port and input1 needs balance, Multi bit delay register needs to be added to the input1 port
                        # form the necessary input port details
                        inputPortDetails = [{"Name":arithmeticNode.input1,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                        
                        # attach the pipeline registers built to the input port of the arithmetic node
                        mbRightSHR = MBRightSHR()
                        mbRightSHR.configurationDetailsOfOperator = {"Name":"MBRightSHR","Frequency":arithmeticNode.frequency,"NumberSystem":arithmeticNode.numberSystem,"Number":(str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)), "InputDataPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Input"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Output"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":arithmeticNode.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages, "Width":1,"ShiftDirection":"Right","NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                        
                        mbRightSHR.configure()
                        mbRightSHR.process()
                        mbRightSHR.perform()
                        
                        shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input1,"ShiftRegister":mbRightSHR}
                        
                        # check whether the level exists or not
                        if level in pythonHWPipelineStagesInfo:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            oldSHRInfo = pythonHWPipelineStagesInfo[level]
                            oldSHRInfo.append(shiftRegistersInfo)
                            pythonHWPipelineStagesInfo[level] = oldSHRInfo
                        else:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]

                elif arithmeticNode.swOperator.shouldInput2BeBalanced == True:
            
                    # input1 is driven by another node from the lower level
                    # form the necessary input port details
                    inputPortDetails = [{"Name":arithmeticNode.input1,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                    
                    # attach the pipeline registers built to the input port of the arithmetic node
                    cascaded_MB_D_FF = Cascaded_MB_D_FF()
                    cascaded_MB_D_FF.configurationDetailsOfLogic = {"Name":"Cascaded_MB_D_FF","Frequency":arithmeticNode.frequency,"InputDataPorts":inputPortDetails,"Number":(level+"_"+str(arithmeticNode.number)),"CascadeRegisters":True,"NumberSystem":"Posit","NumberOfCascadeStages":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages,"FFResetType":"ASYNC","Width":arithmeticNode.numberOfBits,"NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                    cascaded_MB_D_FF.configure()
                    cascaded_MB_D_FF.process()
                    cascaded_MB_D_FF.perform()
                    
                     
                    shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input1,"CascadedRegisters":cascaded_MB_D_FF}
                            
                    # check whether the level exists or not
                    if level in pythonHWPipelineStagesInfo:
                        # access the level using it as key and update the value object with shiftRegisterInfo
                        oldSHRInfo = pythonHWPipelineStagesInfo[level]
                        oldSHRInfo.append(shiftRegistersInfo)
                        pythonHWPipelineStagesInfo[level] = oldSHRInfo
                    else:
                        # access the level using it as key and update the value object with shiftRegisterInfo
                        pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]
                    
                    
                    # check whether the balancing input is a weight or port
                    if arithmeticNode.swOperator.input2Driver.isDriverAWeight == True:
                        
                        # input1 is a weight and as input1 needs balance, Multi bit delay register needs to be added to the input1 port
                        # form the necessary input port details
                        inputPortDetails = [{"Name":arithmeticNode.input2,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                        
                        # attach the pipeline registers built to the input port of the arithmetic node
                        mbRightSHR = MBRightSHR()
                        mbRightSHR.configurationDetailsOfOperator = {"Name":"MBRightSHR","Frequency":arithmeticNode.frequency,"NumberSystem":arithmeticNode.numberSystem,"Number":(str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)), "InputDataPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Input"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Output"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":arithmeticNode.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages, "Width":1,"ShiftDirection":"Right","NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                        
                        mbRightSHR.configure()
                        mbRightSHR.process()
                        mbRightSHR.perform()
                        
                        shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input2,"ShiftRegister":mbRightSHR}
                        
                        # check whether the level exists or not
                        if level in pythonHWPipelineStagesInfo:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            oldSHRInfo = pythonHWPipelineStagesInfo[level]
                            oldSHRInfo.append(shiftRegistersInfo)
                            pythonHWPipelineStagesInfo[level] = oldSHRInfo
                        else:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]
                    elif arithmeticNode.swOperator.input2Driver.isDriverAPort == True:
                        # input1 is a port and input1 needs balance, Multi bit delay register needs to be added to the input1 port
                        # form the necessary input port details
                        inputPortDetails = [{"Name":arithmeticNode.input2,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input"}]
                        
                        # attach the pipeline registers built to the input port of the arithmetic node
                        mbRightSHR = MBRightSHR()
                        mbRightSHR.configurationDetailsOfOperator = {"Name":"MBRightSHR","Frequency":arithmeticNode.frequency,"NumberSystem":arithmeticNode.numberSystem,"Number":(str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)), "InputDataPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Input"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Output"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":arithmeticNode.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages, "Width":1,"ShiftDirection":"Right","NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}

                        mbRightSHR.configure()
                        mbRightSHR.process()
                        mbRightSHR.perform()
                        
                        shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input2,"ShiftRegister":mbRightSHR}
                        
                        # check whether the level exists or not
                        if level in pythonHWPipelineStagesInfo:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            oldSHRInfo = pythonHWPipelineStagesInfo[level]
                            oldSHRInfo.append(shiftRegistersInfo)
                            pythonHWPipelineStagesInfo[level] = oldSHRInfo
                        else:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]

                else:
                    #print("ArithmeticNode inputs are balanced in level", level)
                    
                    # access the inputs of the arithmetic nodes
                    #print("Balanced Arithmetic Node Input1", arithmeticNode.input1)
                    #print("Balanced Arithmetic Node Input2", arithmeticNode.input2)

                    # access the ports of the respective arithmetic nodes
                    #print("Length of the Arithmetic Node ports",len(arithmeticNode.inputPorts))
                    
                    # for some levels there is not need of balancing inputs 
                    if len(arithmeticNode.swOperator.drivers) == 0:
                        # if the arithmetic node has input ports
                        # check which input is port and the other is a weight, if so add cascaded registers and shift registers accordingly
                        # check whether which input is a port
                        if arithmeticNode.swOperator.input1Driver.isDriverAPort == True:
                            # input1 is the port
                            # form the necessary input port details
                            inputPortDetails = [{"Name":arithmeticNode.input1,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                            
                            # attach the pipeline registers built to the port of the arithmetic node
                            cascaded_MB_D_FF = Cascaded_MB_D_FF()
                            cascaded_MB_D_FF.configurationDetailsOfLogic = {"Name":"Cascaded_MB_D_FF","Frequency":arithmeticNode.frequency,"InputDataPorts":inputPortDetails,"Number":(level+"_"+str(arithmeticNode.number)),"CascadeRegisters":True,"NumberSystem":"Posit","NumberOfCascadeStages":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages,"FFResetType":"ASYNC", "Width":arithmeticNode.numberOfBits,"NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                            cascaded_MB_D_FF.configure()
                            cascaded_MB_D_FF.process()
                            cascaded_MB_D_FF.perform()
                            
                            # form the dictionary to store the information of the arithmetic node, and the input along with the cascaded input registers
                            shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input1,"CascadedRegisters":cascaded_MB_D_FF}
                            # check whether the level exists or not
                            if level in pythonHWPipelineStagesInfo:
                               # access the level using it as key and update the value object with shiftRegisterInfo
                               oldSHRInfo = pythonHWPipelineStagesInfo[level]
                               #print("Old PythonHWPipelineStages Info", pythonHWPipelineStagesInfo)
                               oldSHRInfo.append(shiftRegistersInfo)
                               pythonHWPipelineStagesInfo[level] = oldSHRInfo
                               #print("New PythonHWPipelineStages Info", pythonHWPipelineStagesInfo)

                            else:
                                # access the level using it as key and update the value object with shiftRegisterInfo
                                pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]

                        elif arithmeticNode.swOperator.input1Driver.isDriverAWeight == True:
                            # input1 is a weight and as input1 needs balance, Multi bit delay register needs to be added to the input1 port
                            # form the necessary input port details
                            inputPortDetails = [{"Name":arithmeticNode.input1,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                        
                            # attach the pipeline registers built to the input port of the arithmetic node
                            mbRightSHR = MBRightSHR()
                            mbRightSHR.configurationDetailsOfOperator = {"Name":"MBRightSHR","Frequency":arithmeticNode.frequency,"NumberSystem":arithmeticNode.numberSystem,"Number":(str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)), "InputDataPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Input"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Output"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":arithmeticNode.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages, "Width":1,"ShiftDirection":"Right","NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                        
                            mbRightSHR.configure()
                            mbRightSHR.process()
                            mbRightSHR.perform()
                            
                            shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input1,"ShiftRegister":mbRightSHR}
                            
                            # check whether the level exists or not
                            if level in pythonHWPipelineStagesInfo:
                                # access the level using it as key and update the value object with shiftRegisterInfo
                                oldSHRInfo = pythonHWPipelineStagesInfo[level]
                                oldSHRInfo.append(shiftRegistersInfo)
                                pythonHWPipelineStagesInfo[level] = oldSHRInfo
                            else:
                                # access the level using it as key and update the value object with shiftRegisterInfo
                                pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]

                        
                        
                        if arithmeticNode.swOperator.input2Driver.isDriverAPort == True:
                            # input2 is the port
                            # form the necessary input port details
                            inputPortDetails = [{"Name":arithmeticNode.input2,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                            
                            # attach the pipeline registers built to the port of the arithmetic node
                            cascaded_MB_D_FF = Cascaded_MB_D_FF()
                            cascaded_MB_D_FF.configurationDetailsOfLogic = {"Name":"Cascaded_MB_D_FF","Frequency":arithmeticNode.frequency,"InputDataPorts":inputPortDetails,"Number":(level+"_"+str(arithmeticNode.number)),"CascadeRegisters":True,"NumberSystem":"Posit","NumberOfCascadeStages":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages,"FFResetType":"ASYNC","Width":arithmeticNode.numberOfBits,"NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                            cascaded_MB_D_FF.configure()
                            cascaded_MB_D_FF.process()
                            cascaded_MB_D_FF.perform()


                            # form the dictionary to store the information of the arithmetic node, and the input along with the cascaded input registers
                            shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input2,"CascadedRegisters":cascaded_MB_D_FF}
                            # check whether the level exists or not
                            if level in pythonHWPipelineStagesInfo:
                               # access the level using it as key and update the value object with shiftRegisterInfo
                               oldSHRInfo = pythonHWPipelineStagesInfo[level]
                               #print("Old PythonHWPipelineStages Info", pythonHWPipelineStagesInfo)
                               oldSHRInfo.append(shiftRegistersInfo)
                               pythonHWPipelineStagesInfo[level] = oldSHRInfo
                               #print("New PythonHWPipelineStages Info", pythonHWPipelineStagesInfo)

                            else:
                                # access the level using it as key and update the value object with shiftRegisterInfo
                                pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]
                        
                        elif arithmeticNode.swOperator.input2Driver.isDriverAWeight == True:
                            
                            # input2 is a weight and as input1 could be a port, Multi bit delay register needs to be added to the input1 port
                            # form the necessary input port details
                            inputPortDetails = [{"Name":arithmeticNode.input2,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                        
                            # attach the pipeline registers built to the input port of the arithmetic node
                            mbRightSHR = MBRightSHR()
                            mbRightSHR.configurationDetailsOfOperator = {"Name":"MBRightSHR","Frequency":arithmeticNode.frequency,"NumberSystem":arithmeticNode.numberSystem,"Number":(str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)), "InputDataPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Input"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mbRightSHR" + (str(arithmeticNode.number) + "_" + str(arithmeticNode.arithmeticNodeNumber)) + "Output"),"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":arithmeticNode.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "ShiftRegisterResetType":"ASYNC","Depth":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages, "Width":1,"ShiftDirection":"Right","NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                        
                            mbRightSHR.configure()
                            mbRightSHR.process()
                            mbRightSHR.perform()
                            
                            shiftRegistersInfo = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input2,"ShiftRegister":mbRightSHR}
                            
                            # check whether the level exists or not
                            if level in pythonHWPipelineStagesInfo:
                                # access the level using it as key and update the value object with shiftRegisterInfo
                                oldSHRInfo = pythonHWPipelineStagesInfo[level]
                                oldSHRInfo.append(shiftRegistersInfo)
                                pythonHWPipelineStagesInfo[level] = oldSHRInfo
                            else:
                                # access the level using it as key and update the value object with shiftRegisterInfo
                                pythonHWPipelineStagesInfo[level] = [shiftRegistersInfo]

                     
                    elif len(arithmeticNode.swOperator.drivers) > 1:
                        # input1 and input2 is driven by another node
                        
                        # form the necessary input port details
                        input1PortDetails = [{"Name":arithmeticNode.input1,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                        
                        # print the inputPortDetails 
                        #print("Input1PortDetails", input1PortDetails)
                        #print("ArithmeticNode is driven by arithmetic nodes from lower level")
                        # attach the pipeline registers built to the port of the arithmetic node
                        #print("Original ArithmeticNode Input1", arithmeticNode.input1)
                        
                        # two sets of cascaded registers are needed to pipeline two inputs of the arithmetic node
                        cascaded_MB_D_FFInput1 = Cascaded_MB_D_FF()
                        cascaded_MB_D_FFInput1.configurationDetailsOfLogic = {"Name":"Cascaded_MB_D_FF","Frequency":arithmeticNode.frequency,"InputDataPorts":input1PortDetails,"Number":(level + "_" + "Input1" + "_"+str(arithmeticNode.number)),"CascadeRegisters":True,"NumberSystem":"Posit","NumberOfCascadeStages":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages,"FFResetType":"ASYNC","Depth":1, "Width":arithmeticNode.numberOfBits,"NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                        cascaded_MB_D_FFInput1.configure()
                        cascaded_MB_D_FFInput1.process()
                        cascaded_MB_D_FFInput1.perform()

                        #print("Updated ArithmeticNode Input1", arithmeticNode.input1)

                                                
                        input2PortDetails = [{"Name":arithmeticNode.input2,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                        # print the inputPortDetails 
                        #print("Input1PortDetails", input2PortDetails)
                        
                        cascaded_MB_D_FFInput2 = Cascaded_MB_D_FF()
                        cascaded_MB_D_FFInput2.configurationDetailsOfLogic = {"Name":"Cascaded_MB_D_FF","Frequency":arithmeticNode.frequency,"InputDataPorts":input2PortDetails,"Number":(level + "_" + "Input2" + "_"+str(arithmeticNode.number)),"CascadeRegisters":True,"NumberSystem":"Posit","NumberOfCascadeStages":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages,"FFResetType":"ASYNC","Width":arithmeticNode.numberOfBits,"NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
                        cascaded_MB_D_FFInput2.configure()
                        cascaded_MB_D_FFInput2.process()
                        cascaded_MB_D_FFInput2.perform()

                        
                        # form the dictionary to store the information of the arithmetic node, and the input along with the cascaded input registers
                        shiftRegistersInfoInput1 = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input1,"CascadedRegisters":cascaded_MB_D_FFInput1}
                        shiftRegistersInfoInput2 = {"ArithmeticNode":arithmeticNode,"Input":arithmeticNode.input2,"CascadedRegisters":cascaded_MB_D_FFInput2}

                        # check whether the level exists or not
                        if level in pythonHWPipelineStagesInfo:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            oldSHRInfo = pythonHWPipelineStagesInfo[level]
                            oldSHRInfo.append(shiftRegistersInfoInput1)
                            oldSHRInfo.append(shiftRegistersInfoInput2)
                            pythonHWPipelineStagesInfo[level] = oldSHRInfo
                        else:
                            # access the level using it as key and update the value object with shiftRegisterInfo
                            pythonHWPipelineStagesInfo[level] = [shiftRegistersInfoInput1,shiftRegistersInfoInput2]

                    # access the weight port and update the weight depth relative to the pipeline stages built
                    # update the definiton of the arithmetic nodes
                    continue
        
        # print the arithmetic node information
        #print("Pipeline HW levels Info", pythonHWPipelineStagesInfo)
        
        if "1" in self.childrenOfEachLevelOfPCTree.keys():
            arithmeticNode = self.childrenOfEachLevelOfPCTree["1"][0]
            # access the level MMACUnit arithmetic Node that is mostly a sumNode
            # generate a new cascaed MB_D_FF flipflop based on the pipeline
            # form the necessary input port details
            outputPortDetails = [{"Name":arithmeticNode.output,"NumberOfBits":arithmeticNode.numberOfBits,"PortType":"Output","ConstantSignalValue":0}]

            cascaded_MB_D_FFOutput = Cascaded_MB_D_FF()
            cascaded_MB_D_FFOutput.configurationDetailsOfLogic = {"Name":"Cascaded_MB_D_FF","Frequency":arithmeticNode.frequency,"InputDataPorts":outputPortDetails,"Number":(str(1) + "_" + "Output" + "_"+str(arithmeticNode.number)),"CascadeRegisters":True,"NumberSystem":"Posit","NumberOfCascadeStages":self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStages,"FFResetType":"ASYNC","Width":arithmeticNode.numberOfBits,"NumberOfBits":arithmeticNode.numberOfBits, "EsBits":arithmeticNode.esBits}
            cascaded_MB_D_FFOutput.configure()
            cascaded_MB_D_FFOutput.process()
            cascaded_MB_D_FFOutput.perform()
            
            # form the dictionary to store the information of the arithmetic node, and the input along with the cascaded input registers
            cascadedRegisterInfo = {"ArithmeticNode":arithmeticNode,"Output":arithmeticNode.output,"CascadedRegisters":cascaded_MB_D_FFOutput}
            
            # check whether the level exists or not
            if level in pythonHWPipelineStagesInfo:
                # access the level using it as key and update the value object with shiftRegisterInfo
                oldSHRInfo = pythonHWPipelineStagesInfo[level]
                oldSHRInfo.append(cascadedRegisterInfo)
                pythonHWPipelineStagesInfo[level] = oldSHRInfo
            else:
                # access the level using it as key and update the value object with shiftRegisterInfo
                pythonHWPipelineStagesInfo[level] = [cascadedRegisterInfo]


        return pythonHWPipelineStagesInfo

    
    
    def generateHWPipelineProcessUsingPipelineStagesOfPCTree(self):
        """
        The function will help build the connection as part of the hw process, the rest of the connection is built
        
        1. First, access every level of the MMACUnit from the pythonHWPipelineStages
        2. For every level, access the key cascaded registers
        3. Then, access the number of pipline stages and build a forloop
        4. Using the for loop index, access the information of the arithmetic node, cascadedRegister, input that cascaded registers are connected to 
        5. Check the inputName whether its is connected to the arithmeticnode input1 or input2
        6. If the input1 or input2 is not a port, then input1 or input2 is connected to another node 
        7. Now, replace the input1 or input2 of the arithmetic node with the input and output of the cascaded register (single MBRightSHR objects)
        7. For example, access the index 0 MBRightSHR, replace the input of the MBRightSHR with the arithmetic node input and replace the arithmetic node input with the cascaded registers last index MBRightSHR.
        8. Additionally, the if the input2 is not a port, then check the input1 whether it needs to balanced or not
        9. If the input1 needs to be balanced, update the input1 definition alone by replacing the necessary inputs and outputs 
        8. If the input1 or the input2 is a port, then form the VHDL process information
        9. While forming the process information, do not replace the input and output of the shift registers in the cascaded registers
        10. Rather, access the cascaded registers mbrightSHR registers input and form the process with the correspoding arithmetic nodes input ports
        """
        # access the number of levels of mmacunit
        pcTreeLevels = self.childrenOfEachLevelOfPCTree.keys()
        pythonHWPipelineStagesInfo = self.pythonHWPipelineStagesOfPCTree
        #print("PCTree Level Based Pipeline Stages Info", pythonHWPipelineStagesInfo)
        pythonHWPipelineStagesProcessInfo = dict()
        pythonHWPipelineStagesAsyncResetProcessInfo = dict()
        
        for level in pythonHWPipelineStagesInfo.keys():
            #print("The level on which the pipeline stages will be added", level)
            for levelDetails in pythonHWPipelineStagesInfo[level]:
                #print("Level details", levelDetails)
                # change the input of the arithmetic node by attaching the output of the last index mbrightshr register from the
                # cascaded registers
                
                # variable to store and access the arithmetic nodes
                arithmeticNode = None
                # variable to store the input details or the input name
                inputName = None
                # variable to store the cascadedMBRightSHR
                cascaded_MB_D_FF = None
                # variable to store the port status of an input variable
                isInputNameAPort = False
                
                if "ArithmeticNode" in levelDetails:
                    arithmeticNode = levelDetails["ArithmeticNode"]
                    #print("The name of the arithmetic node",arithmeticNode.name)
                    #print("The number of the arithmetic node", arithmeticNode.number)

                if "Input" in levelDetails:
                    # access the input details, which is one of the input of the arithmetic node
                    #print("The input that the cascaded mbrightSHR is connected to is", levelDetails["Input"])
                    # check whether the input is input1 or the input2 of the arithmetic node
                    inputName = levelDetails["Input"]
                    #print("The set inputName", inputName)
                                        
                    
                if "CascadedRegisters" in levelDetails:
                    
                    cascaded_MB_D_FF = levelDetails["CascadedRegisters"]
                    # access the 0th MB_D_FF from the cascaded MB_D_FF
                    othMB_D_FF = cascaded_MB_D_FF.cascadedRegisters[0]
                    # access the input of the othMB_D_FF
                    othMB_D_FFName = othMB_D_FF.inputDataPorts[0].name
                    # print the name of the othMB_D_FF
                    #print("Original othMB_D_FFName", othMB_D_FFName)
                    
                    # access the last index mb_d_ff from the cascaded mb_d_ff
                    lastIndexMB_D_FF = cascaded_MB_D_FF.cascadedRegisters[len(cascaded_MB_D_FF.cascadedRegisters)-1]
                    # access the input of the lastIndexMB_D_FF
                    lastIndexMB_D_FFName = lastIndexMB_D_FF.inputDataPorts[0].name
                    # print the name of the othMB_D_FF
                    #print("Original lastIndexMB_D_FF Name", lastIndexMB_D_FFName)

                    
                    if inputName == arithmeticNode.input1:
                        
                        if arithmeticNode.swOperator.input1Driver.isDriverAnArithmeticNode == True:
                            
                            arithmeticNodeInput2Registers = None
                                
                            #print("InputName is attached to the arithmeticNode Input1")
                            # replace the name of the othMB_D_FF name with the arithmeticNode input1 stage1Register
                            inputRegisters = None                             
                            if arithmeticNode.inputRegisters != None:
                                #print("Input Registers",arithmeticNode.inputRegisters)
                                #print("ArithmeticNode SWOperator Input1", arithmeticNode.swOperator.input1)
                                #print("ArithmeticNode Name", arithmeticNode.name)
                                #print("ArithmeticNode Input1", arithmeticNode.input1)
                                if arithmeticNode.swOperator.input1 in arithmeticNode.inputRegisters:
                                    inputRegisters = arithmeticNode.inputRegisters[arithmeticNode.swOperator.input1]

                            #print("Stage1 & Stage2 Register",inputRegisters)
                            stage1Register = inputRegisters["Stage1Register"]
                            stage2Register = inputRegisters["Stage2Register"]

                            othMB_D_FF.inputDataPorts[0].name = arithmeticNode.input1
                            # update the inputdata ports modified property of the MB_D_FF operator
                            othMB_D_FF.isInputDataPortsModified = True
                                
                            # print the updated MB_D_FF VHDL Description
                            # reset the cascaded_MB_D_FF name
                            cascaded_MB_D_FF.inputDataPorts[0].name = othMB_D_FF.inputDataPorts[0].name
                            # update the cascaded_MB_D_FF
                            cascaded_MB_D_FF.isInputDataPortsModified = True
                                
                            # replace the stage1Register input with the last index mb_d_ff output
                            # connect the stage1Register and stage2Register
                            # replace the arithmeticNode inpu1 with the stage2Register outputname
                            # Then update the vhdl description of the arithmetic node
                            #print("Original Stage1Register VHDL PythonHW", stage1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW)
                            stage1Register.inputDataPorts[0].name = lastIndexMB_D_FF.outputPorts[0].name
                            stage1Register.isInputDataPortsModified = True
                            #print("Updated Stage1Register VHDL PythonHW", stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                            #print("Original Stage1Register VHDL PythonHW", stage2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW)
                            stage2Register.inputDataPorts[0].name = stage1Register.outputPorts[0].name
                            stage2Register.isInputDataPortsModified = True
                            #print("Updated Stage2Register VHDL PythonHW", stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                            #print("Original arithmeticNode VHDL PythonHW", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                            arithmeticNode.input1 = stage2Register.outputPorts[0].name
                            arithmeticNode.isInputDataPortsModified = True

                            #print("ArithmeticNode Cascaded",arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals)
                            #print("Updated arithmeticNode VHDL at Input1", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                                 
                            # print the original python hw of the cascade register
                            #print("Updated Cascaded_MB_D_FF Python HW", cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW)

                            self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                            #print("Cascaded MB_D_FF OutputSignals", cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals)

                            # check whether the input2 of the arithmeticNode is added with PipelinedRegsiters or not
                            if arithmeticNode.isInput2PipelinedWithRegisters == True:
                                
                                # before updating the vhdl instance of the arithmetic node
                                # access the input2 registers and store it in a local variables
                                arithmeticNodeInput2Register = arithmeticNode.inputRegisters["Input2"]
                                # update the vhdl instance with two input based vhdl instances
                                #arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascadedMB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage2Register.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage1Register.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                #print("ArithmeticNode HWDescription VHDL at Input1", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                                if isinstance(arithmeticNodeInput2Register,Cascaded_MB_D_FF):
                                   
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

                                elif isinstance(arithmeticNodeInput2Register,MBRightSHR):
                                    # update the vhdl instance with two input based vhdl instances
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition


                                
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals
                                
                                # updated the inputPipelinedWithShiftRegisterInfo with input2 cascadedMB_D_FF
                                arithmeticNode.inputRegisters["Input1"] = cascaded_MB_D_FF
                                arithmeticNode.isInput1PipelinedWithRegisters = True
    
                            else:

                                # update the python hw of the cascaded mb d ff with the input registers attached to the input1
                                cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW = cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                
                                #print("Updated Cascaded_MB_D_FF VHDL at Input1", cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW)
                                arithmeticNode.inputRegisters["Input1"] = cascaded_MB_D_FF
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput1PipelinedWithRegisters = True
                                #print("Stage1 & Stage2 & Cascaded_MB_D_FF Registers",arithmeticNode.inputRegisters)                               
                                #print("VHDL Instances in the form of python HW",cascadedMBRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW)
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals


                        elif arithmeticNode.swOperator.input1Driver.isDriverAPort == True:
                            # print the port
                            #print("The port Name is", arithmeticNode.input1)
                            #print("Computation to be done on input that is a port attached to Input1")
                            # add the original arithmetic node input name to the process details dictionary
                            hwPipelineProcessString = othMB_D_FF.inputDataPorts[0].name + " " + "<=" + " " + arithmeticNode.input1 + ";"
                            hwPipelineAsyncResetProcessString = othMB_D_FF.inputDataPorts[0].name + " " + "<=" + " " + "(" + "others" + "=>" + "'" + "0" + "'" + ")" + ";"
                            #print("InputName is attached to the arithmeticNode Input1")
                            # replace the name of the othMB_D_FF name with the arithmeticNode.input1
                            othMB_D_FF.inputDataPorts[0].name = arithmeticNode.input1
                            # reset the cascadedMB_D_FF name
                            cascaded_MB_D_FF.inputDataPorts[0].name = othMB_D_FF.inputDataPorts[0].name
                            
                            inputRegisters = None                        
                            if arithmeticNode.inputRegisters != None:
                                #print("Input Registers",arithmeticNode.inputRegisters)
                                #print("ArithmeticNode SWOperator Input1", arithmeticNode.swOperator.input2)
                                #print("ArithmeticNode Name", arithmeticNode.name)
                                #print("ArithmeticNode Input2", arithmeticNode.input2)

                                if arithmeticNode.swOperator.input1 in arithmeticNode.inputRegisters:
                                    inputRegisters = arithmeticNode.inputRegisters[arithmeticNode.swOperator.input1]

                            #print("Stage1 & Stage2 Register",inputRegisters)
                            stage1Register = inputRegisters["Stage1Register"]
                            stage2Register = inputRegisters["Stage2Register"]

                            # replace the arithmeticNode.input1 with the name of the last index mb_D_FF output
                            # replace the stage1Register input with the last index mb_d_ff outputports name
                            # connect the stage1 register to the stage2 register
                            # replace the arithmeticNode input1 with the stage2 register output name
                            stage1Register.inputDataPorts[0].name = lastIndexMB_D_FF.outputPorts[0].name
                            stage1Register.isInputDataPortsModified = True

                            stage2Register.inputDataPorts[0].name = stage1Register.outputPorts[0].name
                            stage2Register.isInputDataPortsModified = True
      
                            # Then update the vhdl description of the arithmetic node
                            arithmeticNode.input1 = stage2Register.outputPorts[0].name
                            # update the input data ports are modified or not
                            arithmeticNode.isInputDataPortsModified = True
                            #print("ArithmeticNode Cascaded Port",arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals)
                            
                            # if there is one, update the value with the new string
                            if level in pythonHWPipelineStagesProcessInfo:
                                oldhwPipelineProcessAsyncResetStringArray = pythonHWPipelineStagesAsyncResetProcessInfo[level]
                                oldhwPipelineProcessAsyncResetStringArray.append(hwPipelineAsyncResetProcessString)
                                oldhwPipelineProcessStringArray = pythonHWPipelineStagesProcessInfo[level]
                                oldhwPipelineProcessStringArray.append(hwPipelineProcessString)
                                pythonHWPipelineStagesProcessInfo[level] = oldhwPipelineProcessStringArray
                                pythonHWPipelineStagesAsyncResetProcessInfo[level] = oldhwPipelineProcessAsyncResetStringArray
                            else:
                                pythonHWPipelineStagesProcessInfo[level] = [hwPipelineProcessString]
                                pythonHWPipelineStagesAsyncResetProcessInfo[level] = [hwPipelineAsyncResetProcessString]
                            
                            # add the output signals of the CascadedMBRightSHR to the PCSystemVHDLDescription
                            self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                            self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = cascaded_MB_D_FF.cascadedRegisters[0].hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals
                            
                            # check whether the input2 of the arithmeticNode is added with PipelinedRegsiters or not
                            if arithmeticNode.isInput2PipelinedWithRegisters == True:
                                
                                # before updating the vhdl instance of the arithmetic node
                                # access the input2 registers and store it in a local variables
                                arithmeticNodeInput2Register = arithmeticNode.inputRegisters["Input2"]
                                # update the vhdl desription of the arithmetic node updated
                                #arithmeticNode.updateVHDLInstance()
                                # attach the input1 and input2 MBRightSHR to the arithmeticNode
                                # update the vhdl instance with two input based vhdl instances
                                #arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput2Registers.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                if isinstance(arithmeticNodeInput2Register,Cascaded_MB_D_FF):
                                   
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

                                elif isinstance(arithmeticNodeInput2Register,MBRightSHR):
                                    # update the vhdl instance with two input based vhdl instances
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

                                

                                
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals

                                
                                # updated the inputRegisters with input2 cascadedMB_D_FF
                                arithmeticNode.inputRegisters["Input1"] = cascaded_MB_D_FF
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput1PipelinedWithRegisters = True

                            else:
                                # update the VHDL instance
                                cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW = cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                
                                arithmeticNode.inputRegisters["Input1"] = cascaded_MB_D_FF
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput1PipelinedWithRegisters = True
                                # print the original vhdl instance
                                #print("Original VHDL Instance", arithmeticNode.vhdlInstance)
                                # update the vhdl desription of the arithmetic node updated
                                #arithmeticNode.updateVHDLInstance()
                                                                
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals

                                
                    elif inputName == arithmeticNode.input2:

                        if arithmeticNode.swOperator.input2Driver.isDriverAnArithmeticNode == True:
                            # check if the arithmeticNode has shift register depth or forward path updated needed
                            inputRegisters = None                        
                            if arithmeticNode.inputRegisters != None:
                                #print("Input Registers",arithmeticNode.inputRegisters)
                                #print("ArithmeticNode SWOperator Input2", arithmeticNode.swOperator.input2)
                                #print("ArithmeticNode Name", arithmeticNode.name)
                                #print("ArithmeticNode Input2", arithmeticNode.input2)

                                if arithmeticNode.swOperator.input2 in arithmeticNode.inputRegisters:
                                    inputRegisters = arithmeticNode.inputRegisters[arithmeticNode.swOperator.input2]

                            #print("Stage1 & Stage2 Register",inputRegisters)
                            stage1Register = inputRegisters["Stage1Register"]
                            stage2Register = inputRegisters["Stage2Register"]

                            
                            # print the original name of the othMB_D_FF
                            #print("Original othMB_D_FF Name", othMB_D_FF.inputDataPorts[0].name)
                            othMB_D_FF.inputDataPorts[0].name = arithmeticNode.input2
                            # print the updated name of the othMB_D_FF
                            #print("Updated othMB_D_FF Name", othMB_D_FF.inputDataPorts[0].name)
                            # update the inputdata ports modified property of the MB_D_FF operator
                            othMB_D_FF.isInputDataPortsModified = True    
                             
                            # reset the cascaded_MB_D_FF name
                            cascaded_MB_D_FF.inputDataPorts[0].name = othMB_D_FF.inputDataPorts[0].name
                            # update the cascaded_MB_D_FF
                            cascaded_MB_D_FF.isInputDataPortsModified = True
                            
                            # connect the stage1Register and stage2Register
                            # replace the arithmeticNode inpu1 with the stage2Register outputname
                            # Then update the vhdl description of the arithmetic node
                            #print("Original Stage1Register VHDL PythonHW", stage1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW)
                            stage1Register.inputDataPorts[0].name = lastIndexMB_D_FF.outputPorts[0].name
                            stage1Register.isInputDataPortsModified = True
                            #print("Updated Stage1Register VHDL PythonHW", stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                            #print("Original Stage1Register VHDL PythonHW", stage2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW)
                            stage2Register.inputDataPorts[0].name = stage1Register.outputPorts[0].name
                            stage2Register.isInputDataPortsModified = True
                            #print("Updated Stage1Register VHDL PythonHW", stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                            #print("Original arithmeticNode VHDL PythonHW", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                            arithmeticNode.input2 = stage2Register.outputPorts[0].name
                            arithmeticNode.isInputDataPortsModified = True
                            #print("Updated arithmeticNode VHDL Input2", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)

                            # arithmeticNodeInput1 Registers
                            arithmeticNodeInput1Registers= None
                            
                            self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals

                                
                            # check whether the input1 of the arithmeticNode is added with PipelinedRegsiters or not
                            if arithmeticNode.isInput1PipelinedWithRegisters == True:
                                
                                # before updating the vhdl instance of the arithmetic node
                                # access the input2 cascaded_MB_D_FF and store it in a local variables
                                arithmeticNodeInput1Register = arithmeticNode.inputRegisters["Input1"]
                                #print(arithmeticNode.name)
                                
                                #update the vhdl instance with two input based vhdl instances
                                #arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                #print("Updated ArithmeticNode VHDL at Input2", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                                #print("Second Input Cascaded")
                                if isinstance(arithmeticNodeInput1Register,Cascaded_MB_D_FF):
                                    
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                    #print("Hi again")

                                elif isinstance(arithmeticNodeInput1Register,MBRightSHR):
                                    #print("First Input FLPMBRightSHR")
                                    # update the vhdl instance with two input based vhdl instances
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals

                                
                                # updated the inputPipelinedWithShiftRegisterInfo with input2 cascadedMB_D_FF
                                arithmeticNode.inputRegisters["Input2"] = cascaded_MB_D_FF
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput2PipelinedWithRegisters = True

                            else:
                                # update the python hw of the cascaded mb d ff with the input registers attached to the input1
                                cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW = cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                #print("Cascaded MB_D_FF Python HW Description", cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW)

                                arithmeticNode.inputRegisters["Input2"] = cascaded_MB_D_FF
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput2PipelinedWithRegisters = True
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals


                        elif arithmeticNode.swOperator.input2Driver.isDriverAPort == True:
                            # print the port
                            #print("The Input2 Port Name is", arithmeticNode.input2)
                            #print("Computation to be done on input that is a port attached to Input2")
                            # add the original arithmetic node input name to the process details dictionary
                            hwPipelineProcessString = othMB_D_FF.inputDataPorts[0].name + " " + "<=" + " " + arithmeticNode.input2 +  ";"
                            hwPipelineAsyncResetProcessString = othMB_D_FF.inputDataPorts[0].name + " " + "<=" + " " + "(" + "others" + "=>" + "'" + "0" + "'" + ")" + ";"

                            
                            #print("HWPipeline Process String", hwPipelineProcessString)
                            
                            #print("InputName is attached to the arithmeticNode Input2")
                            # replace the arithmeticNode.input2 with the name of the first index mbrightSHR output
                            # Then update the vhdl description of the arithmetic node
                                
                            # print the original name of the othMB_D_FF
                            #print("Original othMB_D_FF Name", othMB_D_FF.inputDataPorts[0].name)
                            othMB_D_FF.inputDataPorts[0].name = arithmeticNode.input2
                            # print the updated name of the othMB_D_FF
                            #print("Updated othMB_D_FF Name", othMB_D_FF.inputDataPorts[0].name)
                                
                            # reset the cascadedMBRightSHR name
                            cascaded_MB_D_FF.inputDataPorts[0].name = othMB_D_FF.inputDataPorts[0].name
                            
                            inputRegisters = None                        
                            if arithmeticNode.inputRegisters != None:
                                #print("Input Registers",arithmeticNode.inputRegisters)
                                #print("ArithmeticNode SWOperator Input1", arithmeticNode.swOperator.input2)
                                #print("ArithmeticNode Name", arithmeticNode.name)
                                #print("ArithmeticNode Input2", arithmeticNode.input2)

                                if arithmeticNode.swOperator.input2 in arithmeticNode.inputRegisters:
                                    inputRegisters = arithmeticNode.inputRegisters[arithmeticNode.swOperator.input2]

                            #print("Stage1 & Stage2 Register",inputRegisters)
                            stage1Register = inputRegisters["Stage1Register"]
                            stage2Register = inputRegisters["Stage2Register"]
                            
                            # replace the arithmeticNode.input2 with the name of the last index mbrightSHR output
                            # replace the stage1Register input with the last index mb_d_ff outputports name
                            # connect the stage1 register to the stage2 register
                            # replace the arithmeticNode input1 with the stage2 register output name
                            stage1Register.inputDataPorts[0].name = lastIndexMB_D_FF.outputPorts[0].name
                            stage1Register.isInputDataPortsModified = True

                            stage2Register.inputDataPorts[0].name = stage1Register.outputPorts[0].name
                            stage2Register.isInputDataPortsModified = True
      
                            # Then update the vhdl description of the arithmetic node
                            arithmeticNode.input2 = stage2Register.outputPorts[0].name
                            # update the input data ports are modified or not
                            arithmeticNode.isInputDataPortsModified = True
                            
                            #print(arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals)

                                                         
                            # if there is one, update the value with the new string
                            if level in pythonHWPipelineStagesProcessInfo:
                                oldhwPipelineProcessAsyncResetStringArray = pythonHWPipelineStagesAsyncResetProcessInfo[level]
                                oldhwPipelineProcessAsyncResetStringArray.append(hwPipelineAsyncResetProcessString)
                                oldhwPipelineProcessStringArray = pythonHWPipelineStagesProcessInfo[level]
                                oldhwPipelineProcessStringArray.append(hwPipelineProcessString)
                                pythonHWPipelineStagesProcessInfo[level] = oldhwPipelineProcessStringArray
                                pythonHWPipelineStagesAsyncResetProcessInfo[level] = oldhwPipelineProcessAsyncResetStringArray
                            else:
                                pythonHWPipelineStagesProcessInfo[level] = [hwPipelineProcessString]
                                pythonHWPipelineStagesAsyncResetProcessInfo[level] = [hwPipelineAsyncResetProcessString]
                            
                            
                            self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                            self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = cascaded_MB_D_FF.cascadedRegisters[0].hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals

                            
                            # check whether the input1 of the arithmeticNode is added with PipelinedRegsiters or not
                            if arithmeticNode.isInput1PipelinedWithRegisters == True:
                                
                                # before updating the vhdl instance of the arithmetic node
                                # access the input1 registers and store it in a local variables
                                arithmeticNodeInput1Register = arithmeticNode.inputRegisters["Input1"]
                                #print("Input1 Register",arithmeticNodeInput1Registers)
                                #print("Input1 Registers VHDL", arithmeticNodeInput1Registers.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)

                                # update the vhdl instance with two input based vhdl instances
                                #arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + arithmeticNodeInput1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition  + cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                
                                if isinstance(arithmeticNodeInput1Register,Cascaded_MB_D_FF):
                                   
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

                                elif isinstance(arithmeticNodeInput1Register,MBRightSHR):
                                    # update the vhdl instance with two input based vhdl instances
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

                                #print("ArithmeticNode VHDL Instance Definition",arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                                
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals

                                
                                # updated the inputRegisters with input2 cascadedMB_D_FF
                                arithmeticNode.inputRegisters["Input2"] = cascaded_MB_D_FF
                                # update the arithmetic node input2 pipeline with mbright shr properties
                                arithmeticNode.isInput2PipelinedWithRegisters = True

                            else:
                                # update the vhdl desription of the Cascaded_MB_D_FF
                                cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW = cascaded_MB_D_FF.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

                                arithmeticNode.inputRegisters["Input2"] = cascaded_MB_D_FF
                                # update the arithmetic node input2 pipeline with mbright shr properties
                                arithmeticNode.isInput2PipelinedWithRegisters = True
                                # print the original vhdl instance
                                #print("Original VHDL Instance", arithmeticNode.vhdlInstance)
                                # update the vhdl desription of the arithmetic node updated

                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals

                
                
                if "ShiftRegister" in levelDetails:
                    mbRightSHR = levelDetails["ShiftRegister"]                    
                    #print("ArithmeticNode", arithmeticNode.input1)
                    #print("ArithmeticNode", arithmeticNode.input2)
                    
                    #print("ArithmeticNode Input1", arithmeticNode.swOperator.input1)
                    #print("ArithmeticNode Input2", arithmeticNode.swOperator.input2)

                    #print("Input Name", inputName)
                    
                    if inputName == arithmeticNode.input1:
                        if arithmeticNode.swOperator.input1Driver.isDriverAPort == True:
                            hwPipelineProcessString =  mbRightSHR.inputDataPorts[0].name + " " + "<=" + " " + arithmeticNode.input1 + ";"
                            hwPipelineAsyncResetProcessString = mbRightSHR.inputDataPorts[0].name + " " + "<=" + " " + "(" + "others" + "=>" + "'" + "0" + "'" + ")" + ";"

                            # if there is one, update the value with the new string
                            if level in pythonHWPipelineStagesProcessInfo:
                                oldhwPipelineProcessAsyncResetStringArray = pythonHWPipelineStagesAsyncResetProcessInfo[level]
                                oldhwPipelineProcessAsyncResetStringArray.append(hwPipelineAsyncResetProcessString)
                                oldhwPipelineProcessStringArray = pythonHWPipelineStagesProcessInfo[level]
                                oldhwPipelineProcessStringArray.append(hwPipelineProcessString)
                                pythonHWPipelineStagesProcessInfo[level] = oldhwPipelineProcessStringArray
                                pythonHWPipelineStagesAsyncResetProcessInfo[level] = oldhwPipelineProcessAsyncResetStringArray
                            else:
                                pythonHWPipelineStagesProcessInfo[level] = [hwPipelineProcessString]
                                pythonHWPipelineStagesAsyncResetProcessInfo[level] = [hwPipelineAsyncResetProcessString]
                            
                            #print("MBRightSHR Attached to Input1 Depth", mbRightSHR.depth)
                            #print("Original ArithmeticNode Input1 Delay", arithmeticNode.shiftRegisterDelay)
                            #print("Level of the arithmeticNode", level)
                            #print("Current Level of the arithmeticNode in MMACUnit Tree", level)
                            if arithmeticNode.shiftRegisterDelay > 0:
                                # check whether the input2 of the arithmeticNode is added with PipelinedRegsiters or not
                                if arithmeticNode.isInput2PipelinedWithRegisters == False:
                                    # shift registers delay needs to be updated
                                    arithmeticNode.shiftRegisterDelay  = arithmeticNode.shiftRegisterDelay \
                                                                        + ((len(pcTreeLevels)-int(level)+1) * mbRightSHR.depth)\
                                                                        + (1+2)\
                                                                        + ((len(pcTreeLevels)-int(level)))*2
                                                                        # extra two level registers for every arithmeticNode 
                                                                        # port arithmeticNode overhead and interface overhead till the leaf level of the tree
                                    #print("PCTree Levels", pcTreeLevels)
                                    #print("Level", level)
                                    #print("Input1", arithmeticNode.input1)
                                    #print("Updated arithmeticNode Input1 Delay", arithmeticNode.shiftRegisterDelay)
                                else:
                                    # input 2 has shift register attached to it
                                    arithmeticNodeInput2Register = arithmeticNode.inputRegisters["Input2"]
                                    if isinstance(arithmeticNodeInput2Register, Cascaded_MB_D_FF):
                                        # shift registers depth needs to be updated
                                        arithmeticNode.shiftRegisterDelay = arithmeticNode.shiftRegisterDelay \
                                                                            + ((len(pcTreeLevels)-int(level)+1) * mbRightSHR.depth) \
                                                                            + (1 + 2) \
                                                                            + (len(pcTreeLevels)-int(level))*2

                                    elif isinstance(arithmeticNodeInput2Register, MBRightSHR):
                                        #print("Input2 based ArithmeticNode Delay",arithmeticNode.shiftRegisterDelay)
                                        #print("Level of the arithmeticNode", level)
                                        # shift registers depth needs to be updated
                                        #arithmeticNode.shiftRegisterDelay = arithmeticNode.shiftRegisterDelay \
                                                                            #+ ((len(pcTreeLevels)-int(level)+1) * mbRightSHR.depth) \
                                                                            #+ (1 + 2) \
                                                                            #+ ((len(pcTreeLevels)-int(level)))*2
                                                                            pass
                                        
                                     
                                #print("Updated arithmeticNode Input1 Delay", arithmeticNode.shiftRegisterDelay)
                                 

                                
                                mbRightSHR.depth = arithmeticNode.shiftRegisterDelay
                                #print("Updated MBRightSHR Attached to Input1 Depth", mbRightSHR.depth)
                            
                            #TODO Check again
                            #mbRightSHR.inputDataPorts[0].name = arithmeticNode.input1
                            
                            # print the updated name of the othMBRightSHR
                            #print("Updated OthMBRightSHR Name", othMBRightSHR.inputDataPorts[0].name)
                            # update the inputdata ports modified property of the MBRightSHR operator
                            mbRightSHR.isInputDataPortsModified = True
                            self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals
                            
                            inputRegisters = None                        
                            if arithmeticNode.inputRegisters != None:
                                #print("Input Registers",arithmeticNode.inputRegisters)
                                #print("ArithmeticNode SWOperator Input1", arithmeticNode.swOperator.input1)
                                #print("ArithmeticNode Name", arithmeticNode.name)
                                #print("ArithmeticNode Input2", arithmeticNode.input1)

                                if arithmeticNode.swOperator.input1 in arithmeticNode.inputRegisters:
                                    inputRegisters = arithmeticNode.inputRegisters[arithmeticNode.swOperator.input1]

                            #print("Stage1 & Stage2 Register",inputRegisters)
                            stage1Register = inputRegisters["Stage1Register"]
                            stage2Register = inputRegisters["Stage2Register"]

                            stage1Register.inputDataPorts[0].name = mbRightSHR.outputPorts[0].name
                            stage1Register.isInputDataPortsModified = True

                            stage2Register.inputDataPorts[0].name = stage1Register.outputPorts[0].name
                            stage2Register.isInputDataPortsModified = True
      
                            # Then update the vhdl description of the arithmetic node
                            arithmeticNode.input1 = stage2Register.outputPorts[0].name
                            # update the input data ports are modified or not
                            arithmeticNode.isInputDataPortsModified = True

                            # replace the arithmeticNode.input2 with the name of the last index mbrightSHR output
                            #arithmeticNode.input1 = mbRightSHR.outputPorts[0].name
                            #arithmeticNode.isInputDataPortsModified = True
                            
                            # check whether the input2 of the arithmeticNode is added with PipelinedRegsiters or not
                            if arithmeticNode.isInput2PipelinedWithRegisters == True:
                                
                                # before updating the vhdl instance of the arithmetic node
                                # access the input2  and store it in a local variables
                                arithmeticNodeInput2Register = arithmeticNode.inputRegisters["Input2"]
                                # update the vhdl desription of the arithmetic node updated
                                #arithmeticNode.updateVHDLInstance()
                                
                                if isinstance(arithmeticNodeInput2Register,Cascaded_MB_D_FF):
                                     # update the vhdl instance with two input based vhdl instances
                                     arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

                                elif (isinstance(arithmeticNodeInput2Register,MBRightSHR) or isinstance(arithmeticNodeInput2Register,MBRightSHR)):
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

                                
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals

                                if mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                # updated the inputPipelinedWithShiftRegisterInfo with input mbRightSHR
                                arithmeticNode.inputRegisters["Input1"] = mbRightSHR
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput1PipelinedWithRegisters = True
                                   
                            else:
                                mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                
                                arithmeticNode.inputRegisters["Input1"] = mbRightSHR
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput1PipelinedWithRegisters = True
                                # print the original vhdl instance
                                #print("Original VHDL Instance", arithmeticNode.vhdlInstance)
                                # update the vhdl desription of the arithmetic node updated
                                #arithmeticNode.updateVHDLInstance()
                                
                                 # python HW after adding the shift registers
                                arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                #print(arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                                
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals


                                if mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    
                        else:
                            #hwPipelineProcessString =  mbRightSHR.inputDataPorts[0].name + " " + "<=" + " " + arithmeticNode.input1 + ";"
                            #hwPipelineAsyncResetProcessString = mbRightSHR.inputDataPorts[0].name + " " + "<=" + " " + "(" + "others" + "=>" + "'" + "0" + "'" + ")" + ";"
                            #print("MBRightSHR Attached to ArithmeticNode Input1 Name", arithmeticNode.input1)
                            #print("Original arithmeticNode Input1 Depth", arithmeticNode.shiftRegisterDelay)
                            #print("Current Level of the arithmeticNode in MMACUnit Tree", level)
                            if arithmeticNode.shiftRegisterDelay > 0:
                                # check whether the input2 of the arithmeticNode is added with PipelinedRegsiters or not
                                if arithmeticNode.isInput2PipelinedWithRegisters == False:
                                    # shift registers are added only to balanced inputs or weight inputs
                                    arithmeticNode.shiftRegisterDelay = arithmeticNode.shiftRegisterDelay \
                                                                        + ((len(pcTreeLevels)-int(level)+1) * mbRightSHR.depth)\
                                                                        + (1+2)\
                                                                        + ((len(pcTreeLevels)-int(level)))*2
                                                                        # extra two level registers for every arithmeticNode 
                                                                        # port arithmeticNode overhead and interface overhead till the leaf level of the tree
                                    
                                    #print("PCTree Levels", len(pcTreeLevels))
                                    #print("Current Level", level)
                                    #print("Updated arithmeticNode Input1 Depth", arithmeticNode.shiftRegisterDelay)     
                                else:
                                    # access the input2 and store it in a local variables
                                    arithmeticNodeInput2Register = arithmeticNode.inputRegisters["Input2"]
                                    if isinstance(arithmeticNodeInput2Register,Cascaded_MB_D_FF):
                                        # shift registers are added only balanced inputs or weight inputs
                                        arithmeticNode.shiftRegisterDelay = arithmeticNode.shiftRegisterDelay \
                                                                            + ((len(pcTreeLevels)-int(level)+1) * mbRightSHR.depth) \
                                                                            + (1 + 2) \
                                                                            + ((len(pcTreeLevels)-int(level)))*2
                                                                        # extra two level registers for every arithmeticNode
                                                                            # port arithmeticNode overhead and interface overhead till the leaf level of the tree
                                        #print("PCTree Levels", len(pcTreeLevels))
                                        #print("Current Level", level)
                                        #print("Updated arithmeticNode Input1 Depth", arithmeticNode.shiftRegisterDelay)
                                    
                                                                  
                                mbRightSHR.depth = arithmeticNode.shiftRegisterDelay
                                #print("Updated MBRightSHR Attached to Input1 Depth", mbRightSHR.depth)
                            
                            
                            elif arithmeticNode.shiftRegisterDelay == 0:
                                # update the shift register delay with the overhead of interface and port                                 
                                arithmeticNode.shiftRegisterDelay = mbRightSHR.depth \
                                                                    + (1+2)
                                #print("ArithmeticNode Input1 with zero shiftRegisterDelay", arithmeticNode.input1)
                                #print("ArithmeticNode Input2 with zero shiftRegisterDelay", arithmeticNode.swOperator.input2)
                                
                                mbRightSHR.depth = arithmeticNode.shiftRegisterDelay
                                #print("Updated MBRightSHR Attached to Input1 Depth", mbRightSHR.depth)


                            
                            mbRightSHR.inputDataPorts[0].name = arithmeticNode.input1
                            
                            
                            # print the updated name of the othMBRightSHR
                            #print("Updated OthMBRightSHR Name", mbRightSHR.inputDataPorts[0].name)
                            # update the inputdata ports modified property of the MBRightSHR operator
                            mbRightSHR.isInputDataPortsModified = True
                            
                            # check if the arithmeticNode has shift register depth or forward path updated needed
                            inputConverter = None                        
                            if arithmeticNode.inputConverters != None:
                                #print("Input Converters",arithmeticNode.inputConverters)
                                #print("ArithmeticNode SWOperator Input1", arithmeticNode.swOperator.input1)
                                #print("ArithmeticNode Name", arithmeticNode.name)
                                #print("ArithmeticNode Input1", arithmeticNode.input1)

                                if  arithmeticNode.swOperator.input1 in arithmeticNode.inputConverters:
                                    inputConverter = arithmeticNode.inputConverters[arithmeticNode.swOperator.input1]

                            #print("Input Weight Converters",inputConverter)
                            input_mb_d_ff = inputConverter.input_MB_D_FF
                            #print("Weight Converter Input MB_D_FF", input_mb_d_ff)
                            output_mb_d_ff = inputConverter.output_MB_D_FF
                            #print("Weight Converter Output MB_D_FF", output_mb_d_ff)
                                
                            # replace the arithmeticNode.input2 with the name of the last index mbrightSHR output
                            # connect mbRightSHR output port to arithmeticNode input converter input stage
                            # connect the weight converter output mb_d_ff to the weight input of the arithmeticnode
                            input_mb_d_ff.inputDataPorts[0].name = mbRightSHR.outputPorts[0].name
                            input_mb_d_ff.isInputDataPortsModified = True
                            #print("Weight Converter Input MB_D_FF Input Name",input_mb_d_ff.inputDataPorts[0].name)
                            #print("Weight Converter Input MB_D_FF VHDl Instance", input_mb_d_ff.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                            
                            #print("Original ArithmeticNode VHDL Description", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)

                            #print("Original ArithmetNode VHDL Extra OutputSignals", arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals)

                            #TODO Check again 
                            arithmeticNode.input1 = output_mb_d_ff.outputPorts[0].name
                            arithmeticNode.isInputDataPortsModified = True
                            
                            #print("ArithmetNode VHDL OutputSignals", arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals)
                            #print("Update ArithmetNode VHDL Extra OutputSignals", arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals)
                            
                            #print("Updated ArithmeticNode VHDL Description", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)


                            #print("Updated ArithmeticNode VHDL Description Input1 Weight", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)

                            # update the arithmeticNode HW by appending the weight converter
                            mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition =  mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + input_mb_d_ff.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + inputConverter.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + output_mb_d_ff.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition 

                            #print("Updated MBRightSHR VHDL Description", mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)



                             # check whether the input2 of the arithmeticNode is added with PipelinedRegsiters or not
                            if arithmeticNode.isInput2PipelinedWithRegisters == True:
                                
                                # before updating the vhdl instance of the arithmetic node
                                # access the input2 and store it in a local variables
                                arithmeticNodeInput2Register = arithmeticNode.inputRegisters["Input2"]
                                # update the vhdl desription of the arithmetic node updated
                                #arithmeticNode.updateVHDLInstance()
                                # attach the input1 and input2 MBRightSHR to the arithmeticNode
                                                                
                                if isinstance(arithmeticNodeInput2Register,Cascaded_MB_D_FF):
                                   
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput2Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                elif (isinstance(arithmeticNodeInput2Register,MBRightSHR)):
                                    # update the vhdl instance with two input based vhdl instances
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

                                       
                                if  arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals


                                if mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                
                                # updated the inputPipelinedWithShiftRegisterInfo with input mbRightSHR
                                arithmeticNode.inputRegisters["Input1"] = mbRightSHR
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput1PipelinedWithRegisters = True
                         
                            else:
                                arithmeticNode.inputRegisters["Input1"] = mbRightSHR
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput1PipelinedWithRegisters = True

                                # update the vhdl desription of the arithmetic node updated
                                #arithmeticNode.updateVHDLInstance()
                                #print("Updated VHDL Instance After Input1 MBRightSHR Being Updated", arithmeticNode.vhdlInstance)
                                
                                # update HW after adding the shift registers to the weight port
                                arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition =  arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                
                                #print("Updated ArithmeticNode VHDL Description", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                                
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals


                                if mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals

                                    
                    elif inputName == arithmeticNode.input2:
                        #print("InputName",inputName)
                        if arithmeticNode.swOperator.input2Driver.isDriverAPort == True:
                            #print("InputName",inputName)
                            hwPipelineProcessString = mbRightSHR.inputDataPorts[0].name + " " + "<=" + " " + arithmeticNode.input2 + ";"
                            hwPipelineAsyncResetProcessString = mbRightSHR.inputDataPorts[0].name + " " + "<=" + " " + "(" + "others" + "=>" + "'" + "0" + "'" + ")" + ";"

                                                                                    
                            # if there is one, update the value with the new string
                            if level in pythonHWPipelineStagesProcessInfo:
                                oldhwPipelineProcessAsyncResetStringArray = pythonHWPipelineStagesAsyncResetProcessInfo[level]
                                oldhwPipelineProcessAsyncResetStringArray.append(hwPipelineAsyncResetProcessString)
                                oldhwPipelineProcessStringArray = pythonHWPipelineStagesProcessInfo[level]
                                oldhwPipelineProcessStringArray.append(hwPipelineProcessString)
                                pythonHWPipelineStagesProcessInfo[level] = oldhwPipelineProcessStringArray
                                pythonHWPipelineStagesAsyncResetProcessInfo[level] = oldhwPipelineProcessAsyncResetStringArray
                            else:
                                pythonHWPipelineStagesProcessInfo[level] = [hwPipelineProcessString]
                                pythonHWPipelineStagesAsyncResetProcessInfo[level] = [hwPipelineAsyncResetProcessString]                            
                            
                            #print("MBRightSHR Attached to Input2 Depth", mbRightSHR.depth)
                            #print("Original arithmeticNode Attached to Input2 Delay", arithmeticNode.shiftRegisterDelay)
                            #print("Current Level of the arithmeticNode in MMACUnit Tree", level)
                            
                            if arithmeticNode.shiftRegisterDelay > 0:
                               # check whether the input1 of the arithmeticNode is added with PipelinedRegsiters or not
                                if arithmeticNode.isInput1PipelinedWithRegisters == False:
                                    # shift registers are added only balanced inputs or weight inputs
                                    arithmeticNode.shiftRegisterDelay = arithmeticNode.shiftRegisterDelay \
                                                                        + ((len(pcTreeLevels)-int(level)+1) * mbRightSHR.depth) \
                                                                        + (1 + 2) \
                                                                        + ((len(pcTreeLevels)-int(level)))*2
                                    #print("Updated ArithmeticNode Attached to Input2 Delay",arithmeticNode.shiftRegisterDelay)
                                else:
                                    # access the input1 register and store it in a local variables
                                    arithmeticNodeInput1Register = arithmeticNode.inputRegisters["Input1"]
                                    if isinstance(arithmeticNodeInput1Register,Cascaded_MB_D_FF):
                                        # shift registers are added only balanced inputs or weight inputs
                                        arithmeticNode.shiftRegisterDelay = arithmeticNode.shiftRegisterDelay \
                                                                        + ((len(pcTreeLevels)-int(level)+1) * mbRightSHR.depth) \
                                                                        + (1 + 2) \
                                                                        + ((len(pcTreeLevels)-int(level)))*2                                       
                                        #print("Updated ArithmeticNode Attached to Input2 Depth",arithmeticNode.shiftRegisterDelay)
                                    
                                                                       
                                #print("Updated ArithmeticNode Attached to Input2 Depth",arithmeticNode.shiftRegisterDelay)
                                
                                mbRightSHR.depth = arithmeticNode.shiftRegisterDelay
                                #print("Updated MBRightSHR Attached to Input2 Depth", mbRightSHR.depth)

                            #TODO Check again
                            #mbRightSHR.inputDataPorts[0].name = arithmeticNode.input2
                            # print the updated name of the othMBRightSHR
                            #print("Updated OthMBRightSHR Name", othMBRightSHR.inputDataPorts[0].name)
                            # update the inputdata ports modified property of the MBRightSHR operator
                            mbRightSHR.isInputDataPortsModified = True
                            self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals

                            
                            inputRegisters = None                        
                            if arithmeticNode.inputRegisters != None:
                                #print("Input Registers",arithmeticNode.inputRegisters)
                                #print("ArithmeticNode SWOperator Input1", arithmeticNode.swOperator.input2)
                                #print("ArithmeticNode Name", arithmeticNode.name)
                                #print("ArithmeticNode Input2", arithmeticNode.input2)

                                if arithmeticNode.swOperator.input2 in arithmeticNode.inputRegisters:
                                    inputRegisters = arithmeticNode.inputRegisters[arithmeticNode.swOperator.input2]

                            #print("Stage1 & Stage2 Register",inputRegisters)
                            stage1Register = inputRegisters["Stage1Register"]
                            stage2Register = inputRegisters["Stage2Register"]
                            
                            stage1Register.inputDataPorts[0].name = mbRightSHR.outputPorts[0].name
                            stage1Register.isInputDataPortsModified = True

                            stage2Register.inputDataPorts[0].name = stage1Register.outputPorts[0].name
                            stage2Register.isInputDataPortsModified = True
      
                            # Then update the vhdl description of the arithmetic node
                            arithmeticNode.input2 = stage2Register.outputPorts[0].name
                            # update the input data ports are modified or not
                            arithmeticNode.isInputDataPortsModified = True

                                
                            # replace the arithmeticNode.input2 with the name of the last index mbrightSHR output
                            #arithmeticNode.input2 = mbRightSHR.outputPorts[0].name
                            #arithmeticNode.isInputDataPortsModified = True
                            
                            # check whether the input1 of the arithmeticNode is added with PipelinedRegsiters or not
                            if arithmeticNode.isInput1PipelinedWithRegisters == True:
                                #print("yes")
                                # before updating the vhdl instance of the arithmetic node
                                # access the input1 register and store it in a local variables
                                arithmeticNodeInput1Register = arithmeticNode.inputRegisters["Input1"]
                                # update the vhdl desription of the arithmetic node updated
                                #arithmeticNode.updateVHDLInstance()
                                
                                if isinstance(arithmeticNodeInput1Register,Cascaded_MB_D_FF):
                                     # update the vhdl instance with two input based vhdl instances
                                     arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

                                elif (isinstance(arithmeticNodeInput1Register,MBRightSHR)):
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                    #print(arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                                
                                
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals


                                if mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                # updated the inputRegisters with input mbRightSHR
                                arithmeticNode.inputRegisters["Input2"] = mbRightSHR
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput2PipelinedWithRegisters = True
                                    
                            else:
                                mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + stage2Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

                                arithmeticNode.inputRegisters["Input2"] = mbRightSHR
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput2PipelinedWithRegisters = True
                                # print the original vhdl instance
                                #print("Original VHDL Instance", arithmeticNode.vhdlInstance)
                                # update the vhdl desription of the arithmetic node updated
                                #arithmeticNode.updateVHDLInstance()
                                arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals =  arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals

                                if mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals

                                    
                        else:
                            #print("MBRightSHR Attached to ArithmeticNode Input2 Name", arithmeticNode.input2)
                            #print("Original arithmeticNode Input2 Depth", arithmeticNode.shiftRegisterDelay
                            #hwPipelineProcessString = mbRightSHR.inputDataPorts[0].name + " " + "<=" + " " + arithmeticNode.input2 + ";"
                            #hwPipelineAsyncResetProcessString = mbRightSHR.inputDataPorts[0].name + " " + "<=" + " " + "(" + "others" + "=>" + "'" + "0" + "'" + ")" + ";"

                            if arithmeticNode.shiftRegisterDelay > 0:
                                # check whether the input1 of the arithmeticNode is added with PipelinedRegsiters or not
                                if arithmeticNode.isInput1PipelinedWithRegisters == False:
                                    # shift registers are added only balanced inputs or weight inputs
                                    arithmeticNode.shiftRegisterDelay = arithmeticNode.shiftRegisterDelay \
                                                                        + ((len(pcTreeLevels)-int(level)+1) * mbRightSHR.depth) \
                                                                        + (1 + 2) \
                                                                        + ((len(pcTreeLevels)-int(level)))*2 \
                                                                        # port arithmeticNode overhead and interface overhead till the leaf level of the tree
                                    #print("PCTree Levels", len(pcTreeLevels))
                                    #print("Current Level", level)
                                    #print("Updated arithmeticNode Input2 Depth", arithmeticNode.shiftRegisterDelay)
                                else:
                                    # access the input1
                                    arithmeticNodeInput1Register = arithmeticNode.inputRegisters["Input1"]
                                    #print(arithmeticNodeInput1Register)
                                    if isinstance(arithmeticNodeInput1Register,Cascaded_MB_D_FF):
                                        # shift registers are added only balanced inputs or weight inputs
                                        arithmeticNode.shiftRegisterDelay = arithmeticNode.shiftRegisterDelay \
                                                                            + ((len(pcTreeLevels)-int(level)+1) * mbRightSHR.depth) \
                                                                            + (1+2) \
                                                                            + ((len(pcTreeLevels)-int(level)))*2 \
                                                                            # port arithmeticNode overhead and interface overhead till the leaf level of the tree
                                        #print("PCTree Levels", len(pcTreeLevels))
                                        #print("Current Level", level)
                                        #print("Updated arithmeticNode Input2 Depth", arithmeticNode.shiftRegisterDelay)
                                    
                                                                
                                mbRightSHR.depth = arithmeticNode.shiftRegisterDelay
                                #print("Updated MBRightSHR Attached to Input2 Depth", mbRightSHR.depth)
                                
                            
                            elif arithmeticNode.shiftRegisterDelay == 0:
                                # update the shift register delay with the overhead of interface and port                                 
                                arithmeticNode.shiftRegisterDelay =  mbRightSHR.depth \
                                                                            + (1+2) \
                                                                            # port arithmeticNode overhead and interface overhead till the leaf level of the tree
                                
                                mbRightSHR.depth = arithmeticNode.shiftRegisterDelay
                                #print("Updated MBRightSHR Attached to Input2 Depth", mbRightSHR.depth)

                                #print("ArithmeticNode Input2 with zero shiftRegisterDelay", arithmeticNode.input2)
                                #print("ArithmeticNode Input1 with zero shiftRegisterDelay", arithmeticNode.swOperator.input1)

                                

                            mbRightSHR.inputDataPorts[0].name = arithmeticNode.input2
                            # print the updated name of the othMBRightSHR
                            #print("Updated OthMBRightSHR Name", othMBRightSHR.inputDataPorts[0].name)
                            # update the inputdata ports modified property of the MBRightSHR operator
                            mbRightSHR.isInputDataPortsModified = True
                            
                            # check if the arithmeticNode has shift register depth or forward path updated needed
                            inputConverter = None                        
                            if arithmeticNode.inputConverters != None:
                                #print("Input Converters",arithmeticNode.inputConverters)
                                #print("ArithmeticNode SWOperator Input2", arithmeticNode.swOperator.input2)
                                #print("ArithmeticNode Name", arithmeticNode.name)
                                #print("ArithmeticNode Input2", arithmeticNode.input2)

                                if  arithmeticNode.swOperator.input2 in arithmeticNode.inputConverters:
                                    inputConverter = arithmeticNode.inputConverters[arithmeticNode.swOperator.input2]

                            #print("Input Weight Converters",inputConverter)
                            input_mb_d_ff = inputConverter.input_MB_D_FF
                            #print("Weight Converter Input MB_D_FF", input_mb_d_ff)
                            output_mb_d_ff = inputConverter.output_MB_D_FF
                            #print("Weight Converter Output MB_D_FF", output_mb_d_ff)
                                 
                            # replace the arithmeticNode.input2 with the name of the last index mbrightSHR output
                            # replace the arithmeticNode.input2 with the name of the last index mbrightSHR output
                            # connect mbRightSHR output port to arithmeticNode input converter input stage
                            # connect the weight converter output mb_d_ff to the weight input of the arithmeticnode
                            input_mb_d_ff.inputDataPorts[0].name = mbRightSHR.outputPorts[0].name
                            input_mb_d_ff.isInputDataPortsModified = True

                            arithmeticNode.input2 = output_mb_d_ff.outputPorts[0].name                       
                            arithmeticNode.isInputDataPortsModified = True
                            
                            #print("Original ArithmeticNode VHDL Description", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)

                            # update the arithmeticNode HW by appending the weight converter
                            arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition =  input_mb_d_ff.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + inputConverter.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + output_mb_d_ff.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                            
                            #print("Updated ArithmeticNode VHDL Description", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)


                             # check whether the input1 of the arithmeticNode is added with PipelinedRegsiters or not
                            if arithmeticNode.isInput1PipelinedWithRegisters == True:
                                
                                # before updating the vhdl instance of the arithmetic node
                                # access the input1 register and store it in a local variables
                                arithmeticNodeInput1Register = arithmeticNode.inputRegisters["Input1"]
                                # update the vhdl desription of the arithmetic node updated
                                #arithmeticNode.updateVHDLInstance()
                                # attach the input1 and input2 MBRightSHR to the arithmeticNode
                                # python HW after adding the shift registers                                
                                if isinstance(arithmeticNodeInput1Register,Cascaded_MB_D_FF):
                                   
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput1Register.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                elif isinstance(arithmeticNodeInput1Register,MBRightSHR):
                                    # update the vhdl instance with two input based vhdl instances
                                    arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNodeInput1Register.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                   
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals


                                if mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals

                                # updated the inputRegisters with input mbRightSHR
                                arithmeticNode.inputRegisters["Input2"] = mbRightSHR
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput2PipelinedWithRegisters = True
                                                            
                            else:
                                arithmeticNode.inputRegisters["Input2"] = mbRightSHR
                                # update the arithmetic node input1 pipeline with mbright shr properties
                                arithmeticNode.isInput2PipelinedWithRegisters = True

                                # update the vhdl desription of the arithmetic node updated
                                #arithmeticNode.updateVHDLInstance()
                                #print("Updated VHDL Instance After Input1 MBRightSHR Being Updated", arithmeticNode.vhdlInstance)
                                
                                arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition = arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
                                
                                if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.extraVHDLOutputSignals


                                if mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                                    self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
                            
                       
        # print the pythonHWPipelineStagesProcessInfo
        #print("The python HW pipeline stages process info", pythonHWPipelineStagesProcessInfo)
        #print("The python HW pipeline stages async reset process info", pythonHWPipelineStagesAsyncResetProcessInfo)
        # print the pythonHWPipelineStages Info
        #print("The python HW pipeline stages info",pythonHWPipelineStagesInfo)
        self.addPipelineToPCTreeTopArithmeticNodeOutput(pythonHWPipelineStagesInfo)

        self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStagesInfo = pythonHWPipelineStagesInfo
        self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStagesProcessInfo = pythonHWPipelineStagesProcessInfo
        self.vhdlEntityArchitectureDescription.vhdlProcessDescription.pythonHWPipelineStagesAsyncResetProcessInfo = pythonHWPipelineStagesAsyncResetProcessInfo
    
    
    
    def addPipelineToPCTreeTopArithmeticNodeOutput(self,pythonHWPipelineStagesInfo):
        
        # access the level 1 of the pctree from the dictionary
        # the value for the key,level will have the information of the arithmetic node 
        # use the arithmeticNode to access the information of the output key value from pipelineStagesInfo
        
        levelDetails = pythonHWPipelineStagesInfo["1"]
        #print("Level Details", levelDetails)
        # it will have three values for the key "1"
        # access the output CascadedMBDFF value from the level details
        outputCascadedMBDFF = levelDetails[len(levelDetails)-1]
        # access the arithmeticNode
        arithmeticNode = outputCascadedMBDFF["ArithmeticNode"]
        # access the OutputCascadedMBDFF Registers
        cascadedMBDFFRegisters = outputCascadedMBDFF["CascadedRegisters"]
        # now change the output of the arithmeticNode and update the VHDL instance of the arithmeticNode
        
        # access the 0th MB_D_FF from the cascaded MB_D_FF
        othMB_D_FF = cascadedMBDFFRegisters.cascadedRegisters[0]
        # access the input of the othMB_D_FF
        othMB_D_FFName = othMB_D_FF.inputDataPorts[0].name
        # print the name of the othMB_D_FF
        #print("Original othMB_D_FFName", othMB_D_FFName)
                    
        # access the last index mb_d_ff from the cascaded mb_d_ff
        lastIndexMB_D_FF = cascadedMBDFFRegisters.cascadedRegisters[len(cascadedMBDFFRegisters.cascadedRegisters)-1]
        # access the input of the lastIndexMB_D_FF
        lastIndexMB_D_FFName = lastIndexMB_D_FF.inputDataPorts[0].name
        # print the name of the othMB_D_FF
        #print("Original lastIndexMB_D_FF Name", lastIndexMB_D_FFName)
                
        # print the original name of the othMB_D_FF
        #print("Original othMB_D_FF Name", othMB_D_FF.inputDataPorts[0].name)
        othMB_D_FF.inputDataPorts[0].name = arithmeticNode.output
        # print the updated name of the othMB_D_FF
        #print("Updated othMB_D_FF Name", othMB_D_FF.inputDataPorts[0].name)
        # update the inputdata ports modified property of the MB_D_FF operator
        othMB_D_FF.isInputDataPortsModified = True    
        
        # reset the cascaded_MB_D_FF name
        cascadedMBDFFRegisters.inputDataPorts[0].name = othMB_D_FF.inputDataPorts[0].name
        # update the cascaded_MB_D_FF
        cascadedMBDFFRegisters.isInputDataPortsModified = True
        
        # replace the arithmeticNode.input2 with the name of the last index mbrightSHR output
        arithmeticNode.outputRegisters[arithmeticNode.swOperator.summation] = {"CascadedRegisters":cascadedMBDFFRegisters}
                            
        self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals = cascadedMBDFFRegisters.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals
        
        # update the vhdl instance with two input based vhdl instances
        arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition =  arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition + cascadedMBDFFRegisters.hwVHDLDescription.vhdlEntityArchitectureDescription.pythonHW
        #print("Top ArithmeticNode Object", self.arithmeticNodes[len(self.arithmeticNodes)-1])
        #print("Level1ArithmeticNode Object", level1ArithmeticNode)
        #print("Top ArithmeticNode VHDL Instance Definition",level1ArithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                                
        if arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals[0] not in self.vhdlEntityArchitectureDescription.vhdlOutputSignals:
            # attach the arithmeticNode VHDLOutputSignal to the vhdlOutputSignal array
            self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals =  arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals


    
    """
    # Start: balance forward paths of arithmetic nodes
    """

    def performExtractionOfPCTreeLevelBasedArithmeticNodeDetails(self):
        # access all the keys of the nodes of all levels object
        levelKeys = self.childrenOfEachLevelOfPCTree.keys()
        # object to store the maxDepth for each level that is used to balance the level of PC
        pcTreeShiftRegisterDelay = dict()

        #print the level keys
        #print("Level Keys", levelKeys)
        # loop through the nodes of all levels
        for levelKey in levelKeys:
            # access the array of the children per level using levelKey
            children = self.childrenOfEachLevelOfPCTree[levelKey]
            arithmeticNodeLevelBasedDelayDetails = list()
            # now loop through the same level children and find the child that is having shouldInput1andInput2BeBalanced set to true
            for child in children:
                arithmeticNodeDelayDetails = dict()
                
                arithmeticNodeDelayDetails[child.hwDescription.hwInstanceName] = child.shiftRegisterDelay
                arithmeticNodeLevelBasedDelayDetails.append(arithmeticNodeDelayDetails)     
                
                # add children hwInstance name and the shiftRegisterDelay based on the level to a separate dictionary
                pcTreeShiftRegisterDelay[levelKey] = arithmeticNodeLevelBasedDelayDetails

        #print("PCTree Final Level Based ShiftRegister Details", pcTreeShiftRegisterDelay)
    
        
    """
    # End: balance forwards paths of  arithmetic nodes
    """

    def process(self):
        self.pythonHWPipelineStagesOfPCTree = self.processHWPipelineStagesForPCTree()
        self.generateHWPipelineProcessUsingPipelineStagesOfPCTree()
        super().process()  
    
    def perform(self):
        super().perform()
        self.performExtractionOfPCTreeLevelBasedArithmeticNodeDetails()

                          
        
    def reset(self):
        super().reset()
        self.resetProperties()

    def resetProperties(self):
        self.numberOfPipelineStages = 0
        self._childrenOfEachLevelOfPCTree = None
        self.arithmeticNodes = None


    def main(self):
        super().main()
    
    def run(self):
        self.main()
