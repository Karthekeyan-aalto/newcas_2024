"""
Created by Karthekeyan Periasamy
Edited on October 26 09:42 AM
"""

from HWDescription.HWVHDLDescription import HWVHDLDescription

class LogicVHDLDescription(HWVHDLDescription):

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

