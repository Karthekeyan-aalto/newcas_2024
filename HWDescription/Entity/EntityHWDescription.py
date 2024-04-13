"""
Created by Karthekeyan Periasamy
Edited on July 7, 08:54 2023
"""

from HWDescription.HWDescription import HWDescription

class EntityHWDescription(HWDescription):

    def __init__(self):
        sef.connect()

    
    def connect(self):
        super().connect()
        self.connectProperties()
    
    """
    # Start: pythonHWOutputPorts getters
    """

    @property
    def pythonHWOutputPorts(self):
        if self._pythonHWOutputPorts == None:
            self._pythonHWOutputPorts = list()
            
        return self._pythonHWOutputPorts
        
    @pythonHWOutputPorts.setter
    def pythonHWOutputPorts(self, value):
        self._pythonHWOutputPorts = value
       
    """
    # End: pythonHWOutputPorts setters and getters
    """
    
    """
    # Start: pythonHWInputPorts getters
    """

    @property
    def pythonHWInputPorts(self):
        if self._pythonHWInputPorts == None:
            self._pythonHWInputPorts = list()
            
        return self._pythonHWInputPorts
        
    @pythonHWInputPorts.setter
    def pythonHWInputPorts(self, value):
        self._pythonHWInputPorts = value
       
    """
    # End: pythonHWInputPorts setters and getters
    """

    def connectProperties(self):
        super().connectProperties()
        self._pythonHWOutputPorts = None
        self._pythonHWInputPorts = None
        self.pythonHWClockPort = None
        self.pythonHWResetPort = None
        self.pythonHWEnablePort = None

        # property to store the architecture type
        # architecture type 1. RTL for the entity or the hwName 2. behavioural of the hwName that is part of the for test bench of the entity
        self.typeName = None


    def configure(self):
        #print("Hi, again")
        super().configure()
        if self.configurationDetailsOfHW == None:
            return

        configurationDetails = self.configurationDetailsOfHW
        #print("Configuration Details of HW", configurationDetails)
        
        if "InputDataPorts" in configurationDetails:
            self.pythonHWInputPorts = configurationDetails["InputDataPorts"]

        if "OutputDataPorts" in configurationDetails:
            self.pythonHWOutputPorts = configurationDetails["OutputDataPorts"]
            
            
        if "InputClockPort" in configurationDetails:
            self.pythonHWClockPort = configurationDetails["InputClockPort"]
        
        if "InputResetPort" in configurationDetails:
            self.pythonHWResetPort = configurationDetails["InputResetPort"]
        
        if "InputEnablePort" in configurationDetails:
            self.pythonHWEnablePort = configurationDetails["InputEnablePort"]
            #print("Python HW Enable Port", self.pythonHWEnablePort)
        else:
            #print("Python HW Enable Port", self.pythonHWEnablePort)
            pass

        # check whether the property of the configuration detials is available or not
        if "HWEntityTypeName" in configurationDetails:
            self.typeName = self.configurationDetails["HWEntityTypeName"]

    
    def main(self):
        self.process()

    def perform(self):
        pass

    def process(self):
        pass

    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()
        self._pythonHWOutputPorts = None
        self._pythonHWInputPorts = None
        self.pythonHWClockPort = None
        self.pythonHWResetPort = None
        self.pythonHWEnablePort = None

    def run(self):
        self.main()

