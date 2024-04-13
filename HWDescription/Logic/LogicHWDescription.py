"""
Created by Karthekeyan Periasamy
Created on Oct 26, 09:46
"""

from HWDescription.HWDescription import HWDescription

class LogicHWDescription(HWDescription):

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

