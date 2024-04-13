"""
Created by Karthekeyan Periasamy
Edited on Oct 25 14:48 
"""

from Logic.FF.FF import FF
from HWDescription.Logic.FF.SB_D_FF.SB_D_FF_VHDLDescription import SB_D_FF_VHDLDescription

class SB_D_FF(FF):

    def __init__(self):
        super().__init__()
        self.connect()
    
    @property
    def isInputDataPortsModified(self):
        return self._isInputDataPortsModified
    
    @isInputDataPortsModified.setter
    def isInputDataPortsModified(self,value):
        self._isInputDataPortsModified = value

        # update the hwDescription of the FF
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the FF
        if self._isInputDataPortsModified == True:
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
        self.hwVHDLDescription = SB_D_FF_VHDLDescription()        

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
        if self.ffRegisterResetType == 1:
            # its async reset so form the process string with IF THEN statement
            # where the IF statement will have the reset and else statement will have the FF logic
            asyncIFConditionSyntax = "    " + "IF" + " " + self.resetPort.name + " " + "=" + " " + "1" + " " + "THEN" + "\n" \
                                          + "          " + self.outputPorts[0].name + " " + "<=" + "\'0\'" + ";" + "\n" + "          " \

            asyncIFELSEConditionSyntax = "        " + "ELSIF" + " " + "rising_edge" + "(" + self.clockPort.name + ")"+ " " + "and" + "rst" + " " + "=" + " " + "0" + " " + "THEN" + "\n" \
                                          + "          " + self.outputPorts[0].name + " " + "<=" + " " + self.inputDataPorts[0].name + ";" + "\n" \
                                          
            self.pythonHWLogic = asyncIFConditionSyntax + asyncIFELSEConditionSyntax

        elif self.ffRegisterResetType == 2:
            pass
    
    
    def processSWFF(self):
        super().processSWFF()
        # check the width of the shift registers
        if self.width == 1:
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

        # print the final hw description of the Sb d ff
        #print("SB_D_FF VHDL Description",self.hwVHDLDescription.vhdlDescription)
        # print the final hw instance of SB_D_FF
        #print("SB_D_FF VHDL Instance", self.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)

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


