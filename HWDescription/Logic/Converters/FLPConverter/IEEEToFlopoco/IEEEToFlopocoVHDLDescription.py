"""
Created by Karthekeyan Periasamy
Edited on December 05 16:54
"""

from HWDescription.Logic.Converters.FLPConverter.FLPConverterVHDLDescription import FLPConverterVHDLDescription
from HWDescription.Logic.FF.MB_D_FF.MB_D_FF_VHDLDescription import MB_D_FF_VHDLDescription
from HWDescription.Entity.Converters.FLPConverter.IEEEToFlopoco.IEEEToFlopocoEntityVHDLDescription import IEEEToFlopocoEntityVHDLDescription


class IEEEToFlopocoVHDLDescription(FLPConverterVHDLDescription):

    def __init__(self):
        super().__init__()
    
    def connect(self):
        super().connect()
    
    def connectProperties(self):
        super().connectProperties()

    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        self.vhdlEntityDescription = IEEEToFlopocoEntityVHDLDescription()
    
   
    def configure(self):
        #print("Hi")
        super().configure()
        #print("Configuration Details of the IEEEToFlopocoVHDLDescription", self.configurationDetailsOfHW)
 
    def reset(self):
        super().reset()
    
    def process(self):
        self.vhdlEntityDescription.process()
        self.vhdlEntityArchitectureDescription.process()
    
    def perform(self):
        # first perfeorm the entity description
        # it will generate necessary VHDL definitions
        self.vhdlEntityDescription.perform()

    def main(self):
        self.process()

    def run(self):
        self.main()

