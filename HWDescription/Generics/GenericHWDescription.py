"""
Created by Karthekeyan Periasamy
Edited on June 16 11:45
"""


class GenericHWDescription():

    def __init__(self):
        self.connectProperties()
        
    def configure(self):
        # check if the configuration details are there or not
        if self.configurationDetailsOfHWGenerics == None:
            return

        # store the configuraiton details to a local variable
        configurationDetails = self.configurationDetailsOfHWGenerics
        
        # check if the name key is available in the configuration details
        if "GenericTypeName" in configurationDetails:
            self.hwGenericTypeName = configurationDetails["GenericTypeName"]
            
        # check if the name key is available in the configuration details
        if "PythonHWGeneric" in configurationDetails:
            self.pythonHWGeneric = configurationDetails["PythonHWGeneric"]


    def process(self):
        pass

    def perform(self):
        pass
    
    @property
    def pythonHWGeneric(self):
        return self._pythonHWGeneric
    
    @pythonHWGeneric.setter
    def pythonHWGeneric(self,value):
        self.pythonHWGeneric = value


    def connectProperties(self):
        # property to store the generic map details of the HW
        # it is a dictionary , where the keys are the generics name
        # and the values are the generic values
        self._pythonHWGeneric = None
        # property to store the generic type name
        self.hwGenericTypeName = None
        # property to store the configuration details, which will be used to build a generic
        self.configurationDetailsOfHWGenerics = None


    def resetProperties(self):
        # property to store the generic map details of the HW
        # it is a dictionary , where the keys are the generics name
        # and the values are the generic values
        self._pythonHWGeneric = None
        # property to store the generic type name
        self.hwGenericTypeName = None
        # property to store the configuration details, which will be used to build a generic
        self.configurationDetailsOfHWGenerics  = None
     
    
    
    def reset(self):
        self.resetProperties()

    def main(self):
        pass
