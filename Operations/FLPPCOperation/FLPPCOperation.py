#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:09:37 2022

@author: Karthekeyan Periasamy
"""

from Operations.EquationParser.EquationParser import EquationParser
from Operators.Multipliers.FLPMultiplier.FLPMultiplier import FLPMultiplier
from Operators.Adders.FLPAdder.FLPAdder import FLPAdder
import re



def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)',text)]



class FLPPCOperation(EquationParser):

        
    def __init__(self):
        super().__init__()
        self.connect()
        
           
    @property
    def operationFrequency(self):
        if self._operationFrequency == None:
            self._operationFrequency = 400
        return self._operationFrequency

    @operationFrequency.setter
    def operationFrequency(self,value):
        self._operationFrequency = value
   
   
    @property
    def numberOfBits(self):
        if self._numberOfBits == None:
            self._numberOfBits = self.mantissaBits + self.exponentBits
        return self._numberOfBits

    @numberOfBits.setter
    def numberOfBits(self,value):
        self._numberOfBits = value
    

    def connectProperties(self):
        # the equation upon which the FLPPCOperation is performed
        self.equation = None
        # the mantissa bits required for the FLPPCOperation
        self.mantissaBits = 0
        # the exponentBits required for the FLPOperation
        self.exponentBits = 0
        # initialise the new property to store multipliers
        self.multipliers = list()
        # new property to store the adders
        self.adders = list()
        # new property to store both the arithmetic nodes
        self.arithmeticNodes = list()
        # new property to store the FLPPCOperation ports that is extracted from the arithmeticNodes of the FLPPC
        self.operationPorts = list()
        # new property to store the system port names
        self.arithmeticNodesPortNames = dict()
        # new property to store the equation of an arithmetic node along with the arithmeticNode index
        self.equationsOfArithmeticNodesWithDetails = dict()
        # property to store the operation Frequency
        self._operationFrequency = None
        # property to store the configuration details
        self.configurationDetailsOfOperation = None
        # property to store the number of bits
        self._numberOfBits = 0
        # property to the computation equation of every arithemeticnode
        self.equationsOfArithmeticNodes = dict()
        # property to store the arithmetic node duplicates
        self.arithmeticNodeIndicesWithTheirDuplicatesIndices = dict()
        # property to store the duplicate arithmeticNodes and its child arithmeticNodes
        self.duplicatesOfArithmeticNodesWithTheirReceiverIndices = dict()
        # property to store the equation with original arithmeticNodes and its duplicates (without drivers)
        self.equationsOfArithmeticNodesWithDetails = dict()

    """
    #Start - configure PCOperation
    """
    def configure(self):
        configurationDetails = self.configurationDetailsOfOperation

        if "Frequency" in configurationDetails:
            self.operationFrequency = configurationDetails["Frequency"]
        if "Equation" in configurationDetails:
            self.equation = configurationDetails["Equation"]
            
        if "MantissaBits" in configurationDetails:
            self.mantissaBits = configurationDetails["MantissaBits"]
        
        if "ExponentBits" in configurationDetails:
            self.exponentBits = configurationDetails["ExponentBits"]
        
        if "NumberOfBits" in configurationDetails:
            self.numberOfBits = configurationDetails["NumberOfBits"]

    """
    #End - configure PCOperation
    """

    def connect(self):
        self.connectProperties()

    """
    # Start: performOperation function
    ===================================
    # 1. Override the function of parent class to support generation of ProductNode and SumNode objects while parsing the equation
    ===================================
    """
    
    def performOperation(self):
        # check the length of the operandValueStack
        operandValueStackLength = len(self.operandValueStack)
        # if the length of the operandValueStack is less than 2
        if (operandValueStackLength < 2):
            # abort the operation as operandValues are not enough to perfom operation
            return False
        # print the operator
        #print("The operator: \n", self.currentOperator)
        # set the number of operations to number of operators
        numberOfOperators = self.currentNumberOfOperators
        #print("NumberOfOperators: \n", numberOfOperators)
        # make the startrange, stop range to access the required number of operandValues
        numberOfOperandValuesToBeAccessed = numberOfOperators + 1
        #print("NumberOfOperandValuesToBeAccessed: \n", numberOfOperandValuesToBeAccessed)
        # print the stack of the operandValueStack
        #print("OriginalOperandValueStack \n",self.operandValueStack)
        # design the start range for the for loop
        startRange = (len(self.operandValueStack)-1)
        #print("The start range \n",startRange)
        # design the stop range for the loop
        operandValueLength = (len(self.operandValueStack))
        # the stop range for the for loop to access the operandValueStack
        stopRange = ((operandValueLength - numberOfOperandValuesToBeAccessed) - 1)
        #print("The stop range \n",stopRange)
                              
        # append the existing elements of the operandElementStack
        # as its a stack LIFO retreival scheme should be followed to correctly represent the operandValues
        # also, the operandValues are the one available for this closed and opening brackets to be computed
        operationValue = None
        for indexOfOperandValue in range(startRange,stopRange,-1):
            # access and set again the relevant operator for the whole range
            # It helps support multiple type of operations
            # print the indexOfOperangValue
            #print("The index of  operand value : \n", indexOfOperandValue)
            # access the operandValue using the index
            operandValue = self.operandValueStack[indexOfOperandValue]
            # print the indexOfOperandElement and operandElement
            #print("IndexOfOperandValue , OperandValue: \n", indexOfOperandValue, operandValue)
            # check the indexOfOperandValue, if its top element index we need to set the operandValue with the firstElement
            if indexOfOperandValue == (len(self.operandValueStack)-1):
                operationValue = operandValue
                # print the updated operationValue
                #print( "The updated operationValue: ", operationValue)
            else:
                # Then check the operator, for now two operations are supported
                # 1. Multiplication 
                # 2. Addition
                if self.currentOperator is self.multiplicationOperator:
                    # check whether the zeroth index of the operationValue or the operandValue is having its first letter as "v"
                    # If the operationValue or the operandValue has first letter as v, it means that it is a port
                    # Then, form a port object
                    # do multiplication

                    # intialise the new FLPMultiplier
                    flpMultiplier = FLPMultiplier()
                    flpMultiplier.configurationDetailsOfOperator = {"Name":"Multiplier","Frequency":self.operationFrequency,"NumberSystem":"Float","Number":len(self.multipliers),"ArithmeticNodeNumber":len(self.arithmeticNodes),"MantissaBits":self.mantissaBits,"ExponentBits":self.exponentBits,"NumberOfBits":self.numberOfBits,"Multiplicand":operationValue, "Multiplier":operandValue,"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.operationFrequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}}
                    # configure the flpMultiplier
                    flpMultiplier.configure()
                    # process the flpMultiplier
                    flpMultiplier.process()
                    # perform the flpMultiplier
                    flpMultiplier.perform()
                    
                    operationValue = flpMultiplier.product


                    if len(flpMultiplier.swMultiplier.drivers) > 1:

                        driverEquations = list()
                        multiplicandDriver = flpMultiplier.swMultiplier.driversInfo[flpMultiplier.multiplicand]
                        # access the multiplicanddriver info
                        multiplicandDriverIndex = multiplicandDriver.info[flpMultiplier.multiplicand]
                        #print("MultiplicandDriver Index", multiplicandDriverIndex)
                        # access the driver from arithmetic nodes
                        flpMultiplierMultiplicandDriver = self.arithmeticNodes[int(multiplicandDriverIndex)]
                        
                        # access the flpMultiplier multiplicand driver
                        driverEquations.append(flpMultiplierMultiplicandDriver.equation)
                        
                        multiplierDriver = flpMultiplier.swMultiplier.driversInfo[flpMultiplier.multiplier]
                        # access the multiplicanddriver info
                        multiplierDriverIndex = multiplierDriver.info[flpMultiplier.multiplier]
                        #print("MultiplierDriver Index", multiplicandDriverIndex)
                        # access the driver from arithmetic nodes
                        flpMultiplierMultiplierDriver = self.arithmeticNodes[int(multiplierDriverIndex)]
                        
                        
                        # access the product node input2 driver
                        driverEquations.append(flpMultiplierMultiplierDriver.equation)
                        #print("DriverEquations", driverEquations)
                        # set the flpMultiplier driver equations
                        flpMultiplier.swMultiplier.driverEquations = driverEquations
                        #print("FLPMultiplier DriverEquations", flpMultiplier.swMultiplier.driverEquations)

                        
                        if flpMultiplier.equation in self.equationsOfArithmeticNodes:
                            # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                            equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]
                            if "Duplicate" not in equationParentAndChildren:
                                #print("Duplicate Node Equation", flpMultiplier.equation)
                                #print("Duplicate Node ArithmeticNodeNumber", flpMultiplier.arithmeticNodeNumber)
                                #print("Duplicate Node Output", flpMultiplier.output)
                                #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = {str(flpMultiplier.arithmeticNodeNumber):list()}
                                # add the original to the dictionary and add the duplicate to a list
                                #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber,flpMultiplier.equation]
                                self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber]

                                # add the duplicate to other arithmetic nodes
                                self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                
                            else:
                                # if the duplicate is already there, add the new child to the duplicates dictionary       
                                equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"]
                                # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                equationsOfArithmeticNodesWithDetails[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                # add the original to the dictionary and add the duplicate to a list
                                arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpMultiplier.arithmeticNodeNumber)
                                self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                # add the duplicate to other arithmetic nodes
                                self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                                                    
                        
                        #print("MultiplicandDriver Index", multiplicandDriverIndex)
                        #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                        # check whether the multiplierDriver Index and multiplicand Driver Index exists in duplicatesOfArithmeticNodesWithTheirReceiverIndices
                        #print("Multiplier Equation",flpMultiplier.equation)
                        #print("Multiplier ArithmeticNode Number",flpMultiplier.arithmeticNodeNumber)
                        #print("Multiplier Driver Index", multiplierDriverIndex)
                        #print("Multiplier Driver Output", flpMultiplierMultiplierDriver.output)
                        #print("Multiplier Driver Equation", flpMultiplierMultiplierDriver.equation)
                        if str(multiplierDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                            # add the duplicate to other arithmetic nodes
                            duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[multiplierDriverIndex]
                            duplicates.append(flpMultiplier.arithmeticNodeNumber)
                            
                        #print("Multiplier Equation",flpMultiplier.equation)
                        #print("Multiplier ArithmeticNode Number",flpMultiplier.arithmeticNodeNumber)
                        #print("Multiplicand Driver Index", multiplicandDriverIndex)
                        #print("Multiplicand Driver Output", flpMultiplierMultiplicandDriver.output)
                        #print("Multiplicand Driver Equation", flpMultiplierMultiplicandDriver.equation)
                        #print("MultiplierDriver Index", multiplierDriverIndex)
                        #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                        if str(multiplicandDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                            # add the duplicate to other arithmetic nodes
                            duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[multiplicandDriverIndex]
                            duplicates.append(flpMultiplier.arithmeticNodeNumber)

                    
                    elif len(flpMultiplier.swMultiplier.drivers) == 1:
                        
                        driverEquations = list()
                        
                        if flpMultiplier.multiplicand in flpMultiplier.swMultiplier.driversInfo:
                            multiplicandDriver = flpMultiplier.swMultiplier.driversInfo[flpMultiplier.multiplicand]
                            # access the multiplicanddriver info
                            multiplicandDriverIndex = multiplicandDriver.info[flpMultiplier.multiplicand]
                            # access the driver from arithmetic nodes
                            flpMultiplierMultiplicandDriver = self.arithmeticNodes[int(multiplicandDriverIndex)]
                            
                                                        
                            # access the flpMultiplier node multiplicand driver
                            driverEquations.append(flpMultiplierMultiplicandDriver.equation)
                            #print("DriverEquations", driverEquations)

                            # set the product node driver equations
                            flpMultiplier.swMultiplier.driverEquations = driverEquations
                            
                            if flpMultiplier.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]

                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", flpMultiplier.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", flpMultiplier.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", flpMultiplier.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = {str(flpMultiplier.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber,flpMultiplier.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber]

                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()

                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.equationsOfArithmeticNodesWithDetails[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpMultiplier.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                    
                            #print("MultiplicandDriver Index", multiplicandDriverIndex)
                            #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                            #print("Multiplier Equation",flpMultiplier.equation)
                            #print("Multiplier ArithmeticNode Number",flpMultiplier.arithmeticNodeNumber)
                            #print("Multiplicand Driver Index", multiplicandDriverIndex)
                            #print("Multiplicand Driver Output", flpMultiplierMultiplicandDriver.product)
                            #print("Multiplicand Driver Equation", flpMultiplierMultiplicandDriver.equation)
                            if str(multiplicandDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                                # add the duplicate to other arithmetic nodes
                                duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[multiplicandDriverIndex]
                                duplicates.append(flpMultiplier.arithmeticNodeNumber)
                            
                            if flpMultiplier.swMultiplier.multiplierDriver.isDriverAPort == True:
                                # access the port information
                                if flpMultiplier.swMultiplier.multiplierDriver.name not in self.arithmeticNodesPortNames:
                                    self.arithmeticNodesPortNames[flpMultiplier.multiplier] = flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplier]
                                    self.operationPorts.append(flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplier])
                        
                        elif flpMultiplier.multiplier in flpMultiplier.swMultiplier.driversInfo:
                            multiplierDriver = flpMultiplier.swMultiplier.driversInfo[flpMultiplier.multiplier]
                            # access the multiplicanddriver info
                            multiplierDriverIndex = multiplierDriver.info[flpMultiplier.multiplier]

                            # access the driver from arithmetic nodes
                            flpMultiplierMultiplierDriver = self.arithmeticNodes[int(multiplierDriverIndex)]
                            
                            # access the product node input1 driver
                            driverEquations.append(flpMultiplierMultiplierDriver.equation)
                            #print("DriverEquations", driverEquations)

                            # set the product node driver equations
                            flpMultiplier.swMultiplier.driverEquations = driverEquations
                            
                            if flpMultiplier.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", flpMultiplier.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", flpMultiplier.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", flpMultiplier.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = {str(flpMultiplier.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber,flpMultiplier.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber]

                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                    
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpMultiplier.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                    
                            #print("Multiplier Equation",flpMultiplier.equation)
                            #print("Multiplier ArithmeticNode Number",flpMultiplier.arithmeticNodeNumber)
                            #print("Multiplier Driver Index", multiplierDriverIndex)
                            #print("Multiplier Driver Output", flpMultiplierMultiplierDriver.output)
                            #print("Multiplier Driver Equation", flpMultiplierMultiplierDriver.equation)
                            if str(multiplierDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                                # add the duplicate to other arithmetic nodes
                                duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[multiplierDriverIndex]
                                duplicates.append(flpMultiplier.arithmeticNodeNumber)

                            if flpMultiplier.swMultiplier.multiplicandDriver.isDriverAPort == True:
                                # access the port information
                                if flpMultiplier.swMultiplier.multiplicandDriver.name not in self.arithmeticNodesPortNames:
                                    self.arithmeticNodesPortNames[flpMultiplier.multiplicand] = flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplicand]
                                    self.operationPorts.append(flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplicand])
                        
                    else:
                        # check if the driver is a weight or port
                        if flpMultiplier.swMultiplier.multiplicandDriver.isDriverAPort == True:
                            if flpMultiplier.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", flpMultiplier.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", flpMultiplier.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", flpMultiplier.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = {str(flpMultiplier.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber,flpMultiplier.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber]

                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpMultiplier.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()


                            
                            # access the port information
                            if flpMultiplier.swMultiplier.multiplicandDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[flpMultiplier.multiplicand] = flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplicand]
                                self.operationPorts.append(flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplicand])

                        elif flpMultiplier.swMultiplier.multiplierDriver.isDriverAPort == True:
                            if flpMultiplier.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", flpMultiplier.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", flpMultiplier.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", flpMultiplier.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = {str(flpMultiplier.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber,flpMultiplier.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber]

                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpMultiplier.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()

                            
                            
                            # access the port information
                            if flpMultiplier.swMultiplier.multiplierDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[flpMultiplier.multiplier] = flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplier]
                                self.operationPorts.append(flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplier])
                        
                        elif (flpMultiplier.swMultiplier.multiplicandDriver.isDriverAPort == True) and (flpMultiplier.swMultiplier.multiplierDriver.isDriverAPort == True):
                            if flpMultiplier.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", flpMultiplier.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", flpMultiplier.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", flpMultiplier.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = {str(flpMultiplier.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber]
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpMultiplier.arithmeticNodeNumber,flpMultiplier.equation]

                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[flpMultiplier.arithmeticNodeNumber] = list()
                                    self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpMultiplier.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpMultiplier.arithmeticNodeNumber)] = list()
                            
                            
                            # access the port information
                            if flpMultiplier.swMultiplier.multiplicandDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[flpMultiplier.multiplicand] = flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplicand]
                                self.operationPorts.append(flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplicand])
                            
                            # access the port information
                            if flpMultiplier.swMultiplier.multiplicandDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[flpMultiplier.multiplier] = flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplier]
                                self.operationPorts.append(flpMultiplier.inputDataPortsInfo[flpMultiplier.multiplier])
                                

                    #append the multiplier to the multipliers array
                    self.multipliers.append(flpMultiplier)
                    # add the productNode to the arithmetic node
                    self.arithmeticNodes.append(flpMultiplier)
                    
                    # check if the equation is already there or not
                    if flpMultiplier.equation not in self.equationsOfArithmeticNodes:
                        #print("Adding Multiplier Equation for the first time")
                        #print("Multiplier Equation",flpMultiplier.equation)
                        #print("Multiplier ArithmeticNode Number",flpMultiplier.arithmeticNodeNumber)
                        # add the flpAdder equation to the arithmeticNodesCompuationInfo dictionary
                        self.equationsOfArithmeticNodes[flpMultiplier.equation] = flpMultiplier.arithmeticNodeNumber
                        # add the equation to drivers of arithmetic nodes and add the parent dictionary with the arithmeticNodeNumber       
                        self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation] = {"Original":flpMultiplier.arithmeticNodeNumber}

                                                            
                elif self.currentOperator is self.additionOperator:
                    # check whether the zeroth index of the operationValue or the operandValue is having its first letter as "v"
                    # initialise sumNode
                    
                    # intialise the new FLPAdder
                    flpAdder = FLPAdder()
                    flpAdder.configurationDetailsOfOperator = {"Name":"Adder","Frequency":self.operationFrequency,"NumberSystem":"Float","Number":len(self.adders),"ArithmeticNodeNumber":len(self.arithmeticNodes),"MantissaBits":self.mantissaBits,"ExponentBits":self.exponentBits,"NumberOfBits":self.numberOfBits,"Augend":operationValue, "Addend":operandValue,"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.operationFrequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}}
                    # configure the flpAdder
                    flpAdder.configure()
                    # process the flpAdder
                    flpAdder.process()
                    # perform the flpAdder
                    flpAdder.perform()

                    # set the output of the FLPAdder
                    operationValue = flpAdder.summation
                                        
                    # acces the drivers of productNode and access the receiverEquation
                    if len(flpAdder.swAdder.drivers) > 1:
                        driverEquations = list()
                        augendDriver = flpAdder.swAdder.driversInfo[flpAdder.augend]
                        augendDriverIndex = augendDriver.info[flpAdder.augend]
                        #print("Augend Driver Index", augendDriverIndex)
                        # access the driver from arithmetic nodes
                        flpAdderAugendDriver = self.arithmeticNodes[int(augendDriverIndex)]
                        
                        # access the flpAdder augend driver
                        driverEquations.append(flpAdderAugendDriver.equation)

                        addendDriver = flpAdder.swAdder.driversInfo[flpAdder.addend]
                        addendDriverIndex = addendDriver.info[flpAdder.addend]
                        #print("Addend Driver Index", addendDriverIndex)
                        # access the flpAdder from arithmetic nodes
                        flpAdderAddendDriver = self.arithmeticNodes[int(addendDriverIndex)]
                        # access the adder node addend driver
                        driverEquations.append(flpAdderAddendDriver.equation)
                        #print("DriverEquations", driverEquations)
                        # set the sum node driver equations
                        flpAdder.swAdder.driverEquations = driverEquations
                        
                        if flpAdder.equation in self.equationsOfArithmeticNodes:
                            # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                            equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]
                            
                            if "Duplicate" not in equationParentAndChildren:
                                #print("Duplicate Node Equation", flpAdder.equation)
                                #print("Duplicate Node ArithmeticNodeNumber", flpAdder.arithmeticNodeNumber)
                                #print("Duplicate Node Output", flpAdder.output)
                                #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = {str(flpAdder.arithmeticNodeNumber):list()}
                                # add the original to the dictionary and add the duplicate to a list
                                #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpAdder.arithmeticNodeNumber,flpAdder.equation]
                                self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpAdder.arithmeticNodeNumber]
                                # add the duplicate to other arithmetic nodes
                                self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()
                              
                            else:
                                # if the duplicate is already there, add the new child to the duplicates dictionary       
                                equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"]
                                # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                equationsOfArithmeticNodesWithDetails[str(flpAdder.arithmeticNodeNumber)] = list()
                                self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                # add the original to the dictionary and add the duplicate to a list
                                arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpAdder.arithmeticNodeNumber)
                                self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                # add the duplicate to other arithmetic nodes
                                self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()
                                
                            
                        
                        #print("Augend Driver Index", augendDriverIndex)
                        #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                        #print("Adder Equation",flpAdder.equation)
                        #print("Adder ArithmeticNode Number",flpAdder.arithmeticNodeNumber)
                        #print("Augen Driver Index",augendDriverIndex)
                        #print("Augend Driver Output", flpAdderAugendDriver.output)
                        #print("Adder Driver Equation", flpAdderAugendDriver.equation)
                        
                        # check whether the multiplierDriver Index and multiplicand Driver Index exists in duplicatesOfArithmeticNodesWithTheirReceiverIndices
                        if str(augendDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                            
                            # add the duplicate to other arithmetic nodes
                            duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[augendDriverIndex]
                            duplicates.append(flpAdder.arithmeticNodeNumber)
                            
                        #print("Adder Equation",flpAdder.equation)
                        #print("Adder ArithmeticNode Number",flpAdder.arithmeticNodeNumber)
                        #print("Addend Adder Index",addendDriverIndex)
                        #print("Addend Driver Output", flpAdderAddendDriver.output)
                        #print("Addend Driver Equation", flpAdderAddendDriver.equation)

                        #print("Addend Driver Index", addendDriverIndex)
                        #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)

                        if str(addendDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                            # add the duplicate to other arithmetic nodes
                            duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[addendDriverIndex]
                            duplicates.append(flpAdder.arithmeticNodeNumber)

                    
                    elif len(flpAdder.swAdder.drivers) == 1:
                        driverEquations = list()
                        
                        if flpAdder.augend in flpAdder.swAdder.driversInfo:
                            augendDriver = flpAdder.swAdder.driversInfo[flpAdder.augend]
                            augendDriverIndex = augendDriver.info[flpAdder.augend]

                            # access the driver from arithmetic nodes
                            augendDriver = self.arithmeticNodes[int(augendDriverIndex)]
                            # access the sum node input1 driver
                            driverEquations.append(augendDriver.equation)
                            #print("DriverEquations", driverEquations)
                            # check the augendDriverIndex key is present or not
                            # set the sum node driver equations
                            flpAdder.swAdder.driverEquations = driverEquations
                            
                            if flpAdder.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", flpAdder.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", flpAdder.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", flpAdder.output)    
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = {str(flpAdder.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpAdder.arithmeticNodeNumber,flpAdder.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpAdder.arithmeticNodeNumber]
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()
                                    
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(flpAdder.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpAdder.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()
                                    
                                
                            
                            
                            #print("Augend Driver Index", augendDriverIndex)
                            #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                            #print("Adder Equation",flpAdder.equation)
                            #print("Adder ArithmeticNode Number",flpAdder.arithmeticNodeNumber)
                            #print("Augend Driver Index",augendDriverIndex)
                            #print("Augend Driver Output", flpAdderAugendDriver.output)
                            #print("Augend Driver Equation", flpAdderAugendDriver.equation)
                            
                            if str(augendDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                                # add the duplicate to other arithmetic nodes
                                duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[augendDriverIndex]
                                duplicates.append(flpAdder.arithmeticNodeNumber)


                            
                            if flpAdder.swAdder.addendDriver.isDriverAPort == True:
                                # access the port information
                                if flpAdder.swAdder.addendDriver.name not in self.arithmeticNodesPortNames:
                                    self.arithmeticNodesPortNames[flpAdder.addend] = flpAdder.inputDataPortsInfo[flpAdder.addend]
                                    self.operationPorts.append(flpAdder.inputDataPortsInfo[flpAdder.addend])

                        elif flpAdder.addend in flpAdder.swAdder.driversInfo:
                             addendDriver = flpAdder.swAdder.driversInfo[flpAdder.addend]
                             addendDriverIndex = addendDriver.info[flpAdder.addend]
                             # access the driver from arithmetic nodes
                             addendDriver = self.arithmeticNodes[int(addendDriverIndex)]
                             # access the sum node input1 driver
                             driverEquations.append(addendDriver.equation)
                             #print("DriverEquations", driverEquations)
                             # set the sum node driver equations
                             flpAdder.swAdder.driverEquations = driverEquations
                             
                             if flpAdder.equation in self.equationsOfArithmeticNodes:
                                 # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                 equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]
                                 if "Duplicate" not in equationParentAndChildren:
                                     #print("Duplicate Node Equation", flpAdder.equation)
                                     #print("Duplicate Node ArithmeticNodeNumber", flpAdder.arithmeticNodeNumber)
                                     #print("Duplicate Node Output", flpAdder.output)
                                     #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                     # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                     self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = {str(flpAdder.arithmeticNodeNumber):list()}
                                     # add the original to the dictionary and add the duplicate to a list
                                     #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpAdder.arithmeticNodeNumber,flpAdder.equation]
                                     self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpAdder.arithmeticNodeNumber]
                                     # add the duplicate to other arithmetic nodes
                                     self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()
                                     

                                 else:
                                     # if the duplicate is already there, add the new child to the duplicates dictionary       
                                     equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"]
                                     # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                     equationsOfArithmeticNodesWithDetails[str(flpAdder.arithmeticNodeNumber)] = list()
                                     self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                     # add the original to the dictionary and add the duplicate to a list
                                     arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                     arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpAdder.arithmeticNodeNumber)
                                     self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                     # add the duplicate to other arithmetic nodes
                                     self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()
                                     
                                
                             
                             #print("Addend Driver Index", addendDriverIndex)
                             #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                             #print("Adder Equation",flpAdder.equation)
                             #print("Adder ArithmeticNode Number",flpAdder.arithmeticNodeNumber)
                             #print("Addend Driver Index",addendDriverIndex)
                             #print("Addend Driver Output", flpAdderAddendDriver.output)
                             #print("Addend Driver Equation", flpAdderAddendDriver.equation)
                             
                             if str(addendDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                                 # add the duplicate to other arithmetic nodes
                                 duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[addendDriverIndex]
                                 duplicates.append(flpAdder.arithmeticNodeNumber)



                             # check if the driver is a weight or port
                             if flpAdder.swAdder.augendDriver.isDriverAPort == True:
                                 # access the port information
                                 if flpAdder.swAdder.augendDriver.name not in self.arithmeticNodesPortNames:
                                     self.arithmeticNodesPortNames[flpAdder.augend] = flpAdder.inputDataPortsInfo[flpAdder.augend]
                                     self.operationPorts.append(flpAdder.inputDataPortsInfo[flpAdder.augend])
                    else:
                        # check if the driver is a weight or port
                        if flpAdder.swAdder.augendDriver.isDriverAPort == True:
                            if flpAdder.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", flpAdder.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", flpAdder.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", flpAdder.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = {str(flpAdder.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpAdder.arithmeticNodeNumber,flpAdder.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpAdder.arithmeticNodeNumber]
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(flpAdder.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeDuplicates[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpAdder.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()

                            # access the port information
                            if flpAdder.swAdder.augendDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[flpAdder.augend] = flpAdder.inputDataPortsInfo[flpAdder.augend]
                                self.operationPorts.append(flpAdder.inputDataPortsInfo[flpAdder.augend])
                            
                        elif flpAdder.swAdder.addendDriver.isDriverAPort == True:
                            if flpAdder.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]
                                
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", flpAdder.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", flpAdder.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", flpAdder.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = {str(flpAdder.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpAdder.arithmeticNodeNumber,flpAdder.equation]
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(flpAdder.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpAdder.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()

                            
                            # access the port information
                            if flpAdder.swAdder.addendDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[flpAdder.addend] = flpAdder.inputDataPortsInfo[flpAdder.addend]
                                self.operationPorts.append(flpAdder.inputDataPortsInfo[flpAdder.addend])

                        elif (flpAdder.swAdder.augendDriver.isDriverAPort == True) and (flpAdder.swAdder.addendDriver.isDriverAPort == True):
                            if flpAdder.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", flpAdder.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", flpAdder.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", flpAdder.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])

                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = {str(flpAdder.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpAdder.arithmeticNodeNumber,flpAdder.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [flpAdder.arithmeticNodeNumber]
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(flpAdder.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeDuplicates[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(flpAdder.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(flpAdder.arithmeticNodeNumber)] = list()
                            
                            
                            #access the port information
                            if flpAdder.swAdder.augendDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[flpAdder.augend] = flpAdder.inputDataPortsInfo[flpAdder.augend]
                                self.operationPorts.append(flpAdder.inputDataPortsInfo[flpAdder.augend])
                            
                            # access the port information
                            if flpAdder.swAdder.addendDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[flpAdder.addend] = flpAdder.inputDataPortsInfo[flpAdder.addend]
                                self.operationPorts.append(flpAdder.inputDataPortsInfo[flpAdder.addend])
                        

                                        
                    # set the sumNode ports
                    #self.arithmeticNodePorts = sumNode.ports
                    #append the sumNode to the sumNodes array
                    self.adders.append(flpAdder)
                    # add the sumNode to the arithmetic node
                    self.arithmeticNodes.append(flpAdder)
                    
                    # check if the equation is already there or not
                    if flpAdder.equation not in self.equationsOfArithmeticNodes:
                        #print("Adding Adder equation for the first time")
                        #print("Adder Equation",flpAdder.equation)
                        #print("Adder ArithmeticNode Number",flpAdder.arithmeticNodeNumber)
                        # add the flpAdder equation to the arithmeticNodesCompuationInfo dictionary
                        self.equationsOfArithmeticNodes[flpAdder.equation] = flpAdder.arithmeticNodeNumber
                        # add the equation to drivers of arithmetic nodes and add the parent dictionary with the arithmeticNodeNumber        
                        self.equationsOfArithmeticNodesWithDetails[flpAdder.equation]= {"Original":flpAdder.arithmeticNodeNumber}
                    
                     
        # print the final operationValue
        #print( "The updated operationValue: ", operationValue)
        # pop the operandValueStack
        self.popOperandValueStack(startRange, stopRange)
        # push the calculated new operandValues into operandValueStack
        self.pushIntoOperandValueStack(operationValue)
        # pop the operator or operators from the bracketsAndOperatorStack
        # before popping print the number of operators
        #print( "The number of opertators to be popped: ", numberOfOperators)
        self.popOperatorsFrombracketsAndOperatorStack(numberOfOperators)
        return True
    
    """
    # End: performOperation function
    """
         
    """
    # Start: performPCOperation function
    """
    
    def performPCOperation(self):
        # as the current analysisMode is 0, we do not need to do initial configuration,
        # rather directly parse th equation and generate VHDL
        super().parseEquation()
        # sort the operation ports
        self.operationPorts = self.sortOperationPorts()

        # print the operation ports
        #for operationPort in self.operationPorts:
            #print("OperationPort",operationPort.name)
        
        print("Length of arithmeticNodes", len(self.arithmeticNodes))
        print("Length of multipliers", len(self.multipliers))
        print("Length of adders", len(self.adders))
        #print("Equations of ArithmieticNodes \n",self.equationsOfArithmeticNodes)
        #print("Equations of ArithmeticNodes with details \n",self.equationsOfArithmeticNodesWithDetails)
        #print("ArithmeticNodes Duplicates \n",self.arithmeticNodeIndicesWithTheirDuplicatesIndices)
        #print("Drivers of Duplicate ArithmeticNodes with their receivers \n",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
        
    """
    #End: performPCOperation function
    """
    
    def sortOperationPorts(self):
        """
        Function to sort the pcsystem inputPorts based on the number in the names of the inputPorts
        1. No parameters are given as everything in this is assumed to be of the hardware DUT form
        # First, access the name of the exisitng PCSystem inputPorts, then use it to sort the portNames
        # use the sortedPortNames to sort the pcSystem inputPorts object list and reassign back to the original self.pcSystemPorts
        Return: the sorted list of the PCSystem inputPorts
        """
        portNames = list()
        # new systemPort list which will contain the sortedPCSystemPorts list
        inputPorts = list()
        #print("OriginalPCSystemPorts",operationPorts)
        for port in self.operationPorts:
            portNames.append(port.name)
        portNames.sort(key=natural_keys)

        for portName in portNames:
            for port in self.operationPorts:
                if port.name == portName:
                    inputPorts.append(port)
                    break

        #print("PCSystemPortNames",portNames)
        #print("UpdatedPCSystemPorts",inputPorts)          
        return inputPorts
    
    """
    # Start: resetPCOperation function
    """
    def resetPCOperation(self):
        # reset the equation parser
        super().resetEquationParser()
        self.reset()
       
    """
    # End: resetPCOperation function
    """

    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        # the equation upon which the FLPPCOperation is performed
        self.equation = None
        # the mantissa bits required for the FLPPCOperation
        self.mantissaBits = 0
        # the exponentBits required for the FLPOperation
        self.exponentBits = 0
        # initialise the new property to store multipliers
        self.multipliers = list()
        # new property to store the adders
        self.adders = list()
        # new property to store both the arithmetic nodes
        self.arithmeticNodes = list()
        # new property to store the system inputPorts
        self.operationPorts = list()
        # new property to store the system ports
        self.arithmeticNodesPortNames = dict()
        # new property to store the arithmeticNode that drives some other nodes
        # this property will be updated based on the compute equation info
        self.equationsOfArithmeticNodesWithDetails = dict()
        #new property to store teh system input ports
        self._arithmeticNodesInputPorts = None
        # property to store the operation Frequency
        self._operationFrequency = None
        # property to store the configuration details
        self.configurationDetailsOfOperation = None
        # property to store the number of bits
        self._numberOfBits = 0
        # property to the computation equation of every arithemeticnode
        self.equationsOfArithmeticNodes = dict()
        # property to store the arithmetic node duplicates
        self.arithmeticNodeIndicesWithTheirDuplicatesIndices = dict()
        # property to store the duplicate arithmeticNodes and its child arithmeticNodes
        self.duplicatesOfArithmeticNodesWithTheirReceiverIndices = dict()
        # property to store the equation with original arithmeticNodes and its duplicates (without drivers)
        self.equationsOfArithmeticNodesWithDetails = dict()

    def main(self):
        self.performPCOperation()
    
    def run(self):
        self.main()
