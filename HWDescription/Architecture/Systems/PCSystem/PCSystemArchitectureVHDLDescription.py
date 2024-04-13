"""
Created by Karthekeyan Periasamy
Edited on Jan 11, 2023, 15:38
"""

from HWDescription.Architecture.ArchitectureVHDLDescription import ArchitectureVHDLDescription
from HWDescription.Process.Systems.PCSystem.PCSystemProcessVHDLDescription import PCSystemProcessVHDLDescription
from Operators.Multipliers.Multiplier import Multiplier

class PCSystemArchitectureVHDLDescription(ArchitectureVHDLDescription):

    def __init__(self):
        self.connect()
      
    """
    # Start: vhdlWeightSignals getters
    """

    @property
    def vhdlWeightSignals(self):
        if self._vhdlWeightSignals == None:
            self._vhdlWeightSignals = list()
            
        return self._vhdlWeightSignals
        
    @vhdlWeightSignals.setter
    def vhdlWeightSignals(self, value):
        self._vhdlWeightSignals = value
       
    """
    # End: vhdlWeightSignals setters and getters
    """
    
    """
    # Start: pythonHWOutputPorts getter
    """

    @property
    def pythonHWOutputPorts(self):
        if self._pythonHWOutputPorts == None:
            self._pythonHWOutputPorts = list()
            
        return self._pythonHWOutputPorts
        
    @pythonHWOutputPorts.setter
    def pythonHWOutputPorts(self, value):
        self._pythonHWOutputPorts = value
        # this property is overridden to add the MMACUnit OutputSignal being added to the VHDL output signals
       
       
    """
    # End: pythonHWOutputPorts setter
    """

    
    """
    # Start: arithmeticNodes getters
    """

    @property
    def arithmeticNodes(self):
        return self._arithmeticNodes
        
    @arithmeticNodes.setter
    def arithmeticNodes(self, value):
        self._arithmeticNodes = value
        # print the length of the arithmetic nodes
        #print("The length of arithmetic nodes", len(self.arithmeticNodes))
        for arithmeticNode in self._arithmeticNodes:
            if isinstance(arithmeticNode, Multiplier):
                if (len(arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlWeightSignals) > 0):
                    self.vhdlWeightSignals = self.vhdlWeightSignals + arithmeticNode.hwDescription.vhdlEntityArchitectureDescription.vhdlWeightSignals
                            
        # print the weight signals of the arithmetic nodes
        #print("The length of weight signals of the arithmetic nodes", len(self.vhdlWeightSignals))
       
    """
    # End: arithmeticNodes setters and getters
    """
    
    """
    # Start: extraVHDLOutputSignals getters
    """

    @property
    def extraVHDLOutputSignals(self):
        return self._extraVHDLOutputSignals
        
    @extraVHDLOutputSignals.setter
    def extraVHDLOutputSignals(self, value):
        self._extraVHDLOutputSignals = value

        # update the extraVHDLOutputSignals
        self.appendExtraVHDLOutputSignals()
               
    """
    # End: extraVHDLOutputSignals setters and getters
    """


    
   
    def connect(self):
        super().connect()    

    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        
        self.vhdlProcessDescription = PCSystemProcessVHDLDescription()


    def connectProperties(self):
        super().connectProperties()        
        #property to store the vhdl constant in an array
        self._vhdlWeightSignals = None
        self._arithmeticNodes = None
        self._extraVHDLOutputSignals = None

    
    def reset(self):
        super().reset()
        self.resetProperties()
   
    def appendExtraVHDLOutputSignals(self):
        self.vhdlOutputSignals = self.vhdlOutputSignals + self.extraVHDLOutputSignals

    def generateHWVHDLEntityArchitectureDefinition(self):
        entityArchitectureDefinition = self.hwVHDLEntityArchitectureDefinitionStartSyntax() + "\n" + "    "

        # access the vhdlOutputPortSignals
        # append the entityArchitectureDefinition with output port syntax
        for vhdlOutputPortSignal in self.vhdlOutputSignals:
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
    
    
    
    
    
    def resetProperties(self):
        super().resetProperties()        
         #property to store the vhdl constant in an array
        self._vhdlWeightSignals = None
        self._arithmeticNodes = None
        self._extraVHDLOutputSignals = None


    def configure(self):
        super().configure()

        configurationDetails = self.configurationDetailsOfHW
        
        if "ArithmeticNodes" in configurationDetails:
            self.arithmeticNodes = configurationDetails["ArithmeticNodes"]

    
    def process(self):
        super().process()

      
    def perform(self):
        self.vhdlProcessDescription.perform()
        self.generateHWVHDLEntityArchitectureDefinition()
        self.generateHWVHDLEntityTBArchitectureDefinition()

    def main(self):
        super().main()
        self.process()
        self.perform()

    def run(self):
        self.main()

