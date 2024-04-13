"""
Created by Karthekeyan Periasamy
Created on Jan 18 14:31 PM
"""

from HWDescription.Operators.OperatorHWDescription import OperatorHWDescription

class LUTHWDescription(OperatorHWDescription):
    """
    This class represents the base properties for the LUT HW Description. It will also be the sub class of the operators hw description
    For now, only we have LUTs, in the future we will implement blocks or operators 
    that will be used by the OPerations entity to implement complex systems
    """

    def __init__(self):
        super().__init__()
        # reset the python LUT Generics
        # property to store the generic map details of the LUT HW
        # it is a dictionary , where the keys are the generics name
        # and the values are the generic values
        self.lutGenerics = None
  
    
    def main(self):
        super().main()

    
    def configure(self):
        # call the super function
        super().configure()

    def process(self):
        super().process()

    def reset(self):
        super().reset()
        # reset the python LUT Generics
        # property to store the generic map details of the LUT HW
        # it is a dictionary , where the keys are the generics name
        # and the values are the generic values
        self.lutGenerics = None

    def run(self):
        pass
