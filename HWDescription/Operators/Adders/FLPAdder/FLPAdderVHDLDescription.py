"""
Created by Karthekeyan Periasamy
Edited on June 16 10:00 AM
"""

from HWDescription.HWVHDLDescription import HWVHDLDescription
from HWDescription.Entity.Adders.FLPAdder.FLPAdderEntityVHDLDescription import FLPAdderEntityVHDLDescription
from HWDescription.Architecture.Adders.FLPAdder.FLPAdderArchitectureVHDLDescription import FLPAdderArchitectureVHDLDescription


class FLPAdderVHDLDescription(HWVHDLDescription):


    def __init__(self):
        super().__init__()

    def configure(self):
        super().configure()  
           
          
    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()

    def connect(self):
        self.connectProperties()
        self.connectHWVHDLPackages()

    def connectProperties(self):
        super().connectProperties()

    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        self.vhdlEntityDescription = FLPAdderEntityVHDLDescription()
        # connect the hw architecture packages
        self.vhdlEntityArchitectureDescription = FLPAdderArchitectureVHDLDescription()


    def process(self):
        self.vhdlEntityDescription.process()
        self.vhdlEntityArchitectureDescription.process()

    
    def perform(self):
        # first perfeorm the entity description
        # it will generate necessary VHDL definitions
        self.vhdlEntityDescription.perform()
                             
        
    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()

    def main(self):
        super().main()
    
    def run(self):
        self.main()
