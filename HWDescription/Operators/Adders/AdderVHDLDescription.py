"""
Created by Karthekeyan Periasamy
Edited on Sep 14 12:32 AM
"""

from HWDescription.HWVHDLDescription import HWVHDLDescription

class AdderVHDLDescription(HWVHDLDescription):

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

