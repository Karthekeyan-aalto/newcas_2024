"""
Created by Karthekeyan Periasamy
Edited on Jan 14, 2023, 15:38
"""

from HWDescription.Architecture.Systems.PCSystem.PCSystemArchitectureVHDLDescription import PCSystemArchitectureVHDLDescription
from HWDescription.Process.Systems.PCSystem.PositPCSystem.PositPCSystemProcessVHDLDescription import PositPCSystemProcessVHDLDescription


class FLPPCSystemArchitectureVHDLDescription(PCSystemArchitectureVHDLDescription):

    def __init__(self):
        self.connect()
    
   
    def connect(self):
        super().connect()    

    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()


    def connectProperties(self):
        super().connectProperties()
    
    def reset(self):
        super().reset()
           
        
    def resetProperties(self):
        super().resetProperties()        


    def configure(self):
        super().configure()
    
   
    def process(self):
        super().process()

      
    def perform(self):
        super().perform()

    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()

