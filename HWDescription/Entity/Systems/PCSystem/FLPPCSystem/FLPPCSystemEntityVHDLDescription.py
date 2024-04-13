"""
Created by Karthekeyan Periasamy
Edited on December 7, 2023, 04:18
"""

from HWDescription.Entity.EntityVHDLDescription import EntityVHDLDescription

class FLPPCSystemEntityVHDLDescription(EntityVHDLDescription):

    def __init__(self):
        self.connect()
        
    
    
    def hwVHDLEntityLibrariesSyntax(self):
        return ("LIBRARY ieee; \n" \
                "LIBRARY ieee_proposed; \n" \
                    + "USE ieee.std_logic_1164.all; \n" \
                    + "USE ieee.std_logic_arith.all; \n" \
                    + "USE ieee.std_logic_unsigned.all; \n" \
                    + "USE ieee.std_logic_textio.all; \n \n" \
                    + "LIBRARY std; \n" \
                    + "USE std.textio.all; \n" \
                    + "USE ieee_proposed.fixed_pkg.all; \n" \
                    + "USE ieee_proposed.fixed_float_types.all; \n" \
                    + "USE ieee_proposed.float_pkg.all; \n")

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
            #print("PythonHW Enable VHDL Port HWDescription", self.pythonHWEnablePort.name)
            #print("PythonHW Enable VHDL Port Declaration", self.pythonHWEnablePort.hwDescription.vhdlPortDeclaration)
            # append the enable port definition
            entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + "    " + self.pythonHWEnablePort.hwDescription.vhdlPortDeclaration


        # append the start syntax with the input ports and outputports vhdlDefinition
        for inputPort in self.pythonHWInputPorts:
            #print("Input Port", inputPort.name)
            #print("PythonHW InputPort VHDL Port Description", inputPort.hwDescription)
            #print("PythonHW InputPort VHDL Port Declaration", inputPort.hwDescription.vhdlPortDeclaration)
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
    def reset(self):
        super().reset()
        
    def configure(self):
        super().configure()

    def process(self):
        super().process()
    
    def perform(self):
        super().perform()


    def main(self):
        super().main()

    def run(self):
        self.main()

