"""
Created by Karthekeyan Periasamy
Edited on June 16 10:00 AM
"""

from HWDescription.HWVHDLDescription import HWVHDLDescription
from HWDescription.Entity.Multipliers.FLPMultiplier.FLPMultiplierEntityVHDLDescription import FLPMultiplierEntityVHDLDescription
from HWDescription.Architecture.Multipliers.FLPMultiplier.FLPMultiplierArchitectureVHDLDescription import FLPMultiplierArchitectureVHDLDescription


class FLPMultiplierVHDLDescription(HWVHDLDescription):


    def __init__(self):
        super().__init__()

    def configure(self):
        super().configure()
        #print("Configuration Details", self.configurationDetailsOfHW)
           
          
    def connect(self):
        self.connectProperties()
        self.connectHWVHDLPackages()

    def connectProperties(self):
        super().connectProperties()

    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        self.vhdlEntityDescription = FLPMultiplierEntityVHDLDescription()
        # connect the hw architecture packages
        self.vhdlEntityArchitectureDescription = FLPMultiplierArchitectureVHDLDescription()

    def process(self):
        self.vhdlEntityDescription.process()
        self.vhdlEntityArchitectureDescription.process()

    
    def perform(self):
        # first perfeorm the entity description
        # it will generate necessary VHDL definitions
        self.vhdlEntityDescription.perform()

        #print("VHDL Output Signals", self.vhdlEntityArchitectureDescription.vhdlOutputSignals)
        #print("Total VHDL Output Signals of Multiplier",self.vhdlEntityArchitectureDescription.extraVHDLOutputSignals)

        
    def reset(self):
        super().reset()
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()

    def main(self):
        super().main()
    
    def run(self):
        self.main()
