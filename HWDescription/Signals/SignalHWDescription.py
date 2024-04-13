"""
Created by Karthekeyan Periasamy
Edited on Jan 24 14:22
"""


class SignalHWDescription():

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
            self.isSignalABus = True
        else:
            self.isSignalABus = False

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
        # property to set the name of the signal
        self._name = None
        # property to know whether a signal is a bus or not
        self.isSignalABus = False
        # property to store the number of bits of the Signal
        self._numberOfBits = None
        # property to store the configuration details, which will be used to build a signal
        self.configurationDetailsOfHWSignal = None
        # property to store the signal value or the constant signal value
        self.signalData = None
        # proprety to store the constant signal value
        self.constantSignalValue = None
        # property to store the mantissaBits
        self.manitssaBits = None
        # property to store the es bits
        self.esBits = None
        # property to store the exponent bits
        self.exponentBits = None
        # property to store the flopocoBits
        self.flopocoBits = None

    def configure(self):
        # check if the configuration details are there or not
        if self.configurationDetailsOfHWSignal == None:
            return
        # store the configuraiton details to a local variable
        configurationDetails = self.configurationDetailsOfHWSignal
        #print("Signal Configuration Details", configurationDetails)
        
        # check if the name key is available in the configuration details
        if "Name" in configurationDetails:
            self.name = configurationDetails["Name"]
            
        # check if the name key is available in the configuration details
        if "NumberOfBits" in configurationDetails:
            self.numberOfBits = configurationDetails["NumberOfBits"]
        
        if "MantissaBits" in configurationDetails:
            self.mantissaBits = configurationDetails["MantissaBits"]
        
        if "ExponentBits" in configurationDetails:
            self.exponentBits = configurationDetails["ExponentBits"]

        if "FlopocoBits" in configurationDetails:
            self.flopocoBits = configurationDetails["FlopocoBits"]

        # check if the signal value is there or not
        if "ConstantSignalValue" in configurationDetails:
            self.constantSignalValue = configurationDetails["ConstantSignalValue"]
        
        # check if the signal value is there or not
        if "SignalData" in configurationDetails:
            self.signalData = configurationDetails["SignalData"]



    def resetProperties(self):
        # property to set the name of the signal
        self._name = None
        # property to know whether a signal is a bus or not
        self.isSignalABus = False
        # property to store the number of bits of the Signal
        self._numberOfBits = None
        # property to store the configuration details, which will be used to build a signal
        self.configurationDetailsOfHWSignal = None
        # property to store the signal value or the constant signal value
        self.signalData = None
        # proprety to store the constant signal value
        self.constantSignalValue = None
        # property to store the mantissaBits
        self.manitssaBits = None
        # property to store the es bits
        self.esBits = None
        # property to store the exponent bits
        self.exponentBits = None
        # property to store the flopocoBits
        self.flopocoBits = None


    def reset(self):
        self.resetProperties()
    
    def process(self):
        pass
    def perform(self):
        pass
    def main(self):
        self.process()
        self.perform()
