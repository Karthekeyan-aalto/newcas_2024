"""
Created by Karthekeyan Periasamy
Edited on June 16 09:59 AM
"""

from HWDescription.HWVHDLDescription import HWVHDLDescription

class OperatorVHDLDescription(HWVHDLDescription):

    def __init__(self):
        super().__init__()

    def process(self):
        super().process()
        

    def configure(self):
        super().configure()
 
    def reset(self):
        super().reset()
       

    def main(self):
        self.process()

    def run(self):
        self.main()

