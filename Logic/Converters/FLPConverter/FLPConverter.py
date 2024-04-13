"""
Created by Karthekeyan Peirasamy
Edited on November 28 08:58
"""
from Logic.Converters.Converter import Converter

class FLPConverter(Converter):

    def __init__(self):
        self.connect()

    def connect(self):
        self.connectProperties()
    
    def connectProperties(self):
        super().connectProperties()

    def configure(self):
        super().configure()                
    
    @property
    def flpFlopocoName(self):
        return self._flpFlopocoName

    @flpFlopocoName.setter
    def flpFlopocoName(self,value):
        self._flpFlopocoName = value
    

    def processHWLogicConfigurationDetails(self):
        self.configurationDetailsOfHWLogic = {"Number":self.number,"Name":self.name,"NumberSystem":"Float","PythonHWEntity":{"Name":self.name,"NumberSystem":"Float","Number":self.number,"FLPFlopocoName":self.flpFlopocoName,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":self.pythonHWLogicGeneric},"InputDataPorts":self.inputDataPorts, "OutputDataPorts":self.outputPorts,"InputClockPort":self.clockPort, "InputResetPort":self.resetPort}}
    
    
    def process(self):
        super().process()

    def perform(self):
        super().perform()


    def main(self):
        super().main()
        self.process()
        self.perform()
    
    def run(self):
        self.main() 

