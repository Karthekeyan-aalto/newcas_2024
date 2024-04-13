"""
Created by Karthekeyan Periasamy
Edited on August 4, 2023, 10:41
"""

from SWOptimisers.SWPCSystemOptimiser.SWPCSystemOptimiser import SWPCSystemOptimiser

class SWPCMMACUnitSystemOptimiser(SWPCSystemOptimiser):

    def __init__(self):
        super().__init__()
        self.connect()

    
    def connect(self):
        self.connectProperties()
    

    def connectProperties(self):
        super().connectProperties()

        # property to store the MMACUnits to form the PCSystem
        self.mmacUnits = None
        
    def configure(self):
        super().configure()
        
        configurationDetails = self.configurationDetails

        if "MMACUnits" in configurationDetails:
            self.mmacUnits = configurationDetails["MMACUnits"]

      
    def reset(self):
        super().reset()
     
    def perform(self):
        super().perform()

    def process(self):
        super().process()

    def main(self):
        super().main()
        self.process()
        self.perform()

    def run(self):
        super().run()
