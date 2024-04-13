"""
Created by Karthekeyan Periasamy
Edited on Jan 8, 2023, 13:14
"""

from HWDescription.Architecture.ArchitectureVHDLDescription import ArchitectureVHDLDescription
from HWDescription.Process.Adders.FLPAdder.PositAdderProcessVHDLDescription import PositAdderProcessVHDLDescription


class PositAdderArchitectureVHDLDescription(ArchitectureVHDLDescription):

    def __init__(self):
        self.connect()
      
      
    """
    # Start: vhdlExtraSignals getters
    """

    @property
    def vhdlExtraSignals(self):
        if self._vhdlExtraSignals == None:
            self._vhdlExtraSignals = list()
            
        return self._vhdlExtraSignals
        
    @vhdlExtraSignals.setter
    def vhdlExtraSignals(self, value):
        self._vhdlExtraSignals = value
       
    """
    # End: vhdlExtraSignals setters and getters
    """
    
    """
    # Start: extraVHDLOutputSignals getters
    """

    @property
    def extraVHDLOutputSignals(self):
        return self._extraVHDLOutputSignals
        
    @extraVHDLOutputSignals.setter
    def extraVHDLOutputSignals(self, value):
        self._extraVHDLOutputSignals = value

        # update the extraVHDLOutputSignals
        self.appendExtraVHDLOutputSignals()
               
    """
    # End: extraVHDLOutputSignals setters and getters
    """
    
    """
    # Start: extraVHDLInputSignals getters
    """

    @property
    def extraVHDLInputSignals(self):
        return self._extraVHDLInputSignals
        
    @extraVHDLInputSignals.setter
    def extraVHDLInputSignals(self, value):
        self._extraVHDLInputSignals = value

        # update the extraVHDLInputSignals
        self.appendExtraVHDLInputSignals()
               
    """
    # End: extraVHDLInputSignals setters and getters
    """

   
    def connect(self):
        super().connect()    

    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        # connect the hw process packages
        self.vhdlProcessDescription = PositAdderProcessVHDLDescription()

  

    def connectProperties(self):
        super().connectProperties()
        self._vhdlExtraSignals = None
        self._extraVHDLOutputSignals = None
        self._extraVHDLInputSignals = None


    
    def reset(self):
        super().reset()
   
    def appendExtraVHDLOutputSignals(self):
        self.vhdlExtraSignals = self.vhdlExtraSignals + self.extraVHDLOutputSignals

    
    def appendExtraVHDLInputSignals(self):
        self.vhdlExtraSignals = self.vhdlExtraSignals + self.extraVHDLInputSignals

    def resetProperties(self):
        super().resetProperties()
        self._vhdlExtraSignals = None
        self._extraVHDLOutputSignals = None
        self._extraVHDLInputSignals = None


    def configure(self):
        super().configure()

        configurationDetails = self.configurationDetailsOfHW

        if "ExtraOutputSignals" in configurationDetails:
            self.extraVHDLOutputSignals = configurationDetails["ExtraOutputSignals"]

        if "ExtraInputSignals" in configurationDetails:
            self.extraVHDLInputSignals = configurationDetails["ExtraInputSignals"]
        

    
    def process(self):
        super().process()

      
    def perform(self):
        super().perform()

    def main(self):
        super().main()
        self.process()
        self.perform()

    def run(self):
        self.main()

