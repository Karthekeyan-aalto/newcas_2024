#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:09:37 2022

@author: Karthekeyan Periasamy
"""


from Operations.EquationParser import EquationParser
from Operations.ProductNode import ProductNode
from Operations.SumNode import SumNode
from SWOptimisers.PCArithmeticNodesOptimiser.PCArithmeticNodesOptimiser import PCArithmeticNodesOptimiser


class PCOperation(EquationParser.EquationParser):
    
# =============================================================================
#      Member variables and funciton definitions and declarations to customise and manage the 
#      Equation parser perform operation function for different analysis mode and operationMode
# =============================================================================
    
    def __init__(self):
        super().__init__()
        # every PCOperation needs PCEquaiton.
        # PCEquation is set by the PCSystem
        self.equation = None
        
        """
        # Start: PCOperation properties usually set by PCSystem
        # The properties below will be set by the PCSystem that uses the PCOperation
        """
        self.numberOfBits = 0
        self.mantissaBits = 0
        self.esBits = 0
        self.exponential = 0
        self.analysisMode = 0
        self.numberSystem = 0
        
        """
        # Start: Properties of the PCOperation needed by the PCSystem
        1. It has the productNodes, sumNodes and arithmeticNodes of PCOepration performed
        """
        # initialise the new property to store the productNodes
        self.productNodes = list()
        # new property to store the sumNodes
        self.sumNodes = list()
        # new property to store both the arithmetic nodes
        self.arithmeticNodes = list()
        # new property to store the system ports
        self.ports = list()
        
        # optimisation properties
        
        # connect the PCArithmeticNodeOptimiser
        self.connectPCArithmeticNodeOptimiser()

        # property to remove duplication PCAN
        self.optimisePCANToRemoveDuplicatePCAN = False

        
    
# =============================================================================
#     Custom property getters and setters
# =============================================================================
    
    @property
    def arithmeticNodePorts(self):
        """

        Returns
        -------
        TYPE
            a list object that contain arithmeticNodePorts.
            Here, the arithmeticNodes are Product and SumNodes

        """
        return self._arithmeticNodePorts
    
    
    @arithmeticNodePorts.setter  
    def arithmeticNodePorts(self,value):
        # set the _ports value
        self._arithmeticNodePorts = value
        # loop through the value and find which ports need to be added to the main system
        for port in self._arithmeticNodePorts:
            # newPort that will be added if its not None
            newPort = port
            # access the system port
            for systemPort in self.ports:
                # access the name of the system port and check with the arithmetic port
                if newPort.name == systemPort.name:
                    newPort = None
                    break
            # check if the new port is not None
            if newPort != None:
                # append the arithmetic node port to the ports
                self.ports.append(newPort)
                
        #print("Updated System Ports:", self.ports)
                
    
    
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
        # set a counter variable to count the number of maxNode the function will generate
        sumNodes = 0
                              
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
                    # initialise a productNode
                    productNode = ProductNode.ProductNode()
                    # set the productNode number
                    productNode.number = len(self.productNodes)
                    # set the arithmeticnode number
                    productNode.arithmeticNodeNumber = len(self.arithmeticNodes)
                    # set the number of bits of the productNode
                    productNode.numberOfBits = self.numberOfBits
                    # set the mantissaBits of the productNode
                    productNode.mantissaBits = self.mantissaBits
                    # set the esBits of the productNode
                    productNode.esBits = self.esBits
                    # set the esBits of the productNode
                    productNode.exponentBits = self.exponentBits
                    # set the analysis mode to productNode
                    productNode.analysisMode = self.analysisMode
                    # set the numberSystem of the productNode
                    productNode.numberSystem = self.numberSystem
                    # set the input1 of the productNode
                    productNode.input1 = operationValue
                    # set the input2 of the productNode
                    productNode.input2 = operandValue
                    # check if the outputValue is available or not
                    if productNode.outputValue != None:
                        # set the operationValue with the outputValue
                        operationValue = productNode.outputValue
                    else:
                        # set the output of the productNode
                        operationValue = productNode.output
                    
                    
                    # acces the drivers of productNode and access the receiverEquation
                    if len(productNode.drivers) > 1:
                        driverEquations = list()
                        driverNode0Index = productNode.drivers["Input1"]
                        # access the driver from arithmetic nodes
                        productNodeInput1Driver = self.arithmeticNodes[int(driverNode0Index)]
                        # access the product node input1 driver
                        driverEquations.append(productNodeInput1Driver.receiverEquation)
                        driverNode1Index = productNode.drivers["Input2"]
                        # access the driver from arithmetic nodes
                        productNodeInput2Driver = self.arithmeticNodes[int(driverNode1Index)]
                        # access the product node input2 driver
                        driverEquations.append(productNodeInput2Driver.receiverEquation)
                        # set the product node driver equations
                        productNode.driverEquations = driverEquations

                    elif len(productNode.drivers) == 1:
                        driverEquations = list()
                        if "Input1" in productNode.drivers:
                            driverNode0Index = productNode.drivers["Input1"]
                            # access the driver from arithmetic nodes
                            productNodeInput1Driver = self.arithmeticNodes[int(driverNode0Index)]
                            # access the product node input1 driver
                            driverEquations.append(productNodeInput1Driver.receiverEquation)
                            # set the product node driver equations
                            productNode.driverEquations = driverEquations

                        elif "Input2" in productNode.drivers:
                            driverNode0Index = productNode.drivers["Input2"]
                            # access the driver from arithmetic nodes
                            productNodeInput1Driver = self.arithmeticNodes[int(driverNode0Index)]
                            # access the product node input1 driver
                            driverEquations.append(productNodeInput1Driver.receiverEquation)
                            # set the product node driver equations
                            productNode.driverEquations = driverEquations


                    # set the productNode ports
                    self.arithmeticNodePorts = productNode.ports
                    #append the productNode to the productNodes array
                    self.productNodes.append(productNode)
                    # add the productNode to the arithmetic node
                    self.arithmeticNodes.append(productNode)
                    # increase the multiplication operation counter
                    self.multiplicationOperation = self.multiplicationOperation + 1
                                         
                elif self.currentOperator is self.additionOperator:
                    # check whether the zeroth index of the operationValue or the operandValue is having its first letter as "v"
                    # initialise sumNode
                    sumNode = SumNode.SumNode()
                    # set the sumNode number
                    sumNode.number = len(self.sumNodes)
                    # set the arithmeticnode number
                    sumNode.arithmeticNodeNumber = len(self.arithmeticNodes)
                    # set the number of bits of the sumNode
                    sumNode.numberOfBits = self.numberOfBits
                    # set the mantissaBits of the sumNode
                    sumNode.mantissaBits = self.mantissaBits
                    # set the esBits of the sumNode
                    sumNode.esBits = self.esBits
                    # set the exponentBits of the sumNode
                    sumNode.exponentBits = self.exponentBits
                    # set the analysis mode
                    sumNode.analysisMode = self.analysisMode
                    # set the numberSystem of the sumNode
                    sumNode.numberSystem = self.numberSystem
                    # set the input1 of the sumNode
                    sumNode.input1 = operationValue
                    # set the input2 of the sumNode
                    sumNode.input2 = operandValue
            
                    # check if the outputValue is available or not
                    if sumNode.outputValue != None:
                        # set the operationValue to the outputValue
                        operationValue = sumNode.outputValue
                    else:
                        # set the output of the sumNode
                        operationValue = sumNode.output

                    # acces the drivers of productNode and access the receiverEquation
                    if len(sumNode.drivers) > 1:
                        driverEquations = list()
                        driverNode0Index = sumNode.drivers["Input1"]
                        # access the driver from arithmetic nodes
                        sumNodeInput1Driver = self.arithmeticNodes[int(driverNode0Index)]
                        # access the sum node input1 driver
                        driverEquations.append(sumNodeInput1Driver.receiverEquation)
                        driverNode1Index = sumNode.drivers["Input2"]
                        # access the driver from arithmetic nodes
                        sumNodeInput2Driver = self.arithmeticNodes[int(driverNode1Index)]
                        # access the product node input1 driver
                        driverEquations.append(sumNodeInput2Driver.receiverEquation)
                        # set the sum node driver equations
                        sumNode.driverEquations = driverEquations

                    elif len(sumNode.drivers) == 1:
                        driverEquations = list()
                        if "Input1" in sumNode.drivers:
                            driverNode0Index = sumNode.drivers["Input1"]
                            # access the driver from arithmetic nodes
                            sumNodeInput1Driver = self.arithmeticNodes[int(driverNode0Index)]
                            # access the sum node input1 driver
                            driverEquations.append(sumNodeInput1Driver.receiverEquation)
                            # set the sum node driver equations
                            sumNode.driverEquations = driverEquations
                        elif "Input2" in sumNode.drivers:
                            driverNode0Index = sumNode.drivers["Input2"]
                            # access the driver from arithmetic nodes
                            sumNodeInput1Driver = self.arithmeticNodes[int(driverNode0Index)]
                            # access the sum node input1 driver
                            driverEquations.append(sumNodeInput1Driver.receiverEquation)
                            # set the sum node driver equations
                            sumNode.driverEquations = driverEquations
                    
                    
                    # set the sumNode ports
                    self.arithmeticNodePorts = sumNode.ports
                    #append the sumNode to the sumNodes array
                    self.sumNodes.append(sumNode)
                    # add the sumNode to the arithmetic node
                    self.arithmeticNodes.append(sumNode)
                    # increase the addition operation counter
                    self.additionOperation = self.additionOperation + 1
                    
                    #print("Number of sum operators:", numberOfOperators)
                    #print("Original Number of sumNodes", sumNodes)
                    sumNodes = sumNodes + 1
                    #print("Updatexd Number of sumNodes \n", sumNodes)
                    if sumNodes == numberOfOperators:
                        #print("MMACUnits can be formed \n")
                        #print("Start: Processing MMAC Units \n")
                        #self.mmacUnitOperations = self.mmacUnitOperations + 1
                        # form a MMAC unit
                        #self.formMMACUnit()
                        #print("End: Processing MMAC Units \n")
                        pass
                    
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
        
        # check if the optimie PCAN is set or not
        if self.optimisePCANToRemoveDuplicatePCAN == True:
            # configure the optimiser
            self.configurePCArithmeticNodeOptimiser()
            print("Start - Optimisation of PCAN to remove duplicate PCAN")
            # use the optimiser and process the arithmetic nodes
            self.pcArithmeticNodeOptimiser.process()
            print("End - Optimisation of PCAN and removed duplicate PCAN")

        
    """
    #End: performPCOperation function
    """
    
    """
    # Start: resetPCOperation function
    """
    def resetPCOperation(self):
        # reset the equation parser
        super().resetEquationParser()
        # reset the other lists related to the operation
        self.productNodes = list()
        # new property to store the sumNodes
        self.sumNodes = list()
        # new property to store both the arithmetic nodes
        self.arithmeticNodes = list()
        # new property to store the arithmetic node ports
        self._arithmeticNodePorts = list()
        
    """
    # End: resetPCOperation function
    """
    
    """
    # Start: connectPCArithmeticNodeOptimiser
    """
    def connectPCArithmeticNodeOptimiser(self):
        self.pcArithmeticNodeOptimiser = PCArithmeticNodesOptimiser()
        

    """
    # End: connectPCArithmeticNodeOptimiser
    """



    """
    #Start: configurePCArithmeticNodeOptimiser
    """
    def configurePCArithmeticNodeOptimiser(self):
        self.pcArithmeticNodeOptimiser.configurationDetails = {"OptimisatisePCANToRemoveDuplicatePCAN":self.optimisePCANToRemoveDuplicatePCAN,"ArithmeticNodes":self.arithmeticNodes}
        self.pcArithmeticNodeOptimiser.configure()

    """
    #End: configurePCArithmeticNodeOptimiser
    """


    """
    #Start - configure PCOperation
    """
    def configure(self):
        self.configurePCArithmeticNodeOptimiser()

    """
    #End - configure PCOperation
    """

    
    def main(self):
        self.performPCOperation()
    
    def run(self):
        self.main()
