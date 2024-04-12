#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:40:01 2022

@author: Karthekeyan Periasamy
"""

from Operations.EquationParser import EquationParser
from Operations.ProductNode import ProductNode
from Operations.MaxNode import MaxNode


class PCMaxOperation (EquationParser.EquationParser):
    
    def __init__(self):
        super().__init__()
        
        # every PCOperation needs PCEquaiton.
        # PCEquation is set by the PCSystem
        self.equation = None
        
        """
        # Start: Properties of the PCMaxOperation needed by the PCSystem
        1. It has the details of the productNodes, maxNodes and arithmeticNodes.
        """
        # initialise the new property to store the productNodes
        self.productNodes = list()
        # new property to store the sumNodes
        self.maxNodes = list()
        # new property to store both the arithmetic nodes
        self.arithmeticNodes = list()
        # set the list of ports to the entity PCMinOperation
        self.ports = list()
        # property to store the min value after the analysis
        self.maxValue = 0
    
# =============================================================================
# Function definitions
# =============================================================================
    
    
    def performOperation(self):
        """
        Function to perform MPEInference, here MPEInference means MaxNode will be used instead of SumNode
        Returns
        -------
        bool
            DESCRIPTION. The return of the operation would help make further decisions.
            Still, this return function and the use of it can be made more nice.

        """
        # check the length of the operandValueStack
        operandValueStackLength = len(self.operandValueStack)
        # if the length of the operandValueStack is less than 2
        if (operandValueStackLength < 2):
            # abort the operation as operandValues are not enough to perfom operation
            return False
        # print the operator
        print("The operator: \n", self.currentOperator)
        # set the number of operations to number of operators
        numberOfOperators = self.currentNumberOfOperators
        #print("NumberOfOperators: \n", numberOfOperators)
        # make the startrange, stop range to access the required number of operandValues
        numberOfOperandValuesToBeAccessed = numberOfOperators + 1
        print("NumberOfOperandValuesToBeAccessed: \n", numberOfOperandValuesToBeAccessed)
        # print the stack of the operandValueStack
        print("OriginalOperandValueStack \n",self.operandValueStack)
        # design the start range for the for loop
        startRange = (len(self.operandValueStack)-1)
        print("The start range \n",startRange)
        # design the stop range for the loop
        operandValueLength = (len(self.operandValueStack))
        # the stop range for the for loop to access the operandValueStack
        stopRange = ((operandValueLength - numberOfOperandValuesToBeAccessed) - 1)
        print("The stop range \n",stopRange)
        # set a counter variable to count the number of maxNode the function will generate
        maxNodes = 0
                              
        # append the existing elements of the operandElementStack
        # as its a stack LIFO retreival scheme should be followed to correctly represent the operandValues
        # also, the operandValues are the one available for this closed and opening brackets to be computed
        operationValue = None
        for indexOfOperandValue in range(startRange,stopRange,-1):
            # access and set again the relevant operator for the whole range
            # It helps support multiple type of operations
            # print the indexOfOperangValue
            print("The index of  operand value : \n", indexOfOperandValue)
            # access the operandValue using the index
            operandValue = self.operandValueStack[indexOfOperandValue]
            # print the indexOfOperandElement and operandElement
            print("IndexOfOperandValue , OperandValue: \n", indexOfOperandValue, operandValue)
            # check the indexOfOperandValue, if its top element index we need to set the operandValue with the firstElement
            if indexOfOperandValue == (len(self.operandValueStack)-1):
                operationValue = operandValue
                # print the updated operationValue
                print( "The updated operationValue: ", operationValue)
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
                    # set the number of bits of the productNode
                    productNode.numberOfBits = self.numberOfBits
                    # set the mantissaBits of the productNode
                    productNode.mantissaBits = self.mantissaBits
                    # set the exponentBits of the productNode
                    productNode.exponentBits = self.exponentBits
                    # set the exponentBits of the productNode
                    productNode.esBits = self.esBits
                    # set the opertionMode
                    productNode.operationMode = self.operationMode
                    # set the analysis mode
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
                    # initialise max node or min node based on the analysisMode
                    # analysisMode 0 = sensitivity Analysis
                    # analysisMode 1 = MPEInference
                    
                    # MPE Inference analysis entities
                    maxNode = MaxNode.MaxNode()
                    # set the maxNode number
                    maxNode.number = len(self.maxNodes)
                    # set the number of bits of the maxNode
                    maxNode.numberOfBits = self.numberOfBits
                    # set the mantissaBits of the maxNode
                    maxNode.mantissaBits = self.mantissaBits
                    # set the exponentialBits of the maxNode
                    maxNode.exponentialBits = self.exponentialBits
                    # set the esBits of the maxNode
                    maxNode.esBits = self.esBits
                    # set the opertionMode
                    maxNode.operationMode = self.operationMode
                    # set the analysis mode
                    maxNode.analysisMode = self.analysisMode
                    # set the numberSystem of the maxNode
                    maxNode.numberSystem = self.numberSystem
                    # set the input1 of the maxNode
                    maxNode.input1 = operationValue
                    # set the input2 of the maxNode
                    maxNode.input2 = operandValue
                
                    # check if the outputValue is available or not
                    if maxNode.outputValue != None:
                        # set the operationValue to the outputValue
                        operationValue = maxNode.outputValue
                    else:
                        # set the output of the maxNode
                        operationValue = maxNode.output
                        
                    print("Number of max operators:", numberOfOperators)
                    print("Original Number of maxNodes", maxNodes)
                    maxNodes = maxNodes + 1
                    print("Updatexd Number of maxNodes", maxNodes)
                    if maxNodes == numberOfOperators:
                        print("Computational Units can be formed")
                        self.mmacUnitOperationsPerformed = self.mmacUnitOperationsPerformed + 1
                        # form a computational unit
                        # self.formMMACUnit()
                   
                    # set the maxNode ports
                    self.arithmeticNodePorts = maxNode.ports
                    #append the maxNode to the maxNodes array
                    self.maxNodes.append(maxNode)
                    # add the maxNode to the arithmetic node
                    self.arithmeticNodes.append(maxNode)
                    # increase the addition operation counter
                    self.maxOperations = self.maxOperations + 1
                        
                        
        # print the final operationValue
        print( "The updated operationValue: ", operationValue)
        # pop the operandValueStack
        self.popOperandValueStack(startRange, stopRange)
        # push the calculated new operandValues into operandValueStack
        self.pushIntoOperandValueStack(operationValue)
        # pop the operator or operators from the bracketsAndOperatorStack
        # before popping print the number of operators
        print( "The number of opertators to be popped: ", numberOfOperators)
        self.popOperatorsFrombracketsAndOperatorStack(numberOfOperators)
        return True
    
    """
    # End: performOperation
    """
    
    """
    # Start: performPCMaxOperation function
    """
    
    def performPCMaxOperation(self):
        # parse th equation and generate the min value
        # use the minvalue to do analysis
        super().parseEquation()
        # once the equation is parsed
        # access the operandValueStack
        # check the number of values in operandValueStack, it should not be more than one
        if (len(self.operandValueStack) > 1):
            # throw an error
            print("Error: Parsing failed during PCMinOperation")
        elif (len(self.operandValueStack) == 1):
            # set the min value property
            self.maxValue = self.operandValueStack[0]            
        
    """
    #End: performPCMaxOperation function
    """
    
    """
    # Start: resetPCMaxOperation function
    """
    def resetPCMaxOperation(self):
        # reset the equation parser
        super().resetEquationParser()
        # reset the other lists related to the operation
        self.productNodes = list()
        # new property to store the maxNodes
        self.maxNodes = list()
        # new property to store both the arithmetic nodes
        self.arithmeticNodes = list()
        # new property to store the arithmetic node ports
        self._arithmeticNodePorts = list()
      
    """
    # End: resetPCMaxOperation function
    """
    
    def main(self):
        self.performPCMaxOperation()
   
    def run(self):
        self.main()

