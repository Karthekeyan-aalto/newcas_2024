"""
Created by Karthekeyan Periasamy
Created on Jan 18 12:51 PM
"""

from HWDescription.HWVHDLDescription import HWVHDLDescription

class LUTVHDLDescription(HWVHDLDescription):

    def __init__(self):
        super().__init__()
        self.connect()
    
    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        # property to store the vhdl port definition
        self.vhdlLUTEntityPortDefinition = None
        # property to store the vhdl architecture definition
        self.vhdlLUTEntityArchitectureDefinition = None
        # property to store the vhdlDescription of the LUT
        self.vhdlDescription = None

        #property to store the vhdl constant in an array
        self.vhdlConstantSignals = None

        # property to store the Input Signals
        # this contains the signals of input ports and other input signals that will be fed to the components of the top entity
        self.vhdlInputSignals = None


        #property to store the vhdlOutput signals
        # this contain the signals output port signals and component output signals
        self.vhdlOutputSignals = None

        #proerty to store the lutVHDLLibraries
        self.vhdlLibraries = None


    @property
    def vhdlLibraries(self):
        if self._vhdlLibraries == None:
            self._vhdlLibraries = self.lutVHDLEntityLibrariesSyntax()

        return self._vhdlLibraries

    @vhdlLibraries.setter
    def vhdlLibraries(self, value):
        self._vhdlLibraries = value
    
    
    """
    # Start: vhdlInputSignals getters
    """

    @property
    def vhdlInputSignals(self):
        if self._vhdlInputSignals == None:
            self._vhdlInputSignals = list()
            
        return self._vhdlInputSignals
        
    @vhdlInputSignals.setter
    def vhdlInputSignals(self, value):
        self._vhdlInputSignals = value
       
    """
    # End: vhdlInputSignals setters and getters
    """
    
    """
    # Start: vhdlConstantSignals getters
    """

    @property
    def vhdlConstantSignals(self):
        if self._vhdlConstantSignals == None:
            self._vhdlConstantSignals = list()
            
        return self._vhdlConstantSignals
        
    @vhdlConstantSignals.setter
    def vhdlConstantSignals(self, value):
        self._vhdlConstantSignals = value
       
    """
    # End: vhdlConstantSignals setters and getters
    """

    
    """
    # Start: vhdlOutputSignals getters
    """

    @property
    def vhdlOutputSignals(self):
        if self._vhdlOutputSignals == None:
            self._vhdlOutputSignals = list()
            
        return self._vhdlOutputSignals
        
    @vhdlOutputSignals.setter
    def vhdlOutputSignals(self, value):
        self._vhdlOutputSignals = value
       
    """
    # End: vhdlOutputSignals setters and getters
    """
    
    """
    # Start: inputDataPorts getters
    """

    @property
    def inputDataPorts(self):
        if self._inputDataPorts == None:
            self._inputDataPorts = list()
            
        return self._inputDataPorts
        
    @inputDataPorts.setter
    def inputDataPorts(self, value):
        self._inputDataPorts = value
       
    """
    # End: inputDataPorts setters and getters
    """
    
    """
    # Start: outputPorts getters
    """

    @property
    def outputPorts(self):
        if self._outputPorts == None:
            self._outputPorts = list()
            
        return self._outputPorts
        
    @outputPorts.setter
    def outputPorts(self, value):
        self._outputPorts = value
        # access the vhdlOutputPortSignals
        # add the signals to the output ports
        for outputPort in self.outputPorts:
            print("NumberOfOutput Port",len(self.outputPorts))
            self.vhdlOutputSignals.append(outputPort.hwDescription.vhdlPortSignal)
            print("VHDLOutputPort Signals",len(self.vhdlOutputSignals))

       
    """
    # End: inputDataPorts setters and getters
    """

    def generateLUTVHDLGenerics(self):
        genericsString = "GENERIC" + " " + "("

        # access the length of the dictionary
        lengthOfDictionary = len(self.lutGenerics)
        # local property to know the number of keys
        totalNumberOfKeysIterated = 0
        # loop through the lutGenerics
        for key, value in self.lutGenerics.items():
            totalNumberOfKeysIterated = totalNumberOfKeysIterated + 1
            if totalNumberOfKeysIterated == lengthOfDictionary:
                genericsString = genericsString + key + " " + ":INTEGER" + " " + ":=" + " " + str(value) + ")" + ";" + "\n"
            else:
                genericsString = genericsString + key + " " + ":INTEGER" + " " + ":=" + " " + str(value) + " " + ";" + " "
                            
        return genericsString


    def lutVHDLEntityPortDefinitionStartSyntax(self):
        portDefinitionStartSyntax = ("ENTITY" + " " + self.hwName + " " + "IS" + "\n" \
                + "    " + self.generateLUTVHDLGenerics() \
                + "    " + "PORT" + " " + "(" + "\n")
        return portDefinitionStartSyntax

    def lutVHDLEntityPortDefinitionEndSyntax(self):
        portDefinitionEndSyntax = (")" + ";" + "\n"
                + "END" + " " + self.hwName + ";" + "\n")
        return portDefinitionEndSyntax


    def lutVHDLEntityArchitectureDefinitionStartSyntax(self):
        entityArchitectureDefinitionStartSyntax = ("ARCHITECTURE" + " " + "rtl" + " " + "of " + self.hwName + " " + "IS" + "\n")
        return entityArchitectureDefinitionStartSyntax

    def lutVHDLEntityArchitectureDefinitionEndSyntax(self):
        entityArchitectureDefinitionEndSyntax = ("END" + " " + "ARCHITECTURE" + ";" + "\n")
        return entityArchitectureDefinitionEndSyntax

    def lutVHDLEntityLibrariesSyntax(self):
        return ("LIBRARY ieee; \n" \
                    + "LIBRARY std; \n" \
                    + "USE ieee.std_logic_1164.all; \n" \
                    + "USE ieee.std_logic_arith.all; \n" \
                    + "USE ieee.std_logic_unsigned.all; \n" \
                    + "USE std.textio.all; \n \n")



    def generateLUTVHDLEntityPortDefinition(self):
        entityPortDefinitionStartSyntax = self.vhdlLibraries
        entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + self.lutVHDLEntityPortDefinitionStartSyntax()
        # append the start syntax with the input ports and outputports vhdlDefinition
        for inputPort in self.inputDataPorts:
            entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + "    " + inputPort.hwDescription.vhdlPortDeclaration
            
        # append the clock port definition
        entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + "    " + self.clockPort.hwDescription.vhdlPortDeclaration
        
        # append the reset port definition
        entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + "    " + self.resetPort.hwDescription.vhdlPortDeclaration
        
        # append the output ports syntax
        for outputPort in self.outputPorts:
            entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + "    " + outputPort.hwDescription.vhdlPortDeclaration


        # update the entity port definition with the closure
        entityPortDefinitionStartSyntax = entityPortDefinitionStartSyntax + self.lutVHDLEntityPortDefinitionEndSyntax()

        # set the property to hold the vhdlLUTEntityPortDefinition
        self.vhdlLUTEntityPortDefinition = entityPortDefinitionStartSyntax
        

    def generateLUTVHDLEntityArchitectureDefinition(self):
        entityArchitectureDefinition = self.lutVHDLEntityArchitectureDefinitionStartSyntax()

        # access the vhdlOutputPortSignals
        # append the entityArchitectureDefinition with output port syntax
        for vhdlOutputPortSignal in self.vhdlOutputSignals:
            entityArchitectureDefinition = entityArchitectureDefinition + "    " + vhdlOutputPortSignal
            

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
                entityArchitectureDefinition = entityArchitectureDefinition + "\"" + str(value) + "\"" + " " + "WHEN" + " " + str(key) + ";" + "\n" + "    "
            else:
                entityArchitectureDefinition = entityArchitectureDefinition + "\"" + str(value) + "\"" + " " + "WHEN" + " " + "\'" + str(key) + "\'" + "," + "\n" + "    "

        entityArchitectureDefinition = entityArchitectureDefinition + outputPort.name + " " + "<=" + " " + outputPort.hwDescription.vhdlPortSignalName + ";" + "\n\n"

        entityArchitectureDefinition = entityArchitectureDefinition + self.lutVHDLEntityArchitectureDefinitionEndSyntax()
        self.vhdlLUTEntityArchitectureDefinition = entityArchitectureDefinition


    def process(self):
        super().process()
        self.generateLUTVHDLEntityPortDefinition()
        self.generateLUTVHDLEntityArchitectureDefinition()
        # append the port and architectured
        self.vhdlDescription =  self.vhdlLUTEntityPortDefinition + self.vhdlLUTEntityArchitectureDefinition
        # print the vhdlDescription
        print(self.vhdlDescription)


    def configure(self):
        super().configure()
 
    def reset(self):
        super().reset()
        # property to store the vhdl port definition
        self.vhdlLUTEntityPortDefinition = None
        # property to store the vhdl architecture definition
        self.vhdlLUTEntityArchitectureDefinition = None
        # property to store the vhdlDescription of the LUT
        self.vhdlDescription = None

    def main(self):
        pass

    def run(self):
        pass

