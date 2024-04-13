"""
Created by Karthekeyan Periasamy
Edited on Jan 24 14:09
"""

from HWDescription.Signals.FloatSignal.FloatSignalVHDLDescription import FloatSignalVHDLDescription
from HWDescription.Operators.LUTs.LUTVHDLDescription import LUTVHDLDescription

class FloatLUTVHDLDescription(LUTVHDLDescription):

    """
    This class build the FloatLUT VHDL Description
    Though through the python LUT we could generate the float point look up table
    But the python LUT for float is not equipped to have a software converter
    """

    def __init__(self):
        super().__init__()
        # connect the VHDLSignal HW Description package
        self.connectVHDLSignalHWDescriptionPackage()
        
    @property
    def vhdlLibraries(self):
        if self._vhdlLibraries == None:
            self._vhdlLibraries = self.lutVHDLEntityLibrariesSyntax()

        return self._vhdlLibraries

    @vhdlLibraries.setter
    def vhdlLibraries(self, value):
        self._vhdlLibraries = value


    def lutVHDLEntityLibrariesSyntax(self):
        basicLUTEntityLibrary = super().lutVHDLEntityLibrariesSyntax()
        # append the basic LUT entity library
        floatLUTVHDLEntityLibrary = basicLUTEntityLibrary +  ("LIBRARY ieee_proposed; \n" \
                + "USE ieee_proposed.fixed_pkg.all; \n" \
                + "USE ieee_proposed.fixed_float_types.all; \n" \
                + "USE ieee_proposed.float_pkg.all; \n \n")
        return floatLUTVHDLEntityLibrary
    
    
    def generateLUTVHDLEntityArchitectureDefinition(self):
        entityArchitectureDefinition = self.lutVHDLEntityArchitectureDefinitionStartSyntax()

        # access the vhdlOutputPortSignals
        # append the entityArchitectureDefinition with output port syntax
        for vhdlOutputPortSignal in self.vhdlOutputSignals:
            entityArchitectureDefinition = entityArchitectureDefinition + "    " + vhdlOutputPortSignal
            
        # add the constant signal of the
        for vhdlConstantSignal in self.vhdlConstantSignals:
            entityArchitectureDefinition = entityArchitectureDefinition + "    " + vhdlConstantSignal

        # begin the lutVHDLEntity architecture
        entityArchitectureDefinition = (entityArchitectureDefinition + "BEGIN" + "\n" \
                + "    ")
        
        # as the current LUT supports mapping of only one input port signal
        # the code will be suitable for one input and one output

        # attach the python LUT to the architecture
        inputPort = self.inputDataPorts[0]
        
        entityArchitectureDefinition = entityArchitectureDefinition + "WITH" + " " + inputPort.name + " " + "SELECT" + " " 

        # retrieve the output port and the output port signal
        outputPort = self.outputPorts[0]
        
        entityArchitectureDefinition = entityArchitectureDefinition + " " + outputPort.hwDescription.vhdlPortSignalName + " " + "<=" + "\n" + "    "

        # length of the python LUT
        lengthOfPythonLUT = len(self.pythonLUT)
        # total key counter
        totalKeysOfPythonLUT = 0

        # add the python lut dictionary definition
        for key, value in self.pythonLUT.items():
            #count the items in pythonLUT
            totalKeysOfPythonLUT = totalKeysOfPythonLUT + 1
            if totalKeysOfPythonLUT == lengthOfPythonLUT:
                entityArchitectureDefinition = entityArchitectureDefinition + "\"" \
                + str(value) + "\"" + " " + "WHEN" + " " + str(key) + ";" + "\n" + "    "
            elif totalKeysOfPythonLUT == lengthOfPythonLUT-1:
                entityArchitectureDefinition = entityArchitectureDefinition + str(value) \
                + " " + "WHEN" + " " + "\'" + str(key) + "\'" + "," + "\n" + "    "

            else:
                entityArchitectureDefinition = entityArchitectureDefinition + "\"" + str(value) + "\"" \
                + " " + "WHEN" + " " + "\'" + str(key) + "\'" + "," + "\n" + "    "

        entityArchitectureDefinition = entityArchitectureDefinition + outputPort.name + " " + "<=" + " " + outputPort.hwDescription.vhdlPortSignalName + ";" + "\n\n"

        entityArchitectureDefinition = entityArchitectureDefinition + self.lutVHDLEntityArchitectureDefinitionEndSyntax()
        self.vhdlLUTEntityArchitectureDefinition = entityArchitectureDefinition

    def main(self):
        pass


    def process(self):
        # configure the signal HW package
        self.configureVHDLSignalHWPackage()
        # process the VHDLSignal HW Package
        self.floatSignalVHDLDescription.process()
        # access the processed signal hw description
        vhdlDescription = self.floatSignalVHDLDescription.vhdlDescription
        # access the vhdl description and add it to the vhdlConstant Signal
        self.vhdlConstantSignals.append(vhdlDescription)
        super().process()

    def reset(self):
        pass


    def connectVHDLSignalHWDescriptionPackage(self):
        # connect VHDL Signal HW Package
        self.floatSignalVHDLDescription = FloatSignalVHDLDescription()

    def configureVHDLSignalHWPackage(self):
        # configure VHDL Signal HW Package
        # access the python LUT dictionary definition
        # access the value string for key "1"
        valueForFloatOne = self.pythonLUT["1"]

        # use the information to configure the signals
        # make the necessary configuration details for the VHDL Signal package
        # the access to number of bits, needs to changed for now, we access it from the lutgenerics information
        configurationDetails = {"Name":valueForFloatOne, "NumberOfBits":self.lutGenerics["numberOfBits"],"ConstantSignalValue":1.0}
        # set the value for float one to generate a signal name
        self.floatSignalVHDLDescription.configurationDetails = configurationDetails

        # accesss the signal and store it in the vhdlConstantSignals array
        self.floatSignalVHDLDescription.configure()

    
    def configure(self):
        super().configure()        
