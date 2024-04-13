"""
Created by Karthekeyan Periasamy
Created on Oct 26 09:24
"""


from HWDescription.Logic.LogicVHDLDescription import LogicVHDLDescription

class FFVHDLDescription(LogicVHDLDescription):

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

