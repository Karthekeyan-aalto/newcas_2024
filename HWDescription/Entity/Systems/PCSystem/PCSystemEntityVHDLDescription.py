"""
Created by Karthekeyan Periasamy
Edited on April 4, 2023, 10:16
"""

from HWDescription.Entity.EntityVHDLDescription import EntityVHDLDescription
from HWDescription.Generics.GenericVHDLDescription import GenericVHDLDescription


class PCSystemEntityVHDLDescription(EntityVHDLDescription):

    def __init__(self):
        self.connect()

    def connect(self):
        super().connect()
    
    
    def generateHWVHDLEntityPortDefinition(self):
        entityPortDefinitionStartSyntax = self.vhdlLibraries
        entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + self.hwVHDLEntityDefinitionStartSyntax()
        entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + self.hwVHDLEntityPortDefinitionStartSyntax()
        
        if self.pythonHWClockPort != None:
            #print("PythonHW ClockPort VHDL Port HWDescription", self.pythonHWClockPort.hwDescription)
            #print("PythonHW ClockPort VHDL Port Declaration", self.pythonHWClockPort.hwDescription.vhdlPortDeclaration)
            # append the clock port definition
            entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + "    " + self.pythonHWClockPort.hwDescription.vhdlPortDeclaration
        
        if self.pythonHWResetPort != None:
            # append the reset port definition
            entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + "    " + self.pythonHWResetPort.hwDescription.vhdlPortDeclaration
        
        if self.pythonHWEnablePort != None:
            # append the enable port definition
            entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + "    " + self.pythonHWEnablePort.hwDescription.vhdlPortDeclaration


        # append the start syntax with the input ports and outputports vhdlDefinition
        for inputPort in self.pythonHWInputPorts:
            entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + "    " + inputPort.hwDescription.vhdlPortDeclaration
            
        # append the output ports syntax
        for outputPort in self.pythonHWOutputPorts:
            entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + "    " + outputPort.hwDescription.vhdlPortDeclaration


        # update the entity port definition with the closure
        entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + self.hwVHDLEntityPortDefinitionEndSyntax()
        # update the entity definition with the closure
        entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + self.hwVHDLEntityDefinitionEndSyntax()

        # set the property to hold the vhdlLUTEntityPortDefinition
        self.vhdlEntityPortDefinition = entityPortDefinitionStartSyntax
        
    
    
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
        entityPortMapString = entityPortMapString + self.pythonHWResetPort.name + "," + " "

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
    
    
    def generateHWVHDLEntityTBPortMap(self):
        entityTBPortMapString = "PORT MAP" + " " + "("        

        # access the length of the inputPorts array
        lengthOfInputPorts = len(self.pythonHWInputPorts)
        
        # access the length of the inputPorts array
        lengthOfOutputPorts = len(self.pythonHWOutputPorts)

        
        # local property to know the number of output ports
        totalNumberOfOutputPortsIterated = 0
        
        if self.pythonHWClockPort != None:
            entityTBPortMapString = entityTBPortMapString + self.pythonHWClockPort.name + " " + "=>" + " " + self.pythonHWClockPort.name + "," + " "
        
        if self.pythonHWResetPort != None:
            entityTBPortMapString = entityTBPortMapString + self.pythonHWResetPort.name + " " + "=>" + " " + self.pythonHWResetPort.name + "," + " "
        
        if self.pythonHWEnablePort != None:
            entityTBPortMapString = entityTBPortMapString + self.pythonHWEnablePort.name + " " + "=>" + " " + self.pythonHWEnablePort.name + "," + " "

        # loop through the hwInput ports
        for inputPort in self.pythonHWInputPorts:
            entityTBPortMapString = entityTBPortMapString + inputPort.name + " " + "=>" + " " + inputPort.name + " " + "," + " " 
        
        # loop through the hw output ports
        for outputPort in self.pythonHWOutputPorts:
            totalNumberOfOutputPortsIterated = totalNumberOfOutputPortsIterated + 1
            if totalNumberOfOutputPortsIterated == lengthOfOutputPorts:
                entityTBPortMapString = entityTBPortMapString + outputPort.name + " " +  "=>" + " " + outputPort.name + ")" + ";" + "\n"
            else:
                entityTBPortMapString = entityTBPortMapString + outputPort.name + "," + " "
                            
        return entityTBPortMapString

    
    
    
    def reset(self):
        super().reset()

    def configure(self):
        super().configure()
        
    def process(self):
        super().process()
    
    def perform(self):
        super().perform()

    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()

