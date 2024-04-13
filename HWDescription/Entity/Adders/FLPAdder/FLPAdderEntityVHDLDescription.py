"""
Created by Karthekeyan Periasamy
Edited on December 7, 2023, 04:18
"""

from HWDescription.Entity.EntityVHDLDescription import EntityVHDLDescription

class FLPAdderEntityVHDLDescription(EntityVHDLDescription):

    def __init__(self):
        self.connect()
        
        
    def connect(self):
        super().connect()
        self.connectHWVHDLPackages()
        self.connectProperties()
    
    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
 
    
    def connectProperties(self):
        super().connectProperties()

        self.hwFLPFlopocoName = None
    
    def generateHWVHDLEntityInstanceDefinition(self):
        self.vhdlEntityInstanceDefinition = ("    " + self.hwInstanceName + ":" + " " +"entity work"+"." \
                + self.hwFLPFlopocoName +"("+"arch"+")" "\n" 
                + "    " + self.generateHWVHDLEntityPortMap() \
                + "\n")
    
    def generateHWVHDLEntityTBInstanceDefinition(self):
        self.vhdlEntityTBInstanceDefinition = ("    " + self.hwInstanceName + ":" + " " +"entity work"+"." \
                + self.hwFLPFlopocoName +"("+"arch"+")" "\n"
                + "    " + self.generateHWVHDLEntityTBPortMap() \
                + "\n")

        
    def generateHWVHDLEntityPortMap(self):
        entityPortMapString = "PORT MAP" + " " + "("        

        # access the length of the inputPorts array
        lengthOfInputPorts = len(self.pythonHWInputPorts)
        
        # access the length of the inputPorts array
        lengthOfOutputPorts = len(self.pythonHWOutputPorts)

        # local property to know the number of input ports
        totalNumberOfInputPortsIterated = 0
        
        # local property to know the number of output ports
        totalNumberOfOutputPortsIterated = 0
        
        entityPortMapString = entityPortMapString + self.pythonHWClockPort.name + "," + " "
        #entityPortMapString = entityPortMapString + self.pythonHWResetPort.name + "," + " "

        # loop through the hwInput ports
        for inputPort in self.pythonHWInputPorts:
            totalNumberOfInputPortsIterated = totalNumberOfInputPortsIterated + 1
            entityPortMapString = entityPortMapString + inputPort.name + "," + " "
        
        # loop through the hw output ports
        for outputPort in self.pythonHWOutputPorts:
            totalNumberOfOutputPortsIterated = totalNumberOfOutputPortsIterated + 1
            if totalNumberOfOutputPortsIterated == lengthOfOutputPorts:
                entityPortMapString = entityPortMapString + outputPort.name + ")" + ";" + "\n"
            else:
                entityPortMapString = entityPortMapString + outputPort.name + "," + " "
        #print("EntityPortMapString", entityPortMapString)
        return entityPortMapString

    def reset(self):
        super().reset()
        self.resetProperties()

    def resetPropertiest(self):
        super().resetProperties()
        self.hwFLPFlopocoName = None
        
    def configure(self):
        super().configure()
        
        # configure the VHDL Generics Package
        if self.configurationDetailsOfHW == None:
            return
        
        # store the configuraiton details to a local variable
        configurationDetails = self.configurationDetailsOfHW
        #print(configurationDetails)

        # check the HWFLPFlopocoName
        if "FLPFlopocoName" in configurationDetails:
            self.hwFLPFlopocoName = configurationDetails["FLPFlopocoName"]
        
        # check the generics key of the HW
        if "PythonHWGeneric" in configurationDetails:
            self.vhdlGenericDescription.configurationDetailsOfHWGenerics = configurationDetails["PythonHWGeneric"]
            self.vhdlGenericDescription.configure()


    def process(self):
        super().process()
    
    def perform(self):
        super().perform()


    def main(self):
        super().main()

    def run(self):
        self.main()

