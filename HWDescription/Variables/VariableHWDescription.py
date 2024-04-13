"""
Created by Karthekeyan Periasamy
Edited on Sep 20 14:43
"""

class VariableHWDescription():

    def __init__(self):
        self.connect()

    @property 
    def numberOfBits(self):
        return self._numberOfBits 

    @numberOfBits.setter
    def numberOfBits(self,value):
        self._numberOfBits = value
        # check if the number of bits if its greater than zero or not
        if self._numberOfBits > 1:
            # set the signal is a bus to true
            self.isVariableABus = True
        else:
            self.isVariableABus = False
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        # check if the signal value is none or not
        self._name = value
    
    
    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        #property to store the number of bits
        self._numberOfBits = None
        # property to store the name of the variable
        self.name = None
        # propertu to know whether a variable is a bus or not
        self.isVariableABus = False
        # proeprty to store the constant value of the variable
        self.constantVariableValue = None
    
    
    def configure(self):
        # check if the configuration details are there or not
        if self.configurationDetailsOfHWVariable == None:
            return
        # store the configuraiton details to a local variable
        configurationDetails = self.configurationDetailsOfHWVariable
        
        # check if the name key is available in the configuration details
        if "Name" in configurationDetails:
            self.name = configurationDetails["Name"]
            
        # check if the name key is available in the configuration details
        if "NumberOfBits" in configurationDetails:
            if configurationDetails["NumberOfBits"] != None:
                self.numberOfBits = configurationDetails["NumberOfBits"]
        
        # check if there is a key named constant variable value in the configuration details
        if "ConstantVariableValue" in configurationDetails:
            self.constantVariableValue = configurationDetails["ConstantVariableValue"]

    
    
    def perform(self):
        pass

    def process(self):
        pass

    def main(self):
        self.process()
        self.perform()

    def reset(self):
        self.resetProperties()


    def resetProperties(self):
        #property to store the number of bits
        self._numberOfBits = None
        # property to store the name of the variable
        self.name = None
        # propertu to know whether a variable is a bus or not
        self.isVariableABus = False
        # proeprty to store the constant value of the variable
        self.constantVariableValue = None

    def run(self):
        self.main()

