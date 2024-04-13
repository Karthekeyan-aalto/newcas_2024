"""
Created by Karthekeyan Periasamy
Edited on Oct 25 15:27
""" 

from Logic.Port.Port import Port
from Logic.FF.MB_D_FF.MB_D_FF import MB_D_FF
from HWDescription.Logic.FF.Cascaded_MB_D_FF.Cascaded_MB_D_FF_VHDLDescription import Cascaded_MB_D_FF_VHDLDescription

class Cascaded_MB_D_FF(MB_D_FF):
    # this class do not have a hardware description as of now

    def __init__(self):
        super().__init__()
        self.connect()
    
    
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



    def connect(self):
        self.connectProperties()
        self.connectHWDescriptionPackage()
        

    def connectProperties(self):
        super().connectProperties()
        # proeprty to store the cascaded registers as an array
        self.cascadedRegisters = list()
        # cascade registers property to know whether cascading of number of registers should be preferred or not
        self.cascadeRegisters = False
        # the number of cascade stages to cascade multiple registers
        self.numberOfCascadeStages = 0
    
    def connectHWDescriptionPackage(self):
        # connect the HWDescription Package
        self.hwVHDLDescription = Cascaded_MB_D_FF_VHDLDescription() 
        
    def configure(self):
        super().configure()
        
        configurationDetails = self.configurationDetailsOfLogic
        #print("Configuration Details of Logic Cascaded MB_D_FF", configurationDetails)
        
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
                        mbDFF = MB_D_FF()
                        mbDFF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(cascadeStageNumber)), "InputDataPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(cascadeStageNumber)) + "Input"),"NumberOfBits":self.numberOfBits,"PortType":"Input", "ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(cascadeStageNumber)) + "Output"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Width":self.numberOfBits,"NumberOfBits":self.numberOfBits, "EsBits":self.esBits, "MantissaBits":self.mantissaBits, "ExponentBits":self.exponentBits}
                        mbDFF.configure()
                        mbDFF.process()
                        mbDFF.perform()
                        # append the mbRightSHR to the cascadedRegisters
                        self.cascadedRegisters.append(mbDFF)
                    else:
                        mbDFF = MB_D_FF()
                        mbDFF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":self.frequency,"NumberSystem":self.numberSystemName,"Number":(str(self.number) + "_" + str(cascadeStageNumber)), "InputDataPorts":[{"Name":self.cascadedRegisters[cascadeStageNumber-1].outputPorts[0].name,"NumberOfBits":self.numberOfBits,"PortType":"Input","ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + (str(self.number) + "_" + str(cascadeStageNumber)) + "Output"),"NumberOfBits":self.numberOfBits,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.frequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Depth":1, "Width":self.numberOfBits,"ShiftDirection":"Right","NumberOfBits":self.numberOfBits, "EsBits":self.esBits, "MantissaBits":self.mantissaBits, "ExponentBits":self.exponentBits}
                        mbDFF.configure()
                        mbDFF.process()
                        mbDFF.perform()
                        # append the mbRightSHR to the cascadedRegisters
                        self.cascadedRegisters.append(mbDFF)

                                   
                # build the input and output data ports of the cascadedregisters
                # access the 0th index mbRightSHR and access the inputDataPorts index 0

                if "InputDataPorts" in configurationDetails:
                    inputPortDetails = configurationDetails["InputDataPorts"]
                    
                    for portDetail in inputPortDetails:
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


                else:
                    # the value of the key is expected to be an array
                    inputPortDetails = [{"Name":self.cascadedRegisters[0].name,"NumberOfBits":self.cascadedRegisters[0].numberOfBits,"PortType":"Input","ConstantSignalValue":0}]
                    for portDetail in inputPortDetails:
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
                
                # the value of the key is expected to be an array
                outputPortDetails = [{"Name":"vout","NumberOfBits":self.cascadedRegisters[(len(self.cascadedRegisters)-1)].numberOfBits,"PortType":"Output","ConstantSignalValue":0}]
                for portDetail in outputPortDetails:
                    # access the information about the port or use the configuration details property to configure itself
                    newPort = Port()
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
        # the cascaded registers do not have hw description of its own for now
        # so, the perform function is disabled
        # access the cascaded registers or configure the hwDescription with the cascaded register details
        # once the details are set, we can generate the hw architecture description of the cascadedMBRightSHR
        self.hwVHDLDescription.perform()


    def process(self):
        super().process()
        self.configureHWDescriptionPackage()
        self.hwVHDLDescription.process()
    
    def configureHWDescriptionPackage(self):
        self.configurationDetailsOfHWLogic = {"Number":self.number,"Name":self.name,"PythonHWEntity":{"Name":self.name,"Number":self.number,"NumberSystem":self.numberSystemName,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":self.pythonHWLogicGeneric},"InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort},"PythonHWArchitecture":{"Name":self.name,"HWArchitectureTypeName":"RTL","InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort,"CascadedRegisters":self.cascadedRegisters, "PythonHWProcess":{"SensitivityList":[self.clockPort.name,self.resetPort.name],"PythonHWProcessInfo":self.pythonHWLogic,"PythonHWClockProcessInfo":{"Frequency":self.frequency, "ClockPortName":self.clockPort.name,"ClockStimulusName":(self.clockPort.name + "Stimulus")},"PythonHWIOStimulusProcessInfo":{"PythonHWProcessVariablesInfo":[{"Name":"fileline","Type":"line","NumberOfBits":None},{"NumberOfBits":self.numberOfBits,"Name":"inputBuffer","Type":"bit_vector"},{"Name":"commaBuffer","Type":"character","NumberOfBits":None}],"PythonHWProcessFileInfo":[{"Name":"outputFile","Mode":"write_mode", "Type":"text","FileName":("Output" + "_" + self.name + "_" + str(self.numberOfBits)),"FileExtension":"txt"},{"Name":"inputFile","Mode":"read_mode","Type":"text","FileName":("Input" + "_" + self.name + "_" + str(self.numberOfBits)),"FileExtension":"txt"}],"InputDataPorts":self.inputDataPorts,"OutputDataPorts":self.outputPorts}}}}
        
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
        # proeprty to store the cascaded registers as an array
        self.cascadedRegisters = None
        # cascade registers property to know whether cascading of number of registers should be preferred or not
        self.cascadeRegisters = False
        # the number of cascade stages to cascade multiple registers
        self.numberOfCascadeStages = 0

    def run(self):
        self.main()


