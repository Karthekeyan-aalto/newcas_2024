"""
Created by Karthekeyan Peirasamy
Edited on December 07 04:36
"""
from Logic.Converters.FLPConverter.FLPConverter import FLPConverter
from Logic.FF.MB_D_FF.MB_D_FF import MB_D_FF
from HWDescription.Logic.Converters.FLPConverter.FlopocoToIEEE.FlopocoToIEEEVHDLDescription import FlopocoToIEEEVHDLDescription

class FlopocoToIEEE(FLPConverter):

    def __init__(self):
        super().__init__()
    
    
    @property
    def flpFlopocoName(self):
        if self._flpFlopocoName == None:
            self._flpFlopocoName = "OutputIEEE" + "_" + str(self.exponentBits) + "_" +  str(self.mantissaBits-1) + "_" + "to" + "_" + str(self.exponentBits) + "_" + str(self.mantissaBits-1)
        return self._flpFlopocoName

    @flpFlopocoName.setter
    def flpFlopocoName(self,value):
        self._flpFlopocoName = value
    
       
    def connect(self):
        self.connectHWDescriptionPackage()
        self.connectProperties()
    
    def connectHWDescriptionPackage(self):
        self.hwDescription = FlopocoToIEEEVHDLDescription()
    
    def connectProperties(self):
        super().connectProperties()

        # property to add the input mb_d_ff
        self.input_MB_D_FF = None
        # property to add the output mb_d_ff
        self.output_MB_D_FF = None
        self._flpFlopocoName = None

    def configure(self):
        super().configure()

        configurationDetails = self.configurationDetailsOfLogic
        # configure the MB_D_FF using the given information
        if "Input_MB_D_FF" in configurationDetails:
            # add D_FF to input
            input_mb_d_ff = MB_D_FF()
            input_mb_d_ff.configurationDetailsOfLogic = configurationDetails["Input_MB_D_FF"]
            input_mb_d_ff.configure()
            self.input_MB_D_FF = input_mb_d_ff
            
        if "Output_MB_D_FF" in configurationDetails:
             # add D_FF to output
            output_mb_d_ff = MB_D_FF()
            output_mb_d_ff.configurationDetailsOfLogic = configurationDetails["Output_MB_D_FF"]
            output_mb_d_ff.configure()
            self.output_MB_D_FF = output_mb_d_ff

    def configureHWDescriptionPackage(self):
        self.hwDescription.configurationDetailsOfHW = self.configurationDetailsOfHWLogic
        self.hwDescription.configure()    
    
    def process(self):
        super().process()

    def perform(self):
        self.performHWGeneration()
    
    def performHWGeneration(self):
        self.configureHWDescriptionPackage()
        self.hwDescription.process()
        self.hwDescription.perform()
        
        self.input_MB_D_FF.process()
        self.input_MB_D_FF.perform()
        
        self.output_MB_D_FF.process()
        self.output_MB_D_FF.perform()

        print()

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

