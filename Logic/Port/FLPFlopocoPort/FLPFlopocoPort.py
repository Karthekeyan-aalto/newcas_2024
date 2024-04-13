"""
Created by Karthekeyan Periasamy
Created on Dec 13 14:28
"""

from Logic.Port.Port import Port
from HWDescription.Logic.Port.FLPFlopocoPort.FLPFlopocoPortVHDLDescription import FLPFlopocoPortVHDLDescription

class FLPFlopocoPort (Port):
    """
    This class will be the new sample Port class
    The older Ports on Operations and PCSystem are not really serving the purpose as the system became complex
    This new port class will redefine the attributes of the Port and even support its own HW Description
    Ofcourse, Port object cannot be siumulated and so it cannot support HWSimulation
    """

    def __init__(self):
        # connect the necessary packages
        self.connect()

    
    """
    Object Function Definitions
    """
    def connect(self):
        self.connectProperties()
        self.connectHWDescriptionPackage()
        
    
    def connectProperties(self):
        super().connectProperties()
        
      
    def connectHWDescriptionPackage(self):
        # connect the hwDescription package to generate VHDL definitions of a port
        self.hwDescription = FLPFlopocoPortVHDLDescription()


    def configure(self):
        super().configure()
        
        configurationDetails = self.configurationDetails
        if "FlopocoBits" in configurationDetails:
            self.flopocoBits = configurationDetails["FlopocoBits"]

                   
    def process(self):
        super().process()
   
    def reset(self):
        self.resetProperties()
        self.resetHWDescriptionPackage()

  
    def resetProperties(self):
        super().resetProperties()
    
    def resetHWDescriptionPackage(self):
        # connect the hwDescription package to generate VHDL definitions of a port
        self.hwDescription = FLPFlopocoPortVHDLDescription()

    def perform(self):
        super().perform()

    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()
