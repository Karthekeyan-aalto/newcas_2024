"""
Created by Karthekeyan Periasamy
Edited on June 16 10:00 AM
"""

from HWDescription.HWDescription import HWDescription
from HWDescription.Architecture.ArchitectureVHDLDescription import ArchitectureVHDLDescription
from HWDescription.Entity.EntityVHDLDescription import EntityVHDLDescription

class HWVHDLDescription(HWDescription):

    def __init__(self):
        super().__init__()
        self.connect()

    
    def connect(self):
        super().connect()
        self.connectHWVHDLPackages()
        self.connectProperties()

    def connectHWVHDLPackages(self):
        # connect the hw entity packages
        self.vhdlEntityDescription = EntityVHDLDescription()
        # connect the hw architecture packages
        self.vhdlEntityArchitectureDescription = ArchitectureVHDLDescription()

    def connectProperties(self):
        super().connectProperties()
        # property to store the vhdl port definition
        self.vhdlEntityPortDefinition = None
        # property to store the vhdl architecture definition
        self.vhdlEntityArchitectureDefinition = None
        # property to store the vhdlDescription of an entity
        self.vhdlDescription = None
        # property to store the test bench vhdl description of an entity
        self.vhdlTBDescription = None 
       

    def process(self):
        super().process()

        self.vhdlEntityDescription.process()
        self.vhdlEntityArchitectureDescription.process()

    def configure(self):
        super().configure()

        # configure the VHDL Generics Package
        if self.configurationDetailsOfHW == None:
            return
        
        # store the configuraiton details to a local variable
        configurationDetails = self.configurationDetailsOfHW
        # check the generics key of the HW
        if "PythonHWEntity" in configurationDetails:
            self.vhdlEntityDescription.configurationDetailsOfHW = configurationDetails["PythonHWEntity"]
            self.vhdlEntityDescription.configure()
        
        if "PythonHWArchitecture" in configurationDetails:
            #print("Super Architecture Definition")
            self.vhdlEntityArchitectureDescription.configurationDetailsOfHW = configurationDetails["PythonHWArchitecture"]
            self.vhdlEntityArchitectureDescription.configure()
    
    def reset(self):
        super().reset()
        self.resetProperties()
        self.resetHWVHDLPackages()

     
    def resetHWVHDLPackages(self):
        # connect the hw entity packages
        self.vhdlEntityDescription = EntityVHDLDescription()
        # connect the hw architecture packages
        self.vhdlEntityArchitectureDescription = ArchitectureVHDLDescription()
    
    
    def resetProperties(self):
        # property to store the vhdl port definition
        self.vhdlEntityPortDefinition = None
        # property to store the vhdl architecture definition
        self.vhdlEntityArchitectureDefinition = None
        # property to store the vhdlDescription
        self.vhdlDescription = None
        self.vhdlTBDescription = None
            

    def perform(self):
        # first perfeorm the entity description
        # it will generate necessary VHDL definitions
        self.vhdlEntityDescription.perform()
        # access the vhdl instance from the entity description
        # set the accessed vhdl instace definition to the entity architecture
        self.vhdlEntityArchitectureDescription.vhdlEntityInstance = self.vhdlEntityDescription.vhdlEntityInstanceDefinition
        self.vhdlEntityArchitectureDescription.vhdlEntityTBInstance = self.vhdlEntityDescription.vhdlEntityTBInstanceDefinition
        self.vhdlEntityArchitectureDescription.perform()

        # print the vhdl architecture Description
        #print(self.vhdlEntityArchitectureDescription.vhdlEntityArchitectureDefinition)

        # append the entity and the architecture
        self.vhdlDescription =  self.vhdlEntityDescription.vhdlEntityPortDefinition + self.vhdlEntityArchitectureDescription.vhdlEntityArchitectureDefinition
        # print the vhdlDescription
        # print the hw vhdl test bench
        #print("Entity VHDL Description", self.vhdlDescription)

        # build the test bench definition of the mmacunit
        self.vhdlTBDescription = self.vhdlEntityDescription.vhdlEntityTBPortDefinition + self.vhdlEntityArchitectureDescription.vhdlEntityArchitectureTBDefinition
        # print the hw vhdl test bench
        #print("Entity VHDL TB Description", self.vhdlTBDescription)


    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()

