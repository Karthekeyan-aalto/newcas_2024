"""
Created by Karthekeyan Periasamy
Edited on June 16 12:17 PM
"""
from HWDescription.Generics.GenericHWDescription import GenericHWDescription

class GenericVHDLDescription(GenericHWDescription):

    def __init__(self):
        super().__init__()

    
    def connect(self):
        super().connect()
        self.connectProperties()
        self.connectHWPackages()


    def connectHWPackages(self):
        pass

    def connectProperties(self):
        self.vhdlGenericMap = None
        self.vhdlGeneric = None
        self._pythonHWGeneric = None
        self._vhdlConstantSignals = None

    
    def configure(self):
        super().configure()
    
    @property
    def pythonHWGeneric(self):
        return self._pythonHWGeneric
    
    @pythonHWGeneric.setter
    def pythonHWGeneric(self,value):
        self._pythonHWGeneric = value
        # loop through the generics
        for key, value in self._pythonHWGeneric.items():
            genericConstant = str()
            genericConstant = genericConstant + "CONSTANT" + " " + key + " " + ":" + self.hwGenericTypeName + " " + ":=" + " " + str(value) + ";" + "\n"
            self.vhdlConstantSignals.append(genericConstant)
               
    """
    # Start: vhdlConstantSignals getters
    """

    @property
    def vhdlConstantSignals(self):
        if self._vhdlConstantSignals == None:
            self._vhdlConstantSignals = list()
            
        return self._vhdlConstantSignals
        
    @vhdlConstantSignals.setter
    def vhdlConstantSignals(self, value):
        self._vhdlConstantSignals = value
       
    """
    # End: vhdlConstantSignals setters and getters
    """

    def generateHWVHDLGenerics(self):
        genericsString = "GENERIC" + " " + "("

        # access the length of the dictionary
        lengthOfDictionary = len(self.pythonHWGeneric)
        # local property to know the number of keys
        totalNumberOfKeysIterated = 0
        # loop through the generics
        for key, value in self.pythonHWGeneric.items():
            totalNumberOfKeysIterated = totalNumberOfKeysIterated + 1
            if totalNumberOfKeysIterated == lengthOfDictionary:
                genericsString = genericsString + key + " " + ":" + self.hwGenericTypeName + " " + ":=" + " " + str(value) + ")" + ";" + "\n"
            else:
                genericsString = genericsString + key + " " + ":" + self.hwGenericTypeName + " " + ":=" + " " + str(value) + " " + ";" + " "
                            
        return genericsString
    
    
    def generateHWVHDLGenericsMap(self):
        genericsMapString = "GENERIC MAP" + " " + "("

        # access the length of the dictionary
        lengthOfDictionary = len(self.pythonHWGeneric)
        # local property to know the number of keys
        totalNumberOfKeysIterated = 0
        # loop through the generics
        for key, value in self.pythonHWGeneric.items():
            totalNumberOfKeysIterated = totalNumberOfKeysIterated + 1
            if totalNumberOfKeysIterated == lengthOfDictionary:
                genericsMapString = genericsMapString + key + ")" + "\n"
            else:
                genericsMapString = genericsMapString + key + "," + " "
                            
        return genericsMapString

  
    def process(self):
        super().process()
    
    def perform(self):
        super().perform()
        # generate generic string
        self.vhdlGeneric = self.generateHWVHDLGenerics()
        self.vhdlGenericMap = self.generateHWVHDLGenericsMap()

    def reset(self):
        super().reset()
        self.resetProperties()

    def resetProperties(self):
        self.vhdlGeneric = None
        self.vhdlGenericMap = None
        self._pythonHWGeneric = None
        self._vhdlConstantSignals = None
    
    
    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()

