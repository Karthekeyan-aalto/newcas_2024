"""
Created by Karthekeyan Periasamy
Edited on December 05 16:41
"""

from HWDescription.Logic.LogicVHDLDescription import LogicVHDLDescription

class ConverterVHDLDescription(LogicVHDLDescription):

    def __init__(self):
        super().__init__()

    def connect(self):
        super().connect()

    def process(self):
        super().process()
        
    def configure(self):
        super().configure()
 
    def reset(self):
        super().reset()
    
    def perform(self):
        super().perform()

    def main(self):
        self.process()

    def run(self):
        self.main()

