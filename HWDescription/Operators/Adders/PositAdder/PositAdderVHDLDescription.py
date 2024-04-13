"""
Created by Karthekeyan Periasamy
Edited on Sep 14 13:28
"""

from HWDescription.HWVHDLDescription import HWVHDLDescription
from HWDescription.Entity.EntityVHDLDescription import EntityVHDLDescription

class PositAdderVHDLDescription(HWVHDLDescription):

    def __init__(self):
        super().__init__()
  
    
    @property
    def hwName(self):
        return  self._hwName

    def hwName(self,value):
        self._hwName = value
        if self.vhdlEntityDescription.configurationDetailsOfHW["PythonHWEntity"]["EsBits"] > 3:
            
            if self.vhdlEntityDescription.pythonHWClockPort.frequency == 0:
                # set another POSIT custom name
                self._hwName = ("PositMult" + "_" + str(self.numberOfBits) + "_" + str(self.vhdlEntityDescription.configurationDetailsOfHW["PythonHWEntity"]["EsBits"]) + "_" + "comb" + "_" + "uid" + "2")
            elif self.vhdlEntityDescription.pythonHWClockPort.frequency > 0:
                # set another POSIT custom name
                self._hwName = ("PositMult" + "_" + str(self.numberOfBits) + "_" + str(self.vhdlEntityDescription.configurationDetailsOfHW["PythonHWEntity"]["EsBits"]) + "_" + "F" + str(self.frequency) + "_" + "uid" + "2")
        else:
            # set another POSIT custom name
            self._hwName = ("PositMult" + "_" + str(self.numberOfBits) + "_" + str(self.vhdlEntityDescription.configurationDetailsOfHW["PythonHWEntity"]["EsBits"]) + "_" + "F0" + "_" + "uid" + "2") 

    
    
    def connect(self):
        self.connectHWVHDLPackages()
        self.connectProperties()

    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()

    def connectProperties(self):
        super().connectProperties()
       

    def process(self):
        super().process()


    def perform(self):
        super().perform()

    def configure(self):
        super().configure()

    def reset(self):
        super().reset()
        
      
    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()

