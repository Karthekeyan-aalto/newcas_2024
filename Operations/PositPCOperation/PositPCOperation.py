#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  22 09:59:26 2024

@author: Karthekeyan Periasamy
"""

from Operations.EquationParser.EquationParser import EquationParser
from Operators.Multipliers.PositMultiplier.PositMultiplier import PositMultiplier
from Operators.Adders.PositAdder.PositAdder import PositAdder
import re


# we will move the sorting of ports to PCOperation, once the whole PCOperation is revamped
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)',text)]


class PositPCOperation(EquationParser):

        
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
       

    def connectProperties(self):
        # the equation upon which the FLPPCOperation is performed
        self.equation = None
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

        if "EsBits" in configurationDetails:
            self.esBits = configurationDetails["EsBits"]

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
        numberOfOperators = self.currentNumberOfOperations
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

                    # intialise the new PositMultiplier
                    positMultiplier = PositMultiplier()
                    positMultiplier.configurationDetailsOfOperator = {"Name":"Multiplier","Frequency":self.operationFrequency,"NumberSystem":"Float","Number":len(self.multipliers),"ArithmeticNodeNumber":len(self.arithmeticNodes),"EsBits":self.esBits,"NumberOfBits":self.numberOfBits,"Multiplicand":operationValue, "Multiplier":operandValue,"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.operationFrequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}}
                    # configure the positMultiplier
                    positMultiplier.configure()
                    # process the positMultiplier
                    positMultiplier.process()
                    # perform the positMultiplier
                    positMultiplier.perform()
                    
                    operationValue = positMultiplier.product


                    if len(positMultiplier.swMultiplier.drivers) > 1:

                        driverEquations = list()
                        multiplicandDriver = positMultiplier.swMultiplier.driversInfo[positMultiplier.multiplicand]
                        # access the multiplicanddriver info
                        multiplicandDriverIndex = multiplicandDriver.info[positMultiplier.multiplicand]
                        #print("MultiplicandDriver Index", multiplicandDriverIndex)
                        # access the driver from arithmetic nodes
                        positMultiplierMultiplicandDriver = self.arithmeticNodes[int(multiplicandDriverIndex)]
                        
                        # access the positMultiplier multiplicand driver
                        driverEquations.append(positMultiplierMultiplicandDriver.equation)
                        
                        multiplierDriver = positMultiplier.swMultiplier.driversInfo[positMultiplier.multiplier]
                        # access the multiplicanddriver info
                        multiplierDriverIndex = positMultiplier.info[positMultiplier.multiplier]
                        #print("MultiplierDriver Index", multiplicandDriverIndex)
                        # access the driver from arithmetic nodes
                        positMultiplierMultiplierDriver = self.arithmeticNodes[int(multiplierDriverIndex)]
                        
                        
                        # access the product node input2 driver
                        driverEquations.append(positMultiplierMultiplierDriver.equation)
                        #print("DriverEquations", driverEquations)
                        # set the positMultiplier driver equations
                        positMultiplier.swMultiplier.driverEquations = driverEquations
                        #print("PositMultiplier DriverEquations", positMultiplier.swMultiplier.driverEquations)

                        
                        if positMultiplier.equation in self.equationsOfArithmeticNodes:
                            # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                            equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]
                            if "Duplicate" not in equationParentAndChildren:
                                #print("Duplicate Node Equation", positMultiplier.equation)
                                #print("Duplicate Node ArithmeticNodeNumber", positMultiplier.arithmeticNodeNumber)
                                #print("Duplicate Node Output", positMultiplier.output)
                                #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = {str(positMultiplier.arithmeticNodeNumber):list()}
                                # add the original to the dictionary and add the duplicate to a list
                                #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber,positMultiplier.equation]
                                self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber]

                                # add the duplicate to other arithmetic nodes
                                self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()
                                
                            else:
                                # if the duplicate is already there, add the new child to the duplicates dictionary       
                                equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"]
                                # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                equationsOfArithmeticNodesWithDetails[str(positMultiplier.arithmeticNodeNumber)] = list()
                                self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                # add the original to the dictionary and add the duplicate to a list
                                arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positMultiplier.arithmeticNodeNumber)
                                self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                # add the duplicate to other arithmetic nodes
                                self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()
                                                                    
                        
                        #print("MultiplicandDriver Index", multiplicandDriverIndex)
                        #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                        # check whether the multiplierDriver Index and multiplicand Driver Index exists in duplicatesOfArithmeticNodesWithTheirReceiverIndices
                        #print("Multiplier Equation",positMultiplier.equation)
                        #print("Multiplier ArithmeticNode Number",positMultiplier.arithmeticNodeNumber)
                        #print("Multiplier Driver Index", multiplierDriverIndex)
                        #print("Multiplier Driver Output", positMultiplierMultiplierDriver.output)
                        #print("Multiplier Driver Equation", positMultiplierMultiplierDriver.equation)
                        if str(multiplierDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                            # add the duplicate to other arithmetic nodes
                            duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[multiplierDriverIndex]
                            duplicates.append(positMultiplier.arithmeticNodeNumber)
                            
                        #print("Multiplier Equation",positMultiplier.equation)
                        #print("Multiplier ArithmeticNode Number",positMultiplier.arithmeticNodeNumber)
                        #print("Multiplicand Driver Index", multiplicandDriverIndex)
                        #print("Multiplicand Driver Output", positMultiplierMultiplicandDriver.output)
                        #print("Multiplicand Driver Equation", positMultiplierMultiplicandDriver.equation)
                        #print("MultiplierDriver Index", multiplierDriverIndex)
                        #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                        if str(multiplicandDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                            # add the duplicate to other arithmetic nodes
                            duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[multiplicandDriverIndex]
                            duplicates.append(positMultiplier.arithmeticNodeNumber)

                    
                    elif len(positMultiplier.swMultiplier.drivers) == 1:
                        
                        driverEquations = list()
                        
                        if positMultiplier.multiplicand in positMultiplier.swMultiplier.driversInfo:
                            multiplicandDriver = positMultiplier.swMultiplier.driversInfo[positMultiplier.multiplicand]
                            # access the multiplicanddriver info
                            multiplicandDriverIndex = multiplicandDriver.info[positMultiplier.multiplicand]
                            # access the driver from arithmetic nodes
                            positMultiplierMultiplicandDriver = self.arithmeticNodes[int(multiplicandDriverIndex)]
                            
                                                        
                            # access the positMultiplier node multiplicand driver
                            driverEquations.append(positMultiplierMultiplicandDriver.equation)
                            #print("DriverEquations", driverEquations)

                            # set the product node driver equations
                            positMultiplier.swMultiplier.driverEquations = driverEquations
                            
                            if positMultiplier.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]

                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", positMultiplier.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", positMultiplier.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", positMultiplier.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = {str(positMultiplier.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber,positMultiplier.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber]

                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()

                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(positMultiplier.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.equationsOfArithmeticNodesWithDetails[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positMultiplier.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()
                                    
                            #print("MultiplicandDriver Index", multiplicandDriverIndex)
                            #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                            #print("Multiplier Equation",positMultiplier.equation)
                            #print("Multiplier ArithmeticNode Number",positMultiplier.arithmeticNodeNumber)
                            #print("Multiplicand Driver Index", multiplicandDriverIndex)
                            #print("Multiplicand Driver Output", positMultiplierMultiplicandDriver.product)
                            #print("Multiplicand Driver Equation", positMultiplierMultiplicandDriver.equation)
                            if str(multiplicandDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                                # add the duplicate to other arithmetic nodes
                                duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[multiplicandDriverIndex]
                                duplicates.append(positMultiplier.arithmeticNodeNumber)
                            
                            if positMultiplier.swMultiplier.multiplierDriver.isDriverAPort == True:
                                # access the port information
                                if positMultiplier.swMultiplier.multiplierDriver.name not in self.arithmeticNodesPortNames:
                                    self.arithmeticNodesPortNames[positMultiplier.multiplier] = positMultiplier.inputDataPortsInfo[positMultiplier.multiplier]
                                    self.operationPorts.append(positMultiplier.inputDataPortsInfo[positMultiplier.multiplier])
                        
                        elif positMultiplier.multiplier in positMultiplier.swMultiplier.driversInfo:
                            multiplierDriver = positMultiplier.swMultiplier.driversInfo[positMultiplier.multiplier]
                            # access the multiplicanddriver info
                            multiplierDriverIndex = multiplierDriver.info[positMultiplier.multiplier]

                            # access the driver from arithmetic nodes
                            positMultiplierMultiplierDriver = self.arithmeticNodes[int(multiplierDriverIndex)]
                            
                            # access the product node input1 driver
                            driverEquations.append(positMultiplierMultiplierDriver.equation)
                            #print("DriverEquations", driverEquations)

                            # set the product node driver equations
                            positMultiplier.swMultiplier.driverEquations = driverEquations
                            
                            if positMultiplier.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", positMultiplier.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", positMultiplier.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", positMultiplier.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = {str(positMultiplier.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber,positMultiplier.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber]

                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()
                                    
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(positMultiplier.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positMultiplier.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()
                                    
                            #print("Multiplier Equation",positMultiplier.equation)
                            #print("Multiplier ArithmeticNode Number",positMultiplier.arithmeticNodeNumber)
                            #print("Multiplier Driver Index", multiplierDriverIndex)
                            #print("Multiplier Driver Output", positMultiplierMultiplierDriver.output)
                            #print("Multiplier Driver Equation", positMultiplierMultiplierDriver.equation)
                            if str(multiplierDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                                # add the duplicate to other arithmetic nodes
                                duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[multiplierDriverIndex]
                                duplicates.append(positMultiplier.arithmeticNodeNumber)

                            if positMultiplier.swMultiplier.multiplicandDriver.isDriverAPort == True:
                                # access the port information
                                if positMultiplier.swMultiplier.multiplicandDriver.name not in self.arithmeticNodesPortNames:
                                    self.arithmeticNodesPortNames[positMultiplier.multiplicand] = positMultiplier.inputDataPortsInfo[positMultiplier.multiplicand]
                                    self.operationPorts.append(positMultiplier.inputDataPortsInfo[positMultiplier.multiplicand])
                        
                    else:
                        # check if the driver is a weight or port
                        if positMultiplier.swMultiplier.multiplicandDriver.isDriverAPort == True:
                            if positMultiplier.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", positMultiplier.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", positMultiplier.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", positMultiplier.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = {str(positMultiplier.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber,positMultiplier.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber]

                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(positMultiplier.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positMultiplier.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()


                            
                            # access the port information
                            if positMultiplier.swMultiplier.multiplicandDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[positMultiplier.multiplicand] = positMultiplier.inputDataPortsInfo[positMultiplier.multiplicand]
                                self.operationPorts.append(positMultiplier.inputDataPortsInfo[positMultiplier.multiplicand])

                        elif positMultiplier.swMultiplier.multiplierDriver.isDriverAPort == True:
                            if positMultiplier.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", positMultiplier.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", positMultiplier.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", positMultiplier.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = {str(positMultiplier.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber,positMultiplier.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber]

                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(positMultiplier.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positMultiplier.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()

                            
                            
                            # access the port information
                            if positMultiplier.swMultiplier.multiplierDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[positMultiplier.multiplier] = positMultiplier.inputDataPortsInfo[positMultiplier.multiplier]
                                self.operationPorts.append(positMultiplier.inputDataPortsInfo[positMultiplier.multiplier])
                        
                        elif (positMultiplier.swMultiplier.multiplicandDriver.isDriverAPort == True) and (positMultiplier.swMultiplier.multiplierDriver.isDriverAPort == True):
                            if positMultiplier.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", positMultiplier.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", positMultiplier.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", positMultiplier.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = {str(positMultiplier.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber]
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positMultiplier.arithmeticNodeNumber,positMultiplier.equation]

                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[positMultiplier.arithmeticNodeNumber] = list()
                                    self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positMultiplier.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positMultiplier.arithmeticNodeNumber)] = list()
                            
                            
                            # access the port information
                            if positMultiplier.swMultiplier.multiplicandDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[positMultiplier.multiplicand] = positMultiplier.inputDataPortsInfo[positMultiplier.multiplicand]
                                self.operationPorts.append(positMultiplier.inputDataPortsInfo[positMultiplier.multiplicand])
                            
                            # access the port information
                            if positMultiplier.swMultiplier.multiplicandDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[positMultiplier.multiplier] = positMultiplier.inputDataPortsInfo[positMultiplier.multiplier]
                                self.operationPorts.append(positMultiplier.inputDataPortsInfo[positMultiplier.multiplier])
                                

                    #append the multiplier to the multipliers array
                    self.multipliers.append(positMultiplier)
                    # add the productNode to the arithmetic node
                    self.arithmeticNodes.append(positMultiplier)
                    
                    # check if the equation is already there or not
                    if positMultiplier.equation not in self.equationsOfArithmeticNodes:
                        #print("Adding Multiplier Equation for the first time")
                        #print("Multiplier Equation",positMultiplier.equation)
                        #print("Multiplier ArithmeticNode Number",positMultiplier.arithmeticNodeNumber)
                        # add the positAdder equation to the arithmeticNodesCompuationInfo dictionary
                        self.equationsOfArithmeticNodes[positMultiplier.equation] = positMultiplier.arithmeticNodeNumber
                        # add the equation to drivers of arithmetic nodes and add the parent dictionary with the arithmeticNodeNumber       
                        self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation] = {"Original":positMultiplier.arithmeticNodeNumber}

                                                            
                elif self.currentOperator is self.additionOperator:
                    # check whether the zeroth index of the operationValue or the operandValue is having its first letter as "v"
                    # initialise sumNode
                    
                    # intialise the new FLPAdder
                    positAdder = PositAdder()
                    positAdder.configurationDetailsOfOperator = {"Name":"Adder","Frequency":self.operationFrequency,"NumberSystem":"Float","Number":len(self.adders),"ArithmeticNodeNumber":len(self.arithmeticNodes),"EsBits":self.esBits,"NumberOfBits":self.numberOfBits,"Augend":operationValue, "Addend":operandValue,"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":self.operationFrequency,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}}
                    # configure the positAdder
                    positAdder.configure()
                    # process the positAdder
                    positAdder.process()
                    # perform the positAdder
                    positAdder.perform()

                    # set the output of the FLPAdder
                    operationValue = positAdder.summation
                                        
                    # acces the drivers of productNode and access the receiverEquation
                    if len(positAdder.swAdder.drivers) > 1:
                        driverEquations = list()
                        augendDriver = positAdder.swAdder.driversInfo[positAdder.augend]
                        augendDriverIndex = augendDriver.info[positAdder.augend]
                        #print("Augend Driver Index", augendDriverIndex)
                        # access the driver from arithmetic nodes
                        positAdderAugendDriver = self.arithmeticNodes[int(augendDriverIndex)]
                        
                        # access the positAdder augend driver
                        driverEquations.append(positAdderAugendDriver.equation)

                        addendDriver = positAdder.swAdder.driversInfo[positAdder.addend]
                        addendDriverIndex = addendDriver.info[positAdder.addend]
                        #print("Addend Driver Index", addendDriverIndex)
                        # access the positAdder from arithmetic nodes
                        positAdderAddendDriver = self.arithmeticNodes[int(addendDriverIndex)]
                        # access the adder node addend driver
                        driverEquations.append(positAdderAddendDriver.equation)
                        #print("DriverEquations", driverEquations)
                        # set the sum node driver equations
                        positAdder.swAdder.driverEquations = driverEquations
                        
                        if positAdder.equation in self.equationsOfArithmeticNodes:
                            # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                            equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positAdder.equation]
                            
                            if "Duplicate" not in equationParentAndChildren:
                                #print("Duplicate Node Equation", positAdder.equation)
                                #print("Duplicate Node ArithmeticNodeNumber", positAdder.arithmeticNodeNumber)
                                #print("Duplicate Node Output", positAdder.output)
                                #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = {str(positAdder.arithmeticNodeNumber):list()}
                                # add the original to the dictionary and add the duplicate to a list
                                #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positAdder.arithmeticNodeNumber,positAdder.equation]
                                self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positAdder.arithmeticNodeNumber]
                                # add the duplicate to other arithmetic nodes
                                self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()
                              
                            else:
                                # if the duplicate is already there, add the new child to the duplicates dictionary       
                                equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"]
                                # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                equationsOfArithmeticNodesWithDetails[str(positAdder.arithmeticNodeNumber)] = list()
                                self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                # add the original to the dictionary and add the duplicate to a list
                                arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positAdder.arithmeticNodeNumber)
                                self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                # add the duplicate to other arithmetic nodes
                                self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()
                                
                            
                        
                        #print("Augend Driver Index", augendDriverIndex)
                        #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                        #print("Adder Equation",positAdder.equation)
                        #print("Adder ArithmeticNode Number",positAdder.arithmeticNodeNumber)
                        #print("Augen Driver Index",augendDriverIndex)
                        #print("Augend Driver Output", positAdderAugendDriver.output)
                        #print("Adder Driver Equation", positAdderAugendDriver.equation)
                        
                        # check whether the multiplierDriver Index and multiplicand Driver Index exists in duplicatesOfArithmeticNodesWithTheirReceiverIndices
                        if str(augendDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                            
                            # add the duplicate to other arithmetic nodes
                            duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[augendDriverIndex]
                            duplicates.append(positAdder.arithmeticNodeNumber)
                            
                        #print("Adder Equation",positAdder.equation)
                        #print("Adder ArithmeticNode Number",positAdder.arithmeticNodeNumber)
                        #print("Addend Adder Index",addendDriverIndex)
                        #print("Addend Driver Output", positAdderAddendDriver.output)
                        #print("Addend Driver Equation", positAdderAddendDriver.equation)

                        #print("Addend Driver Index", addendDriverIndex)
                        #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)

                        if str(addendDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                            # add the duplicate to other arithmetic nodes
                            duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[addendDriverIndex]
                            duplicates.append(positAdder.arithmeticNodeNumber)

                    
                    elif len(positAdder.swAdder.drivers) == 1:
                        driverEquations = list()
                        
                        if positAdder.augend in positAdder.swAdder.driversInfo:
                            augendDriver = positAdder.swAdder.driversInfo[positAdder.augend]
                            augendDriverIndex = augendDriver.info[positAdder.augend]

                            # access the driver from arithmetic nodes
                            augendDriver = self.arithmeticNodes[int(augendDriverIndex)]
                            # access the sum node input1 driver
                            driverEquations.append(augendDriver.equation)
                            #print("DriverEquations", driverEquations)
                            # check the augendDriverIndex key is present or not
                            # set the sum node driver equations
                            positAdder.swAdder.driverEquations = driverEquations
                            
                            if positAdder.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positAdder.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", positAdder.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", positAdder.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", positAdder.output)    
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = {str(positAdder.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positAdder.arithmeticNodeNumber,positAdder.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positAdder.arithmeticNodeNumber]
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()
                                    
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(positAdder.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positAdder.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()
                                    
                                
                            
                            
                            #print("Augend Driver Index", augendDriverIndex)
                            #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                            #print("Adder Equation",positAdder.equation)
                            #print("Adder ArithmeticNode Number",positAdder.arithmeticNodeNumber)
                            #print("Augend Driver Index",augendDriverIndex)
                            #print("Augend Driver Output", positAdderAugendDriver.output)
                            #print("Augend Driver Equation", positAdderAugendDriver.equation)
                            
                            if str(augendDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                                # add the duplicate to other arithmetic nodes
                                duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[augendDriverIndex]
                                duplicates.append(positAdder.arithmeticNodeNumber)


                            
                            if positAdder.swAdder.addendDriver.isDriverAPort == True:
                                # access the port information
                                if positAdder.swAdder.addendDriver.name not in self.arithmeticNodesPortNames:
                                    self.arithmeticNodesPortNames[positAdder.addend] = positAdder.inputDataPortsInfo[positAdder.addend]
                                    self.operationPorts.append(positAdder.inputDataPortsInfo[positAdder.addend])

                        elif positAdder.addend in positAdder.swAdder.driversInfo:
                             addendDriver = positAdder.swAdder.driversInfo[positAdder.addend]
                             addendDriverIndex = addendDriver.info[positAdder.addend]
                             # access the driver from arithmetic nodes
                             addendDriver = self.arithmeticNodes[int(addendDriverIndex)]
                             # access the sum node input1 driver
                             driverEquations.append(addendDriver.equation)
                             #print("DriverEquations", driverEquations)
                             # set the sum node driver equations
                             positAdder.swAdder.driverEquations = driverEquations
                             
                             if positAdder.equation in self.equationsOfArithmeticNodes:
                                 # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                 equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positAdder.equation]
                                 if "Duplicate" not in equationParentAndChildren:
                                     #print("Duplicate Node Equation", positAdder.equation)
                                     #print("Duplicate Node ArithmeticNodeNumber", positAdder.arithmeticNodeNumber)
                                     #print("Duplicate Node Output", positAdder.output)
                                     #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                     # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                     self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = {str(positAdder.arithmeticNodeNumber):list()}
                                     # add the original to the dictionary and add the duplicate to a list
                                     #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positAdder.arithmeticNodeNumber,positAdder.equation]
                                     self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positAdder.arithmeticNodeNumber]
                                     # add the duplicate to other arithmetic nodes
                                     self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()
                                     

                                 else:
                                     # if the duplicate is already there, add the new child to the duplicates dictionary       
                                     equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"]
                                     # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                     equationsOfArithmeticNodesWithDetails[str(positAdder.arithmeticNodeNumber)] = list()
                                     self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                     # add the original to the dictionary and add the duplicate to a list
                                     arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                     arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positAdder.arithmeticNodeNumber)
                                     self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                     # add the duplicate to other arithmetic nodes
                                     self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()
                                     
                                
                             
                             #print("Addend Driver Index", addendDriverIndex)
                             #print("DuplicatesOfArithmeticNodesWithTheirReceivers",self.duplicatesOfArithmeticNodesWithTheirReceiverIndices)
                             #print("Adder Equation",positAdder.equation)
                             #print("Adder ArithmeticNode Number",positAdder.arithmeticNodeNumber)
                             #print("Addend Driver Index",addendDriverIndex)
                             #print("Addend Driver Output", positAdderAddendDriver.output)
                             #print("Addend Driver Equation", positAdderAddendDriver.equation)
                             
                             if str(addendDriverIndex) in self.duplicatesOfArithmeticNodesWithTheirReceiverIndices:
                                 # add the duplicate to other arithmetic nodes
                                 duplicates = self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[addendDriverIndex]
                                 duplicates.append(positAdder.arithmeticNodeNumber)



                             # check if the driver is a weight or port
                             if positAdder.swAdder.augendDriver.isDriverAPort == True:
                                 # access the port information
                                 if positAdder.swAdder.augendDriver.name not in self.arithmeticNodesPortNames:
                                     self.arithmeticNodesPortNames[positAdder.augend] = positAdder.inputDataPortsInfo[positAdder.augend]
                                     self.operationPorts.append(positAdder.inputDataPortsInfo[positAdder.augend])
                    else:
                        # check if the driver is a weight or port
                        if positAdder.swAdder.augendDriver.isDriverAPort == True:
                            if positAdder.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positAdder.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", positAdder.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", positAdder.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", positAdder.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = {str(positAdder.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positAdder.arithmeticNodeNumber,positAdder.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positAdder.arithmeticNodeNumber]
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(positAdder.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeDuplicates[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positAdder.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()

                            # access the port information
                            if positAdder.swAdder.augendDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[positAdder.augend] = positAdder.inputDataPortsInfo[positAdder.augend]
                                self.operationPorts.append(positAdder.inputDataPortsInfo[positAdder.augend])
                            
                        elif positAdder.swAdder.addendDriver.isDriverAPort == True:
                            if positAdder.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positAdder.equation]
                                
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", positAdder.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", positAdder.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", positAdder.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])
                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = {str(positAdder.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positAdder.arithmeticNodeNumber,positAdder.equation]
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positMultiplier.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(positAdder.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positAdder.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()

                            
                            # access the port information
                            if positAdder.swAdder.addendDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[positAdder.addend] = positAdder.inputDataPortsInfo[positAdder.addend]
                                self.operationPorts.append(positAdder.inputDataPortsInfo[positAdder.addend])

                        elif (positAdder.swAdder.augendDriver.isDriverAPort == True) and (positAdder.swAdder.addendDriver.isDriverAPort == True):
                            if positAdder.equation in self.equationsOfArithmeticNodes:
                                # access the child dictionary from the equationsOfArithmeticNodesWithDetails
                                equationParentAndChildren = self.equationsOfArithmeticNodesWithDetails[positAdder.equation]
                                if "Duplicate" not in equationParentAndChildren:
                                    #print("Duplicate Node Equation", positAdder.equation)
                                    #print("Duplicate Node ArithmeticNodeNumber", positAdder.arithmeticNodeNumber)
                                    #print("Duplicate Node Output", positAdder.output)
                                    #print("Original Node ArithmeticNodeNumber", equationParentAndChildren["Original"])

                                    # if the equation is already there, the children of FLPMultiplier are not present add the children as dictionary       
                                    self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = {str(positAdder.arithmeticNodeNumber):list()}
                                    # add the original to the dictionary and add the duplicate to a list
                                    #self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positAdder.arithmeticNodeNumber,positAdder.equation]
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = [positAdder.arithmeticNodeNumber]
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()
                                else:
                                    # if the duplicate is already there, add the new child to the duplicates dictionary       
                                    equationsOfArithmeticNodesWithDetails = self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"]
                                    # append the duplicate arithmeticNode number to the equationsOfArithmeticNodesWithDetails
                                    equationsOfArithmeticNodesWithDetails[str(positAdder.arithmeticNodeNumber)] = list()
                                    self.equationsOfArithmeticNodesWithDetails[positAdder.equation]["Duplicate"] = equationsOfArithmeticNodesWithDetails
                                    # add the original to the dictionary and add the duplicate to a list
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeDuplicates[equationParentAndChildren["Original"]]
                                    arithmeticNodeIndicesWithTheirDuplicatesIndices.append(positAdder.arithmeticNodeNumber)
                                    self.arithmeticNodeIndicesWithTheirDuplicatesIndices[equationParentAndChildren["Original"]] = arithmeticNodeIndicesWithTheirDuplicatesIndices
                                    # add the duplicate to other arithmetic nodes
                                    self.duplicatesOfArithmeticNodesWithTheirReceiverIndices[str(positAdder.arithmeticNodeNumber)] = list()
                            
                            
                            #access the port information
                            if positAdder.swAdder.augendDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[positAdder.augend] = positAdder.inputDataPortsInfo[positAdder.augend]
                                self.operationPorts.append(positAdder.inputDataPortsInfo[positAdder.augend])
                            
                            # access the port information
                            if positAdder.swAdder.addendDriver.name not in self.arithmeticNodesPortNames:
                                self.arithmeticNodesPortNames[positAdder.addend] = positAdder.inputDataPortsInfo[positAdder.addend]
                                self.operationPorts.append(positAdder.inputDataPortsInfo[positAdder.addend])
                        

                                        
                    # set the sumNode ports
                    #self.arithmeticNodePorts = sumNode.ports
                    #append the sumNode to the sumNodes array
                    self.adders.append(positAdder)
                    # add the sumNode to the arithmetic node
                    self.arithmeticNodes.append(positAdder)
                    
                    # check if the equation is already there or not
                    if positAdder.equation not in self.equationsOfArithmeticNodes:
                        #print("Adding Adder equation for the first time")
                        #print("Adder Equation",positAdder.equation)
                        #print("Adder ArithmeticNode Number",positAdder.arithmeticNodeNumber)
                        # add the positAdder equation to the arithmeticNodesCompuationInfo dictionary
                        self.equationsOfArithmeticNodes[positAdder.equation] = positAdder.arithmeticNodeNumber
                        # add the equation to drivers of arithmetic nodes and add the parent dictionary with the arithmeticNodeNumber        
                        self.equationsOfArithmeticNodesWithDetails[positAdder.equation]= {"Original":positAdder.arithmeticNodeNumber}
                    
                     
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
        for port in operationPorts:
            portNames.append(port.name)
        portNames.sort(key=natural_keys)

        for portName in portNames:
            for port in operationPorts:
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
