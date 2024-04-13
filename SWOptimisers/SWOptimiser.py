"""
Created by Karthekeyan Periasamy
Edited on August 04, 2023
"""

class SWOptimiser():
    """
    Class to optimise 1) ArithmeticNodes 2) MMACUnits and so on

    For now, optimisation is done for repeated arithmetic nodes, in future this class will be expanded
    """
    def __init__(self):
        self.connect()
    

    @property
    def arithmeticNodes(self):
        return self._arithmeticNodes

    @arithmeticNodes.setter
    def arithmeticNodes(self,value):
        self._arithmeticNodes  = value
    
    def connect(self):
        self.connectProperties()


    def connectProperties(self):
        # property to store the array of arithmetic nodes
        self._arithmeticNodes = None

        # property to store the configuration details of the arithmetic nodes
        self.configurationDetails = None
        
        # property to store the optimised arithmetic nodes
        self.optimisedArithmeticNodes = None

        # property to store the total number of arithmeticNodes
        self.totalNumberOfArithmeticNodes = 0

        #property to store the total number of adder nodes
        self.totalNumberOfAdders = 0

        # property to store the total number of multiplier nodes
        self.totalNumberOfMultipliers = 0
        
        # property to know the pipelineDepth of the Adder and Multiplier
        self.adderPipelineDepth = 2

        self.multiplierPipelineDepth = 2

    
    def configure(self):
        
        # check if the configuration details are present for optimisation
        if self.configurationDetails == None:
            return

        # locally store the configuration details
        configurationDetails = self.configurationDetails 
        # check whether the arithmetic nodes  are present or not
        if "ArithmeticNodes" in configurationDetails:
            self.arithmeticNodes = configurationDetails["ArithmeticNodes"]

        # set the pcSystemAdderPipeline Depth
        if "AdderPipelineDepth" in self.configurationDetails:
            self.adderPipelineDepth = self.configurationDetails["AdderPipelineDepth"]
        
        # set the pcSystem Multiplier Pipeline Depth
        if "MultiplierPipelineDepth" in self.configurationDetails:
            self.multiplierPipelineDepth = self.configurationDetails["MultiplierPipelineDepth"]
        
        if "TopNode" in configurationDetails:
            self.topNode = configurationDetails["TopNode"]
    
    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        # property to store the array of arithmetic nodes
        self._arithmeticNodes = None

        # property to store the configuration details of the arithmetic nodes
        self.configurationDetails = None
        
        # property to store the optimised arithmetic nodes
        self.optimisedArithmeticNodes = None
        
        # property to know the pipelineDepth of the Adder and Multiplier
        self.adderPipelineDepth = 2

        self.multiplierPipelineDepth = 2
        
        # property to store the total number of arithmeticNodes
        self.totalNumberOfArithmeticNodes = 0

        #property to store the total number of adder nodes
        self.totalNumberOfAdders = 0

        # property to store the total number of multiplier nodes
        self.totalNumberOfMultipliers = 0

    
    def process(self):
        pass

    def perform(self):
        pass


    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()


