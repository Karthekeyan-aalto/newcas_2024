"""
Created by Karthekeyan Periasamy
Edited on April 4, 2023, 10:16
"""

from HWDescription.Entity.EntityHWDescription import EntityHWDescription
from HWDescription.Generics.GenericVHDLDescription import GenericVHDLDescription


class EntityVHDLDescription(EntityHWDescription):

    def __init__(self):
        self.connect()
        
        
    
    @property
    def vhdlLibraries(self):
        if self._vhdlLibraries == None:
            self._vhdlLibraries = self.hwVHDLEntityLibrariesSyntax()

        return self._vhdlLibraries

    @vhdlLibraries.setter
    def vhdlLibraries(self, value):
        self._vhdlLibraries = value

    
    
    def hwVHDLEntityDefinitionStartSyntax(self):
        entityDefinitionStartSyntax = ("ENTITY" + " " + self.hwName + " " + "IS" + "\n")
        return entityDefinitionStartSyntax
    
    def hwVHDLEntityTBDefinitionStartSyntax(self):
        entityTBDefinitionStartSyntax = ("ENTITY" + " " + self.hwName + "_" + "tb" + " " + "IS" + "\n")
        return entityTBDefinitionStartSyntax

    def hwVHDLEntityPortDefinitionStartSyntax(self):
        entityPortDefinitionStartSyntax = ("    " + self.vhdlGenericDescription.vhdlGeneric \
                + "    " + "PORT" + " " + "(" + "\n")
        return entityPortDefinitionStartSyntax
    
    
    def hwVHDLEntityPortDefinitionEndSyntax(self):
        entityPortDefinitionEndSyntax = (")" + ";" + "\n")
        return entityPortDefinitionEndSyntax


    def hwVHDLEntityDefinitionEndSyntax(self):
        entityDefinitionEndSyntax = ("END" + " " + self.hwName + ";" + "\n\n")
        return entityDefinitionEndSyntax
    
    
    def hwVHDLEntityTBDefinitionEndSyntax(self):
        entityTBDefinitionEndSyntax = ("END" + " " + self.hwName + "_" + "tb" + ";" + "\n\n")
        return entityTBDefinitionEndSyntax

    
    
    def hwVHDLEntityLibrariesSyntax(self):
        return ("LIBRARY ieee; \n" \
                    + "USE ieee.std_logic_1164.all; \n" \
                    + "USE ieee.std_logic_arith.all; \n" \
                    + "USE ieee.std_logic_unsigned.all; \n" \
                    + "USE ieee.std_logic_textio.all; \n \n" \
                    + "LIBRARY std; \n" \
                    + "USE std.textio.all; \n \n")


    def connect(self):
        super().connect()
        self.connectHWVHDLPackages()
        self.connectProperties()
    
    def connectHWVHDLPackages(self):
        # connect the hw generic packages
        self.vhdlGenericDescription = GenericVHDLDescription()    
    
    def connectProperties(self):
        super().connectProperties()
        # property to store the vhdl port definition
        self.vhdlEntityPortDefinition = None
        self.vhdlEntityInstanceDefinition = None
        self.vhdlEntityTBInstanceDefnition = None
        self.vhdlEntityTBPortDefinition = None
        #proerty to store the lutVHDLLibraries
        self._vhdlLibraries = None
    
    
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

    def generateHWVHDLEntityInstanceDefinition(self):
        self.vhdlEntityInstanceDefinition = ("    " + self.hwInstanceName + ":" + " " +"entity work"+"." \
                + self.hwName +"("+"rtl"+")" "\n" + "    " + self.vhdlGenericDescription.vhdlGenericMap 
                + "    " + self.generateHWVHDLEntityPortMap() \
                + "\n")
    
    def generateHWVHDLEntityTBInstanceDefinition(self):
        self.vhdlEntityTBInstanceDefinition = ("    " + self.hwInstanceName + ":" + " " +"entity work"+"." \
                + self.hwName +"("+"rtl"+")" "\n" + "    " + self.vhdlGenericDescription.vhdlGenericMap 
                + "    " + self.generateHWVHDLEntityTBPortMap() \
                + "\n")

    def generateHWVHDLEntityTBPortDefinition(self):
        entityTBDefinitionSyntax = self.vhdlLibraries
        entityTBDefinitionSyntax = entityTBDefinitionSyntax + self.hwVHDLEntityTBDefinitionStartSyntax()

        # update the entity port definition with the closure
        entityTBDefinitionSyntax = entityTBDefinitionSyntax + self.hwVHDLEntityTBDefinitionEndSyntax()

        # set the property to hold the vhdlEntityTBDefinition
        self.vhdlEntityTBPortDefinition = entityTBDefinitionSyntax
    
    
    def reset(self):
        super().reset()
        self.resetProperties()

    def resetPropertiest(self):
        super().resetProperties()
        # property to store the vhdl port definition
        self.vhdlEntityPortDefinition = None
        # propertu to store the vhdl entity definition
        self.vhdlEntityInstanceDefinition = None
        self.vhdlEntityTBInstanceDefinition = None
        # property to store the vhdl entity testbench port definition
        self.vhdlEntityTBPortDefinition = None
        #proerty to store the lutVHDLLibraries
        self._vhdlLibraries = None

    def configure(self):
        super().configure()
        
        # configure the VHDL Generics Package
        if self.configurationDetailsOfHW == None:
            return
        
        # store the configuraiton details to a local variable
        configurationDetails = self.configurationDetailsOfHW
        #print(configurationDetails)
        
        # check the generics key of the HW
        if "PythonHWGeneric" in configurationDetails:
            self.vhdlGenericDescription.configurationDetailsOfHWGenerics = configurationDetails["PythonHWGeneric"]
            self.vhdlGenericDescription.configure()


    def process(self):
        super().process()
        self.vhdlGenericDescription.process()
    
    def perform(self):
        super().perform()
        self.vhdlGenericDescription.perform()
        self.generateHWVHDLEntityPortDefinition()
        self.generateHWVHDLEntityTBPortDefinition()
        self.generateHWVHDLEntityInstanceDefinition()
        self.generateHWVHDLEntityTBInstanceDefinition()


    def main(self):
        pass

    def run(self):
        pass

