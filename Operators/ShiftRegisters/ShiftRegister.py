"""
Created by Karthekeyan Periasamy
Edited on Feb 13 10:24

"""

from Operators.Operator import Operator

class ShiftRegister(Operator):


    def __init__(self):
        super().__init__()
        self.connect()
        
        
    @property
    def pythonHWOperatorGeneric(self):
        if self._pythonHWOperatorGeneric == None:
            self._pythonHWOperatorGeneric = dict()
            if self.numberSystem > -1 :
                if self.numberSystem == 0:
                    self._pythonHWOperatorGeneric["NumberOfBits"] = self.numberOfBits
                elif self.numberSystem == 1:
                    self._pythonHWOperatorGeneric[str(self.depth)] = self.depth
                    self._pythonHWOperatorGeneric["NumberOfBits"] = self.numberOfBits
                elif self.numberSystem == 2:
                    self._pythonHWOperatorGeneric[str(self.depth)] = self.depth
                    self._pythonHWOperatorGeneric["NumberOfBits"] = self.numberOfBits
        return self._pythonHWOperatorGeneric

    @pythonHWOperatorGeneric.setter
    def pythonHWOperatorGeneric(self,value):
        self._pythonHWOperatorGeneric = value
    
    
    @property
    def shiftDirectionName (self):
        return  self._shiftDirectionName
    
    @shiftDirectionName.setter
    def shiftDirectionName (self,value):
        self._shiftDirectionName = value
        # check if the name is right or wrong
        if self._shiftDirectionName == "Right":
            self.shiftDirection = 1
        elif self._shiftDirectionName == "Left":
            self.shiftDirection = 2
    
    @property
    def shiftRegisterResetTypeName (self):
        return  self._shiftRegisterResetTypeName
    
    @shiftRegisterResetTypeName.setter
    def shiftRegisterResetTypeName (self,value):
        self._shiftRegisterResetTypeName = value
        if self._shiftRegisterResetTypeName == "ASYNC":
            self.shiftRegisterResetType = 1
        elif self._shiftRegisterResetTypeName == "SYNC":
            self.shiftRegisterResetType = 2
    
       
    def configure(self):
        super().configure()
        
        # store the configuration details temporarily
        configurationDetails = self.configurationDetailsOfOperator

        # check if depth is available or not
        if "Depth" in configurationDetails:
            self.depth = configurationDetails["Depth"]
        
        # check if the width is available or not
        if "Width" in configurationDetails:
            self.width = configurationDetails["Width"]

        if "ShiftDirection" in configurationDetails:
            self.shiftDirectionName = configurationDetails["ShiftDirection"]

        # check for the type of reset whether it is async or sync
        if "ShiftRegisterResetType" in configurationDetails:
            self.shiftRegisterResetTypeName = configurationDetails["ShiftRegisterResetType"]


                      
    def process(self):
        # process HW ShiftRegister
        self.processHWShiftRegister()
        self.processSWShiftRegister()
        self.processHWOperatorConfigurationDetails()
    
    
    def processHWShiftRegister(self):
        pass
        
    def processSWShiftRegister(self):
        self.processSWShiftRegisterDepth()
        self.processSWShiftRegisterWdith()

    
    def processSWShiftRegisterDepth(self):
        if self.depth > 0:
            # check if the python register is set or not
            if self.pythonRegister != None:
                # use the python regsiter
                # reset the python registers or initialise the python registers
                self.pythonRegisters = [[self.pythonRegister]] * self.depth
            else:
                # make a python register with a given width
                if self.width == 0:
                    self.pythonRegister = [0]*1
                else:
                    self.pythonRegister = [0] * self.width
                    
                # use the newly intialised python register to form the python registers
                self.pythonRegisters = [[self.pythonRegister]] * self.depth

        elif self.depth  == 0:
            self.pythonRegisters = None


    def processSWShiftRegisterWdith(self):
        
        if self.width > 0:
            # check if the pythonRegister is already intialised
            if self.pythonRegister != None:
                self.pythonRegister = [0] * self.width

                # also check the depth
                if self.depth > 0:
                    # check the pythonRegisters
                    if self.pythonRegisters != None:
                        self.pythonRegisters = [[self.pythonRegister]]*self.depth
                
        elif self.width == 0:
            self.pythonRegister = None



    def perform(self):
        self.performSWShifting()
        self.performHWGeneration()

    def performSWShifting(self):
        pass

   
    def processHWOperatorConfigurationDetails(self):
        self.configurationDetailsOfHWOperator = {"Number":self.number,"Name":self.name,"PythonHWEntity":{"Name":self.name,"Number":self.number,"NumberSystem":self.numberSystemName,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":self.pythonHWOperatorGeneric},"InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort},"PythonHWArchitecture":{"Name":self.name,"HWArchitectureTypeName":"RTL","InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort,"PythonHWProcess":{"SensitivityList":[self.clockPort.name,self.resetPort.name],"PythonHWProcessInfo":self.pythonHWOperator,"PythonHWClockProcessInfo":{"Frequency":self.frequency, "ClockPortName":self.clockPort.name,"ClockStimulusName":(self.clockPort.name + "Stimulus")},"PythonHWIOStimulusProcessInfo":{"PythonHWProcessVariablesInfo":[{"Name":"fileline","Type":"line","NumberOfBits":None},{"NumberOfBits":self.numberOfBits,"Name":"inputBuffer","Type":"bit_vector"},{"Name":"commaBuffer","Type":"character","NumberOfBits":None}],"PythonHWProcessFileInfo":[{"Name":"outputFile","Mode":"write_mode", "Type":"text","FileName":("Output" + "_" + self.name + "_" + str(self.numberOfBits)),"FileExtension":"txt"},{"Name":"inputFile","Mode":"read_mode","Type":"text","FileName":("Input" + "_" + self.name + "_" + str(self.numberOfBits)),"FileExtension":"txt"}],"InputDataPorts":self.inputDataPorts,"OutputDataPorts":self.outputPorts}}}}
    

    def performHWGeneration():
        pass


    def connect(self):
        super().connect()
        self.connectProperties()


    def connectProperties(self):
        super().connectProperties()
        # property to store the depth and width of the shift register
        self.depth = None
        # width of the shift regsiter is the number of bits
        self.width = None
        # shift direction name
        self._shiftDirectionName = None
        # shift direction
        self.shiftDirection = None
        # shift register reset type name
        self._shiftRegisterResetTypeName = None
        # shift register reset type
        self.shiftRegisterResetType = None
        # unique identifier of the Shift register
        # this will be used when the shift register is used in big systems
        self.uniqueIdentifier = None
        # register is one dimensional and can be used to configure the width
        self.pythonRegister = None
        # registers is two dimensional and can be used to configure the depth
        self.pythonRegisters = None
        
    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()
        # property to store the depth and width of the shift register
        self.depth = None
        # width of the shift regsiter is the number of bits
        self.width = None
        # shift direction name
        self._shiftDirectionName = None
        # shift register reset type name
        self._shiftRegisterResetTypeName = None
        # shift direction
        self.shiftDirection = None
        # shift register reset type
        self.shiftRegisterResetType = None
        # unique identifier of the Shift register
        # this will be used when the shift register is used in big systems
        self.uniqueIdentifier = None
        # register is one dimensional and can be used to configure the width
        self.pythonRegister = None
        # registers is two dimensional and can be used to configure the depth
        self.pythonRegisters = None
        # cascade registers property to know whether cascading of number of registers should be preferred or not
        self.cascadeRegisters = False
        # the number of cascade stages to cascade multiple registers
        self.numberOfCascadeStages = 0



    def main(self):
        self.process()


    def run(self):
        self.main()


