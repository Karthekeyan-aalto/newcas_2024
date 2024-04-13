"""
Created by Karthekeyan Periasamy
Edited on April 4, 2023
"""

from HWDescription.Entity.EntityHWDescription import EntityHWDescription

class ArchitectureHWDescription(EntityHWDescription):

    def __init__(self):
        sef.connect()
      
    

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,value):
        self._type = value

    @property
    def typeName(self):
        return self._typeName

    @typeName.setter
    def typeName(self,value):
        self._typeName = value

    def connect(self):
        super().connect()
        self.connectProperties()
    

    def connectProperties(self):
        super().connectProperties()

        # property to store the architecture type
        # architecture type 1. RTL for the entity or the hwName 2. behavioural of the hwName that is part of the for test bench of the entity
        self._typeName = None

        # property to store the architecture for behavioural or the rtl 
        # 1. for RTL and 2. Behvioural
        self._type = None

    def configure(self):
        super().configure()
        if self.configurationDetailsOfHW == None:
            return

        configurationDetails = self.configurationDetailsOfHW

        # check whether the property of the configuration detials is available or not
        if "HWArchitectureTypeName" in configurationDetails:
            self.typeName = configurationDetails["HWArchitectureTypeName"]

    
    def main(self):
        self.process()

    
    def process(self):
        pass

    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()
        self._typeName = None
        self._type = None

    def run(self):
        self.main()

