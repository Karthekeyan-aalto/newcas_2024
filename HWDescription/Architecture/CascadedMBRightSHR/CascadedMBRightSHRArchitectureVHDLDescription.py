"""
Created by Karthekeyan Periasamy
Edited on September 9, 2023, 19:00
"""

from HWDescription.Architecture.ArchitectureVHDLDescription import ArchitectureVHDLDescription
from HWDescription.Process.ProcessVHDLDescription import ProcessVHDLDescription


class CascadedMBRightSHRArchitectureVHDLDescription(ArchitectureVHDLDescription):

    def __init__(self):
        self.connect()
    
    
    @property
    def vhdlInputSignals(self):
        if self._vhdlInputSignals == None:
            self._vhdlInputSignals = list()

        return self._vhdlInputSignals
    
    @vhdlInputSignals.setter
    def vhdlInputSignals(self,value):
        self._vhdlInputSignals = value
    
    
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
    #Start: Custom getters and setters
    """
    @property
    def cascadedRegisters(self):
        return self._cascadedRegisters


    @cascadedRegisters.setter
    def cascadedRegisters(self,value):
        self._cascadedRegisters = value

        # extract the MBRightSHR and its associated vhdl output signals and vhdl input signals
        for index in range(0,len(self._cascadedRegisters)):
            mbRightSHR = self._cascadedRegisters[index]
            self.vhdlOutputSignals = self.vhdlOutputSignals + (mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals)
            if index == 0:
                # print the vhdl input signals
                self.vhdlInputSignals = self.vhdlInputSignals + (mbRightSHR.hwVHDLDescription.vhdlEntityArchitectureDescription.vhdlInputSignals)
        
    
    def configure(self):
        super().configure()

        if "CascadedRegisters" in self.configurationDetailsOfHW:
            self.cascadedRegisters = self.configurationDetailsOfHW["CascadedRegisters"]
    
    def connectProperties(self):
        super().connectProperties()

        self._cascadedRegisters = None


    def generateHWVHDLEntityArchitectureDefinition(self):
        entityArchitectureDefinition = self.hwVHDLEntityArchitectureDefinitionStartSyntax() + "\n"

        # access the vhdlOutputPortSignals
        # append the entityArchitectureDefinition with output port syntax
        for vhdlOutputPortSignal in self.vhdlOutputSignals:
            entityArchitectureDefinition = entityArchitectureDefinition + "    " + vhdlOutputPortSignal + "    "
            
            
        entityArchitectureDefinition = entityArchitectureDefinition + "    " + self.vhdlInputSignals[len(self.vhdlInputSignals)-1] + "    "
        entityArchitectureDefinition = entityArchitectureDefinition + "\n"

        # begin the lutVHDLEntity architecture
        entityArchitectureDefinition = (entityArchitectureDefinition + "BEGIN" + "\n" \
                + "    ")

        if self.pythonHWClockPort != None:

            # attach the process start and end description of the HW
            entityArchitectureDefinition = entityArchitectureDefinition + self.vhdlProcessDescription.vhdlEntityProcessDefinition + "\n"
        
        # update the python HW with the instances of the mbrightSHR from the cascadedRegisters array
        for mbRightSHR in self.cascadedRegisters:
            #print("MBRightSHR Node Entity Definition", mbRightSHR.hwVHDLDescription.vhdlEntityDescription)
            #print("MBRightSHR Node Instance Definition", mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
            self.pythonHW = self.pythonHW +  mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition
            
            # add the vhdl instances to the VHDLInstances array
            self.vhdlEntityInstances.append(mbRightSHR.hwVHDLDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
            

        # updating the python hw wth the instances of the multiplier and adder is not enough
        # as addition of the pipeline stages are important when we have automatic pipeline
        
        # attach the python HW to the architecture
        entityArchitectureDefinition = entityArchitectureDefinition + self.pythonHW
        
        lastIndexḾBRightSHR = self.cascadedRegisters[len(self.cascadedRegisters)-1]
        finalOutput = lastIndexḾBRightSHR.outputPorts[0].name
        entityArchitectureDefinition = entityArchitectureDefinition + self.pythonHWOutputPorts[0].name + " " + "<= " + finalOutput + ";" + "\n \n"
        
        entityArchitectureDefinition = entityArchitectureDefinition + self.hwVHDLEntityArchitectureDefinitionEndSyntax()
        self.vhdlEntityArchitectureDefinition = entityArchitectureDefinition
        #print("Cascaded MBRightSHR Entity Architecture Definition",self.vhdlEntityArchitectureDefinition)
    
    
    def process(self):
        super().process()


    def perform(self):
        #print("Perform Function of the cascadedd mbright SHR is called")
        super().perform()

    def resetProperties(self):
        self.resetProperties()
        self._cascadedRegisters = None
   
    def main(self):
        super().main()
