"""
Created by Karthekeyan Periasamy
Edited on Jan 1 15:29 
"""

from Logic.FF.MB_D_FF.MB_D_FF import MB_D_FF
from Logic.Port.FLPFlopocoPort.FLPFlopocoPort import FLPFlopocoPort
from HWDescription.Logic.FF.MB_D_FF.MB_D_FF_VHDLDescription import MB_D_FF_VHDLDescription

class FLPMB_D_FF(MB_D_FF):

    def __init__(self):
        super().__init__()    
    
    
    @property
    def pythonHWLogicGeneric(self):
        if self._pythonHWLogicGeneric == None:
            self._pythonHWLogicGeneric = dict()
            if self.numberSystem > -1 :
                if self.numberSystem == 0:
                    self._pythonHWLogicGeneric["NumberOfBits"] = self.numberOfBits
                elif self.numberSystem == 1:
                    self._pythonHWLogicGeneric["NumberOfBits+FlopocoBits"] = self.numberOfBits
                elif self.numberSystem == 2:
                    self._pythonHWLogicGeneric["NumberOfBits"] = self.numberOfBits
        return self._pythonHWLogicGeneric

    @pythonHWLogicGeneric.setter
    def pythonHWLogicGeneric(self,value):
        self._pythonHWLogicGeneric = value

    
    def connect(self):
        super().connect()

    def connectHWDescriptionPackage(self):
        # connect the HWDescription Package
        self.hwVHDLDescription = MB_D_FF_VHDLDescription()        
       
    def configure(self):
        super().configure()
        
        # intialise the inputDataPorts array
        self.inputDataPorts = list()
        # intialise the outputPorts array
        self.outputPorts = list()

        
        configurationDetails = self.configurationDetailsOfLogic
        #print("Logic configurationDetails", configurationDetails)
        
        # check the configuration details contains input data ports
        if "InputDataPorts" in configurationDetails:

            # access the ports and set the details of the port
            # the value of the key is expected to be an array
            portDetails = configurationDetails["InputDataPorts"]
            #print("Logic InputDataPorts", portDetails)
            for portDetail in portDetails:
                # access the information about the port or use the configuration details property to configure itself
                newPort = FLPFlopocoPort()
                newPort.configurationDetails = portDetail
                # configure the port
                newPort.configure()
                # process the port
                newPort.process()
                newPort.perform()
                # once the port is configured, add the port to the InputDataPorts array
                self.inputDataPorts.append(newPort)
                self.inputDataPortsInfo[newPort.name] = newPort



        # check the configuration details contains output port details
        if "OutputPorts" in configurationDetails:
            # access the ports and set the details of the port
            # the value of the key is expected to be an array
            portDetails = configurationDetails["OutputPorts"]
            for portDetail in portDetails:
                # access the information about the port or use the configuration details property to configure itself
                newPort = FLPFlopocoPort()
                newPort.configurationDetails = portDetail
                # configure the port
                newPort.configure()
                # process the port
                newPort.process()
                newPort.perform()
                # once the port is configured, add the port to the output array
                self.outputPorts.append(newPort)
                self.outputPortsInfo[newPort.name] = newPort

    
    def perform(self):
        super().perform()
        #print("FLP_MB_D_FF VHDL Output Signals",self.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals)

    def process(self):
        super().process()
        
    
    def main(self):
        self.process()
        self.perform()
    

    def reset(self):
        super().reset()

    def resetHWDescriptionPackage(self):
        self.connectHWDescriptionPackage()

    def run(self):
        self.main()


