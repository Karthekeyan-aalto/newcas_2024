"""
Created by Karthekeyan Periasamy
Edited on Jan 20 16:22
""" 

from Logic.Port.FLPFlopocoPort.FLPFlopocoPort import FLPFlopocoPort
from Logic.Port.Port import Port
from Logic.FF.MB_D_FF.FLPMB_D_FF.FLPMB_D_FF import FLPMB_D_FF
from Logic.FF.Cascaded_MB_D_FF.Cascaded_MB_D_FF import Cascaded_MB_D_FF
from HWDescription.Logic.FF.Cascaded_MB_D_FF.Cascaded_MB_D_FF_VHDLDescription import Cascaded_MB_D_FF_VHDLDescription

class FLPCascaded_MB_D_FF(Cascaded_MB_D_FF):
    # this class do not have a hardware description as of now

    def __init__(self):
        super().__init__()    

    def connect(self):
        super().connect()        

    def connectProperties(self):
        super().connectProperties()
    
    def connectHWDescriptionPackage(self):
        # connect the HWDescription Package
        self.hwVHDLDescription = Cascaded_MB_D_FF_VHDLDescription() 
        
    def configure(self):
        super().configure()
        
        configurationDetails = self.configurationDetailsOfLogic
        #print("Configuration Details of Logic Cascaded MB_D_FF", configurationDetails)
        
        # intialise the inputDataPorts array
        self.inputDataPorts = list()
        # intialise the outputPorts array
        self.outputPorts = list()
        # intialise the cascaded registers again
        self.cascadedRegisters = list()
        
        # check whether we need to cascde registers
        if "CascadeRegisters" in configurationDetails:
            # cascade registers property is a true or false property
            self.cascadeRegisters = configurationDetails["CascadeRegisters"]
            
            # check if number of cascading stages of shiftregister is present or not
            if "NumberOfCascadeStages" in configurationDetails:
                self.numberOfCascadeStages = configurationDetails["NumberOfCascadeStages"]
                
            # check the number of cascade stage
            if self.cascadeRegisters == True:
                # as per the number of cascade stages
                # loop through and generate multiple MBRightSHR instance
                for cascadeStageNumber in range(0,self.numberOfCascadeStages):
                    # form the basic connections of the between the cascaded mbRightSHR registers
                    # for the first index, the input is same as its controlled at the process stage
                    # if the index is greater than 0, its input should be same as the previous element or the previous MBRightSHR
                    if cascadeStageNumber == 0:
                        #print("Number One", cascadeStageNumber)
                        mbDFF = FLPMB_D_FF()
                        mbDFF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(cascadeStageNumber)), "InputDataPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(cascadeStageNumber)) + "Input"),"NumberOfBits":(self.mantissaBits + self.exponentBits + self.flopocoBits),"PortType":"Input", "ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(cascadeStageNumber)) + "Output"),"NumberOfBits":(self.mantissaBits + self.exponentBits + self.flopocoBits),"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Width":(self.mantissaBits + self.exponentBits + self.flopocoBits),"NumberOfBits":(self.mantissaBits + self.exponentBits + self.flopocoBits), "EsBits":self.esBits, "MantissaBits":self.mantissaBits, "EsBits":self.esBits}
                        mbDFF.configure()
                        mbDFF.process()
                        mbDFF.perform()
                        #print("FLPMB_D_FF OutputPorts", mbDFF.outputPorts)
                        #print("VHDL Output Signals",mbDFF.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals)
                        # append the mbRightSHR to the cascadedRegisters
                        #print("Original Cascaded Registers",self.cascadedRegisters)
                        self.cascadedRegisters.append(mbDFF)
                        #print("Updated Cascaded Registers", self.cascadedRegisters)
                    else:
                        mbDFF = FLPMB_D_FF()
                        mbDFF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(cascadeStageNumber)), "InputDataPorts":[{"Name":self.cascadedRegisters[cascadeStageNumber-1].outputPorts[0].name,"NumberOfBits":(self.mantissaBits + self.exponentBits + self.flopocoBits),"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(cascadeStageNumber)) + "Output"),"NumberOfBits":(self.mantissaBits + self.exponentBits + self.flopocoBits),"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":(self.mantissaBits + self.exponentBits + self.flopocoBits),"ShiftDirection":"Right","NumberOfBits":(self.mantissaBits + self.exponentBits + self.flopocoBits), "EsBits":self.esBits, "MantissaBits":self.mantissaBits, "ExponentBits":self.exponentBits}
                        mbDFF.configure()
                        mbDFF.process()
                        mbDFF.perform()
                        #print("FLPMB_D_FF OutputPorts", mbDFF.outputPorts)
                        #print("VHDL Output Signals",mbDFF.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals)
                        # append the mbRightSHR to the cascadedRegisters
                        self.cascadedRegisters.append(mbDFF)

                                   
                # build the input and output data ports of the cascadedregisters
                # access the 0th index mbRightSHR and access the inputDataPorts index 0

                if "InputDataPorts" in configurationDetails:
                    inputPortDetails = configurationDetails["InputDataPorts"]
                    
                    for portDetail in inputPortDetails:
                        # access the information about the port or use the configuration details property to configure itself
                        newPort = FLPFlopocoPort()
                        newPort.configurationDetails = portDetail
                        # configure the port
                        newPort.configure()
                        # process the port
                        newPort.process()
                        newPort.perform()
                        # once the port is configured, add the port to the InputDataPorts array
                        self.inputDataPorts.append(newPort)


                else:
                    # the value of the key is expected to be an array
                    inputPortDetails = [{"Name":self.cascadedRegisters[0].name,"NumberOfBits":self.cascadedRegisters[0].numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                    for portDetail in inputPortDetails:
                        # access the information about the port or use the configuration details property to configure itself
                        newPort = FLPFlopocoPort()
                        newPort.configurationDetails = portDetail
                        # configure the port
                        newPort.configure()
                        # process the port
                        newPort.process()
                        newPort.perform()
                        # once the port is configured, add the port to the InputDataPorts array
                        self.inputDataPorts.append(newPort)
                
                # the value of the key is expected to be an array
                outputPortDetails = [{"Name":"vout","NumberOfBits":self.cascadedRegisters[(len(self.cascadedRegisters)-1)].numberOfBits,"PortType":"Output","ConstantSignalValue":0}]
                for portDetail in outputPortDetails:
                    # access the information about the port or use the configuration details property to configure itself
                    newPort = FLPFlopocoPort()
                    newPort.configurationDetails = portDetail
                    # configure the port
                    newPort.configure()
                    # process the port
                    newPort.process()
                    newPort.perform()
                    # once the port is configured, add the port to the InputDataPorts array
                    self.outputPorts.append(newPort)
                 
                clockPortDetail = {"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0}
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
                
                resetPortDetail = {"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}
                newPort = Port()
                newPort.configurationDetails = resetPortDetail
                # configure the port
                newPort.configure()
                # process the port
                newPort.process()
                newPort.perform()
                # once the port is configured, set the port
                self.resetPort = newPort
                
                enablePortDetail = {"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}
                newPort = Port()
                newPort.configurationDetails = enablePortDetail
                # configure the port
                newPort.configure()
                # process the port
                newPort.process()
                newPort.perform()
                # once the port is configured, set the port
                self.enablePort = newPort




    
    def perform(self):
        super().perform()
        #print("FLPCascadedMB_D_FF OutputPorts", self.outputPorts)
        #print("FLPCascadedMB_D_FF VHDL Output Signals", self.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals)



    def process(self):
        super().process()
    
    def configureHWDescriptionPackage(self):
        self.configurationDetailsOfHWLogic = {"Number":self.number,"Name":self.name,"PythonHWEntity":{"Name":self.name,"Number":self.number,"NumberSystem":self.numberSystemName,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":self.pythonHWLogicGeneric},"InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort},"PythonHWArchitecture":{"Name":self.name,"HWArchitectureTypeName":"RTL","InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort,"CascadedRegisters":self.cascadedRegisters, "PythonHWProcess":{"SensitivityList":[self.clockPort.name,self.resetPort.name],"PythonHWProcessInfo":self.pythonHWLogic,"PythonHWClockProcessInfo":{"Frequency":self.frequency, "ClockPortName":self.clockPort.name,"ClockStimulusName":(self.clockPort.name + "Stimulus")},"PythonHWIOStimulusProcessInfo":{"PythonHWProcessVariablesInfo":[{"Name":"fileline","Type":"line","NumberOfBits":None},{"NumberOfBits":(self.mantissaBits + self.exponentBits + self.flopocoBits),"Name":"inputBuffer","Type":"bit_vector"},{"Name":"commaBuffer","Type":"character","NumberOfBits":None}],"PythonHWProcessFileInfo":[{"Name":"outputFile","Mode":"write_mode", "Type":"text","FileName":("Output" + "_" + self.name + "_" + str((self.mantissaBits + self.exponentBits + self.flopocoBits))),"FileExtension":"txt"},{"Name":"inputFile","Mode":"read_mode","Type":"text","FileName":("Input" + "_" + self.name + "_" + str((self.mantissaBits + self.exponentBits + self.flopocoBits))),"FileExtension":"txt"}],"InputDataPorts":self.inputDataPorts,"OutputDataPorts":self.outputPorts}}}}
        
        self.hwVHDLDescription.configurationDetailsOfHW = self.configurationDetailsOfHWLogic
        self.hwVHDLDescription.configure()
    
    def main(self):
        self.process()
        self.perform()

    def reset(self):
        self.resetProperties()
        self.resetHWDescriptionPackage()
    
    def resetProperties(self):
        super().resetProperties()
 
    def run(self):
        self.main()


