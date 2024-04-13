"""
Created by Karthekeyan Periasamy
Edited on October 26 09:59
"""

from HWDescription.Logic.FF.MB_D_FF.MB_D_FF_VHDLDescription import MB_D_FF_VHDLDescription
from HWDescription.Architecture.Cascaded_MB_D_FF.Cascaded_MB_D_FF_ArchitectureVHDLDescription import Cascaded_MB_D_FF_ArchitectureVHDLDescription

class Cascaded_MB_D_FF_VHDLDescription(MB_D_FF_VHDLDescription):


    def __init__(self):
        super().__init__()
    

    def connectProperties(self):
        super().connectProperties()
        self.cascadedRegisters = None


    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        # connect the hw architecture packages
        self.vhdlEntityArchitectureDescription = Cascaded_MB_D_FF_ArchitectureVHDLDescription()

    def resetProperties(self):
        super().resetProperties()
        self.cascadedRegisters = None
    
    def configure(self):
        super().configure()
        # store the configuraiton details to a local variable
        configurationDetails = self.configurationDetailsOfHW
        #print("Configuration Details of Cascaded MB_D_FF", configurationDetails)

        if "CascadedRegisters" in configurationDetails:
            self.cascadedRegisters = configurationDetails["CascadedRegisters"]
           
    def process(self):
        super().process()

    def perform(self):
        super().perform()

    def main(self):
        super().main()
    
    def run(self):
        self.main()
