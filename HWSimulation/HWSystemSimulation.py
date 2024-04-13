"""
Created by Karthekeyan Periasamy
Edited on June 16 11:04 AM
"""

class HWSystemSimulation():
    """
    This class represents the base properties for the HW Simulation.
    """

    def __init__(self):
        self.connect()    
    

    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        self.hwDesignLibraries = None
        self.hwInputPorts = None
        self.hwClockPort = None
        self.hwResetPort = None
        self.hwOutputPorts = None
        self.hwFileName = None
        self.hwFileLocation = None
        self.hwName = None
        
    def main(self):
        pass
    
    def configure(self):
        if self.configurationDetails == None:
            return

        configurationDetails = self.configurationDetails

        if "AddWaveToHWIOPorts" in configurationDetails:
            self.addWaveToHWIOPorts = configurationDetails["AddWaveToHWIOPorts"]

        if "HWInputPorts" in configurationDetails:
            self.hwInputPorts = configurationDetails["HWInputPorts"]
        
        if "HWOutputPorts" in configurationDetails:
            self.hwOutputPorts = configurationDetails["HWOutputPorts"]

        if "HWClockPort" in configurationDetails:
            self.hwClockPort = configurationDetails["HWClockPort"]

        if "HWResetPort" in configurationDetails:
            self.hwResetPort = configurationDetails["HWResetPort"]

        if "HWDesignLibraries" in configurationDetails:
            self.hwDesignLibraries = configurationDetails["HWDesignLibraries"]
        
        if "HWName" in configurationDetails:
            self.hwName = configurationDetails["HWName"]



    def process(self):
        pass

    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        self.hwDesignLibraries = None
        self.hwInputPorts = None
        self.hwClockPort = None
        self.hwResetPort = None
        self.hwOutputPorts = None
        self.hwFileName = None
        self.hwFileLocation = None
        self.hwName = None



    def run(self):
        pass
