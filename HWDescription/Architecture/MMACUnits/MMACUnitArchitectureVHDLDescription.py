"""
Created by Karthekeyan Periasamy
Edited on August 1, 2023, 14:43
"""

from HWDescription.Architecture.ArchitectureVHDLDescription import ArchitectureVHDLDescription
from HWDescription.Process.MMACUnits.MMACUnitProcessVHDLDescription import MMACUnitProcessVHDLDescription
from Operations.ProductNode.ProductNode import ProductNode

class MMACUnitArchitectureVHDLDescription(ArchitectureVHDLDescription):

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
            if isinstance(arithmeticNode, ProductNode):
                if (arithmeticNode.vhdlWeightSignal != None):
                    self.vhdlWeightSignals.append(arithmeticNode.vhdlWeightSignal)
        
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
        self.connectHWVHDLPackages()
        self.connectProperties()
    

    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        self.vhdlProcessDescription = MMACUnitProcessVHDLDescription()
  

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
            #print("Arithmetic Node Instance", arithmeticNode.vhdlInstance)
            self.pythonHW = self.pythonHW + arithmeticNode.vhdlInstance
            

        # updating the python hw wth the instances of the multiplier and adder is not enough
        # as addition of the pipeline stages are important when we have automatic pipeline
        
        # attach the python HW to the architecture
        entityArchitectureDefinition = entityArchitectureDefinition + self.pythonHW
        
        topArithmeticNodeOfMMACUnit = self.arithmeticNodes[len(self.arithmeticNodes)-1]
        finalOutput = topArithmeticNodeOfMMACUnit.output
        entityArchitectureDefinition = entityArchitectureDefinition + self.pythonHWOutputPorts[0].name + " " + "<= " + finalOutput + ";" + "\n \n"
        
        entityArchitectureDefinition = entityArchitectureDefinition + self.hwVHDLEntityArchitectureDefinitionEndSyntax()
        self.vhdlEntityArchitectureDefinition = entityArchitectureDefinition
        #print("MMACUnit Entity Architecture Definition",self.vhdlEntityArchitectureDefinition)
    
    
    
    
    
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

