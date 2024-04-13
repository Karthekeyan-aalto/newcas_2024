"""
Created by Karthekeyan Periasamy
Edited on Oct 25 14:48 
"""

from Logic.FF.FF import FF
from HWDescription.Logic.FF.MB_D_FF.MB_D_FF_VHDLDescription import MB_D_FF_VHDLDescription

class MB_D_FF(FF):

    def __init__(self):
        super().__init__()
        self.connect()
    
    @property
    def isInputDataPortsModified(self):
        return self._isInputDataPortsModified
    
    @isInputDataPortsModified.setter
    def isInputDataPortsModified(self,value):
        self._isInputDataPortsModified = value
        #print("Input Ports MB_D_FF Modified", value)
        # update the hwDescription of the FF
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the FF
        if self._isInputDataPortsModified == True:
            #print("MB_D_FF _isInputDataPortsModified")
            # reset the HWDescription package
            self.resetHWDescriptionPackage()
            # process the HWOperatorsConfiguration details
            self.process()
            self.perform()
    
    @property
    def isOutputPortsModified(self):
        return self._isOutputPortsModified
    
    @isOutputPortsModified.setter
    def isOutputPortsModified(self,value):
        self._isOutputPortsModified = value

        # update the hwDescription of the FF
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
        
        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
        if self._isOutputPortsModified == True:
            # reset the HWDescription package
            self.resetHWDescriptionPackage()
            # process the HWOperatorsConfiguration details
            self.process()
            self.perform()

    
    @property
    def pythonHWLogicGeneric(self):
        if self._pythonHWLogicGeneric == None:
            self._pythonHWLogicGeneric = dict()
            if self.numberSystem > -1 :
                if self.numberSystem == 0:
                    self._pythonHWLogicGeneric["NumberOfBits"] = self.numberOfBits
                elif self.numberSystem == 1:
                    self._pythonHWLogicGeneric["NumberOfBits"] = self.numberOfBits
                    #self._pythonHWLogicGeneric["MantissaBits"] = self.mantissaBits
                    #self._pythonHWLogicGeneric["ExponentBits"] = self.exponentBits
                elif self.numberSystem == 2:
                    self._pythonHWLogicGeneric["NumberOfBits"] = self.numberOfBits
                    #self._pythonHWLogicGeneric["EsBits"] = self.esBits
        return self._pythonHWLogicGeneric

    @pythonHWLogicGeneric.setter
    def pythonHWLogicGeneric(self,value):
        self._pythonHWLogicGeneric = value
    
    
    def connect(self):
        super().connect()
        # connect the HWDescriptionPackage
        self.connectHWDescriptionPackage()

        # connect the HWSimulationPackage
        self.connectHWSimulationPackage()

        # connect the properties
        self.connectProperties()


    def connectHWDescriptionPackage(self):
        # connect the HWDescription Package
        self.hwVHDLDescription = MB_D_FF_VHDLDescription()        

    def connectProperties(self):
        super().connectProperties()

    
    def connectHWSimulationPackage(self):
        # connect the HWSimulation Package
        #self.hwSimulation = MBRightSHRVHDLSimulation()
        pass


    def processHWFF(self):
        # print the output ports
        #print("The output ports of the MBDFF", self.outputPorts)
        # check the reset type of the ff 
        if self.ffResetType == 1:
            # its async reset so form the process string with IF THEN statement
            # where the IF statement will have the reset and else statement will have the FF logic
            asyncIFConditionSyntax = "    " + "IF" + " " + self.resetPort.name + " " + "=" + " " + "1" + " " + "THEN" + "\n" \
                                          + "          " + self.outputPorts[0].name + " " + "<=" + "(" \
                                          + "OTHERS" + "=>" + "\'0\'"  + ")" + ";" + "\n" + "          " \

            asyncIFELSEConditionSyntax = "        " + "ELSIF" + " " + "rising_edge" + "(" + self.clockPort.name + ")"+ " " +"and" + "rst"+ "=" + " " + "0" + " " + "THEN" + "\n" \
                                          + "          " + self.outputPorts[0].name + " " + "<=" + " " + self.inputDataPorts[0].name + ";" + "\n" \
                                          
            self.pythonHWLogic = asyncIFConditionSyntax + asyncIFELSEConditionSyntax

        elif self.ffResetType == 2:
            pass
    
    
    def processSWFF(self):
        super().processSWFF()
        # check the width of the shift registers
        if self.width > 1:
            pass
    
    def configure(self):
        super().configure()
    
    def perform(self):
        # perform sw FF process
        self.performSWFF()
        # perform hw generation
        self.performHWGeneration()
    
    def performSWFF(self):
        pass

    def process(self):
        super().process()
        # process HW ShiftRegister
        self.processHWFF()
        
    def performHWGeneration(self):
        self.hwVHDLDescription.configurationDetailsOfHW = self.configurationDetailsOfHWLogic
        # configure the logic
        self.hwVHDLDescription.configure()
        # process the logic
        self.hwVHDLDescription.run()

        # print the final hw description of the mb d ff
        #print("MB_D_FF VHDL Description",self.hwVHDLDescription.vhdlDescription)
        # print the final hw instance of MB_D_FF
        #print("MB_D_FF VHDL Instance", self.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
        #print("MB_D_FF VHDL Output Signals",self.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals)

    def main(self):
        self.process()
        self.perform()
    

    def reset(self):
        super().resetProperties()
        self.resetHWDescriptionPackage()


    def resetHWDescriptionPackage(self):
        self.connectHWDescriptionPackage()

    def run(self):
        self.main()


