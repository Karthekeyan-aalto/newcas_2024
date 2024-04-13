"""
Created by Karthekeyan Periasamy
Edited on April 29, 2023
"""

from SWOptimisers.PCOptimiser import PCOptimiser

class PCArithmeticNodesOptimiser(PCOptimiser):

    def __init__(self):
        super().__init__()

        #property to know the removeDuplicationPCAN property is set or not
        self.removeDuplicatePCAN = False

        # property to store the optimised arithmetic nodes
        self.optimisedArithmeticNodes = None


    def configure(self):
        super().configure()
        
        if self.arithmeticNodes == None:
            return
        else:
            # set the arithmeticNodes to optimise arithmetic nodes
            self.optimisedArithmeticNodes = self.arithmeticNodes.copy()
        
        
        if "OptimisatisePCANToRemoveDuplicatePCAN" in self.configurationDetails:
            self.removeDuplicatePCAN = self.configurationDetails["OptimisatisePCANToRemoveDuplicatePCAN"]


    def removeDuplicateArithmeticNodes(self):
        duplicateNodeDetails = dict()
        duplicateNodeIndiciesDetails = dict()
        visitedArithmeticNodes = list()
        for arithmeticNodeIndex, arithmeticNode in enumerate(self.arithmeticNodes):
            # print the arithmeticNode Index if the nextArithmetic Node Index is 307
            #if arithmeticNodeIndex == 307:
                #print("ArithmeticNode Index", arithmeticNodeIndex)
                #print("The VHDL Description of the ArithmeticNode",arithmeticNode.vhdlInstance)

            # check whether arithmetic node has been visited or not
            if arithmeticNode in visitedArithmeticNodes:
                continue
            else:
                # add teh arithmeticNode to the visited arithmetic nodes
                visitedArithmeticNodes.append(arithmeticNode)
            
            # using the arithemtic node index, we have to set the range
            if arithmeticNode.receiverEquation != None:
                numberOfDuplicateNodes = 0
                duplicateNodeIndices = list()
                for nextArithmeticNodeIndex in range((arithmeticNodeIndex+1), len(self.arithmeticNodes)):
                    nextArithmeticNode = self.arithmeticNodes[nextArithmeticNodeIndex]
                    if nextArithmeticNode in visitedArithmeticNodes:
                        continue
                    # now check the equation
                    if nextArithmeticNode.receiverEquation != None:
                        #if isinstance(nextArithmeticNode, ProductNode):
                        #print("ArithmeticNode Receiver Equation", arithmeticNode.receiverEquation)
                        if nextArithmeticNode.receiverEquation == arithmeticNode.receiverEquation:
                            # print the arithmeticNode Index if the nextArithmetic Node Index is 307
                            #if nextArithmeticNodeIndex == 307:
                                #print("NextArithmeticNode is matched with ArithmeticNode Index", arithmeticNodeIndex)
                                #print("The VHDL Description of the matched ArithmeticNode",arithmeticNode.vhdlInstance)
                                #print("The VHDL Description of the NextArithmeticNode",nextArithmeticNode.vhdlInstance)

                                #print("Matched NextArithmeticNode Equation",arithmeticNode.receiverEquation)
                                #print("Matched ArithmeticNode Equation",nextArithmeticNode.receiverEquation)


                            #print("NextArithmeticNode Receiver Equation", nextArithmeticNode.receiverEquation)
                            # add the nextArithmeticNode to visited Arithmetic Nodes
                            visitedArithmeticNodes.append(nextArithmeticNode)
                            # check which node has the input of the nextArithmeticNode equation
                            for receiverIndex in range((nextArithmeticNodeIndex+1), len(self.arithmeticNodes)):
                                receiverNode = self.arithmeticNodes[receiverIndex]
                                if receiverNode.input1  == nextArithmeticNode.output:
                                    # print the driver of the nextArithmetic node input1 if the nextArithmetic Node Index is 307
                                    #if nextArithmeticNodeIndex == 307:
                                        #print("The original input1 of the driver of NextArithmetic Node with Index 307 is ",receiverNode.input1)

                                    # change the input1 with the output of the arithmeticNode output
                                    # regenerate the vhdl instance and signal of the node
                                    #print("The receiver node input1", receiverNode.input1)
                                    #print("The receiver node arithmeticNode Index", receiverNode.arithmeticNodeNumber)
                                    
                                    # access the optimised arithmetic node
                                    # access the arithemeticNode using arithmeticNode index
                                    # access the receiverNode using the receiver node index
                                    toBeOptimisedArithmeticNodeIndex = self.optimisedArithmeticNodes.index(arithmeticNode)
                                    toBeOptimisedArithmeticNode = self.optimisedArithmeticNodes[toBeOptimisedArithmeticNodeIndex]
                                    toBeOptimisedReceiverArithmeticNodeIndex = self.optimisedArithmeticNodes.index(receiverNode)
                                    toBeOptimisedReceiverArithmeticNode = self.optimisedArithmeticNodes[toBeOptimisedReceiverArithmeticNodeIndex]
                                            
                                    # access the output and set the to be optimised arithmetic node input1
                                    toBeOptimisedReceiverArithmeticNode.input1 = toBeOptimisedArithmeticNode.output
                                    
                                    toBeOptimisedReceiverArithmeticNode.performHWGeneration()
                                    # print the driver of the nextArithmetic node input1 if the nextArithmetic Node Index is 307
                                    #if nextArithmeticNodeIndex == 307:
                                        #print("The updated input1 of the driver of NextArithmetic Node with Index 307 is ",toBeOptimisedReceiverArithmeticNode.input1)
                                        #print("The original driver of NextArithmetic Node VHDL Instance", toBeOptimisedReceiverArithmeticNode.vhdlInstance)
                                        #toBeOptimisedReceiverArithmeticNode.processHWGeneration()
                                        
                                        #print("The updated driver of NextArithmetic Node VHDL Instance", toBeOptimisedReceiverArithmeticNode.vhdlInstance)

                                        #print("The name of the driver of NextArithmetic Node, that is toBeOptimisedArithemeticNode is",(toBeOptimisedReceiverArithmeticNode.name)+str(toBeOptimisedReceiverArithmeticNode.number))
                                    #print("Original length of the arithmetic nodes",len(self.optimisedArithmeticNodes))
                                    self.optimisedArithmeticNodes.remove(nextArithmeticNode)
                                    #print("Updated length of the arithmetic nodes",len(self.optimisedArithmeticNodes))
                                    break
                                
                                elif receiverNode.input2 == nextArithmeticNode.output:
                                    # print the driver of the nextArithmetic node input1 if the nextArithmetic Node Index is 307
                                    #if nextArithmeticNodeIndex == 307:
                                        #print("The original input2 of the driver of NextArithmetic Node with Index 307 is ",receiverNode.input2)

                                    #print("The receiver node input2", receiverNode.input2)
                                    #print("Replace the receiver node input2 with", arithmeticNode.output)
                                    #print("The receiver node arithmeticNode Index", receiverNode.arithmeticNodeNumber)
                                            
                                    # access the optimised arithmetic node
                                    # access the arithemeticNode using arithmeticNode index
                                    # access the receiverNode using the receiver node index
                                    toBeOptimisedArithmeticNodeIndex = self.optimisedArithmeticNodes.index(arithmeticNode)
                                    toBeOptimisedArithmeticNode = self.optimisedArithmeticNodes[toBeOptimisedArithmeticNodeIndex]
                                    toBeOptimisedReceiverArithmeticNodeIndex = self.optimisedArithmeticNodes.index(receiverNode)
                                    toBeOptimisedReceiverArithmeticNode = self.optimisedArithmeticNodes[toBeOptimisedReceiverArithmeticNodeIndex]

                                    # print the original VHDL instance of the toBeOptimisedReceiverArithmeticNode
                                    #print("To Be Optimised ArithmeticNode VHDL Instance",toBeOptimisedReceiverArithmeticNode.vhdlInstance)
                                    # access the output and set the to be optimised arithmetic node input2
                                    toBeOptimisedReceiverArithmeticNode.input2 = toBeOptimisedArithmeticNode.output

                                    toBeOptimisedReceiverArithmeticNode.performHWGeneration()
                                    # print the updated VHDL instance of the toBeOptimisedReceiverArithmeticNode
                                    #print("Optimised ArithmeticNode VHDL Instance",toBeOptimisedReceiverArithmeticNode.vhdlInstance)
                                    
                                    # print the driver of the nextArithmetic node input1 if the nextArithmetic Node Index is 307
                                    #if nextArithmeticNodeIndex == 307:
                                        #print("The updated input2 of the driver of NextArithmetic Node with Index 307 is ",toBeOptimisedReceiverArithmeticNode.input2)
                                        #print("The original driver of NextArithmetic Node VHDL Instance", toBeOptimisedReceiverArithmeticNode.vhdlInstance)
                                        #toBeOptimisedReceiverArithmeticNode.processHWGeneration()
                                        
                                        #print("The updated driver of NextArithmetic Node VHDL Instance", toBeOptimisedReceiverArithmeticNode.vhdlInstance)

 
                                        #print("The name of the driver of NextArithmetic Node, that is toBeOptimisedArithemeticNode is",toBeOptimisedReceiverArithmeticNode.name)


                                    #print("Original length of the arithmetic nodes",len(self.optimisedArithmeticNodes))
                                    self.optimisedArithmeticNodes.remove(nextArithmeticNode)
                                    #print("Updated length of the arithmetic nodes",len(self.optimisedArithmeticNodes))
                                    break
                            
                            numberOfDuplicateNodes = numberOfDuplicateNodes + 1
                            duplicateNodeIndices.append(nextArithmeticNodeIndex)
                            #print("The output of the nextArithmeticNode", nextArithmeticNode.output)
                            #print("Two ProductNodes have same equation",arithmeticNode.receiverEquation)
                            
                        else:
                            #print("Next ArithmeticNode Receiver Equation that is not matched" + nextArithmeticNode.receiverEquation + "with ArithmeticNodeReceiver equation", arithmeticNode.receiverEquation)
                            pass
                
                #print("The duplication nodes are", numberOfDuplicateNodes)
                #print("Original Duplicate Nodes Details", duplicateNodeDetails)
                # check if the number of duplicates is greater than zero or not
                if numberOfDuplicateNodes > 0:
                    duplicateNodeDetails[arithmeticNode.receiverEquation] = numberOfDuplicateNodes
                    duplicateNodeIndiciesDetails[str(arithmeticNodeIndex)] = duplicateNodeIndices
                #print("Updated Duplicate Nodes Details", duplicateNodeDetails)
                    
            
        #print("Total duplicate node details", duplicateNodeDetails)
        #print("Duplicate Node Indices Details", duplicateNodeIndiciesDetails)
    
    
    def disableDuplicateArithmeticNodes(self):
        duplicateNodeDetails = dict()
        duplicateNodeIndiciesDetails = dict()
        visitedArithmeticNodes = list()
        duplicateNodeDetailsWithTheirReceivers = dict() 
        
        for arithmeticNodeIndex, arithmeticNode in enumerate(self.arithmeticNodes):
            # print the arithmeticNode Index if the nextArithmetic Node Index is 307
            #if arithmeticNodeIndex == 307:
                #print("ArithmeticNode Index", arithmeticNodeIndex)
                #print("The VHDL Description of the ArithmeticNode",arithmeticNode.vhdlInstance)

            # check whether arithmetic node has been visited or not
            if arithmeticNode in visitedArithmeticNodes:
                continue
            else:
                # add teh arithmeticNode to the visited arithmetic nodes
                visitedArithmeticNodes.append(arithmeticNode)
            # using the arithemtic node index, we have to set the range
            if arithmeticNode.receiverEquation != None:
                numberOfDuplicateNodes = 0
                duplicateNodeIndices = list()
                duplicateNodeIndicesWithTheirReceiverDetails = dict()
                duplicateNodeReceiverIndices = list()
                for nextArithmeticNodeIndex in range((arithmeticNodeIndex+1), len(self.arithmeticNodes)):
                    nextArithmeticNode = self.arithmeticNodes[nextArithmeticNodeIndex]
                    if nextArithmeticNode in visitedArithmeticNodes:
                        continue
                    
                    # now check the equation
                    if nextArithmeticNode.receiverEquation != None:
                        #if isinstance(nextArithmeticNode, ProductNode):
                        #print("ArithmeticNode Receiver Equation", arithmeticNode.receiverEquation)
                        if nextArithmeticNode.receiverEquation == arithmeticNode.receiverEquation:
                            #print("ArithmeticNode Index", arithmeticNodeIndex)
                            #print("NextArithmeticNode Index", nextArithmeticNodeIndex)

                            # print the arithmeticNode Index if the nextArithmetic Node Index is 307
                            #if nextArithmeticNodeIndex == 307:
                                #print("NextArithmeticNode is matched with ArithmeticNode Index", arithmeticNodeIndex)
                                #print("The VHDL Description of the matched ArithmeticNode",arithmeticNode.vhdlInstance)
                                #print("The VHDL Description of the NextArithmeticNode",nextArithmeticNode.vhdlInstance)

                                #print("Matched NextArithmeticNode Equation",arithmeticNode.receiverEquation)
                                #print("Matched ArithmeticNode Equation",nextArithmeticNode.receiverEquation)


                            #print("NextArithmeticNode Receiver Equation", nextArithmeticNode.receiverEquation)
                            # add the nextArithmeticNode to visited Arithmetic Nodes
                            visitedArithmeticNodes.append(nextArithmeticNode)
                            # check which node has the input of the nextArithmeticNode equation
                            for receiverIndex in range((nextArithmeticNodeIndex+1), len(self.arithmeticNodes)):
                                receiverNode = self.arithmeticNodes[receiverIndex]
                                if receiverNode.input1  == nextArithmeticNode.output:
                                    #print("Receiver ArithmeticNode Index", receiverIndex)

                                    duplicateNodeReceiverIndices.append(receiverIndex)
                                    # print the driver of the nextArithmetic node input1 if the nextArithmetic Node Index is 307
                                    #if nextArithmeticNodeIndex == 307:
                                        #print("The original input1 of the driver of NextArithmetic Node with Index 307 is ",receiverNode.input1)

                                    # change the input1 with the output of the arithmeticNode output
                                    # regenerate the vhdl instance and signal of the node
                                    #print("The receiver node input1", receiverNode.input1)
                                    #print("The receiver node arithmeticNode Index", receiverNode.arithmeticNodeNumber)
                                    
                                    # access the optimised arithmetic node
                                    # access the arithemeticNode using arithmeticNode index
                                    # access the receiverNode using the receiver node index
                                    toBeOptimisedArithmeticNodeIndex = self.optimisedArithmeticNodes.index(arithmeticNode)
                                    toBeOptimisedArithmeticNode = self.optimisedArithmeticNodes[toBeOptimisedArithmeticNodeIndex]
                                    toBeOptimisedReceiverArithmeticNodeIndex = self.optimisedArithmeticNodes.index(receiverNode)
                                    toBeOptimisedReceiverArithmeticNode = self.optimisedArithmeticNodes[toBeOptimisedReceiverArithmeticNodeIndex]
                                            
                                    # access the output and set the to be optimised arithmetic node input1
                                    toBeOptimisedReceiverArithmeticNode.input1 = toBeOptimisedArithmeticNode.output
                                    
                                    toBeOptimisedReceiverArithmeticNode.performHWGeneration()
                                    # print the driver of the nextArithmetic node input1 if the nextArithmetic Node Index is 307
                                    #if nextArithmeticNodeIndex == 307:
                                        #print("The updated input1 of the driver of NextArithmetic Node with Index 307 is ",toBeOptimisedReceiverArithmeticNode.input1)
                                        #print("The original driver of NextArithmetic Node VHDL Instance", toBeOptimisedReceiverArithmeticNode.vhdlInstance)
                                        #toBeOptimisedReceiverArithmeticNode.processHWGeneration()
                                        
                                        #print("The updated driver of NextArithmetic Node VHDL Instance", toBeOptimisedReceiverArithmeticNode.vhdlInstance)

                                        #print("The name of the driver of NextArithmetic Node, that is toBeOptimisedArithemeticNode is",(toBeOptimisedReceiverArithmeticNode.name)+str(toBeOptimisedReceiverArithmeticNode.number))
                                    #print("Original length of the arithmetic nodes",len(self.optimisedArithmeticNodes))
                                    # disabling the nextArithmeticNode (for now we do not remove the node for testing)
                                    nextArithmeticNode.enable = False
                                    # print the nextArithmeticNode name
                                    #print("Next ArithmeticNode that is disabled is", nextArithmeticNode.name  + str(nextArithmeticNode.number) + "_" + str(nextArithmeticNode.arithmeticNodeNumber))

                                    #print("Updated length of the arithmetic nodes",len(self.optimisedArithmeticNodes))
                                    break
                                
                                elif receiverNode.input2 == nextArithmeticNode.output:
                                    #print("Receiver ArithmeticNode Index", receiverIndex)
                                    duplicateNodeReceiverIndices.append(receiverIndex)
                                    # print the driver of the nextArithmetic node input1 if the nextArithmetic Node Index is 307
                                    #if nextArithmeticNodeIndex == 307:
                                        #print("The original input2 of the driver of NextArithmetic Node with Index 307 is ",receiverNode.input2)

                                    #print("The receiver node input2", receiverNode.input2)
                                    #print("Replace the receiver node input2 with", arithmeticNode.output)
                                    #print("The receiver node arithmeticNode Index", receiverNode.arithmeticNodeNumber)
                                            
                                    # access the optimised arithmetic node
                                    # access the arithemeticNode using arithmeticNode index
                                    # access the receiverNode using the receiver node index
                                    toBeOptimisedArithmeticNodeIndex = self.optimisedArithmeticNodes.index(arithmeticNode)
                                    toBeOptimisedArithmeticNode = self.optimisedArithmeticNodes[toBeOptimisedArithmeticNodeIndex]
                                    toBeOptimisedReceiverArithmeticNodeIndex = self.optimisedArithmeticNodes.index(receiverNode)
                                    toBeOptimisedReceiverArithmeticNode = self.optimisedArithmeticNodes[toBeOptimisedReceiverArithmeticNodeIndex]

                                    # print the original VHDL instance of the toBeOptimisedReceiverArithmeticNode
                                    #print("To Be Optimised ArithmeticNode VHDL Instance",toBeOptimisedReceiverArithmeticNode.vhdlInstance)
                                    # access the output and set the to be optimised arithmetic node input2
                                    toBeOptimisedReceiverArithmeticNode.input2 = toBeOptimisedArithmeticNode.output

                                    toBeOptimisedReceiverArithmeticNode.performHWGeneration()
                                    # print the updated VHDL instance of the toBeOptimisedReceiverArithmeticNode
                                    #print("Optimised ArithmeticNode VHDL Instance",toBeOptimisedReceiverArithmeticNode.vhdlInstance)
                                    
                                    # print the driver of the nextArithmetic node input1 if the nextArithmetic Node Index is 307
                                    #if nextArithmeticNodeIndex == 307:
                                        #print("The updated input2 of the driver of NextArithmetic Node with Index 307 is ",toBeOptimisedReceiverArithmeticNode.input2)
                                        #print("The original driver of NextArithmetic Node VHDL Instance", toBeOptimisedReceiverArithmeticNode.vhdlInstance)
                                        #toBeOptimisedReceiverArithmeticNode.processHWGeneration()
                                        
                                        #print("The updated driver of NextArithmetic Node VHDL Instance", toBeOptimisedReceiverArithmeticNode.vhdlInstance)

 
                                        #print("The name of the driver of NextArithmetic Node, that is toBeOptimisedArithemeticNode is",toBeOptimisedReceiverArithmeticNode.name)


                                    #print("Original length of the arithmetic nodes",len(self.optimisedArithmeticNodes))
                                    # disabling the nextArithmeticNode (for now we do not remove the node for testing)
                                    nextArithmeticNode.enable = False
                                    # print the nextArithmeticNode name
                                    #print("Next ArithmeticNode that is disabled is", nextArithmeticNode.name + str(nextArithmeticNode.number) +"_" + str(nextArithmeticNode.arithmeticNodeNumber))
                                    #self.optimisedArithmeticNodes.remove(nextArithmeticNode)
                                    #print("Updated length of the arithmetic nodes",len(self.optimisedArithmeticNodes))
                                    break
                            
                            numberOfDuplicateNodes = numberOfDuplicateNodes + 1
                            duplicateNodeIndices.append(nextArithmeticNodeIndex)
                            #duplicateNodeIndicesWithTheirReceiverDetails[str(nextArithmeticNodeIndex)] = [duplicateNodeReceiverIndices,arithmeticNode.receiverEquation]
                            duplicateNodeIndicesWithTheirReceiverDetails[str(nextArithmeticNodeIndex)] = [duplicateNodeReceiverIndices]

                            #print("The output of the nextArithmeticNode", nextArithmeticNode.output)
                            #print("Two ProductNodes have same equation",arithmeticNode.receiverEquation)
                            
                        else:
                            #print("Next ArithmeticNode Receiver Equation that is not matched" + nextArithmeticNode.receiverEquation + "with ArithmeticNodeReceiver equation", arithmeticNode.receiverEquation)
                            pass
                
                #print("The duplication nodes are", numberOfDuplicateNodes)
                #print("Original Duplicate Nodes Details", duplicateNodeDetails)
                # check if the number of duplicates is greater than zero or not
                if numberOfDuplicateNodes > 0:
                    duplicateNodeDetails[arithmeticNode.receiverEquation] = numberOfDuplicateNodes
                    duplicateNodeIndiciesDetails[str(arithmeticNodeIndex)] = duplicateNodeIndices
                    duplicateNodeDetailsWithTheirReceivers[str(arithmeticNodeIndex)] = duplicateNodeIndicesWithTheirReceiverDetails
                    #print("Updated Duplicate Nodes Details", duplicateNodeDetails)
                    
            
        #print("Duplicate node equations", duplicateNodeDetails)
        #print("Duplicate Node Indices Details", duplicateNodeIndiciesDetails)
        #print("Duplicate Node Details With Their Receivers", duplicateNodeDetailsWithTheirReceivers)
    
    
    def process(self):
        super().process()

        # check if the removeDuplicatePCAN is set or not
        if self.removeDuplicatePCAN == True:
            # call the removeDuplicateArithmeticNodes function
            #self.removeDuplicateArithmeticNodes()
            self.disableDuplicateArithmeticNodes()
            
        
        counter = 0
        for arithmeticNode in self.optimisedArithmeticNodes:
            if arithmeticNode.enable == True:
                counter = counter + 1

        print("Optimised number of arithmetic nodes",counter)

    def main(self):
        super().main()
        self.process()

    def run(self):
        super().run()
