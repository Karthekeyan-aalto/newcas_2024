"""
Created by Karthekeyan Peirasamy
Edited on July 10 12:48
"""
from Operators.Multipliers.FLPMultiplier.FLPMultiplier import FLPMultiplier
from Operators.Port.FLPFlopocoPort.FLPFlopocoPort import FLPFlopocoPort

class FLPMMACUnitMultiplier(FLPMultiplier):

    def __init__(self):
        super().__init__()

    def connect(self):
        super().connect()

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
            # this is for mmacunit
            if self.swMultiplier.isInputDataModified == True:
                self.swMultiplier.isInputDataModified = False
                self.processHWGeneration()

            # process the HWOperatorsConfiguration details
            self.processHWOperatorConfigurationDetails()
            self.perform()
            # set the input data port modified to false
            self._isInputDataPortsModified = False
    
        
    
    
        
    @property
    def multiplicand(self):
        return self._multiplicand

    @multiplicand.setter
    def multiplicand(self,value):
        if self.swMultiplier.multiplicand == None:
            self.swMultiplier.multiplicand = value
        else:
            if self.swMultiplier.isInputDataModified == True:
                # reset the input registers
                self.inputRegisters = dict()
                # reset the input converters
                self.inputConverters = dict()
                self.swMultiplier.isInputDataModified = False
                self.swMultiplier.input1 = value
                self.swMultiplier.isInputDataModified = True
                self.swMultiplier.multiplicand = value
        
        if self.swMultiplier.multiplicandDriver.isDriverAPort == True:
            self._multiplicand = value
            # make a new port with configuration details
            portDetail = {"Name":self._multiplicand,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Input", "ConstantSignalValue":0}
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
        elif self.swMultiplier.multiplicandDriver.isDriverAWeight == True:
            #print("Multiplicand", value)
            #print("Multiplicand Input is a weight with", value)
            if value == self.swMultiplier.weight.name:
                #print("Multiplicand is a float", value)
                self._multiplicand = self.name + str(self.number) + "Weight"
            else:
                #print("Multiplicand is a string", value)
                self._multiplicand = value

            #self._multiplicand = self.name + str(self.number) + "Weight"
            # make a new port with configuration details
            portDetail = {"Name":self._multiplicand,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Weight","SignalData":self.swMultiplier.weight.name}
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
        elif self.swMultiplier.multiplicandDriver.isDriverAnArithmeticNode == True:
            self._multiplicand = value
            # make a new port with configuration details
            portDetail = {"Name":self._multiplicand,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Input","ConstantSignalValue":0}
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
            

        
    @property
    def multiplier(self):
        return self._multiplier

    @multiplier.setter
    def multiplier(self,value):
        if self.swMultiplier.multiplier == None:
            self.swMultiplier.multiplier = value
        else:
            if self.swMultiplier.isInputDataModified == True:
                # reset the input registers
                self.inputRegisters = dict()
                # reset the input converters
                self.inputConverters = dict()
                self.swMultiplier.isInputDataModified = False
                self.swMultiplier.input2 = value
                self.swMultiplier.isInputDataModified = True
                self.swMultiplier.multiplier = value
        
        if self.swMultiplier.multiplierDriver.isDriverAPort == True:
            # once the port is configured, add the port to the InputDataPorts array
            self._multiplier = value
            # make a new port with configuration details
            portDetail = {"Name":self._multiplier,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Input","ConstantSignalValue":0}
            # access the information about the port or use the configuration details property to configure itself
            newPort = FLPFlopocoPort()
            newPort.configurationDetails = portDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            newPort.perform()
            self.inputDataPorts.append(newPort)
            self.inputDataPortsInfo[newPort.name] = newPort
        elif self.swMultiplier.multiplierDriver.isDriverAWeight == True:
            #print("Multiplier Input is a weight with value", value)
            # the below check is made to support updation of input ports while generating vhdl
            if value == self.swMultiplier.weight.name:
                #print("Multiplier is a float", value)
                self._multiplier = self.name + str(self.number) + "Weight"
            else:
                #print("Multiplier is a string", value)
                self._multiplier = value

            #self._multiplier = self.name + str(self.number) + "Weight"
            # make a new port with configuration details
            portDetail = {"Name":self._multiplier,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Weight","SignalData":self.swMultiplier.weight.name}
            # access the information about the port or use the configuration details property to configure itself
            newPort = FLPFlopocoPort()
            newPort.configurationDetails = portDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            newPort.perform()
            self.inputDataPorts.append(newPort)
            self.inputDataPortsInfo[newPort.name] = newPort
        elif self.swMultiplier.multiplierDriver.isDriverAnArithmeticNode == True:
            self._multiplier = value
            # make a new port with configuration details
            portDetail = {"Name":self._multiplier,"NumberOfBits":self.numberOfBits,"MantissaBits": self.mantissaBits,"ExponentBits":self.exponentBits,"FlopocoBits":self.flopocoBits,"PortType":"Input","ConstantSignalValue":0}
            # access the information about the port or use the configuration details property to configure itself
            newPort = FLPFlopocoPort()
            newPort.configurationDetails = portDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            newPort.perform()
            self.inputDataPorts.append(newPort)
            self.inputDataPortsInfo[newPort.name] = newPort
    
    @property
    def product(self):
        if self._product == None:
            if (self.swMultiplier.multiplicandDriver and self.swMultiplier.multiplierDriver) != None:
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
                # form the outputPorts Info
                self.outputPortsInfo[outputPort.name] = outputPort
                # set the product expression with the equation
                self._product = outputPort.name
            else:
                self._product = None

        return self._product

    @product.setter
    def product(self,value):
        self._product = value
    
       
    def configure(self):
        super().configure()            
                    
    def reset(self):
        super().reset()
    
    
    def main(self):
        self.process()
        self.perform()
    
    def process(self):
        super().process()
     
    def perform(self):
        super().perform()
        #print("FLPMultiplier VHDLInstance", self.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)

        #for inputPort in self.inputDataPorts:
            #print("FLPMultiplier inputPort VHDL Signal", inputPort.hwDescription.vhdlPortSignal)

    def run(self):
        self.main()
    


        

