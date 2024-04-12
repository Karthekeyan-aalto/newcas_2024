#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:17:30 2022

@author: Karthekeyan Periasamy
"""


class PCSystemVHDLConfiguration():
    
    def __init__(self):
        
        # simulation run time
        self._simulationRunTime = None
        # numberOfBits to represeent a PC
        self.numberOfBits = 0
        # mantissaBits to represent a PC
        self.mantissaBits = 0
        # exponentBits to represent a PC
        self.exponentBits = 0
        # esBits to represent a PC
        self.esBits = 2
        # property to store the fixedVHDL libraries
        self._fixedPCSystemVHDLLibrariesSyntax = None 
        # property to store the floatVHDL libraries
        self._floatPCSystemVHDLLibrariesSyntax = None
        # property to store the POSITVHDL libraries
        self._positPCSystemVHDLLibrariesSyntax = None 
        # property to store the float generic VHDL syntax
        self._floatPCSystemGenericsVHDLSyntax = None
        # property to store the float generic VHDL syntax
        self._fixedPCSystemGenericsVHDLSyntax = None
        # property to store the POSIT Generic VHDL syntax
        self._positPCSystemGenericsVHDLSyntax = None 
        # property to store fixed pcSystem constantsVHDL syntax
        self._fixedPCSystemConstantsVHDLSyntax = None
        # property to store the float constants VHDL syntax
        self._floatPCSystemConstantsVHDLSyntax = None
        # property to store the posit constants VHDL syntax
        self._positPCSystemConstantsVHDLSyntax = None 
        # property to store the fixed generic map syntax
        self._fixedPCSystemGenericMapVHDLSyntax = None
        # property to store the float generic map syntax
        self._floatPCSystemGenericMapVHDLSyntax = None
        # property to store the floatPCSystemVHDLCompileScriptSyntax
        self._floatPCSystemVHDLCompileScriptSyntax = None
        # property to store the fixedPCSystemVHDLCompileScriptSyntax
        self._fixedPCSystemVHDLCompileScriptSyntax = None
        # property to store the positPCSystemVHDLCompileScriptSyntax
        self._positPCSystemVHDLCompileScriptSyntax = None
        # property to store the _fixedPCSystemVHDLTestBenchLibrariesSyntax
        self._fixedPCSystemVHDLTestBenchLibrariesSyntax = None
        # property to store the _floatPCSystemVHDLTestBenchLibrariesSyntax
        self._floatPCSystemVHDLTestBenchLibrariesSyntax = None
        # property to store the positPCSystemVHDLTestBenchLibrariesSyntax
        self._positPCSystemVHDLTestBenchLibrariesSyntax = None
        # property to store the _pcSystemVHDLSimulationScript
        self._pcSystemVHDLSimulationScript = None

    
    
    @property
    def simulationRunTime(self):
        if self._simulationRunTime == None:
            self._simulationRunTime = (" run 160 ns \n")
        return self._simulationRunTime


    @simulationRunTime.setter
    def simulationRunTime(self,value):
        self._simulationRunTime = "run" + " " + value + " " + "ns" + "\n"
        
   
    @property
    def fixedPCSystemVHDLLibrariesSyntax(self):
        if self._fixedPCSystemVHDLLibrariesSyntax == None:
            self._fixedPCSystemVHDLLibrariesSyntax = ("library ieee; \n" + "library ieee_proposed; \n" \
                    + "use ieee.std_logic_1164.all; \n" \
                    + "use ieee.numeric_std.all; \n" \
                    + "use std.textio.all; \n" \
                    + "use ieee_proposed.fixed_pkg.all; \n" \
                    + "use ieee_proposed.fixed_float_types.all; \n")
        return self._fixedPCSystemVHDLLibrariesSyntax


    @fixedPCSystemVHDLLibrariesSyntax.setter
    def fixedPCSystemVHDLLibrariesSyntax(self,value):
        self._fixedPCSystemVHDLLibrariesSyntax = value
        


    @property
    def floatPCSystemVHDLLibrariesSyntax(self):
        if self._floatPCSystemVHDLLibrariesSyntax == None:
            self._floatPCSystemVHDLLibrariesSyntax = ("library ieee; \n" + "library ieee_proposed; \n" \
                    + "use ieee.std_logic_1164.all; \n" \
                    + "use ieee.numeric_std.all; \n" \
                    + "use std.textio.all; \n" \
                    + "use ieee_proposed.fixed_pkg.all; \n" \
                    + "use ieee_proposed.fixed_float_types.all; \n" \
                    + "USE ieee_proposed.float_pkg.all; \n \n")
        return self._floatPCSystemVHDLLibrariesSyntax


    @floatPCSystemVHDLLibrariesSyntax.setter
    def floatPCSystemVHDLLibrariesSyntax(self,value):
        self._floatPCSystemVHDLLibrariesSyntax = value
        
    
    @property
    def positPCSystemVHDLLibrariesSyntax(self):
        if self._positPCSystemVHDLLibrariesSyntax == None:
            self._positPCSystemVHDLLibrariesSyntax = ("LIBRARY ieee; \n" \
                    + "LIBRARY std; \n" \
                    + "USE ieee.std_logic_1164.all; \n" \
                    + "USE ieee.std_logic_arith.all; \n" \
                    + "USE ieee.std_logic_unsigned.all; \n" \
                    + "USE std.textio.all; \n" \
                    + "LIBRARY work; \n \n")
        return self._positPCSystemVHDLLibrariesSyntax


    @positPCSystemVHDLLibrariesSyntax.setter
    def positPCSystemVHDLLibrariesSyntax(self,value):
        self._positPCSystemVHDLLibrariesSyntax = value 

    

    @property
    def fixedPCSystemVHDLTestBenchLibrariesSyntax(self):
        if self._fixedPCSystemVHDLTestBenchLibrariesSyntax == None:
            self._fixedPCSystemVHDLTestBenchLibrariesSyntax = ("library ieee; \n" + "library ieee_proposed; \n" \
                    + "use ieee.std_logic_1164.all; \n" \
                    + "use ieee.numeric_std.all; \n" \
                    + "use std.textio.all; \n" \
                    + "use ieee_proposed.fixed_pkg.all; \n" \
                    + "use ieee_proposed.fixed_float_types.all; \n\n")
        return self._fixedPCSystemVHDLTestBenchLibrariesSyntax


    @fixedPCSystemVHDLTestBenchLibrariesSyntax.setter
    def fixedPCSystemVHDLTestBenchLibrariesSyntax(self,value):
        self._fixedPCSystemVHDLTestBenchLibrariesSyntax = value


    @property
    def floatPCSystemVHDLTestBenchLibrariesSyntax(self):
        if self._fixedPCSystemVHDLTestBenchLibrariesSyntax == None:
            self._floatPCSystemVHDLTestBenchLibrariesSyntax = ("library ieee; \n" + "library ieee_proposed; \n" \
                    + "use ieee.std_logic_1164.all; \n" \
                    + "use ieee.numeric_std.all; \n" \
                    + "use std.textio.all; \n" \
                    + "use ieee_proposed.fixed_pkg.all; \n" \
                    + "use ieee_proposed.fixed_float_types.all; \n" \
                    + "USE ieee_proposed.float_pkg.all; \n\n")
        return self._floatPCSystemVHDLTestBenchLibrariesSyntax


    @floatPCSystemVHDLTestBenchLibrariesSyntax.setter
    def floatPCSystemVHDLTestBenchLibrariesSyntax(self,value):
        self._floatPCSystemVHDLTestBenchLibrariesSyntax = value
        
    
    @property
    def positPCSystemVHDLTestBenchLibrariesSyntax(self):
        if self._positPCSystemVHDLTestBenchLibrariesSyntax == None:
            self._positPCSystemVHDLTestBenchLibrariesSyntax = ("LIBRARY ieee; \n" \
                    + "use ieee.std_logic_1164.all; \n" \
                    + "use ieee.numeric_std.all; \n" \
                    + "use std.textio.all; \n \n")
        return self._positPCSystemVHDLTestBenchLibrariesSyntax


    @positPCSystemVHDLTestBenchLibrariesSyntax.setter
    def positPCSystemVHDLTestBenchLibrariesSyntax(self,value):
        self._positPCSystemVHDLTestBenchLibrariesSyntax = value

    
       
    @property
    def floatPCSystemGenericsVHDLSyntax(self):
        if self._floatPCSystemGenericsVHDLSyntax == None:
            self._floatPCSystemGenericsVHDLSyntax = ("generic(" + "mantissaBits : integer := " + str(self.mantissaBits) + ";" + " " \
                    + "exponentBits : integer := " + str(self.exponentBits) + ")" +";" + "\n")
        return self._floatPCSystemGenericsVHDLSyntax


    @floatPCSystemGenericsVHDLSyntax.setter
    def floatPCSystemGenericsVHDLSyntax(self,value):
        self._floatPCSystemGenericsVHDLSyntax = value

    
    @property
    def positPCSystemGenericsVHDLSyntax(self):
        if self._positPCSystemGenericsVHDLSyntax == None:
            self._positPCSystemGenericsVHDLSyntax = ("generic(" + "numberOfBits : integer := " + str(self.numberOfBits) + ")" +";" + "\n")
        return self._positPCSystemGenericsVHDLSyntax


    @positPCSystemGenericsVHDLSyntax.setter
    def positPCSystemGenericsVHDLSyntax(self,value):
        self._positPCSystemGenericsVHDLSyntax = value


    @property
    def fixedPCSystemGenericsVHDLSyntax(self):
        if self._fixedPCSystemGenericsVHDLSyntax == None:
            self._fixedPCSystemGenericsVHDLSyntax = ("generic( numberOfBits : integer := " + str(self.numberOfBits) + ")" +";" + "\n")
        return self._fixedPCSystemGenericsVHDLSyntax


    @fixedPCSystemGenericsVHDLSyntax.setter
    def fixedPCSystemGenericsVHDLSyntax(self,value):
        self._fixedPCSystemGenericsVHDLSyntax = value
        
        
    @property
    def fixedPCSystemConstantsVHDLSyntax(self):
        if self._fixedPCSystemConstantsVHDLSyntax == None:
            self._fixedPCSystemConstantsVHDLSyntax = ("CONSTANT numberOfBits : integer :=" + str(self.numberOfBits) + ";" + "\n \n")
        return self._fixedPCSystemConstantsVHDLSyntax


    @fixedPCSystemConstantsVHDLSyntax.setter
    def fixedPCSystemConstantsVHDLSyntax(self,value):
        self._fixedPCSystemConstantsVHDLSyntax = value
        
    
    @property
    def floatPCSystemConstantsVHDLSyntax(self):
        if self._floatPCSystemConstantsVHDLSyntax == None:
            self._floatPCSystemConstantsVHDLSyntax = ("CONSTANT mantissaBits : integer :=" + str(self.mantissaBits) + ";" + "\n \n" \
                    + "CONSTANT exponentBits : integer :=" + str(self.exponentBits) + ";" + "\n \n")
        return self._floatPCSystemConstantsVHDLSyntax


    @floatPCSystemConstantsVHDLSyntax.setter
    def floatPCSystemConstantsVHDLSyntax(self,value):
        self._floatPCSystemConstantsVHDLSyntax = value
        
    @property
    def positPCSystemConstantsVHDLSyntax(self):
        if self._positPCSystemConstantsVHDLSyntax == None:
            self._positPCSystemConstantsVHDLSyntax = ("CONSTANT numberOfBits : integer :=" + str(self.numberOfBits) + ";" + "\n \n")
        return self._positPCSystemConstantsVHDLSyntax


    @positPCSystemConstantsVHDLSyntax.setter
    def positPCSystemConstantsVHDLSyntax(self,value):
        self._positPCSystemConstantsVHDLSyntax = value

    
    @property
    def fixedPCSystemGenericMapVHDLSyntax(self):
        if self._fixedPCSystemGenericMapVHDLSyntax == None:
            self._fixedPCSystemGenericMapVHDLSyntax = ("generic map" + "(" + "numberOfBits" + ")"+ "\n")
        return self._fixedPCSystemGenericMapVHDLSyntax


    @fixedPCSystemGenericMapVHDLSyntax.setter
    def fixedPCSystemGenericMapVHDLSyntax(self,value):
        self._fixedPCSystemGenericMapVHDLSyntax = value
        
    
    @property
    def floatPCSystemGenericMapVHDLSyntax(self):
        if self._floatPCSystemGenericMapVHDLSyntax == None:
            self._floatPCSystemGenericMapVHDLSyntax = ("generic map" + "(" + "mantissaBits" + "," + "exponentBits" +")"+ "\n")
        return self._floatPCSystemGenericMapVHDLSyntax


    @floatPCSystemGenericMapVHDLSyntax.setter
    def floatPCSystemGenericMapVHDLSyntax(self,value):
        self._floatPCSystemGenericMapVHDLSyntax = value


    
    @property
    def fixedPCSystemVHDLCompileScriptSyntax(self):
        if self._fixedPCSystemVHDLCompileScriptSyntax == None:
            self._fixedPCSystemVHDLCompileScriptSyntax = ("vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_float_types_c.vhdl" + "\n" \
                    + "vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_pkg_c.vhdl" + "\n" \
                    + "vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_noresized.vhdl" + "\n" \
                    + "vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_synth.vhdl" + "\n")
        return self._fixedPCSystemVHDLCompileScriptSyntax


    @fixedPCSystemVHDLCompileScriptSyntax.setter
    def fixedPCSystemVHDLCompileScriptSyntax(self,value):
        self._fixedPCSystemVHDLCompileScriptSyntax = value
        
        
    @property
    def floatPCSystemVHDLCompileScriptSyntax(self):
        if self._floatPCSystemVHDLCompileScriptSyntax == None:
            self._floatPCSystemVHDLCompileScriptSyntax = ("vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_float_types_c.vhdl" + "\n" \
                    + "vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_pkg_c.vhdl" + "\n" \
                    + "vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_noresized.vhdl" + "\n" \
                    + "vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_synth.vhdl" + "\n" \
                    + "vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/float_pkg_c.vhdl" + "\n" \
                    + "vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/float_noround_pkg.vhdl" + "\n" \
                    + "vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/float_synth.vhdl" + "\n")

        return self._floatPCSystemVHDLCompileScriptSyntax


    @floatPCSystemVHDLCompileScriptSyntax.setter
    def floatPCSystemVHDLCompileScriptSyntax(self,value):
        self._floatPCSystemVHDLCompileScriptSyntax = value

   
   
    @property
    def pcSystemVHDLSimulationScript(self):
        if self._pcSystemVHDLSimulationScript == None:
            self._pcSystemVHDLSimulationScript = ("vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_float_types_c.vhdl" + "\n" \
                    + "vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_pkg_c.vhdl" + "\n" \
                    + "vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_noresized.vhdl" + "\n" \
                    + "vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_synth.vhdl" + "\n" \
                    + "vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/float_pkg_c.vhdl" + "\n" \
                    + "vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/float_noround_pkg.vhdl" + "\n" \
                    + "vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/float_synth.vhdl" + "\n")

        return self._pcSystemVHDLSimulationScript


    @pcSystemVHDLSimulationScript.setter
    def pcSystemVHDLSimulationScript(self,value):
        self._pcSystemVHDLSimulationScript = value
    
    
        
    def main(self):
        pass
    
    def run(self):
        pass


        

