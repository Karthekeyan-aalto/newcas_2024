"""
Created by Karthekeyan Peirasamy
Edited on November 28 08:58
"""
from Logic.Converters.FLPConverter.FLPConverter import FLPConverter
from Operators.Port.FLPFlopocoPort.FLPFlopocoPort import FLPFlopocoPort
from Logic.FF.MB_D_FF.MB_D_FF import MB_D_FF
from Logic.FF.MB_D_FF.FLPMB_D_FF.FLPMB_D_FF import FLPMB_D_FF
from HWDescription.Logic.Converters.FLPConverter.IEEEToFlopoco.IEEEToFlopocoVHDLDescription import IEEEToFlopocoVHDLDescription

class IEEEToFlopoco(FLPConverter):

    def __init__(self):
        super().__init__()
        
    @property
    def flpFlopocoName(self):
        if self._flpFlopocoName == None:
            self._flpFlopocoName = "InputIEEE" + "_" + str(self.exponentBits) + "_" +  str(self.mantissaBits-1) + "_" + "to" + "_" + str(self.exponentBits) + "_" + str(self.mantissaBits-1)
        return self._flpFlopocoName

    @flpFlopocoName.setter
    def flpFlopocoName(self,value):
        self._flpFlopocoName = value
    
       
    def connect(self):
        self.connectHWDescriptionPackage()
        self.connectProperties()
    
    def connectHWDescriptionPackage(self):
        self.hwDescription = IEEEToFlopocoVHDLDescription()
    
    def connectProperties(self):
        super().connectProperties()

        # property to add the input mb_d_ff
        self.input_MB_D_FF = None
        # property to add the output mb_d_ff
        self.output_MB_D_FF = None
        self._flpFlopocoName = None

    def configure(self):
        super().configure()
        
        # intialise the inputDataPorts array
        self.inputDataPorts = list()
        # intialise the outputPorts array
        self.outputPorts = list()
        
        configurationDetails = self.configurationDetailsOfLogic

        
        # check the configuration details contains input data ports
        if "InputDataPorts" in configurationDetails:

            # access the ports and set the details of the port
            # the value of the key is expected to be an array
            portDetails = configurationDetails["InputDataPorts"]
            #print("Operator InputDataPorts", portDetails)
            for portDetail in portDetails:
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
                self.inputDataPortsInfo[newPort.name] = newPort


        # check the configuration details contains output port details
        if "OutputPorts" in configurationDetails:
            # access the ports and set the details of the port
            # the value of the key is expected to be an array
            portDetails = configurationDetails["OutputPorts"]
            for portDetail in portDetails:
                # access the information about the port or use the configuration details property to configure itself
                newPort = FLPFlopocoPort()
                newPort.configurationDetails = portDetail
                # configure the port
                newPort.configure()
                # process the port
                newPort.process()
                newPort.perform()
                # once the port is configured, add the port to the output array
                self.outputPorts.append(newPort)
                self.outputPortsInfo[newPort.name] = newPort

        
        # configure the MB_D_FF using the given information
        if "Input_MB_D_FF" in configurationDetails:
            # add D_FF to input
            input_mb_d_ff = MB_D_FF()
            input_mb_d_ff.configurationDetailsOfLogic = configurationDetails["Input_MB_D_FF"]
            input_mb_d_ff.configure()
            self.input_MB_D_FF = input_mb_d_ff
            
        if "Output_MB_D_FF" in configurationDetails:
             # add D_FF to output
            output_mb_d_ff = FLPMB_D_FF()
            output_mb_d_ff.configurationDetailsOfLogic = configurationDetails["Output_MB_D_FF"]
            output_mb_d_ff.configure()
            self.output_MB_D_FF = output_mb_d_ff


    def processHWLogicConfigurationDetails(self):
        self.configurationDetailsOfHWLogic = {"Name":self.name,"NumberSystem":"Float","Number":self.number,"PythonHWEntity":{"Name":self.name,"NumberSystem":"Float","Number":self.number,"FLPFlopocoName":self.flpFlopocoName,"InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort},"PythonHWArchitecture":{"Name":self.flpFlopocoName,"HWArchitectureTypeName":"RTL","InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"PythonHWProcess":{"SensitivityList":[self.clockPort.name,self.resetPort.name]}},"PythonHW":{self.pythonHWLogic}}
        self.hwDescription.configurationDetailsOfHW = self.configurationDetailsOfHWLogic
        self.hwDescription.configure() 
    
    def process(self):
        super().process()

    def perform(self):
        self.performHWGeneration()

    
    def performHWGeneration(self):
        self.hwDescription.process()
        self.hwDescription.perform()
        
        self.input_MB_D_FF.process()
        self.input_MB_D_FF.perform()
        
        self.output_MB_D_FF.process()
        self.output_MB_D_FF.perform()

    def reset(self):
        super().reset()
        
        # this name will be the name of the hardware
        self._flpFlopocoName = None
        # property to add the input mb_d_ff
        self.input_MB_D_FF = None
        # property to add the output mb_d_ff
        self.output_MB_D_FF = None


    def main(self):
        self.process()
        self.perform()
    
    def run(self):
        self.main() 

