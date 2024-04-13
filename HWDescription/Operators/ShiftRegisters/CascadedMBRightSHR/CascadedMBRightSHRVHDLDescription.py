"""
Created by Karthekeyan Periasamy
Edited on September 9 13:00 PM
"""

from HWDescription.Operators.ShiftRegisters.MBRightSHR.MBRightSHRVHDLDescription import MBRightSHRVHDLDescription
from HWDescription.Architecture.CascadedMBRightSHR.CascadedMBRightSHRArchitectureVHDLDescription import CascadedMBRightSHRArchitectureVHDLDescription

class CascadedMBRightSHRVHDLDescription(MBRightSHRVHDLDescription):


    def __init__(self):
        super().__init__()
    

    def connectProperties(self):
        super().connectProperties()
        self.cascadedRegisters = None


    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        # connect the hw architecture packages
        self.vhdlEntityArchitectureDescription = CascadedMBRightSHRArchitectureVHDLDescription()
        #print("VHDL entity architecture description", self.vhdlEntityArchitectureDescription)

    def resetProperties(self):
        super().resetProperties()
        self.cascadedRegisters = None
    
    def configure(self):
        super().configure()
        # store the configuraiton details to a local variable
        configurationDetails = self.configurationDetailsOfHW
        #print("Configuration Details of Cascaded MBRightSHR HW", configurationDetails)

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
