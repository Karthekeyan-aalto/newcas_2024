"""
Created by Karthekeyan Periasamy
Edited on December 31 10:42 AM
"""

from HWDescription.Systems.PCSystem.PCSystemVHDLDescription import PCSystemVHDLDescription
from HWDescription.Entity.Systems.PCSystem.PositPCSystem.PositPCSystemEntityVHDLDescription import PositPCSystemEntityVHDLDescription
from HWDescription.Architecture.Systems.PCSystem.PositPCSystem.PositPCSystemArchitectureVHDLDescription import PositPCSystemArchitectureVHDLDescription


class PositPCSystemVHDLDescription(PCSystemVHDLDescription):


    def __init__(self):
        super().__init__()

  
    def configure(self):
        super().configure()  
           
          
    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        self.vhdlEntityDescription = PositPCSystemEntityVHDLDescription()
        # connect the hw architecture packages
        self.vhdlEntityArchitectureDescription = PositPCSystemArchitectureVHDLDescription()

    def connect(self):
        super().connect()
    
    
    def processHWPipelineStagesForPCTree(self):
        return super().processHWPipelineStagesForPCTree()
                                
    
    def generateHWPipelineProcessUsingPipelineStagesOfPCTree(self):
        super().generateHWPipelineProcessUsingPipelineStagesOfPCTree()
           
    """
    # Start: balance forward paths of arithmetic nodes
    """

    def performExtractionOfPCTreeLevelBasedArithmeticNodeDetails(self):
        super().performExtractionOfPCTreeLevelBasedArithmeticNodeDetails()
           
        
    """
    # End: balance forwards paths of  arithmetic nodes
    """
   
    def process(self):
        super().process()

    
    def perform(self):
        super().perform()
        
    def reset(self):
        super().reset()

    def main(self):
        super().main()
    
    def run(self):
        self.main()
