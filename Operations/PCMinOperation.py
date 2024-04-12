#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 13:12:54 2022

@author: 1003907
"""

from Operations.EquationParser import EquationParser
from Operations.ProductNode import ProductNode
from Operations.MinNode import MinNode

class PCMinOperation (EquationParser.EquationParser):
    
    def __init__(self):
        super().__init__()
        
        # every PCOperation needs PCEquaiton.
        # PCEquation is set by the PCSystem
        self.equation = None
        print("PCEquation string is set:", self.equation)
        
        """
        # Start: Properties of the PCMinOperation needed by the PCSystem
        1. It has the details of the productNodes, minNodes and arithmeticNodes.
        """
        # initialise the new property to store the productNodes
        self.productNodes = list()
        # new property to store the sumNodes
        self.minNodes = list()
        # new property to store both the arithmetic nodes
        self.arithmeticNodes = list()
        # set the list of ports to the entity PCMinOperation
        self.ports = list()
        # property to manage the inputs to ports
        self.inputToPorts = dict()
        # property to store the min value after the analysis
        self.minValue = 0
        # property to keep track of the min operations
        self.minOperations = 0
        
    
    """
    # Start: performMinOperation
    """
    def performOperation(self):
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
                    # set the input1 of the productNode
                    productNode.input1 = operationValue
                    # set the input2 of the productNode
                    productNode.input2 = operandValue
                    # the productNode mayhave a port or ports
                    # so we need to access the port object and 
                    # its name to find out the corresponding input binary string
                    # loop through the ports and set the inputs again to calculate the values
                    for port in productNode.ports:
                        # check the port name and access the port NUmber
                        if productNode.portsInfo[port.name] == '1':
                            #print the original input1 of ProductNode
                            print("Original input1 of productNode:", productNode.input1)
                            #print("InputValue for input1 of ProductNode:", self.inputToPorts[port.name])
                            # check the inputs to port for the particular port is available or not
                            # set the portName as a key and set the value of the key to 1 in a global dictionary
                            # set the input to 1 for anyport
                            self.inputToPorts[port.name] = "1"
                            productNode.input1 = self.inputToPorts[port.name]
                            #print the updated input1 of ProductNode
                            print("Updated input1 of productNode:", productNode.input1)
                            # set the input2 of the productNode
                            productNode.input2 = operandValue
                        elif productNode.portsInfo[port.name] == '2':
                            # set the input1 of the productNode
                            productNode.input1 = operationValue
                            print("Original Input2 of productNode:", productNode.input2)
                            #print("InputValue for input2 of ProductNode:", self.inputToPorts[port.name])
                            # set the input to 1 for anyport
                            #print("Original inputToPorts value", self.inputToPorts[port.name], " for PortName:", port.name)
                            self.inputToPorts[port.name] = "1"
                            print("Updated inputToPorts value", self.inputToPorts[port.name], " for PortName:", port.name)
                            productNode.input2 = self.inputToPorts[port.name]
                            #print the updated input1 of ProductNode
                            print("Updated Input2 of productNode:", productNode.input2)
                    
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
                    #perform sensitivity analysis
                    minNode = MinNode.MinNode()
                    # set the minNode number
                    minNode.number = len(self.minNodes)
                    # set the input1 of the minNode
                    minNode.input1 = operationValue
                    # set the input2 of the minNode
                    minNode.input2 = operandValue
                    #check the ports of the minNode
                    # the productNode has a port
                    # so we need to access the port object and 
                    # its name to find out the corresponding input binary string
                    # loop through the ports and set the inputs again to calculate the values
                    for port in minNode.ports:
                        # check the port name and access the port NUmber
                        if minNode.portsInfo[port.name] == '1':
                            print("Original input1 of minNode:", minNode.input1)
                            # set the input to 1 for anyport
                            self.inputToPorts[port.name] = "1"
                            minNode.input1 = self.inputToPorts[port.name]
                            #print the updated input1 of minNode
                            print("Updated input1 of minNode:", minNode.input1)
                            # set the input2 of the minNode
                            minNode.input2 = operandValue
                        elif minNode.portsInfo[port.name] == '2':
                            # set the input to 1 for anyport
                            self.inputToPorts[port.name] = "1"
                            # set the input1 of the minNode
                            minNode.input1 = operationValue
                            minNode.input2 = self.inputToPorts[port.name]
                            
                    if minNode.outputValue != None:
                        # set the operationValue to the outputValue
                        operationValue = minNode.outputValue
                    else:
                        # set the output of the maxNode
                        operationValue = minNode.output
                   
                    # set the minNode ports
                    self.arithmeticNodePorts = minNode.ports
                    #append the minNode to the maxNodes array
                    self.minNodes.append(minNode)
                    # add the minNode to the arithmetic node
                    self.arithmeticNodes.append(minNode)
                    # increase the addition operation counter
                    self.minOperations = self.minOperations + 1
                            
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
    # Start: performPCMinOperation function
    """
    
    def performPCMinOperation(self):
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
            self.minValue = self.operandValueStack[0]            
        
    """
    #End: performPCMinOperation function
    """
    
    """
    # Start: resetPCMinOperation function
    """
    def resetPCMinOperation(self):
        # reset the equation parser
        super().resetEquationParser()
        # reset the other lists related to the operation
        self.productNodes = list()
        # new property to store the minNodes
        self.minNodes = list()
        # new property to store both the arithmetic nodes
        self.arithmeticNodes = list()
        # new property to store the arithmetic node ports
        self._arithmeticNodePorts = list()
        # reset the inputToPorts
        self.inputToPorts = dict()
    """
    # End: resetPCMinOperation function
    """
    
    def main(self):
        self.performPCMinOperation()
   
    def run(self):
        self.main()

    
