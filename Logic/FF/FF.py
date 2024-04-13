"""
Created by Karthekeyan Periasamy
Edited on Oct 25 13:00

"""
from Logic.Logic import Logic

class FF(Logic):


    def __init__(self):
        super().__init__()
        self.connect()
        
      
      
    @property
    def ffResetTypeName (self):
        return  self._ffResetTypeName
    
    @ffResetTypeName.setter
    def ffResetTypeName (self,value):
        self._ffResetTypeName = value
        if self._ffResetTypeName == "ASYNC":
            self.ffResetType = 1
        elif self._ffResetTypeName == "SYNC":
            self.ffResetType = 2
    
       
    def configure(self):
        super().configure()
        
        # store the configuration details temporarily
        configurationDetails = self.configurationDetailsOfLogic

        # check if the width is available or not
        if "Width" in configurationDetails:
            self.width = configurationDetails["Width"]

        # check for the type of reset whether it is async or sync
        if "FFResetType" in configurationDetails:
            self.ffRegisterResetTypeName = configurationDetails["FFResetType"]


                      
    def process(self):
        # process HW ShiftRegister
        self.processHWFF()
        self.processSWFF()
        self.processHWLogicConfigurationDetails()
    
    
    def processHWFF(self):
        pass
        
    def processSWFF(self):
        pass

   
    def perform(self):
        self.performSWShifting()
        self.performHWGeneration()

    def performSWShifting(self):
        pass

   
    def processHWLogicConfigurationDetails(self):
        self.configurationDetailsOfHWLogic = {"Number":self.number,"Name":self.name,"PythonHWEntity":{"Name":self.name,"Number":self.number,"NumberSystem":self.numberSystemName,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":self.pythonHWLogicGeneric},"InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort},"PythonHWArchitecture":{"Name":self.name,"HWArchitectureTypeName":"RTL","InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort,"PythonHWProcess":{"SensitivityList":[self.clockPort.name,self.resetPort.name],"PythonHWProcessInfo":self.pythonHWLogic,"PythonHWClockProcessInfo":{"Frequency":self.frequency, "ClockPortName":self.clockPort.name,"ClockStimulusName":(self.clockPort.name + "Stimulus")},"PythonHWIOStimulusProcessInfo":{"PythonHWProcessVariablesInfo":[{"Name":"fileline","Type":"line","NumberOfBits":None},{"NumberOfBits":self.numberOfBits,"Name":"inputBuffer","Type":"bit_vector"},{"Name":"commaBuffer","Type":"character","NumberOfBits":None}],"PythonHWProcessFileInfo":[{"Name":"outputFile","Mode":"write_mode", "Type":"text","FileName":("Output" + "_" + self.name + "_" + str(self.numberOfBits)),"FileExtension":"txt"},{"Name":"inputFile","Mode":"read_mode","Type":"text","FileName":("Input" + "_" + self.name + "_" + str(self.numberOfBits)),"FileExtension":"txt"}],"InputDataPorts":self.inputDataPorts,"OutputDataPorts":self.outputPorts}}}}
    

    def performHWGeneration():
        pass


    def connect(self):
        super().connect()
        self.connectProperties()


    def connectProperties(self):
        super().connectProperties()
        # width of the ff is the number of bits
        self.width = None
        # flip flop reset type name
        self._ffResetTypeName = None
        # shift register reset type
        self.ffResetType = None
        # unique identifier of the Shift register
        # this will be used when the ff is used in big systems
        self.uniqueIdentifier = None
        # register is one dimensional and can be used to configure the width
        self.pythonFF = None
        # cascade flipflops property to know whether cascading of number of ffs should be preferred or not
        self.cascadeFFs = False
        # the number of cascade stages to cascade multiple registers
        self.numberOfCascadeStages = 0

        
    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()
        # width of the ff is the number of bits
        self.width = None
        # flip flop reset type name
        self._ffResetTypeName = None
        # shift register reset type
        self.ffResetType = None
        # unique identifier of the Shift register
        # this will be used when the ff is used in big systems
        self.uniqueIdentifier = None
        # register is one dimensional and can be used to configure the width
        self.pythonFF = None        
        # cascade registers property to know whether cascading of number of registers should be preferred or not
        self.cascadeRegisters = False
        # the number of cascade stages to cascade multiple registers
        self.numberOfCascadeStages = 0



    def main(self):
        self.process()


    def run(self):
        self.main()


