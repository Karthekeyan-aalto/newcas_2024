"""
Created by Karthekeyan Periasamy
Created on Apr 1, 15:13
"""

from HWDescription.HWDescription import HWDescription

class OperatorHWDescription(HWDescription):

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
