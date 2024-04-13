"""
Created by Karthekeyan Peirasamy
Edited on July 10 12:48
"""
from Operators.Adders.FLPAdder.FLPAdder import FLPAdder
from Operators.Port.FLPFlopocoPort.FLPFlopocoPort import FLPFlopocoPort

class FLPMMACUnitAdder(FLPAdder):

    def __init__(self):
        super().__init__()


    @property
    def isInputDataPortsModified(self):
        return self._isInputDataPortsModified
    
    @isInputDataPortsModified.setter
    def isInputDataPortsModified(self,value):
        self._isInputDataPortsModified = value
        #print("Input Data Ports Modified", self._isInputDataPortsModified)
        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
        if self._isInputDataPortsModified == True:
            # reset the HWDescription package
            self.resetHWDescriptionPackage()            
            # process the HWOperatorsConfiguration details
            self.processHWOperatorConfigurationDetails()
            self.perform()
            # set the input data port modified to false
            self._isInputDataPortsModified = False
    
    @property
    def isOutputPortsModified(self):
        return self._isOutputPortsModified
    
    @isOutputPortsModified.setter
    def isOutputPortsModified(self,value):
        self._isOutputPortsModified = value

        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
        
        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
        if self._isOutputPortsModified == True:
            # reset the HWDescription package
            self.resetHWDescriptionPackage()
            # process the HWOperatorsConfiguration details
            self.processHWOperatorConfigurationDetails()
            self.perform()
            # set the output port modified to false
            self._isOutputPortsModified = False

   
    @property
    def augend(self):
        return self._augend

    @augend.setter
    def augend(self,value):
        if self.swAdder.augend == None:
            self.swAdder.augend = value
        
        if self.swAdder.augendDriver.isDriverAPort == True:
            self._augend = value
            # make a new port with configuration details
            portDetail = {"Name":self._augend,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Input","ConstantSignalValue":0}
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
            # store the port info 
            self.inputDataPortsInfo[newPort.name] = newPort
        elif self.swAdder.augendDriver.isDriverAnArithmeticNode == True:
            self._augend = value
            # make a new port with configuration details
            portDetail = {"Name":self._augend,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Input","ConstantSignalValue":0}
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
            # store the port info 
            self.inputDataPortsInfo[newPort.name] = newPort

        
    @property
    def addend(self):
        return self._addend

    @addend.setter
    def addend(self,value):
        if self.swAdder.addend == None:
            self.swAdder.addend = value
            
        if self.swAdder.addendDriver.isDriverAPort == True:
            self._addend = value
            # make a new port with configuration details
            portDetail = {"Name":self._addend,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Input","ConstantSignalValue":0}
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
            # store the port info 
            self.inputDataPortsInfo[newPort.name] = newPort
        elif self.swAdder.addendDriver.isDriverAnArithmeticNode == True:
            self._addend = value
            #print("Addend", self._addend)
            # make a new port with configuration details
            portDetail = {"Name":self._addend,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Input","ConstantSignalValue":0}
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
            # store the port info 
            self.inputDataPortsInfo[newPort.name] = newPort
            #print(self.inputDataPortsInfo)
            
    
    @property
    def summation(self):
        if self._summation == None:
            if (self.swAdder.augendDriver and self.swAdder.addendDriver) != None:
                outputPort = FLPFlopocoPort()
                portDetail = {"Name":(self.name + str(self.number) + "_" + "Output" + "_" + str(self.arithmeticNodeNumber)),"NumberOfBits":self.flpFlopocoNumberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Output", "ConstantSignalValue":0}                
                # generate the output port using the configuration details
                outputPort.configurationDetails = portDetail
                # configure the port
                outputPort.configure()
                # process the port
                outputPort.process()
                outputPort.perform()
                # once the port is configured, add the port to the outputdata array
                self.outputPorts.append(outputPort)
                self.outputPortsInfo[outputPort.name] = outputPort
                # set the product expression with the equation
                self._summation = outputPort.name
            else:
                self._summation = None

        return self._summation

    @summation.setter
    def summation(self,value):
        self._summation = value

        
    
    def connect(self):
        super().connect()

    
    def main(self):
        self.process()
        self.perform()
    

    def process(self):
        super().process()

    def perform(self):
        super().perform()
        #print("FLPAdder VHDLInstance", self.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
        # print the D_FF and other things
    
    
    def configure(self):
        super().configure()
    
    def reset(self):
        super().reset()



