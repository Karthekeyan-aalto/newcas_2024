"""
Created by Karthekeyan Periasamy
Created on Jan 18 14:31 PM
"""

from HWDescription.Architecture.ArchitectureHWDescription import ArchitectureHWDescription
from HWDescription.Process.ProcessHWDescription import ProcessHWDescription
from HWDescription.Signal.SignalHWDescription import SignalHWDescription

from HWDescription.Process.ProcessHWDescription import ProcessHWDescription
from HWDescription.Logic.LogicHWDescription import LogicHWDescription

class MuxHWDescription(LogicHWDescription):
    """
    This class represents the base properties for the Mux HW Description. It will also be the sub class of the operators hw description
    """

    def __init__(self):
        super().__init__()
        # connect the other packages
        self.connect()

        # set the software or python definition of MUX
        self.pythonMux = None  
    
    def main(self):
        self.process()

    
    def configure(self):
        # call the super function
        super().configure()

        # check the configuration details to know whether the python mux is present or not
        if "SWMux" in self.logicDetails:
            self.pythonMux = self.logicDetails["SWMux"]

    def process(self):
        pass

    def connect(self):
        # property to connect the HWArchitecture
        self.connectHWArchitecturePackage()
        # property to connect the HWProcess
        self.connectHWProcessPackage()
        # property to connect the HWSignal
        self.connectHWSignalPackage()
        

    def connectHWArchitecturePackage(self):
        self.hwArchitecture = ArchitectureHWDescription()
    
    def connectHWProcessPackage(self):
        self.hwProcess = ProcessHWDescription()
    
    def connectHWSignalPackage(self):
        self.hwSignal = SignalHWDescription()


    def configure(self):
        # configure the hw archtiecture
        # configure the hw process
        # configure the hw signals
        # configure the hw entities
        # configure the hw ports
        self.configureHWArchitecture()
        self.configureHWProcess()

    def configureHWArchitecture(self):
        # make a dictionary with the information of the hwArchiecture and use the configuration details
        # dictionary to 
        configurationDetails = dict()
        configurationDetails["HWName"] = self.name
        configurationDetails["HWArchitectureTypeName"] = "rtl"
        # set the details to the hwArchitecture
        self.hwArchitecture.configurationDetails = configurationDetails
        # configure the hwArchitecture
        self.hwArchitecture.configure()
       
    
    
    def configureHWProcess(self):
        # make a dictionary with the information of the hwProcess and use the configuration details
        # dictionary
        #configurationDetails = dict()
        #configurationDetails["HWProcess"] = self.name
        #configurationDetails["HWProcessSensitivityList"] = "rtl"
        # set the details to the hwArchitecture
        #self.hwArchitecture.configurationDetails = configurationDetails
        # configure the hwArchitecture
        #self.hwArchitecture.configure()

    def reset(self):
        super().reset()
        self.pythonMux = None
    
    
    def run(self):
        self.main()
