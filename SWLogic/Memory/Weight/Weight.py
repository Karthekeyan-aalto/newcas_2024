"""
Created by Karthekeyan Periasamy
Edited on Jan 23 =8:15
Rewriting the product node code
"""


class Weight():

    """
    Class to have blueprint of the different types of multipliers
    In general a multiplier will have a LUT, Input Converter, A Multiplier, Output Converter.
    Based on the number systems, we may or may not have the converters, but for sure we will have LUTs.
    """

    def __init__(self):
        self.connect()    
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value
    
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self,value):
        self._number = value
    
    
    @property
    def numberSystemName(self):
        return self._numberSystemName

    @numberSystemName.setter
    def numberSystemName(self,value):
        self._numberSystemName = value

        # check the property if its !0 none
        if self._numberSystemName != None:
            # set the numberSystem based on the name
            if self._numberSystemName == "Fixed":
                self.numberSystem = 0
            elif self._numberSystemName == "Float":
                self.numberSystem = 1
            elif self._numberSystemName == "Posit":
                self._numberSystem = 2

        
    def connect(self):
        self.connectProperties()
    

    def connectProperties(self):

        # property to store the name of the multiplier
        self.name = None


    def configure(self):
        # check if the configuration details of the multiplier is set or not
        if self.configureDetailsOfWeight == None:
            return

        # store the configuration details on the local variable
        configurationDetails = self.configureDetailsOfWeight

        if "Weight" in configurationDetails:
            # set the name of the configuration details
            self.name = configurationDetails["Weight"]
    
    def reset(self):
        self.resetProperties()
    
    def resetProperties(self):
      
        # property to store the name of the multiplier
        self.name = None 


    def process(self):
        pass
  
    def main(self):
        pass

    def run(self):
        pass




