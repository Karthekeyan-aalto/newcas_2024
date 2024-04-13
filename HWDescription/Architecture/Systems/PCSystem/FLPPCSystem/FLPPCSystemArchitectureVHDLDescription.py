"""
Created by Karthekeyan Periasamy
Edited on Jan 14, 2023, 15:38
"""

from HWDescription.Architecture.Systems.PCSystem.PCSystemArchitectureVHDLDescription import PCSystemArchitectureVHDLDescription
from HWDescription.Process.Systems.PCSystem.FLPPCSystem.FLPPCSystemProcessVHDLDescription import FLPPCSystemProcessVHDLDescription


class FLPPCSystemArchitectureVHDLDescription(PCSystemArchitectureVHDLDescription):

    def __init__(self):
        self.connect()
    
   
    def connect(self):
        super().connect()    

    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        # connect the hw process packages
        #self.vhdlProcessDescription = FLPPCSystemProcessVHDLDescription()


    def connectProperties(self):
        super().connectProperties()
    
    def reset(self):
        super().reset()
           
        
    def resetProperties(self):
        super().resetProperties()        


    def configure(self):
        super().configure()
    
    
    def generateHWVHDLEntityArchitectureDefinition(self):
        entityArchitectureDefinition = self.hwVHDLEntityArchitectureDefinitionStartSyntax() + "\n" + "    "

        # access the vhdlOutputPortSignals
        # append the entityArchitectureDefinition with output port syntax
        for vhdlOutputPortSignal in self.vhdlOutputSignals:
            #if isinstance(vhdlOutputPortSignal, list):
                #print("FLPPCSystem Architecture Generate: VHDL Output Port Signal", vhdlOutputPortSignal)
            entityArchitectureDefinition = entityArchitectureDefinition + "    " + vhdlOutputPortSignal + "    "
        
        entityArchitectureDefinition = entityArchitectureDefinition + "    "
        for vhdlWeightSignal in self.vhdlWeightSignals:
            entityArchitectureDefinition = entityArchitectureDefinition + vhdlWeightSignal + "        "

        entityArchitectureDefinition = entityArchitectureDefinition + "\n"

        # begin the lutVHDLEntity architecture
        entityArchitectureDefinition = (entityArchitectureDefinition + "BEGIN" + "\n" \
                + "    ")

        if self.pythonHWClockPort != None:

            # attach the process start and end description of the HW
            entityArchitectureDefinition = entityArchitectureDefinition + self.vhdlProcessDescription.vhdlEntityProcessDefinition + "\n"
        
        # update the python HW with the instances of the multiplier and adder
        for arithmeticNode in self.arithmeticNodes:
            if arithmeticNode.swOperator.isOperatorEnabled == False:
                #print("Arithmetic Node Instance", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                continue
            #print("Arithmetic Node Instance", arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
            self.pythonHW = self.pythonHW + arithmeticNode.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
            

        # updating the python hw wth the instances of the multiplier and adder is not enough
        # as addition of the pipeline stages are important when we have automatic pipeline
        
        # attach the python HW to the architecture
        entityArchitectureDefinition = entityArchitectureDefinition + self.pythonHW
        
        topArithmeticNode = self.arithmeticNodes[len(self.arithmeticNodes)-1]
        cascadedMBDFFRegister = topArithmeticNode.outputRegisters[arithmeticNode.swOperator.summation]["CascadedRegisters"]
        finalOutput = cascadedMBDFFRegister.cascadedRegisters[len(cascadedMBDFFRegister.cascadedRegisters)-1].outputPorts[0].name
        entityArchitectureDefinition = entityArchitectureDefinition + "    " + self.pythonHWOutputPorts[0].name + " " + "<= " + finalOutput + ";" + "\n \n"
        
        entityArchitectureDefinition = entityArchitectureDefinition + self.hwVHDLEntityArchitectureDefinitionEndSyntax()
        self.vhdlEntityArchitectureDefinition = entityArchitectureDefinition
        #print("PCSystemTree Entity Architecture Definition",self.vhdlEntityArchitectureDefinition)

    def process(self):
        super().process()

      
    def perform(self):
        super().perform()

    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()

