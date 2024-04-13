"""
Created by Karthekeyan Periasamy
Edited on Jan 4, 2023, 15:12
"""

from HWDescription.Architecture.ArchitectureVHDLDescription import ArchitectureVHDLDescription
from HWDescription.Process.Multipliers.FLPMultiplier.PositMiultiplierProcessVHDLDescription import PositMultiplierProcessVHDLDescription

class PositMultiplierArchitectureVHDLDescription(ArchitectureVHDLDescription):

    def __init__(self):
        self.connect()
      
    """
    # Start: vhdlWeightSignals getters
    """

    @property
    def vhdlWeightSignals(self):
        if self._vhdlWeightSignals == None:
            self._vhdlWeightSignals = list()
            
        return self._vhdlWeightSignals
        
    @vhdlWeightSignals.setter
    def vhdlWeightSignals(self, value):
        self._vhdlWeightSignals = value
       
    """
    # End: vhdlWeightSignals setters and getters
    """
    
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
        self.vhdlProcessDescription = PositMultiplierProcessVHDLDescription()

  

    def connectProperties(self):
        super().connectProperties()        
        #property to store the vhdl constant in an array
        self._vhdlWeightSignals = None
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
        #property to store the vhdl constant in an array
        self._vhdlWeightSignals = None
        self._vhdlExtraSignals = None
        self._extraVHDLOutputSignals = None
        self._extraVHDLInputSignals = None


    def configure(self):
        super().configure()

        configurationDetails = self.configurationDetailsOfHW

        if "ExtraOutputSignals" in configurationDetails:
            self.extraVHDLOutputSignals = configurationDetails["ExtraOutputSignals"]
            #print("Extra VHDL Output Signals", self.extraVHDLOutputSignals)

        if "ExtraInputSignals" in configurationDetails:
            self.extraVHDLInputSignals = configurationDetails["ExtraInputSignals"]
        
        if "WeightSignal" in configurationDetails:
            self.vhdlWeightSignals = configurationDetails["WeightSignal"]
            self.vhdlExtraSignals = self.vhdlExtraSignals + self.vhdlWeightSignals

    
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

