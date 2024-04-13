"""
Created by Karthekeyan Periasamy
Edited on Jan 20 16:01 
"""

from Operators.ShiftRegisters.MBRightSHR.MBRightSHR import MBRightSHR
from Operators.Port.FLPFlopocoPort.FLPFlopocoPort import FLPFlopocoPort
from HWDescription.Operators.ShiftRegisters.MBRightSHR.MBRightSHRVHDLDescription import MBRightSHRVHDLDescription


class FLPMBRightSHR(MBRightSHR):

    def __init__(self):
        super().__init__()
        
    @property
    def pythonHWOperatorGeneric(self):
        if self._pythonHWOperatorGeneric == None:
            self._pythonHWOperatorGeneric = dict()
            if self.numberSystem > -1 :
                if self.numberSystem == 0:
                    self._pythonHWOperatorGeneric["NumberOfBits"] = self.numberOfBits
                elif self.numberSystem == 1:
                    self._pythonHWOperatorGeneric[str(self.depth)] = self.depth
                    self._pythonHWOperatorGeneric["NumberOfBits+FlopocoBits"] = self.numberOfBits
                elif self.numberSystem == 2:
                    self._pythonHWOperatorGeneric[str(self.depth)] = self.depth
                    self._pythonHWOperatorGeneric["NumberOfBits"] = self.numberOfBits
        return self._pythonHWOperatorGeneric

    @pythonHWOperatorGeneric.setter
    def pythonHWOperatorGeneric(self,value):
        self._pythonHWOperatorGeneric = value

    
    def connect(self):
        super().connect()
        

    def connectHWDescriptionPackage(self):
        # connect the HWDescription Package
        self.hwVHDLDescription = MBRightSHRVHDLDescription()        

    def connectProperties(self):
        super().connectProperties() 
    
    def configure(self):
        super().configure()
        
        # intialise the inputDataPorts array
        self.inputDataPorts = list()
        # intialise the outputPorts array
        self.outputPorts = list()

        
        configurationDetails = self.configurationDetailsOfOperator
        #print("Operator configurationDetails", configurationDetails)
        
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
        #print("FLPMBRightSHR VHDL OutputSignals", self.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals)
 
    def process(self):
        super().process()
        

    def main(self):
        self.process()
        self.perform()
    

    def reset(self):
        super().resetProperties()

    def resetHWDescriptionPackage(self):
        super().resetHWDescriptionPackage()

    def run(self):
        self.main()


