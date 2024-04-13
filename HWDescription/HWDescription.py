"""
Created by Karthekeyan Periasamy
Edited on June 16 11:04 AM
"""


class HWDescription():
    """
    This class represents the base properties for the LUT HW Description. It will also be the sub class of the operators hw description
    For now, only we have LUTs, in the future we will implement blocks or operators 
    that will be used by the OPerations entity to implement complex systems
    """

    def __init__(self):
        super().__init__()
        self.connect()
  

    @property
    def hwInstanceName(self):
        if self._hwInstanceName == None:
            # print the hwname, hwnumber system name and the number
            #print("HWName", self.hwName)
            #print("HWNumberSystemName", self.hwNumberSystemName)
            #print("HWNumber", self.hwNumber)
            self._hwInstanceName = self.hwName + "_" + self.hwNumberSystemName + "_" + str(self.hwNumber)
        return self._hwInstanceName

    @hwInstanceName.setter
    def hwInstanceName(self,value):
        self._hwInstanceName = value
       
    
   
    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        self.hwName = None
        self._hwInstanceName = None
        self.hwNumberSystemName = None
        self.hwNumber = None
        self.configurationDetailsOfHW = None
        # python HW
        self.pythonHW = None

    def main(self):
        pass
    
    def configure(self):
        if self.configurationDetailsOfHW == None:
            return

        configurationDetails = self.configurationDetailsOfHW
        
        if "NumberSystem" in configurationDetails:
            self.hwNumberSystemName = configurationDetails["NumberSystem"]
        
        if "Number" in configurationDetails:
            self.hwNumber = configurationDetails["Number"]

        if "Name" in configurationDetails:
            self.hwName = configurationDetails["Name"]

        if "PythonHW" in configurationDetails:
            self.pythonHW = configurationDetails["PythonHW"]
        else:
            self.pythonHW = str()



    def process(self):
        pass

    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        self.hwName = None
        self._hwInstanceName = None
        self.hwNumberSystemName = None
        self.hwNumber = None
        self.configurationDetailsOfHW = None
        # reset the python HW
        self.pythonHW = None

    def run(self):
        pass
