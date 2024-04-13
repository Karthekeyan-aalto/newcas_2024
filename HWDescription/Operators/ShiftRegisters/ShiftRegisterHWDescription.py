"""
Created by Karthekeyan Periasamy
Created on Jan 18 14:31 PM
"""

from HWDescription.Operators.OperatorHWDescription import OperatorHWDescription

class ShiftRegisterHWDescription(OperatorHWDescription):
    """
    This class represents the base properties for the LUT HW Description. It will also be the sub class of the operators hw description
    For now, only we have LUTs, in the future we will implement blocks or operators 
    that will be used by the OPerations entity to implement complex systems
    """

    def __init__(self):
        super().__init__()
        self.pythonSHR = None
        # reset the python shift register Generics
        # property to store the generic map details of the operator HW
        # it is a dictionary , where the keys are the generics name
        # and the values are the generic values
        self.shrGenerics = None
  
    
    def main(self):
        pass

    
    def configure(self):
        # call the super function
        super().configure()
        

    def process(self):
        pass

    def reset(self):
        super().reset()
        # reset the python LUT
        self.pythonSHR = None
        # reset the python shift register Generics
        # property to store the generic map details of the operator HW
        # it is a dictionary , where the keys are the generics name
        # and the values are the generic values
        self.shrGenerics = None

    def run(self):
        pass
