#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 23 15:23 2023

@author: Karthekeyan Periasamy
"""
from SWSynthesisers.SWSynthesiser import SWSynthesiser

class SWPCTreeSynthesiser(SWSynthesiser):
    
    def __init__(self):
        super().__init__()

    
    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        super().connectProperties()

        #property to store the copy of the arithmetic nodes
        self.copyOfArithmeticNodes = None

        #property to store the total number of adders
        self.totalNumberOfAdders = 0

        # property to store the total number of multipliers
        self.totalNumberOfMultipliers = 0

        # property to store the number of adders traversed while forming the PCTree
        self.numberOfTraversedAdders = 0

        # property to store the number of multipliers traversed while forming the PCTree
        self.numberOfTraversedMultipliers = 0
        
        self.topArithmeticNode = None


    def configure(self):
        super().configure()
        
        configurationDetails = self.configurationDetailsOfSynthesiser

        if "TotalNumberOfAdders" in configurationDetails:
            self.totalNumberOfAdders = configurationDetails["TotalNumberOfAdders"]

        if "TotalNumberOfMultipliers" in configurationDetails:
            self.totalNumberOfMultipliers = configurationDetails["TotalNumberOfMultipliers"]



    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()
        
        #property to store the copy of the arithmetic nodes
        self.copyOfArithmeticNodes = None
        
        #property to store the total number of adders
        self.totalNumberOfAdders = 0

        # property to store the total number of multipliers
        self.totalNumberOfMultipliers = 0

        # property to store the number of adders traversed while forming the PCTree
        self.numberOfTraversedAdders = 0

        # property to store the number of multipliers traversed while forming the PCTree
        self.numberOfTraversedMultipliers = 0

        # property to store the topArithmeticNode of the PCTree
        self.topArithmeticNode = None

       
    def process(self):
        """
        1. Arithmetic Nodes Copy 
        """
        # make a copy of the arithmeticNodes array
        self.copyOfArithmeticNodes = self.arithmeticNodes.copy()
        #print("PCTree ArithmeticNodes", self.copyOfArithmeticNodes)
    
    
    def formChildArithmeticNodes(self,currentNode):
        """
        1. Split the input variable
        2. Access the last element of the split variable
        3. Go to the index and access the respective arithmeticNode
        4. Check the arithmeticNode input whether its from another arithmeticNode or from a port
        5. Repeat the above process till we reach the arithmeticNode with ports
        6. While recurse through the array elements, we store the total number of adders and multipliers traversed
        """
        #compare whether the inputNodeName is Adder or Multiplier
        if currentNode.name == "Adder":
            #print("Driver of Current Node Name", driverOfCurrentNode.name)
            #print("Driver of Current Node is an Adder and its Equation", currentNode.equation)
            self.numberOfTraversedAdders = self.numberOfTraversedAdders + 1

        elif currentNode.name == "Multiplier":
            #print("Driver of Current Node Name", driverOfCurrentNode.name)
            #print("Driver of Current Node is a Multiplier and its Equation", currentNode.equation)
            # update the number of multplication operations traversed
            self.numberOfTraversedMultipliers = self.numberOfTraversedMultipliers + 1

        if (len(currentNode.swOperator.drivers)) == 0:
            #print("Current Node is a Leaf node with input1 and input2", currentNode.input1, currentNode.input2)
            return
       
        
        # if the drivers of current are not ports, recursively reach the next level of the driven current node
        if (len(currentNode.swOperator.drivers) > 1):
            
            # access the currentNode Input  that contains the current node input
            decodedInput = currentNode.input1.split("_")

            # split the input string
            #print("Decoded Input1 List",decodedInput)

            # access the last index element to get the index which drives the input to the current node
            inputNodeIndex = int(decodedInput[(len(decodedInput)-1)])
            #print("InputNode Index", inputNodeIndex)

            # using the inputNode Index we can access the driver of current Node
            driverOfCurrentNode = self.copyOfArithmeticNodes[inputNodeIndex]
            #print("Driver of Current Node is a ", driverOfCurrentNode.name)

            # update the left child of the current node with the driver of the current node
            currentNode.swOperator.leftChild = driverOfCurrentNode
            #print("The current node equation and The current node left child equation", currentNode.equation, currentNode.swOperator.leftChild.equation)

            #print("Recurse to arithmeticNode with equation",  currentNode.swOperator.leftChild.equation)
            # recursively reach the next arithmetic node
            self.formChildArithmeticNodes(driverOfCurrentNode)
            
            # access the currentNode Input  that contains the current node input
            decodedInput = currentNode.input2.split("_")

            # split the input string
            #print("Decoded Input2 List",decodedInput)

            # access the last index element to get the index which drives the input to the current node
            inputNodeIndex = int(decodedInput[(len(decodedInput)-1)])

            # using the inputNode Index we can access the driver of current Node
            driverOfCurrentNode = self.copyOfArithmeticNodes[inputNodeIndex]
            #print("Driver of Current Node is a ", driverOfCurrentNode.name)

                    
            # update the right child of the current node with the driver of the current node
            currentNode.swOperator.rightChild = driverOfCurrentNode
            #print("The current node equation and The current node right child equation", currentNode.equation, currentNode.swOperator.rightChild.equation)
            
            #print("Recurse in right direction of",  currentNode.swOperator.rightChild.equation)
            # recursively reach the next arithmetic node
            self.formChildArithmeticNodes(driverOfCurrentNode)
        
        elif (len(currentNode.swOperator.drivers) == 1):
            
            # find whether input1 or input2 is a port or weight
            if (currentNode.swOperator.input1Driver.isDriverAnArithmeticNode == True):
                
                # access the currentNode Input  that contains the current node input
                decodedInput = currentNode.input1.split("_")

                # split the input string
                #print("Decoded Input1 List",decodedInput)

                # access the last index element to get the index which drives the input to the current node
                inputNodeIndex = int(decodedInput[(len(decodedInput)-1)])

                # using the inputNode Index we can access the driver of current Node
                driverOfCurrentNode = self.copyOfArithmeticNodes[inputNodeIndex]
                #print("Driver of Current Node is a ", driverOfCurrentNode.name)

                
                #print("Input1 Driver an arithmetic Node", driverOfCurrentNode.swOperator.input1Driver.isDriverAnArithmeticNode)
                #print("Input2 Driver an arithmetic Node", driverOfCurrentNode.swOperator.input2Driver.isDriverAnArithmeticNode)
                
                currentNode.swOperator.leftChild = driverOfCurrentNode
                #print("The current node equation and The current node left child equation", currentNode.equation, currentNode.swOperator.leftChild.equation)
                
                #print("Input2 is a weight, Input1Driver is an arithmeticNode")
                #print("Equation of the driver of current node", driverOfCurrentNode.swOperator.equation)
                #print("Input1 of driverOfCurrentNode Name", driverOfCurrentNode.input1)
                #print("Input2 of driverOfCurrentNode Name", driverOfCurrentNode.input2)
                
                #print("Recurse to arithmeticNode with equation",  currentNode.swOperator.leftChild.equation)
                self.formChildArithmeticNodes(driverOfCurrentNode)
                
            elif (currentNode.swOperator.input2Driver.isDriverAnArithmeticNode == True):
                
                # access the currentNode Input  that contains the current node input
                decodedInput = currentNode.input2.split("_")

                # split the input string
                #print("Decoded Input List",decodedInput)

                # access the last index element to get the index which drives the input to the current node
                inputNodeIndex = int(decodedInput[(len(decodedInput)-1)])

                # using the inputNode Index we can access the driver of current Node
                driverOfCurrentNode = self.copyOfArithmeticNodes[inputNodeIndex]
                #print("Driver of Current Node is a ", driverOfCurrentNode.name)
                
                currentNode.swOperator.rightChild = driverOfCurrentNode
                #print("The current node equation and The current node right child equation", currentNode.equation, currentNode.swOperator.rightChild.equation)
                
                #print("Input1 is a weight, Input2Driver is an arithmeticNode")
                #print("Equation of the driver of current node", driverOfCurrentNode.swOperator.equation)
                #print("Input1 of driverOfCurrentNode Name", driverOfCurrentNode.input1)
                #print("Input2 of driverOfCurrentNode Name", driverOfCurrentNode.input2)
               
                #print("Recurse to arithmeticNode with equation",  currentNode.swOperator.rightChild.equation)
               
               
                # recursively reach the next arithmetic node
                self.formChildArithmeticNodes(driverOfCurrentNode)

       
    def perform(self):
        """
        1. Processing includes finding the left and right child of the node, starting from the top sum Node 
        2. For every SumNode inputs, check the connected productNodes and other sum nodes recursively
        """

        # access the top arithmetic node
        # preassumably the top node is always a sum node
        topArithmeticNode = self.copyOfArithmeticNodes[len(self.copyOfArithmeticNodes)-1]
                
        ### non linearisation of the linearised array based arithmetic nodes information to form the PCTree
        
        # process the child arithmetic nodes,
        self.formChildArithmeticNodes(topArithmeticNode)
        
        # set the topNode
        self.topArithmeticNode = topArithmeticNode

        # print the top arithmetic node
        print("Top Arithmetic Node",self.topArithmeticNode)
       
        # print the number of adders traversed
        print("Number of Traversed Adders", self.numberOfTraversedAdders)
        
        # print the number of multipliers traversed
        print("Number of Traversed Multipliers", self.numberOfTraversedMultipliers)

    
    def main(self):
        self.process()
        self.perform()
    
    def run(self):
        self.main()
