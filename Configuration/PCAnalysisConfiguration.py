# class made by Karthek
# Sep 30 09:51


from PCSystemConfiguration import PCSystemConfiguration

class PCAnalysisConfiguration(PCSystemConfiguration):
    """
    This class handles the configuration of Analysis Package
    Why use this module: Given PCSystem Analysis package details as a dictionary
    this class will set the respective properties, which then can be used by other modules or packages. For instance, PCAnalysis module can use
    the configuration package

    """

    def __init__(self):
        super().__init__()
        # propertu to store the details of the analysis package
        self._pcAnalysisMode = None
        # property to store the preferred error analysis type
        self._pcAnalysisErrorType = None
        # property to store the type of analysis
        # zero value is used to deactivate both the minAnalysis and resAnalysis
        self._minAnalysis = None
        self._resAnalysis = None
        # error tolerance on which the analysis should be carried out
        self._pcAnalysisErrorTolerance = None
        # store the configuration details
        self._configurationDetailsOfAnalysisPackage = None
    
    """
    Properties of PCSystem Configuration
    """
    @property
    def configurationDetailsOfAnalysisPackage(self):
        return self._configurationDetailsOfAnalysisPackage
    
    @configurationDetailsOfAnalysisPackage.setter
    def configurationDetailsOfAnalysisPackage(self,value):
        self._configurationDetailsOfAnalysisPackage = value
        # check the configuration details object is not empty
        if self.configurationDetailsOfAnalysisPackage == None:
            print("Configuration Details of Analysis package is missing")
            return

        # read the configuration details dictionary
        configurationDetails = self.configurationDetailsOfAnalysisPackage
        # check whether the bitoptimisation is present or not
        if "ActivateBitOptimisation" in configurationDetails:
            # access the bitoptimisation value
            activateBitOptimisation = configurationDetails["ActivateBitOptimisation"]
            if activateBitOptimisation == "1":
                self.minAnalysis = 1
            else:
                self.minAnalysis = 1


    @property
    def minAnalysis(self):
        return self._minAnalysis

    @minAnalysis.setter
    def minAnalysis(self, value):
        self._minAnalysis = value
        self.resAnalysis = value
    
    @property
    def resAnalysis(self):
        return self._resAnalysis

    @resAnalysis.setter
    def resAnalysis(self, value):
        self._resAnalysis = value
  
    def main(self):
        pass

    def run(self):
        pass
