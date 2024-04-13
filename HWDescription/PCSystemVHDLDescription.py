#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:17:30 2022

@author: Karthekeyan Periasamy
"""

from HWDescription.PCSystemHWDescription import PCSystemHWDescription

class PCSystemVHDLDescription(PCSystemHWDescription):
    
    def __init__(self):
        super().__init__()
        self.configure()


    """
    # Start: __generatePCSystemPortsVHDLDescription function
    """

    def __generatePCSystemPortsVHDLDescription(self):
        # check the numberSystem
        if self.numberSystem == 0:
            self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + self.fixedPCSystemVHDLLibrariesSyntax + "\n"
        elif self.numberSystem == 1:
            self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + self.floatPCSystemVHDLLibrariesSyntax + "\n"
        elif self.numberSystem == 2:
            self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + self.positPCSystemVHDLLibrariesSyntax + "\n"

        # first line of the MMACUnit entity desecribing the ports
        self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "entity" + " " + self.name + " " + "is" + "\n"
        
        # add the space before the ports
        self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "\n"
        
        if self.numberSystem == 1:
            # add generic
            self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "generic(mantissaBits: integer :=" +str( self.mantissaBits) + ";" + "exponentBits: integer :=" + str(self.exponentBits) +")" + "\n"
        else:
            # add generic
            self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "generic(numberOfBits: integer :=" + str(self.numberOfBits) + ")" + "\n"

        # port line of the pcSystemInputPortsVHDLSyntax
        self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "port(\n"
        
        # loop through all the inputports of the mmacUnit
        for port in self.inputPorts:
            # port line of the inputPortsVHDLSyntax
            self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + port.vhdlPort + ";" + "\n"
        
        self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + self.outputPort.vhdlOutputPort + "\n" + ")" + ";" + "\n \n"
        self.inputPortsVHDLSyntax = self.inputPortsVHDLSyntax + "end" +  " " + self.name + ";" + "\n \n"
        
    """
    # End: __generatePCSystemPortsVHDLDescription function
    """

    """
    # Start: __generatePCSystemWithMMACUnitsArchitectureVHDLDescription function
    """
    
    def __generatePCSystemWithMMACUnitsArchitectureVHDLDescription(self):
        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "architecture rtl of" + " " + self.name + " is \n \n"
        
        #for mmacUnit in self.mmacUnits:
            # set the outputsignal of each mmacUnit
            #self.architectureVHDLSyntax = self.architectureVHDLSyntax + mmacUnit.vhdlOutputSignal
            
        # new mmacunit model output signals needs to be accessed differently
        for mmacUnit in self.mmacUnits:
            # set the outputsignal of each mmacUnit 
            for vhdlOutputSignal in mmacUnit.hwDescription.vhdlEntityArchitectureDescription.vhdlOutputSignals:
                self.architectureVHDLSyntax = self.architectureVHDLSyntax + vhdlOutputSignal

        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "\n"
        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "begin \n \n"
        
        for mmacUnit in self.mmacUnits:
            self.architectureVHDLSyntax = self.architectureVHDLSyntax + mmacUnit.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition

        arithmeticNode = self.mmacUnits[len(self.mmacUnits)-1]

        #finalOutput = arithmeticNode.output
        
        # changed the outputports access for new mmacunits
        finalOutput = arithmeticNode.outputPorts[0]
        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "vout <= " + finalOutput.name + ";" + "\n \n"

        #self.architectureVHDLSyntax = self.architectureVHDLSyntax + "vout <= " + finalOutput + ";" + "\n \n"
        
        # append the end architecture syntax
        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "end architecture" + ";" + "\n"    
    
    """
    # End: __generatePCSystemWithMMACUnitsArchitectureVHDLDescription function
    """
    
    """
    # Start: __generatePCSystemWithArithmeticNodesArchitectureVHDLDescription function
    """
    
    def __generatePCSystemWithArithmeticNodesArchitectureVHDLDescription(self):
        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "architecture rtl of" + " " + self.name + " is \n \n"
        
        for arithmeticNode in self.arithmeticNodes:
            if isinstance(arithmeticNode, SumNode):
                if self.numberSystem == 2:
                    self.pcSystemSumNodeName = arithmeticNode.customName
                else:
                    self.pcSystemSumNodeName = arithmeticNode.name

            if isinstance(arithmeticNode, ProductNode):
                if self.numberSystem == 2:
                    self.pcSystemProductNodeName = arithmeticNode.customName
                else:
                    self.pcSystemProductNodeName = arithmeticNode.name

                if (arithmeticNode.vhdlWeightSignal != None):
                    self.architectureVHDLSyntax = self.architectureVHDLSyntax + arithmeticNode.vhdlWeightSignal

            self.architectureVHDLSyntax = self.architectureVHDLSyntax + arithmeticNode.vhdlOutputSignal

        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "\n"
        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "begin \n \n"
        
        for arithmeticNode in self.arithmeticNodes:
            self.architectureVHDLSyntax = self.architectureVHDLSyntax + arithmeticNode.vhdlInstance
        

        arithmeticNode = self.arithmeticNodes[len(self.arithmeticNodes)-1]
        finalOutput = arithmeticNode.output
        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "vout <= " + finalOutput + ";" + "\n \n"
        
        # append the end architecture syntax
        self.architectureVHDLSyntax = self.architectureVHDLSyntax + "end architecture" + ";" + "\n"    
    """
    # End: __generatePCSystemWithArithmeticNodesArchitectureVHDLDescription function
    """

    
    
    """
    # Start: performMMACUnitVHDLHWDescriptionGeneration function
    """

    def performPCSystemVHDLHWDescriptionGeneration(self):
        # generate PCSystem port VHDL Description with the set input ports
        self.__generatePCSystemPortsVHDLDescription()
        #print("PCSystem VHDL Description", self.inputPortsVHDLSyntax)
        if self.operationMode == 1:
            # generate arithmeticNode based PCSystem VHDL
            self.__generatePCSystemWithArithmeticNodesArchitectureVHDLDescription()
            self.vhdlDescription = self.inputPortsVHDLSyntax + self.architectureVHDLSyntax

        elif self.operationMode == 2:
            # generate mmacUnit based PCSystem VHDL
            self.__generatePCSystemWithMMACUnitsArchitectureVHDLDescription()
            self.vhdlDescription = self.inputPortsVHDLSyntax + self.architectureVHDLSyntax
            #print("PCSystem VHDL Description", self.vhdlDescription)
            
        return self.vhdlDescription
        
    """
    # End: performMMACUnitVHDLHWDescriptionGeneration function
    """

    def configure(self):
        self.name = None
        self.arithmeticNodes = None
        self.mmacUnits = None
    
    def reset(self):
        # variable to store the pcSystemInputPortsVHDLSyntax
        self.inputPortsVHDLSyntax = None
        # variable to store the mmacUnitsArchitecture syntax
        self.architectureVHDLSyntax = None
        # variable to store the mmacUnit property
        self.name = None
        # variable to store the mmacUnitOutput port
        self.outputPort = None
        # variable to store the number system of the MMACUnit
        self.numberSystem = None
        # variable to store the mmacUnit VHDL Description
        self.vhdlDescription = None
        # input ports 
        self.inputPorts = None


    def main(self):
        super().main()
        pass
    
    def run(self):
        self.main()
        pass


        

