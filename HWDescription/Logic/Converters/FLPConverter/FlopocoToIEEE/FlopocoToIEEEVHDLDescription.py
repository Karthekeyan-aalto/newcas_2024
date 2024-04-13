"""
Created by Karthekeyan Periasamy
Edited on December 07 16:38
"""

from HWDescription.Logic.Converters.FLPConverter.FLPConverterVHDLDescription import FLPConverterVHDLDescription
from HWDescription.Logic.FF.MB_D_FF.MB_D_FF_VHDLDescription import MB_D_FF_VHDLDescription
from HWDescription.Entity.Converters.FLPConverter.FlopocoToIEEE.FlopocoToIEEEEntityVHDLDescription import FlopocoToIEEEEntityVHDLDescription


class FlopocoToIEEEVHDLDescription(FLPConverterVHDLDescription):

    def __init__(self):
        super().__init__()
    
    def connect(self):
        super().connect()
    
    def connectProperties(self):
        super().connectProperties()

    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        self.vhdlEntityDescription = FlopocoToIEEEEntityVHDLDescription()
    
   
    def configure(self):
        super().configure()
 
    def reset(self):
        super().reset()
    
    def process(self):
        self.vhdlEntityDescription.process()
    
    def perform(self):
        # first perfeorm the entity description
        # it will generate necessary VHDL definitions
        self.vhdlEntityDescription.perform()

    def main(self):
        self.process()

    def run(self):
        self.main()

