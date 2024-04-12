"""
Created by Karthekeyan Periasamy
Edited on April 29, 2023
"""

class PCOptimiser():
    """
    Class to optimise 1) ArithmeticNodes 2) MMACUnits and so on

    For now, optimisation is done for repeated arithmetic nodes, in future this class will be expanded
    """
    def __init__(self):
        
        # property to store the array of arithmetic nodes
        self.arithmeticNodes = None

        # property to store the configuration details of the arithmetic nodes
        self.configurationDetails = None


    def configure(self):
        
        # check if the configuration details are present for optimisation
        if self.configurationDetails == None:
            return

        # locally store the configuration details
        configurationDetails = self.configurationDetails 
        # check whether the arithmetic nodes  are present or not
        if "ArithmeticNodes" in configurationDetails:
            self.arithmeticNodes = configurationDetails["ArithmeticNodes"]


    def process(self):
        pass

    def main(self):
        pass

    def run(self):
        self.main()


