"""
Created by Karthekeyan Periasamy
Edited on April 25 15:49 
"""

from Operators.ShiftRegisters.ShiftRegister import ShiftRegister
from HWSimulation.Operators.ShiftRegisters.SBRightSHR.SBRightSHRHWSimulation import SBRightSHRHWSimulation
from HWDescription.Operators.ShiftRegisters.SBRightSHR.SBRightSHRVHDLDescription import SBRightSHRVHDLDescription


class SBRightSHR(ShiftRegister):

    def __init__(self):
        super().__init__()
        self.connect()

    
    
    
    @property
    def isInputDataPortsModified(self):
        return self._isInputDataPortsModified
    
    @isInputDataPortsModified.setter
    def isInputDataPortsModified(self,value):
        self._isInputDataPortsModified = value

        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
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
        self.hwVHDLDescription = MBRightSHRVHDLDescription()        

    def connectProperties(self):
        super().connectProperties()

    
    def connectHWSimulationPackage(self):
        # connect the HWSimulation Package
        #self.hwSimulation = MBRightSHRVHDLSimulation()
        pass


    def processHWShiftRegister(self):
        # print the output ports
        #print("The output ports of the SBRightSHR", self.outputPorts)
        # check the reset type of the shift register
        if self.shiftRegisterResetType == 1:
            # its async reset so form the process string with IF THEN statement
            # where the IF statement will have the reset and else statement will have the shifting operation based on the direction
            # for now, the shift direction of right is only supported for both HW and SW
            asyncIFConditionSyntax = "    " + "IF" + " " + self.resetPort.name + " " + "=" + " " + "1" + " " + "THEN" + "\n" \
                                          + "          " + self.outputPorts[0].name + " " + "<=" + "(" + "OTHERS" + "=>" \
                                          + "(" "\'0\'" + ")" + ")" + ";" + "\n" + "          " \
                                          + "          " + self.outputPorts[0].name + " " + "<=" + "\'0\'" + ";" + "\n" \

            asyncIFELSEConditionSyntax = "        " + "ELSIF" + " " + "rising_edge" + "(" + self.clockPort.name + ")"+ " " + "=" + " " + "1" + " " + "THEN" + "\n" \
                                          + "          " + self.outputPorts[0].name + " " + "<=" + "(" + "OTHERS" + "=>" + "(" \
                                          + "OTHERS" + "=>" + "\'0\'" + ")" + ")" + ";" + "\n" \
                                          + "          " + self.outputPorts[0].name + " " + "<=" +   "(" + "OTHERS" + "=>" + "\'0\'" + ")" + ";"\

            self.pythonHWOperator = asyncIFConditionSyntax + asyncIFELSEConditionSyntax

        elif self.shiftRegisterResetType == 2:
            pass
    
    
    def processSWShiftRegister(self):
        super().processSWShiftRegister()
        # check the width of the shift registers
        if self.width > 1:
            # it is a multi bit shift register register
            # check the direction
            if self.shiftDirection == 1:
                pass
            elif self.shiftDirection == 2:
                pass

        for index, value in enumerate(self.pythonRegister):
            pass

    
    
    def configure(self):
        super().configure()
    
    def perform(self):
        # perform sw shifting process
        self.performSWShifting()
        # perform hw generation
        self.performHWGeneration()
    
    def performSWShifting(self):
        pass

    def process(self):
        super().process()
        # process HW ShiftRegister
        self.processHWShiftRegister()
        
    def performHWGeneration(self):
        self.hwVHDLDescription.configurationDetailsOfHW = self.configurationDetailsOfHWOperator
        # configure the operator
        self.hwVHDLDescription.configure()
        # process the operator
        self.hwVHDLDescription.run()

        # print the final hw description of the mbright shr
        #print("SBRightSHR VHDL Description",self.hwVHDLDescription.vhdlDescription)
        # print the final hw instance of mbright Shr
        #print("SBRightSHR VHDL Instance", self.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)

    def main(self):
        self.process()
        self.perform()
    

    def reset(self):
        super().resetProperties()
        self.resetHWDescriptionPackage()


    def resetHWDescriptionPackage(self):
        # reset the hwOperatorGeneric property
        self._pythonHWOperatorGeneric = None
        self.connectHWDescriptionPackage()

    def run(self):
        self.main()







