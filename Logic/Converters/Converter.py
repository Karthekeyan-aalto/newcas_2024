"""
Created by Karthekeyan Peirasamy
Edited on November 28 08:58
"""

from Logic.Logic import Logic

class Converter(Logic):

    def __init__(self):
        self.connect()

    def connect(self):
        self.connectProperties()
    
    def connectProperties(self):
        super().connectProperties()

    def configure(self):
        super().configure()       
   
    def processHWLogicConfigurationDetails(self):
        self.configurationDetailsOfHWLogic = {"Name":self.name,"PythonHWEntity":{"Name":self.name,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":self.pythonHWLogicGeneric},"InputDataPorts":[self.inputDataPorts], "OutputDataPorts":[self.outputPorts], "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"InputEnablePort":self.enablePort},"PythonHWArchitecture":{"Name":self.name,"HWArchitectureTypeName":"RTL","InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts, "InputClockPort":self.clockPort, "InputResetPort":self.resetPort,"PythonHWProcess":{"SensitivityList":[self.clockPort.name,self.resetPort.name]}}
            ,"PythonHW":{self.pythonHWOperator}} 

    def performHWGeneration():
        pass

    def process(self):
        super().process()

    def perform(self):
        super().perform()

    def reset(self):
        self.resetProperties()
    
    def resetProperties(self):
        super().resetProperties()

    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()
