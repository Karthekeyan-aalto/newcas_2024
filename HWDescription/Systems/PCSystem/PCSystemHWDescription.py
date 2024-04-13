"""
Created by Karthekeyan Periasamy
Edited on 31 Dec 2023 10:31
"""

from HWDescription.HWDescription import HWDescription

class PCSystemHWDescription(HWDescription):

    def __init__ (self):
        super().__init__()
        self.connect()
    
    def connect(self):
        super().connect()

    def connectProperties(self):
        super().connectProperties()

    def configure(self):
        super().configure()
        
    def reset (self):
        super().reset()
        
    def main(self):
        super().main()

    def run(self):
        self.main()
