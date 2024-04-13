#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:17:30 2022

@author: Karthekeyan Periasamy
"""

from HWDescription.PCSystemVHDLDescription import PCSystemVHDLDescription

class PCSystemProductNodeVHDLDescription(PCSystemVHDLDescription):
    
    def __init__(self):
        super().__init__()
        # reset the properties
        self.configure()

    """
    # Start: vhdlInputConverterInstances getters
    """

    @property
    def vhdlInputConverterInstances(self):
        if self._vhdlInputConverterInstances == None:
            self._vhdlInputConverterInstances = list()
            
        return self._vhdlInputConverterInstances
        
    @vhdlInputConverterInstances.setter
    def vhdlInputConverterInstances(self, value):
        self._vhdlInputConverterInstances = value
       
    """
    # End: vhdlInputConverterInstances setters and getters
    """
    
    """
    # Start: vhdlInputLUTInstances getters
    """

    @property
    def vhdlInputLUTInstances(self):
        if self._vhdlInputLUTInstances == None:
            self._vhdlInputLUTInstances = list()
            
        return self._vhdlInputLUTInstances
        
    @vhdlInputLUTInstances.setter
    def vhdlInputLUTInstances(self, value):
        self._vhdlInputLUTInstances = value
       
    """
    # End: vhdlInputLUTInstances setters and getters
    """

    
    """
    # Start: vhdlOutputConverterInstances getters
    """

    @property
    def vhdlOutputConverterInstances(self):
        if self._vhdlOutputConverterInstances == None:
            self._vhdlOutputConverterInstances = list()
            
        return self._vhdlOutputConverterInstances
        
    @vhdlOutputConverterInstances.setter
    def vhdlOutputConverterInstances(self, value):
        self._vhdlOutputConverterInstances = value
       
    """
    # End: vhdlOutputConverterInstances setters and getters
    """
    
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
    # Start: flopocoVHDLInstance getters
    """

    @property
    def flopocoVHDLInstance(self):
        if self._flopocoVHDLInstance == None:
            self._flopocoVHDLInstance = self.__generateFlopocoVHDLInstance()
        return self._flopocoVHDLInstance
        
    @flopocoVHDLInstance.setter
    def flopocoVHDLInstance(self, value):
        self._flopocoVHDLInstance = value
       
    """
    # End: vhdlOutputConverterInstances setters and getters
    """
    
    @property
    def tempOutputSignalVHDLSyntax(self):
        if self._tempOutputSignalVHDLSyntax == None:
            # have a temporary output signal to store the full output
            self._tempOutputSignalVHDLSyntax = "signal tempOutput: sfixed (1 downto ((1-numberOfBits)*2)):=to_sfixed(1,1,(1-numberOfBits)*2);"

        return self._tempOutputSignalVHDLSyntax

    @tempOutputSignalVHDLSyntax.setter
    def tempOutputSignalVHDLSyntax(self, value):
        self._tempOutputSignalVHDLSyntax = value

    """
    # Start: flopocoWeightName setters and getters
    """
    
    @property
    def flopocoWeightName(self):
        return self._flopocoWeightName
    
    
    @flopocoWeightName.setter  
    def flopocoWeightName(self,value):
        # value is the original weight name and store it in a private variable (it will be used to generate converter instances)
        self._weightName = value
        # concatenate the weightName string with Flopoco
        self._flopocoWeightName = value + "Flopoco"
        # generate the flopocoWeightVHDL Signal
        flopocoWeightSignal = self.__generateFlopocoWeightVHDLSignal()
        # add the flopocoWeight Signal to input signals
        self.vhdlInputSignals.append(flopocoWeightSignal)
        # generate the weight converter
        flopocoWeightConverterInstance = self.__generateWeightIEEEToFlopocoNumberSystemConverterInstance()
        # add the weight converter to the converter instances
        self.vhdlInputConverterInstances.append(flopocoWeightConverterInstance)
            
    """
    # Start: flopocoOutputName setters and getters
    """
    
    @property
    def flopocoOutputName(self):
        return self._flopocoOutputName
    
    
    @flopocoOutputName.setter  
    def flopocoOutputName(self,value):
        # store the output name
        self.outputName = value
        # set the flopoco output name
        self._flopocoOutputName = "outputpn" + value + "Flopoco"
        # generate the flopocoOutput Signal
        flopocoOutputVHDLSignal = self.__generateFlopocoOutputVHDLSignal()
        # add the flopoco OutputVHDL Signal to the vhdl Signals array
        self.vhdlOutputSignals.append(flopocoOutputVHDLSignal)
        # generate the flopocoConverterInstance for output
        outputFlopocoConverterInstance = self.__generateOutputFlopocoToIEEENumberSystemConverterInstance()
        # add the flopocoOutputConverter  to the instances
        self.vhdlOutputConverterInstances.append(outputFlopocoConverterInstance)

            
    """
    # End: flopocoOutputName setters and getters
    """
    
    """
    # Start: lutOutputName setters and getters
    """
    
    @property
    def lutOutputName(self):
        return self._lutOutputName
    
    
    @lutOutputName.setter  
    def lutOutputName(self,value):
        # set the flopoco output name
        self._lutOutputName = value
        # generate the lut output Signal
        lutOutputVHDLSignal = self.__generateLUTOutputVHDLSignal()
        # add the flopoco OutputVHDL Signal to the vhdl Signals array
        self.vhdlOutputSignals.append(lutOutputVHDLSignal)

    """
    # End: lutOutputName setters and getters
    """


    """
    # Start: flopocoInput1Name setters and getters
    """
    
    @property
    def flopocoInput1Name(self):
        return self._flopocoInput1Name
    
    
    @flopocoInput1Name.setter  
    def flopocoInput1Name(self,value):
        # set the value to the Flopoco input1 port name
        self._flopocoInput1Name = value
        # generate the flopocoInput1Port Signal
        vhdlSignal = self.__generateFlopocoInput1VHDLSignal()
        # add the signal to the vhdl input signals
        self.vhdlInputSignals.append(vhdlSignal)
        # generate the input1PortIEEE to Flopoco Converter
        input1FlopocoConverter = self.__generateInput1IEEEToFlopocoNumberSystemConverterInstance()
        # add the flopocoConver to the converter instances array
        self.vhdlInputConverterInstances.append(input1FlopocoConverter)
            
    """
    # End: flopocoInput1Name setters and getters
    """
    
    """
    # Start: flopocoInput2Name setters and getters
    """
    
    @property
    def flopocoInput2Name(self):
        return self._flopocoInput2Name
    
    
    @flopocoInput2Name.setter  
    def flopocoInput2Name(self,value):
        # set the value to the Flopoco input1 port name
        self._flopocoInput2Name = value
        # generate the flopocoInput1Port Signal
        vhdlSignal = self.__generateFlopocoInput2VHDLSignal()
        # add the signal to the vhdl input signals
        self.vhdlInputSignals.append(vhdlSignal)
        # generate the input1PortIEEE to Flopoco Converter
        input2FlopocoConverter = self.__generateInput2IEEEToFlopocoNumberSystemConverterInstance()
        # add the flopocoConver to the converter instances array
        self.vhdlInputConverterInstances.append(input2FlopocoConverter)

            
    """
    # End: flopocoInput2Name setters and getters
    """
    
    """
    # Start: LUTInput1Name setters and getters
    """
    
    @property
    def lutInput1Name(self):
        return self._lutInput1Name
    
    
    @lutInput1Name.setter  
    def lutInput1Name(self,value):
        # store the original input1 name
        self._lutInput1Name = value
        # set the value to the Flopoco input1 port name
        self.lutOutputName = value + "LUT" + str(self.number) + "Output"
        # generate the input1FromLUT instance
        input1LUTInstance = self.__generateInput1LUTInstance()
        # add the input1LUTInstance to the LUT instances array
        self.vhdlInputLUTInstances.append(input1LUTInstance)
            
    """
    # End: lutInput1Name setters and getters
    """
    
    """
    # Start: LUTInput2Name setters and getters
    """
    
    @property
    def lutInput2Name(self):
        return self._lutInput2Name
    
    
    @lutInput2Name.setter  
    def lutInput2Name(self,value):
        # store the original input2 name
        self._lutInput2Name = value
        # set the value to the Flopoco input1 port name
        self.lutOutputName = value + "LUT" + str(self.number) + "Output"
        # generate the input2LUT instance
        input2LUTInstance = self.__generateInput2LUTInstance()
        # add the lutInstance to the input LUT instances array
        self.vhdlInputLUTInstances.append(input2LUTInstance)
            
    """
    # End: lutInput2Name setters and getters
    """

    def __generateProductNodeVHDLDescription(self):
        # check the numberSystem
        if self.numberSystem == 0:
            self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + self.fixedPCSystemVHDLLibrariesSyntax + "\n"
        elif self.numberSystem == 1:
            self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + self.floatPCSystemVHDLLibrariesSyntax + "\n"

        # first line of the productnode entity desecribing the ports
        self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "entity" + " " + self.name + " " + "is" + "\n"
        
        # add the space before the ports
        self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "\n"

        # add generic
        if self.numberSystem == 1:
            # add generic
            self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "generic(mantissaBits: integer :=" +str( self.mantissaBits) + ";" + "exponentBits: integer :=" + str(self.exponentBits) +")" + "\n"
        elif self.numberSystem == 0:
            # add generic
            self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "generic(numberOfBits: integer :=" + str(self.numberOfBits) + ")" + "\n"

        # port line of the inputPortsVHDLSyntax
        self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "port(\n"
        
        # loop through all the inputports of the mmacUnit
        for port in self.inputPorts:
            # port line of the inputPortsVHDLSyntax
            self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + port.vhdlPort + ";" + "\n"
        
        self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + self.outputPort.vhdlOutputPort + "\n" + ")" + ";" + "\n \n"
        self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "end" +  " " + self.name + ";" + "\n \n"
        
        
    """
    # Start: __generateProductNodeArchitectureVHDLDescription function
    """
    
    def __generateProductNodeArchitectureVHDLDescription(self):
        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "architecture rtl of" + " " + self.name + " is \n \n"

        print("The number system of ProductNode", self.numberSystem)
        if self.numberSystem == 0:
            self.architectureVHDLSyntax = self.architectureVHDLSyntax + self.tempOutputSignalVHDLSyntax
               
        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "\n"
        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "begin \n \n"

        if self.numberSystem == 1:
            multiplication = str()
            for index, port in enumerate(self.inputPorts):
                if index == (len(self.inputPorts) -1):
                    multiplication = multiplication + port.name 
                else:
                    multiplication = port.name + "*" + multiplication
            
            self.architectureVHDLSyntax = self.architectureVHDLSyntax + self.outputPort.name + "<=" + multiplication + ";" + "\n \n"
            # append the end architecture syntax
            self.architectureVHDLSyntax = self.architectureVHDLSyntax + "end architecture" + ";" + "\n"
        elif self.numberSystem == 0:
            multiplication = str()
            for index, port in enumerate(self.inputPorts):
                if index == (len(self.inputPorts) -1):
                    multiplication = multiplication + port.name 
                else:
                    multiplication = port.name + "*" + multiplication

            self.architectureVHDLSyntax = self.architectureVHDLSyntax + "tempOutput" + "<=" + multiplication + ";" + "\n \n"
            self.architectureVHDLSyntax = self.architectureVHDLSyntax + self.outputPort.name + "(0 downto (1-numberOfBits))" + "<=" + "tempOutput" + "(0 downto (1-numberOfBits))" + ";" + "\n \n"
            # append the end architecture syntax
            self.architectureVHDLSyntax = self.architectureVHDLSyntax + "end architecture" + ";" + "\n"

    """
    # End: __generateProductNodeArchitectureVHDLDescription function
    """
    
    
    """
    # Start: performProductNodeVHDLHWDescriptionGeneration function
    """

    def performProductNodeVHDLHWDescriptionGeneration(self):
        # generate ProductNode VHDL Description
        self.__generateProductNodeVHDLDescription()
        # generate SumNode VHDL Description with the set input and output ports
        self.__generateProductNodeArchitectureVHDLDescription()
        self.vhdlDescription = self.inputPortsVHDLSyntax + self.architectureVHDLSyntax
        # print the VHDL Description of the productNode
        print("The VHDL Description of the ProductNode", self.vhdlDescription)
        
    """
    # End: performProductNodeVHDLHWDescriptionGeneration function
    """
    
    """
    # Start: __generateFlopocoInput1VHDLSignal function
    """

    def __generateFlopocoInput1VHDLSignal(self):
        return ("SIGNAL" + " " + self.flopocoInput1Name + ":" + "std_logic_vector" + "(" + "(" + "extraFlopocoBits" \
                    + "+" + "(" + "mantissaBits-1" + ")" + "+" + "exponentBits" + ")" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n")          
                                                
    """
    # End: __generateFlopocoInput1VHDLSignal function
    """

    
    """
    # Start: __generateFlopocoInput2VHDLSignal function
    """

    def __generateFlopocoInput2VHDLSignal(self):
        return ("SIGNAL" + " " + self.flopocoInput2Name + ":" + "std_logic_vector" + "(" + "(" + "extraFlopocoBits" \
                    + "+" + "(" + "mantissaBits-1" + ")" + "+" + "exponentBits" + ")" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n")          
                                                
    """
    # End: __generateFlopocoInput2VHDLSignal function
    """
    
    """
    # Start: __generateLUTInput1VHDLSignal function
    """

    def __generateLUTInput1VHDLSignal(self):
        if self.numberSystem == 1:
            return ("SIGNAL" + " " + self.lutInput1Name + ":" + "std_logic_vector" + "(" + "numberOfBits-1" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n")
        elif self.numberSystem == 2:
            #if self.frequency > 0:
            return ("SIGNAL" + " " + self.lutInput1Name + ":" + "std_logic_vector" + "(" + "numberOfBits-1" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n")

                                                
    """
    # End: __generateLUTInput1VHDLSignal function
    """
    
    """
    # Start: __generateLUTInput2VHDLSignal function
    """

    def __generateLUTInput2VHDLSignal(self):
        if self.numberSystem == 1:
            return ("SIGNAL" + " " + self.lutInput2Name + ":" + "std_logic_vector" + "(" + "numberOfBits-1" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n")
        elif self.numberSystem == 2:
            #if self.frequency > 0:
            return ("SIGNAL" + " " + self.lutInput2Name + ":" + "std_logic_vector" + "(" + "numberOfBits-1" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n")


                                                
    """
    # End: __generateLUTInput2VHDLSignal function
    """



    """
    #Start: __generateFlopocoWeightVHDLSignal
    """

    def __generateFlopocoWeightVHDLSignal(self):
        flopocoWeightVHDLSignal = ("Signal" + " " + self.flopocoWeightName \
                                               + " " + ":" + " " + "std_logic_vector" \
                                               + "(" + "(" + "extraFlopocoBits" + "+" + "(" + "mantissaBits-1" \
                                               + ")" + "+" "exponentBits" + ")" + " " + "DOWNTO" \
                                               + " " + "0" \
                                               + ")" \
                                               + ";" + "\n")
                   
        #print("VHDL Weight Signal:", self._vhdlWeightSignal)
        return flopocoWeightVHDLSignal
        
    """
    #End: __generateFlopocoWeightVHDLSignal
    """
    
    
    """
    #Start: __generateFlopocoOutputVHDLSignal
    """

    def __generateFlopocoOutputVHDLSignal(self):
        flopocoOutputVHDLSignal = ("Signal" + " " + self.flopocoOutputName \
                                               + " " + ":" + " " + "std_logic_vector" \
                                               + " " + "(" + "(" + "extraFlopocoBits" + "+" + "(" + "mantissaBits-1" \
                                               + ")" + "+" "exponentBits" + ")" + "DOWNTO" \
                                               + " " + "0" \
                                               + " " + ")" \
                                               + ";" + "\n")
        return flopocoOutputVHDLSignal
                   
        #print("VHDL Weight Signal:", self._vhdlWeightSignal)
        
    """
    #End: __generateFlopocoOutputVHDLSignal
    """
    
    """
    #Start: __generateLUTOutputVHDLSignal
    """

    def __generateLUTOutputVHDLSignal(self):
        lutOutputVHDLSignal = None
        if self.numberSystem == 1:
            lutOutputVHDLSignal = ("Signal" + " " + self.lutOutputName \
                                               + " " + ":" + " " + "std_logic_vector" \
                                               + " " + "(" + "numberOfBits-1" + " " + "DOWNTO" \
                                               + " " + "0" \
                                               + " " + ")" \
                                               + ";" + "\n")
        elif self.numberSystem == 2:
            lutOutputVHDLSignal = ("Signal" + " " + self.lutOutputName \
                                               + " " + ":" + " " + "std_logic_vector" \
                                               + " " + "(" + "numberOfBits-1" + " " + "DOWNTO" \
                                               + " " + "0" \
                                               + " " + ")" \
                                               + ";" + "\n")

        return lutOutputVHDLSignal
                   
        #print("VHDL Weight Signal:", self._vhdlWeightSignal)
        
    """
    #End: __generateLUTOutputVHDLSignal
    """

    
    """
    # Start: __generateWeightIEEEToFlopocoNumberSystemConverterInstance function
    """
    
    def __generateWeightIEEEToFlopocoNumberSystemConverterInstance(self):
        # append the string 
        flopocoWeightConverterInstance = (self.flopocoWeightName + str(self.number) + ":" + " " + "entity work" + "." \
                                                + "InputIEEE" + "_" + str(self.exponentBits) + "_" + str(self.mantissaBits-1) \
                                                + "_" + "to" + "_" + str(self.exponentBits) \
                                                + "_" + str(self.mantissaBits-1) + "(" + "arch" + ")" + "\n" + "port map" + "("\
                                                + self._weightName \
                                                + "," + self.flopocoWeightName + ")" + ";" + "\n \n")
        
        return flopocoWeightConverterInstance

        #print("VHDL Port:", self._vhdlPort)
        
    """
     # End: __generateWeightIEEEToFlopocoNumberSystemConverterInstance function
    """
    
    """
    # Start: __generateOutputFlopocoToIEEENumberSystemConverterInstance function
    """
    
    def __generateOutputFlopocoToIEEENumberSystemConverterInstance(self):
        # append the string 
        flopocoOutputConverterInstance = (self.flopocoOutputName + str(self.number) + ":" + " " + "entity work" + "." \
                                                + "OutputIEEE" + "_" + str(self.exponentBits) + "_" + str(self.mantissaBits-1) \
                                                + "_" + "to" + "_" + str(self.exponentBits) \
                                                + "_" + str(self.mantissaBits-1) + "(" + "arch" + ")" + "\n" + "port map" + "("\
                                                + self.flopocoOutputName \
                                                + "," + self.outputName + ")" + ";" +"\n \n")

        return flopocoOutputConverterInstance
       

        #print("VHDL Port:", self._vhdlPort)
        
    """
     # End: __generateOutputFlopocoToIEEENumberSystemConverterInstance function
    """
    
    """
    # Start: __generateInput1IEEEToFlopocoNumberSystemConverterInstance function
    """
    
    def __generateInput1IEEEToFlopocoNumberSystemConverterInstance(self):
        # append the string 
        flopocoInput1ConverterInstance = (self.flopocoInput1Name + str(self.number) + ":" + " " + "entity work" + "." \
                                                + "InputIEEE" + "_" + str(self.exponentBits) + "_" + str(self.mantissaBits-1) \
                                                + "_" + "to" + "_" + str(self.exponentBits) \
                                                + "_" + str(self.mantissaBits-1) + "(" + "arch" + ")" + "\n" + "port map" + "(" \
                                                + self.flopocoInput1Name \
                                                + "," + self.flopocoInput1Name + ")" + ";" +"\n \n")
        return flopocoInput1ConverterInstance
        #print("VHDL Port:", self._vhdlPort)
        
    """
     # End: __generateInput1ToFlopocoPortConverterVHDLPortInstance function
    """
    
    """
    # Start: __generateInput2IEEEToFlopocoNumberSystemConverterInstance function
    """
    
    def __generateInput2IEEEToFlopocoNumberSystemConverterInstance(self):
        # append the string 
        flopocoInput2ConverterInstance = (self.flopocoInput2Name + str(self.number) + ":" + " " + "entity work" + "." \
                                                + "InputIEEE" + "_" + str(self.exponentBits) + "_" + str(self.mantissaBits-1) \
                                                + "_" + "to" + "_" + str(self.exponentBits) \
                                                + "_" + str(self.mantissaBits-1) + "(" + "arch" + ")" + "\n" + "port map" + "("\
                                                + self.flopocoInput2Name \
                                                + "," + self.flopocoInput2Name + ")" + ";" + "\n \n")
        
        return flopocoInput2ConverterInstance
        #print("VHDL Port:", self._vhdlPort)
        
    """
     # End: __generateInput2IEEEToFlopocoNumberSystemConverterInstance function
    """
    
    """
    # Start: __generateInput1LUTInstance function
    """
    
    def __generateInput1LUTInstance(self):
        lutInput1Instance = None
        if self.numberSystem == 1:
            # append the string
            lutInput1Instance = (self.lutInput1Name + str(self.number) + ":" + " " + "entity work" + "." \
                                                + "FloatLUT" + "(" + "rtl" + ")" + "\n"  \
                                                + "generic map" + "(" + "numberOfBits"+ "," + "mantissaBits" + "," + "exponentBits" +")"+ "\n" \
                                                + "port map" + "(" + self.lutInput1Name + "," + "clk" + "," \
                                                + "rst" + "," + self.lutOutputName + ")" + ";" +"\n \n")
        elif self.numberSystem == 2:
            # append the string 
            lutInput1Instance = ("productNodeLUTInput1_" + str(self.number) + ":" + " " + "entity work" + "." \
                                                + "PositLUT" \
                                                + "(" + "rtl" + ")" + "\n" + "generic map" \
                                                + "(" + "numberOfBits" + ")" + "\n" + "port map" + "(" + self.lutInput1Name + "," + "clk" + "," \
                                                + "rst" \
                                                + "," + self.lutOutputName + ")" + ";" +"\n \n")

        return lutInput1Instance
        #print("VHDL Port:", self._vhdlPort)
        
    """
     # End: __generateInput1LUTInstance function
    """
    
    """
    # Start: __generateInput2LUTInstance function
    """
    
    def __generateInput2LUTInstance(self):
        lutInput2Instance = None
        if self.numberSystem == 1:
            # append the string 
            lutInput2Instance = (self.lutInput2Name + str(self.number) + ":" + " " + "entity work" + "." \
                                                + "FloatLUT" + "(" + "arch" + ")" + "\n" \
                                                + "generic map" + "(" + "numberOfBits"+ "," + "mantissaBits" + "," + "exponentBits" +")" + "\n" \
                                                + "port map" + "(" + self.lutInput2Name + "," + "clk" + "," \
                                                + "rst" \
                                                + "," + self.lutOutputName + ")" + ";" +"\n \n")
        elif self.numberSystem == 2:
            # append the string 
            lutInput2Instance = ("productNodeLUTInput2_" + str(self.number) + ":" + " " + "entity work" + "." \
                                                + "PositLUT" \
                                                + "(" + "rtl" + ")" + "\n" + "generic map" \
                                                + "(" + "numberOfBits" + ")" + "\n" + "port map" + "(" + self.lutInput2Name + "," + "clk" + "," \
                                                + "rst" \
                                                + "," + self.lutOutputName + ")" + ";" +"\n \n")

        return lutInput2Instance
        #print("VHDL Port:", self._vhdlPort)
        
    """
     # End: __generateInput2LUTInstance function
    """


    
    """
    # Start: __generateFlopocoVHDLInstance function
    """

    def __generateFlopocoVHDLInstance(self):
        return (self.name + str(self.number) + ":" + " " +"entity work"+"." \
                        + self.customName +"("+"arch"+")" "\n" \
                        + "\n" + "port map" + "(" + self.flopocoInput1Name + "," \
                        + self.flopocoInput2Name + ","+ self.flopocoOutputName +")" + ";" + "\n" + "\n")



    """
    # End: __generateFlopocoVHDLInstance function
    """

    """
    # Start: Configure 
    """
    def configure(self):
        # variable to store the temporary output signal
        self._tempOutputSignalVHDLSyntax = None
        # variable to store the inputPortsVHDLSyntax
        self.inputPortsVHDLSyntax = str()
        # variable to store the productNode syntax
        self.architectureVHDLSyntax = str()
        # variable to store the productNode property
        self.name = None
        # variable to store the productNode port
        self.outputPort = None
        # variable to store the number system of the MMACUnit
        self.numberSystem = None
        # variable to store the productNode VHDL Description
        self.vhdlDescription = str()
        # variable to store the productnode property number to identify it uniquely
        self.number = None
        # variable to store the custom name of the product node
        self.customName = None
        # variable to store the productNode port
        self.outputPort = None
        # store the original weight name
        self._weightName = None
        # property to generate flopoco weight of the productNode
        self._flopocoWeightName = None
        # variable to store the vhdlInput Signals
        self.vhdlInputSignals = None
        # variable to store the vhdlOutputSignals
        self.vhdlOutputSignals = None
        # variable to store the vhdlInputConverterInstances
        self.vhdlInputConverterInstances = None
        # variable to store the vhdlOutputConverterInstances
        self.vhdlOutputConverterInstances = None
        self.vhdlInputLUTInstances = None
        # store the original input1 name
        self._input1Name = None
        # to store the flopoco InputPort1 Name
        self._flopocoInput1Name = None
        # store the original input2 name
        self._input2Name = None
        # to store the flopoco InputPort2 Name
        self._flopocoInput2Name = None
        # to store the second input lut input Name
        self._lutInput2Name = None
        # to store the first input lut input Name
        self._lutInput1Name = None
        # store the original output name
        self.outputName = None
        # to store the flopoco Output Name
        self._flopocoOutputName = None
        self._lutOutputName = None
        # variable to store the productNode VHDL Description
        self.vhdlDescription = str()
        # variable to store the flopocoVHDLInstance
        self._flopocoVHDLInstance = None
        # productNode ports 
        # when the productNode ports are set, it will generate the entity ports VHDL Description of the productNode
        self.inputPorts = None


    """
    # End: Configure
    """
    
    """
    # Start: Reset 
    """
    def reset(self):
        # variable to store the temporary output signal
        self._tempOutputSignalVHDLSyntax = None
        # variable to store the inputPortsVHDLSyntax
        self.inputPortsVHDLSyntax = str()
        # variable to store the productNode syntax
        self.architectureVHDLSyntax = str()
        # variable to store the mmacUnit property
        self.name = None
        # variable to store the mmacUnitOutput port
        self.outputPort = None
        # variable to store the number system of the MMACUnit
        self.numberSystem = None
        # variable to store the productNode VHDL Description
        self.vhdlDescription = str()
        # mmacUnit ports 
        # when the mmacUnit ports is set, it will generate the entity ports VHDL Description of the MMACUnit
        # variable to store the product property
        self.name = None
        # variable to store the productnode property number to identify it uniquely
        self.number = None
        # custom name
        self.customName = None
        # variable to store the mmacUnitOutput port
        self.outputPort = None
        # variable to store the number system of the productNode
        self.numberSystem = None
        # store the original weight name
        self._weightName = None
        # property to generate flopoco weight of the productNode
        self._flopocoWeightName = None
        # variable to store the productNode VHDL Description
        self.vhdlDescription = str()
        # variable to store the flopocoVHDLInstance
        self._flopocoVHDLInstance = None
        # variable to store the vhdlInput Signals
        self.vhdlInputSignals = None
        # variable to store the vhdlOutputSignals
        self.vhdlOutputSignals = None
        # variable to store the vhdlInputConverterInstances
        self.vhdlInputConverterInstances = None
        # variable to store the vhdlOutputConverterInstances
        self.vhdlOutputConverterInstances = None
        self.vhdlInputLUTInstances = None
        # store the original input1 name
        self._input1Name = None
        # to store the flopoco InputPort1 Name
        self._flopocoInputPort1Name = None
        # store the original input2 name
        self._input2Name = None
        # to store the flopoco InputPort2 Name
        self._flopocoInputPort2Name = None
        # store the original output name
        self.outputName = None
        # to store the flopoco Output Name
        self._flopocoOutputName = None
        self._lutOutputName = None
        # the inputs of the Product Node (for now it is not useful)
        #TODO in the next version of the AutoPC the system design will be corrected
        self.inputPorts = None

    """
    # End: Reset
    """


    def main(self):
        pass
    
    def run(self):
        pass


        

