"""
Created by Karthekeyan Periasamy
Edited on Novermber 09, 2023
"""

from SWOptimisers.SWOptimiser import SWOptimiser
from Operators.Adder.Adder import Adder
from Operators.Multiplier.Multiplier import Multiplier

class SWPCSystemOptimiser(SWOptimiser):
    """
    Class to optimise the arithmetic nodes of the PCSystem (the old code will be changed)

    For now, optimisation is done for repeated arithmetic nodes, in future this class will be expanded
    """
    def __init__(self):
        self.connect()
    
    def connect(self):
        self.connectProperties()


    def connectProperties(self):
        super().connectProperties()
        

        # balancePCSystemTree flag enables to start the process of balancing the PCSystemTree
        # mostly balancing a PCSystemTree is necessary
        self.balancePCSystemTree = False
        
        # new property to store the height of the PC
        self.heightOfPC = 0

        # new property to store the left side height of the PC
        self.leftSideHeightOfPC = 0

        # new property to store the right side height of the PC
        self.rightSideHeightOfPC = 0

        # new property to store the levels of the PC
        self.numberOfLevelsOfPC = 0

        # number of children of all levels of PC
        self.childrenOfEachLevelOfPC = None

        # property to store the number of children information for each level of PC
        self.numberOfChildrenForEachLevelOfPC = None

        # balancing depth informaton for each level
        self.balancingDepthForEachLevelOfPC = None

        # balancing needed or not informaton for each level
        self.balancingNeededOrNotForEachLevelOfPC = None

        # property to know the delay on the longest path of the PC
        self.delayOnTheLongestPathOfPC = 0


    
    def configure(self):
        super().configure()

        # store the configuration Details
        configurationDetails = slef.configurationDetails
        
        if "BalancePCSystemTree" in self.configurationDetails:
            self.balancePCSystemTree = self.configurationDetails["BalancePCSystemTree"]



                
    """
    # Start: ProcessArithmeticNodes 
    """
    def processArithmeticNodes(self):
        """
        Overall logic
        1. First, use depth traversal technique to find left side height and right side height
        2. Then, find the number of levels of PC
        3. To balance the PC level by level, depth of a PC node is calculated
        4. Using the information from levels, depth and height of a PC Node we balance and build the balancing of hardware using Shift Regsiters
        5. As the above operations are mostly software manipulations, we will use parameters in function

        Usually, in the whole of autoPC, we model the hardware and software modeled hardware do not have function parameters
        """

        #print("The length of the arithmeticNodes", len(self.arithmeticNodes))
        topArithmeticNode = self.arithmeticNodes[len(self.arithmeticNodes)-1]
        #print("The top arithmetic node", topArithmeticNode)
        #print("The top arithmetic node arithemeticNodeNumber", topArithmeticNode.arithmeticNodeNumber)


        # process the topArithmeticNodeInput1, here input1 of any operator is assumed to be the left child
        self.leftSideHeightOfPC = self.heightOfPCNode(topArithmeticNode.input1,"Left",topArithmeticNode)
        # print the left side height
        #print("The left side height of PC", self.leftSideHeightOfPC)

        # process the topArithmeticNodeInput2, here input2 of any operator is assumed to be the right child
        self.rightSideHeightOfPC = self.heightOfPCNode(topArithmeticNode.input2,"Right",topArithmeticNode)
        # print the right side height of the whole tree
        #print("The right side height of PC", self.rightSideHeightOfPC)

        self.heightOfPC = max(self.leftSideHeightOfPC, self.rightSideHeightOfPC) + 1
        
        #print("The height of the PC", self.heightOfPC)
        
        # find the longest path on the left side from the top node
        leftSideLongestPathFromPCNodeList = self.longestPathFromPCNode(topArithmeticNode.input1,"Left",topArithmeticNode)
        #print("The length of the longest path on the left side of the top node is ",len(leftSideLongestPathFromPCNodeList))
        #print("The longest path on the left side of the top node list ",leftSideLongestPathFromPCNodeList)
        
        leftSideNumberOfProductNodes = 0
        leftSideNumberOfSumNodes = 0
        #print the left side arithmeticNodes
        #print("The right side arithmetic nodes", rightSideLongestPathArithmeticNodesFromPCNode)
        for arithmeticNode in leftSideLongestPathFromPCNodeList:
            if isinstance(arithmeticNode, Multiplier):
                leftSideNumberOfProductNodes = leftSideNumberOfProductNodes + 1
            elif isinstance(arithmeticNode, Adder):
                leftSideNumberOfSumNodes = leftSideNumberOfSumNodes + 1
       
        
        # find the longest path on the right side from the top node
        rightSideLongestPathFromPCNodeList = self.longestPathFromPCNode(topArithmeticNode.input2,"Right",topArithmeticNode)
        #print("The length of the longest path on the right side of the top node is",len(rightSideLongestPathFromPCNodeList))
        #print("The longest path on the right side of the top node list ",rightSideLongestPathFromPCNodeList)
        
        rightSideNumberOfProductNodes = 0
        rightSideNumberOfSumNodes = 0

        #print("The longest path on the right side of the top node list ",rightSideLongestPathFromPCNodeList) 
        for arithmeticNode in rightSideLongestPathFromPCNodeList:
            if isinstance(arithmeticNode, Multiplier):
                rightSideNumberOfProductNodes = rightSideNumberOfProductNodes + 1
            elif isinstance(arithmeticNode, Adder):
                rightSideNumberOfSumNodes = rightSideNumberOfSumNodes + 1
        
        if (len(leftSideLongestPathFromPCNodeList) > len(rightSideLongestPathFromPCNodeList)):
            self.delayOnTheLongestPathOfPC = (((self.multiplierPipelineDepth*leftSideNumberOfProductNodes) + (self.adderPipelineDepth*leftSideNumberOfSumNodes))) + self.adderPipelineDepth*leftSideNumberOfSumNodes
            #print("The current node right side is the longest and the delays on the longest path is", currentNode.delayOnLongestPath)
        else:
            self.delayOnTheLongestPathOfPC = ((self.multiplierPipelineDepth*rightSideNumberOfProductNodes) + (self.adderPipelineDepth*rightSideNumberOfSumNodes)) + self.adderPipelineDepth*leftSideNumberOfSumNodes

        print("The LongestPath of PC Delay", self.delayOnTheLongestPathOfPC)

        # find the levels of the PC and update the depth of each node with respect to rootNode
        self.levelsOfPC(topArithmeticNode)

        # balance the arithmeticNodes with shift registers 
        self.balanceArithmeticNodes()

        # update the definition of arithmetic nodes after balancing them
        self.updateDefinitionOfArithmeticNodes()
       
    """
    # End: Process ArithmeticNodes 
    """
    
       
    """
    # Start: Function to find the height of the PC Node
    """

    def heightOfPCNode(self,currentNodeInput,depthTraversalDirection,currentNode):
        """
        Logic
        """
        # depth first traversal method to find the each side height

        #print the currentNode input
        #print("The current node input name is", currentNodeInput)

        # TODO check whether the given input is float or not (this condition is needed, as this function looks for productNode,that may have weights)
        # check whether the string has the format defined to find the child of an arithmeticnode from the given array
        if currentNodeInput.find("_") == -1:
            # mostly this would be a port of any arithmetic node
            # print the currentNode input name
            #print("The current node is a port and is named as", currentNodeInput)
            return 0


        # the format is needed to nonlinearise the linear data structure must be of length 3 to know the driver
        # if the length of the text is not three, we cannot find the driver.
        if len(currentNodeInput.split("_")) != 3:
            # mostly this would be a weight of a product node
            # print the currentNode input name
            #print("The current node is a weight and is named as", currentNodeInput)
            return 0
 
        # access the currentNode Input  that contains the topSumNode input
        decodedInput = currentNodeInput.split("_")
        # split the input string
        #print("Decoded ArithmeticNode Input List",decodedInput)
        # access the first index element to access the node name that feeds the input to the MMACUnit SumNode
        inputDriverNodeName = decodedInput[0]
        # print the driver arithmetic node name
        #print("Driver Arithmetic Node name", inputDriverNodeName)
        # access the last index element to get the index which feeds the input to the MMACUnit sumNode
        inputDriverNodeIndex = int(decodedInput[(len(decodedInput)-1)])
        #print("The input driver node index", inputDriverNodeIndex)

        # using the inputDriverNode Index we can access the driverOfcurrent Node 
        driverOfCurrentNode = self.arithmeticNodes[inputDriverNodeIndex]

        # print the current Node object information
        #print("The driver of the current node information", driverOfCurrentNode)

        # recursively process the left  child of the driverOfCurrentNode
        leftSideHeight = self.heightOfPCNode(driverOfCurrentNode.input1,"Left",driverOfCurrentNode)

        # print the left side height
        #print("The left side height", leftSideHeight)
        
        # recursively process the  right child of the driverOfCurrentNode
        rightSideHeight = self.heightOfPCNode(driverOfCurrentNode.input2,"Right",driverOfCurrentNode)
        
        # print the right side height
        #print("The right side height", rightSideHeight)
        
        
        # compare the left height and right side height and increament
        if leftSideHeight > rightSideHeight:
            return leftSideHeight + 1
        else:
            return rightSideHeight + 1
             
    """
    # End: Function to find the height of the PC Node using depth first traversal technique
    """
    
    """
    # Start: Function to find the longest path from the given PC Node 
    """

    def longestPathFromPCNode(self,currentNodeInput,depthTraversalDirection,currentNode):
        """
        Logic
        """

        # check whether the string has the format defined to find the child of an arithmeticnode from the given array
        if currentNodeInput.find("_") == -1:
            # mostly this would be a port of any arithmetic node
            # print the currentNode input name
            #print("The current node is a port and is named as", currentNodeInput)
            return []


        # the format is needed to nonlinearise the linear data structure must be of length 3 to know the driver
        # if the length of the text is not three, we cannot find the driver.
        if len(currentNodeInput.split("_")) != 3:
            # mostly this would be a weight of a product node
            # print the currentNode input name
            #print("The current node is a weight and is named as", currentNodeInput)
            return []
 
        # access the currentNode Input  that contains the topSumNode input
        decodedInput = currentNodeInput.split("_")
        # split the input string
        #print("Decoded ArithmeticNode Input List",decodedInput)
        # access the first index element to access the node name that feeds the input to the MMACUnit SumNode
        inputDriverNodeName = decodedInput[0]
        # print the driver arithmetic node name
        #print("Driver Arithmetic Node name", inputDriverNodeName)
        # access the last index element to get the index which feeds the input to the MMACUnit sumNode
        inputDriverNodeIndex = int(decodedInput[(len(decodedInput)-1)])
        #print("The input driver node index", inputDriverNodeIndex)

        # using the inputDriverNode Index we can access the driverOfcurrent Node 
        driverOfCurrentNode = self.arithmeticNodes[inputDriverNodeIndex]

        # print the current Node object information
        #print("The driver of the current node information", driverOfCurrentNode)


        # recursively process the left  child of the driverOfCurrentNode
        leftSideArithmeticNodeList = self.longestPathFromPCNode(driverOfCurrentNode.input1,"Left",driverOfCurrentNode)
        
        # print the left side arithmeticNodes length
        #print("The left side arithmetic nodes", len(leftSideArithmeticNodeList))
        
        # recursively process the  right child of the driverOfCurrentNode
        rightSideArithmeticNodeList = self.longestPathFromPCNode(driverOfCurrentNode.input2,"Right",driverOfCurrentNode)
        
        # print the left side arithmeticNodes length
        #print("The right side arithmetic nodes", len(rightSideArithmeticNodeList))
        
        
        # compare the left side arithmetic node list and right side arithmetic node list
        if (len(leftSideArithmeticNodeList) > len(rightSideArithmeticNodeList)):
            leftSideArithmeticNodeList.append(driverOfCurrentNode)
        else:
            rightSideArithmeticNodeList.append(driverOfCurrentNode)

        if (len(leftSideArithmeticNodeList) > len(rightSideArithmeticNodeList)):
            return leftSideArithmeticNodeList


        return rightSideArithmeticNodeList


             
    """
    # End: Function to find the height of the PC Node using depth first traversal technique
    """

    
    """
    # Start: Function to find the depth of the PC Node using depth first traversal technique
    """

    def depthOfPCNode(self,rootNodeInput, rootNode, currentNode):
        """
        Logic
        """
        #print("RootNode Name", (rootNode.name+str(rootNode.number)))
        #print("CurrentNode Name", (currentNode.name+str(currentNode.number)))

        depth = -1
        
        # check whether the rootNode and the currentNode are same
        if currentNode == rootNode:
            #print("Reached the CurrentNode from the root node")
            #print("The depth is", depth)
            return depth + 1
        
        # check the input1 if its eligible to be traversed or not
        if (((rootNodeInput.find("_")) == -1) or (len(rootNodeInput.split("_")) !=3)):
            #only traverse the input2 of the rootNode till it reaches the currentNode
            #print("RootNodeInput", rootNodeInput)
            return -1
        
        # access the currentNode Input  that contains the topSumNode input
        decodedInput = rootNodeInput.split("_")
        # split the input string
        #print("Decoded ArithmeticNode Input List",decodedInput)
        # access the first index element to access the node name that feeds the input to the MMACUnit SumNode
        inputDriverNodeName = decodedInput[0]
        # print the driver arithmetic node name
        #print("Driver Arithmetic Node name", inputDriverNodeName)
        # access the last index element to get the index which feeds the input to the MMACUnit sumNode
        inputDriverNodeIndex = int(decodedInput[(len(decodedInput)-1)])
        #print("The input driver node index", inputDriverNodeIndex)
        
        # using the inputDriverNode Index we can access the driverOfcurrent Node 
        driverOfRootNodeInput1 = self.arithmeticNodes[inputDriverNodeIndex]
            
        # recursively process the left  child of the driverOfCurrentNode
        depth = self.depthOfPCNode(driverOfRootNodeInput1.input1, driverOfRootNodeInput1,currentNode)
            
        # print the left side height
        #print("The left side Input1", driverOfRootNodeInput1.input1, "its dpeth", depth)
            
        #  check if the depth on the left side is greater than zero or not the left height and right side height and increament
        if depth >= 0:
            #print("Depth is greater than 0")
            return depth + 1
        
        # recursively process the  right child of the driverOfCurrentNode
        depth = self.depthOfPCNode(driverOfRootNodeInput1.input2, driverOfRootNodeInput1,currentNode)
        
        # print the right side height
        #print("The right side depth Input1", depth)
        
        #  check if the depth on the left side is greater than zero or not the left height and right side height and increament
        if depth >= 0:
            #print("Depth is greater than 0")
            return depth + 1
            
        # print the right side height
        #print("The right side height", rightSideHeight)
        return depth

    """
    # End: Function to find the depth of the PC Node using depth first traversal technique
    """


        
    """
    # Start: Function to levels of PC  
    """

    def levelsOfPC(self,rootNode):
        """
        Logic
        """
        
        # check if the rootNode is none or not
        if rootNode == None:
            return


        # property to find the levels of PC, this property will be incremented
        self.numberOfLevelsOfPC = 1
        #initialise the children of level dict
        numberOfChildrenForEachLevel = dict()
        childrenOfCurrentLevel = None
        childrenOfAllLevels = dict()
        
        # breadth first traversal method using queues to find the levels and the number of nodes per level
        # use list based queue
       
        # we can access the input 1 driver and input 2 driver add them to the queue
        # create a queue using list
        queue = list()

        # add the root node
        queue.append(rootNode)
        
        # access the length of the queue and update the children of level with respect to root node
        numberOfChildrenForEachLevel[str(self.numberOfLevelsOfPC)] = len(queue)
        
        # copy the queue to a new array or list to add it as children to first level
        childrenOfFirstLevel = queue.copy()
        #print("Children Of Current Level", childrenOfCurrentLevel)
        # update the children of current level with the children of all levels dictionary
        childrenOfAllLevels[str(self.numberOfLevelsOfPC)] = childrenOfFirstLevel

        while len(queue) > 0:
            initialLengthOfQueue = len(queue)
            #print the initial length of queue
            #print("Initial length of Queue", initialLengthOfQueue)
            childrenOfCurrentLevel = list()
            #print the length of the queue, as the length of the queue will change dynamically
            #print("The length of the queue", initialLengthOfQueue)
            # for calculating the levels and level based arithmetic node traversal we need to add one more for loop
            for index in range(initialLengthOfQueue):
                # access the top or zeroth index element in an array or pop the top or zeroth indexed element
                currentNode = queue.pop(0)
                #print the current node input 1 and input 2
                # current node name
                #print("The current node name is", currentNode.name + "_" + str(currentNode.arithmeticNodeNumber))
                # print the current node is enabled or not
                #print("The current node is enabled", currentNode.enable)
                #print("The current node input1", currentNode.input1)
                #print("The current node input2", currentNode.input2)
                
                # first check whether there is a valid left child and right child or not
                # As the current datastructure is aan array we need to find the validity of left child and right child differently
                
                # check whether the input1 is of weight and the input 2 is of port 
                if (((len(currentNode.input1.split("_")) != 3) and (currentNode.input2.find("_") == -1))):
                    #print the currentNode input1
                    #print("The current Node Input1 Weight Value is ", currentNode.weight)
                    # mostly this would be a port of any arithmetic node
                    # print the currentNode inputs name
                    #print("The current node, input1", currentNode.input1)
                    # print the currentNode inputs name
                    #print("The current node, input2", currentNode.input2)
                    # find the height of the current node.
                    # if the height of the current node is zero
                    # it can be proved that it is the end of the tree

                    # access the root node
                    #print("The length of the arithmeticNodes", len(self.arithmeticNodes))
                    rootNode = self.arithmeticNodes[len(self.arithmeticNodes)-1]


                    # property to store the node depth, where the node is the current node
                    depthOfCurrentNode = self.depthOfPCNode(rootNode.input1, rootNode, currentNode)
                    #print("Input1 is a weight and Input2 is a port DepthOfCurrentNode", depthOfCurrentNode)

                    if depthOfCurrentNode < 0:                        
                        # property to store the node depth, where the node is the current node
                        depthOfCurrentNode = self.depthOfPCNode(rootNode.input2, rootNode, currentNode)

                        #print("Input1 is a weight and Input2 is a port DepthOfCurrentNode", depthOfCurrentNode)
                        #print("Input1 of current node", currentNode.input1)
                        #print("Input2 of current node", currentNode.input2)

                   
                    # check the difference between depth and height of the current node
                    if (self.heightOfPC-depthOfCurrentNode) != 1:
                       
                        # set the property of the shift register depth
                        currentNode.shiftRegisterDepth = (int(self.heightOfPC-depthOfCurrentNode)-1)
                        # add the shift register with the delay of the difference between height and depth
                        #currentNode.addMBRightSHRToBothInput1andInput2()
                        #print("The difference between height of PC and Depth of CurrentNode", (int(self.heightOfPC-depthOfCurrentNode)-1))
                        currentNode.shouldInput1andInput2BeBalanced = True
                        
                    continue
                
                # check whether the input1 is of the port
                # and the input 2 is of weight
                elif (((currentNode.input1.find("_") == -1) and (len(currentNode.input2.split("_")) != 3))):
                    #print the currentNode input2
                    #print("The current Node Input2 Weight Value is ", currentNode.weight)
                    # mostly this would be a port of any arithmetic node
                    # print the currentNode inputs name
                    #print("The current node, input1", currentNode.input1)
                    # print the currentNode inputs name
                    #print("The current node, input2", currentNode.input2)
                    # find the height of the current node.
                    # if the height of th current node is zero
                    # it can be proved that it is the end of the tree
                    
                    # access the root node
                    #print("The length of the arithmeticNodes", len(self.arithmeticNodes))
                    rootNode = self.arithmeticNodes[len(self.arithmeticNodes)-1]
                    
                    # property to store the node depth, where the node is the current node
                    depthOfCurrentNode = self.depthOfPCNode(rootNode.input1, rootNode, currentNode)
                    #print("Input 1 is a port and Input2 is a weight, and the DepthOfCurrentNode", depthOfCurrentNode)
                    
                    if depthOfCurrentNode < 0:                        
                        # property to store the node depth, where the node is the current node
                        depthOfCurrentNode = self.depthOfPCNode(rootNode.input2, rootNode, currentNode)
                        #print("Input 1 is a port and Input2 is a weight, and the DepthOfCurrentNode", depthOfCurrentNode)
                        #print("Input1 of current node", currentNode.input1)
                        #print("Input2 of current node", currentNode.input2)

                   
                    # check the difference between depth and height of the current node
                    if (self.heightOfPC-depthOfCurrentNode) != 1:
                        
                        # set the property of the shift register depth
                        currentNode.shiftRegisterDepth = (int(self.heightOfPC-depthOfCurrentNode)-1)
                        # add the shift register with the delay of the difference between height and depth
                        #currentNode.addMBRightSHRToBothInput1andInput2()
                        #print("The difference between height of PC and Depth of CurrentNode", (self.heightOfPC-depthOfCurrentNode))
                        currentNode.shouldInput1andInput2BeBalanced = True
                    
                    continue

                # check whether the string has the format that says its of port
                # Two inputs are driven by the ports of the system
                if ((currentNode.input1.find("_") == -1) and (currentNode.input2.find("_") == -1)):
                    # mostly this would be a port of any arithmetic node
                    # print the currentNode inputs name
                    #print("The current node, input1", currentNode.input1)
                    # print the currentNode inputs name
                    #print("The current node, input2", currentNode.input2)
                    # find the height of the current node.
                    # if the height of th current node is zero
                    # it can be proved that it is the end of the tree

                     # access the root node
                    #print("The length of the arithmeticNodes", len(self.arithmeticNodes))
                    rootNode = self.arithmeticNodes[len(self.arithmeticNodes)-1]
                    
                    # property to store the node depth, where the node is the current node
                    depthOfCurrentNode = self.depthOfPCNode(rootNode.input1, rootNode, currentNode)
                    #print("Input 1 is a port and Input2 is a weight, and the DepthOfCurrentNode", depthOfCurrentNode)
                    
                    if depthOfCurrentNode == None:                        
                        # property to store the node depth, where the node is the current node
                        depthOfCurrentNode = self.depthOfPCNode(rootNode.input2, rootNode, currentNode)
                        #print("Input 1 is a port and Input2 is a port, and the DepthOfCurrentNode", depthOfCurrentNode)

                   
                    # check the difference between depth and height of the current node
                    if (self.heightOfPC-depthOfCurrentNode) != 1:
                        # set the property of the shift register depth
                        currentNode.shiftRegisterDepth = (int(self.heightOfPC-depthOfCurrentNode)-1)
                        # add the shift register with the delay of the difference between height and depth
                        #currentNode.addMBRightSHRToBothInput1andInput2()
                        #print("The difference between height of PC and Depth of CurrentNode", (self.heightOfPC-depthOfCurrentNode))
                        currentNode.shouldInput1andInput2BeBalanced = True
                    
                    continue

                # check if any one of the input do not have child
                if ((len(currentNode.input1.split("_")) != 3) or (len(currentNode.input2.split("_")) !=3)):
                    # mostly one of the input is a weight check which one it is would be a weight of a product node
                    if (len(currentNode.input1.split("_")) == 3):
                        #print the currentNode input1
                        #print("The current Node Input1 is ", currentNode.input1)
                        # print the input 1 is not weight, the input 2 is a weight
                        #print("The current node input1 is named as", currentNode.input1)
                        # decode and split the input1 and add the driver of the currentNode
                        # access the currentNode Input  that contains the topSumNode input
                        decodedInput = currentNode.input1.split("_")
                        # split the input string
                        #print("Decoded ArithmeticNode Input List",decodedInput)
                        # access the first index element to access the node name that feeds the input to the MMACUnit SumNode
                        inputDriverNodeName = decodedInput[0]
                        # print the driver arithmetic node name
                        #print("Driver Arithmetic Node name", inputDriverNodeName)
                        # access the last index element to get the index which feeds the input to the MMACUnit sumNode
                        inputDriverNodeIndex = int(decodedInput[(len(decodedInput)-1)])
                        #print("The input driver node index", inputDriverNodeIndex)
                        # using the inputDriverNode Index we can access the driverOfcurrent Node 
                        driverOfCurrentNode = self.arithmeticNodes[inputDriverNodeIndex]
                        
                        queue.append(driverOfCurrentNode)
                                                    
                        # one of the input that is input 1 is driven by another node
                        #print("One of the input, that is input1 of the current node is driven by another node")
                        
                        # print the queue array
                        #print("Updated queue", queue)
                        
                        # access the root node
                        #print("The length of the arithmeticNodes", len(self.arithmeticNodes))
                        rootNode = self.arithmeticNodes[len(self.arithmeticNodes)-1]

                        # property to store the node depth, where the node is the current node
                        depthOfCurrentNode = self.depthOfPCNode(rootNode.input1, rootNode, currentNode)
                        #print("Input1 is a weight and Input2 is a port DepthOfCurrentNode", depthOfCurrentNode)
                        
                        if depthOfCurrentNode < 0:                        
                            # property to store the node depth, where the node is the current node
                            depthOfCurrentNode = self.depthOfPCNode(rootNode.input2, rootNode, currentNode)
                            #print("The currentNode is found on the right side of the rootNode")
                            #print("Input2 is a weight and the DepthOfCurrentNode", depthOfCurrentNode)
                        
                        # check the difference between depth and height of the current node
                        if (self.heightOfPC-depthOfCurrentNode) != 1:
                            
                            # check the longest path from the current node and count the sum nodes and product nodes that is in the longest path
                            # this would help multiply the shift regsiter factor to balance the paths effectively.
                                                    
                            # process the topArithmeticNodeInput1, here input1 of any operator is assumed to be the left child
                            leftSideLongestPathArithmeticNodesFromPCNode = self.longestPathFromPCNode(currentNode.input1,"Left",currentNode)
                            numberOfProductNodes = 0
                            numberOfSumNodes = 0
                            # print the left side arithmeticNodes
                            #print("The left side arithmetic nodes", leftSideLongestPathArithmeticNodesFromPCNode)
                            for arithmeticNode in leftSideLongestPathArithmeticNodesFromPCNode:
                                if isinstance(arithmeticNode, ProductNode.ProductNode):
                                    numberOfProductNodes = numberOfProductNodes + 1
                                elif isinstance(arithmeticNode, SumNode.SumNode):
                                    numberOfSumNodes = numberOfSumNodes + 1

                            shiftRegisterDepth = ((self.multiplierPipelineDepth*numberOfProductNodes) + (self.adderPipelineDepth*numberOfSumNodes)-1)
                            #print("Calcualted shift register depth", shiftRegisterDepth)
                            currentNode.shiftRegisterDepth = shiftRegisterDepth

                            #balance the input 2 of the current node
                            currentNode.shouldInput2BeBalanced = True
                            
                            # add the current node to the children level dictionary
                            childrenOfCurrentLevel.append(currentNode)

 
                    elif (len(currentNode.input2.split("_")) == 3):
                        #print the currentNode input1
                        #print("The current Node Input2 Value is ", currentNode.input2)
                        # print the input 1 is weight
                        #print("The current node input2 is named as", currentNode.input2)
                        # decode and split the input1 and add the driver of the currentNode
                        # access the currentNode Input  that contains the topSumNode input
                        decodedInput = currentNode.input2.split("_")
                        # split the input string
                        #print("Decoded ArithmeticNode Input",decodedInput)
                        # access the first index element to access the node name that feeds the input to the MMACUnit SumNode
                        inputDriverNodeName = decodedInput[0]
                        # print the driver arithmetic node name
                        #print("Driver Arithmetic Node name", inputDriverNodeName)
                        # access the last index element to get the index which feeds the input to the MMACUnit sumNode
                        inputDriverNodeIndex = int(decodedInput[(len(decodedInput)-1)])
                        #print("The input driver node index", inputDriverNodeIndex)
                        # using the inputDriverNode Index we can access the driverOfcurrent Node 
                        driverOfCurrentNode = self.arithmeticNodes[inputDriverNodeIndex]
                        
                        queue.append(driverOfCurrentNode)
                                                
                        # one of the input that is input 1 is driven by another node
                        #print("One of the input, that is input2 of the current node is driven by another node")
                        # print the queue array
                        #print("Updated queue", queue)
                        
                        # access the root node
                        #print("The length of the arithmeticNodes", len(self.arithmeticNodes))
                        rootNode = self.arithmeticNodes[len(self.arithmeticNodes)-1]

                        
                        # property to store the node depth, where the node is the current node
                        depthOfCurrentNode = self.depthOfPCNode(rootNode.input1, rootNode, currentNode)
                        #print("Input2 is a weight and the DepthOfCurrentNode", depthOfCurrentNode)
                        
                        if depthOfCurrentNode < 0: 

                            # property to store the node depth, where the node is the current node
                            depthOfCurrentNode = self.depthOfPCNode(rootNode.input2, rootNode, currentNode)
                            #print("Input1 is a weight and the DepthOfCurrentNode", depthOfCurrentNode)

                            
                        
                        # check the difference between depth and height of the current node
                        if (self.heightOfPC-depthOfCurrentNode) != 1:

                            # check the longest path from the current node and count the sum nodes and product nodes that is in the longest path
                            # this would help multiply the shift regsiter factor to balance the paths effectively.
                                                    
                            # find the longest path of the right side of the PC
                            rightSideLongestPathArithmeticNodesFromPCNode = self.longestPathFromPCNode(currentNode.input2,"Right",currentNode)
                            
                            numberOfProductNodes = 0
                            numberOfSumNodes = 0
                            # print the left side arithmeticNodes
                            #print("The right side arithmetic nodes", rightSideLongestPathArithmeticNodesFromPCNode)
                            for arithmeticNode in rightSideLongestPathArithmeticNodesFromPCNode:
                                if isinstance(arithmeticNode, ProductNode):
                                    numberOfProductNodes = numberOfProductNodes + 1
                                elif isinstance(arithmeticNode, SumNode):
                                    numberOfSumNodes = numberOfSumNodes + 1                                
                            

                            shiftRegisterDepth = (((self.multiplierPipelineDepth*numberOfProductNodes) + (self.adderPipelineDepth*numberOfSumNodes))-1)
                            
                            #print("Calcualted shift register depth", shiftRegisterDepth)
                            # set the property of the shift register depth
                            currentNode.shiftRegisterDepth = shiftRegisterDepth

                            #print("The difference between height of PC and Depth of CurrentNode", (self.heightOfPC-depthOfCurrentNode))
                            #balance the input 1 of the current node
                            currentNode.shouldInput1BeBalanced = True

                    
                elif ((len(currentNode.input1.split("_")) == 3) or (len(currentNode.input2.split("_")) ==3)):

                    # print the input 1 is weight
                    #print("The current node input2 is not a weight or port  and is named as", currentNode.input1)
                    # decode and split the input1 and add the driver of the currentNode
                    # access the currentNode Input  that contains the topSumNode input
                    decodedInput = currentNode.input1.split("_")
                    # split the input string
                    #print("Decoded ArithmeticNode Input List",decodedInput)
                    # access the first index element to access the node name that feeds the input to the MMACUnit SumNode
                    inputDriverNodeName = decodedInput[0]
                    # print the driver arithmetic node name
                    #print("Driver Arithmetic Node name", inputDriverNodeName)
                    # access the last index element to get the index which feeds the input to the MMACUnit sumNode
                    inputDriverNodeIndex = int(decodedInput[(len(decodedInput)-1)])
                    #print("The input driver node index", inputDriverNodeIndex)
                    # using the inputDriverNode Index we can access the driverOfcurrent Node 
                    driverOfCurrentNode = self.arithmeticNodes[inputDriverNodeIndex]

                    queue.append(driverOfCurrentNode)
                        
                    # print the information 
                    #print("Current Node Input1 is driven by another node")
                    #print the decoded input
                    #print("THe decoded input", decodedInput)
                    
                    # print the queue array
                    #print("Updated Queue", queue)
                    
                    # print the input 2 
                    #print("The current node input2 is not a weight or port  is named as", currentNode.input2)
                    # decode and split the input1 and add the driver of the currentNode
                    # access the currentNode Input  that contains the topSumNode input
                    decodedInput = currentNode.input2.split("_")
                    # split the input string
                    #print("Decoded ArithmeticNode Input List",decodedInput)
                    # access the first index element to access the node name that feeds the input to the MMACUnit SumNode
                    inputDriverNodeName = decodedInput[0]
                    # print the driver arithmetic node name
                    #print("Driver Arithmetic Node name", inputDriverNodeName)
                    # access the last index element to get the index which feeds the input to the MMACUnit sumNode
                    inputDriverNodeIndex = int(decodedInput[(len(decodedInput)-1)])
                    #print("The input driver node index", inputDriverNodeIndex)
                    # using the inputDriverNode Index we can access the driverOfcurrent Node 
                    driverOfCurrentNode = self.arithmeticNodes[inputDriverNodeIndex]
                    
                    queue.append(driverOfCurrentNode)

                    # print the information 
                    #print("Current Node Input2 is driven by another node")
                    #print the decoded input
                    #print("THe decoded input", decodedInput)
                    # print the queue array
                    #print("Updated queue", queue)
                    
                    # find the longest path on the left side from the current node
                    leftSideLongestPathFromPCNodeList = self.longestPathFromPCNode(currentNode.input1,"Left",currentNode)
                    #print("The length of the longest path on the left side of the current node that is driven by another node",len(leftSideLongestPathFromPCNodeList))
                    #print("The length of the longest path on the left side of the current node that is driven by another node",leftSideLongestPathFromPCNodeList)
                    
                    leftSideNumberOfProductNodes = 0
                    leftSideNumberOfSumNodes = 0
                    # print the left side arithmeticNodes
                    #print("The right side arithmetic nodes", rightSideLongestPathArithmeticNodesFromPCNode)
                    for arithmeticNode in leftSideLongestPathFromPCNodeList:
                        if isinstance(arithmeticNode, Multiplier):
                            leftSideNumberOfProductNodes = leftSideNumberOfProductNodes + 1
                        elif isinstance(arithmeticNode, Adder):
                            leftSideNumberOfSumNodes = leftSideNumberOfSumNodes + 1 
                    
                    # find the longest path on the right side from the top node
                    rightSideLongestPathFromPCNodeList = self.longestPathFromPCNode(currentNode.input2,"Right",currentNode)
                    #print("The length of the longest path on the left side of the current node that is driven by another node",len(rightSideLongestPathFromPCNodeList))
                    
                    rightSideNumberOfProductNodes = 0
                    rightSideNumberOfSumNodes = 0
                    #print("The longest path on the right side of the top node list ",rightSideLongestPathFromPCNodeList) 
                    for arithmeticNode in rightSideLongestPathFromPCNodeList:
                        if isinstance(arithmeticNode, Multiplier):
                            rightSideNumberOfProductNodes = rightSideNumberOfProductNodes + 1
                        elif isinstance(arithmeticNode, Adder):
                            rightSideNumberOfSumNodes = rightSideNumberOfSumNodes + 1

                    if (len(leftSideLongestPathFromPCNodeList) > len(rightSideLongestPathFromPCNodeList)):
                        currentNode.numberOfArithmeticNodesOnTheLongestPath = len(leftSideLongestPathFromPCNodeList)
                        #print("The current node left side is the longest and number of arithmetic nodes on the longest path", currentNode.numberOfArithmeticNodesOnTheLongestPath)        
                        
                        currentNode.delayOnTheLongestPath = (((self.pcSystemMultiplierPipelineDepth*leftSideNumberOfProductNodes) + (self.pcSystemAdderPipelineDepth*leftSideNumberOfSumNodes))-1)
                        #print("The current node right side is the longest and the delays on the longest path is", currentNode.delayOnLongestPath)

                    else:
                        currentNode.numberOfArithmeticNodesOnTheLongestPath = len(rightSideLongestPathFromPCNodeList)#
                        #print("The current node right side is the longest and number of arithmetic nodes on the longest path", currentNode.numberOfArithmeticNodesOnTheLongestPath)
                        
                        currentNode.delayOnTheLongestPath = ((self.pcSystemMultiplierPipelineDepth*rightSideNumberOfProductNodes) + (self.pcSystemAdderPipelineDepth*rightSideNumberOfSumNodes)-1)
                        #print("The current node right side is the longest and the delays on the longest path is", currentNode.delayOnLongestPath)

                #print the level based children detail
                #print("The level based children detail", childrenOfCurrentLevel)
                    
            # check the queue length
            if len(queue) == 0:
                #print("The total levels of PC", self.numberOfLevelsOfPC)
                #print("Children Of All Levels", childrenOfAllLevels)
                self.childrenOfEachLevelOfPC = childrenOfAllLevels
                #print("Global Children Of All Levels", self.childrenOfEachLevelOfPC)
                #print("Children Of Each Level Of PC", self.childrenOfEachLevelOfPC)
                #print("The number of children detail of all levels", numberOfChildrenForEachLevel)
                self.numberOfChildrenForEachLevelOfPC = numberOfChildrenForEachLevel
                return

            # update the levels count
            self.numberOfLevelsOfPC = self.numberOfLevelsOfPC + 1
            # print the level of the PC
            #print("The level of PC", self.numberOfLevelsOfPC)
            # access the length of the queue
            numberOfChildrenForEachLevel[str(self.numberOfLevelsOfPC)] = len(queue)
            # print the queue
            #print("The queue is", queue)
            # copy the queue to a new array or list
            childrenOfCurrentLevel = queue.copy()
            #print("Children Of Current Level", childrenOfCurrentLevel)
            # update the children of current level with the children of all levels dictionary
            childrenOfAllLevels[str(self.numberOfLevelsOfPC)] = childrenOfCurrentLevel
            #print("Children Of All Levels", childrenOfAllLevels)
            # print the childen of levels with the number of children per level
            #print("Number of Children of each Level Dictionary", numberOfChildrenForEachLevel)
            #print("The current levelof PC", self.levelsOfPC)
            
        #print (" The total number of levels", self.numberOfLevelsOfPC)
       
    """
    # End:  Function to levels of PC
    """

    """
    # Start: updateDefinitionOfArithmeticNodes
    """

    def updateDefinitionOfArithmeticNodes(self):
        # loop through the arithmetic nodes
        # check whether input1 or input2 or both input1 and input2 should be balanced
        for arithmeticNode in self.arithmeticNodes:
            if arithmeticNode.shouldInput1BeBalanced == True:
                # do the necessary changes
                arithmeticNode.addMBRightSHRToInput1()
            elif arithmeticNode.shouldInput2BeBalanced == True:
                # do the necessary changes
                arithmeticNode.addMBRightSHRToInput2()
            elif arithmeticNode.shouldInput1andInput2BeBalanced == True:
                # do the necessary changes
                arithmeticNode.addMBRightSHRToBothInput1andInput2()
    """
    # End: updateDefinitionOfArithmeticNodes
    """
    
    """
    # Start: balance arithmetic nodes
    """

    def balanceArithmeticNodes(self):
        # access all the keys of the nodes of all levels object
        levelKeys = self.childrenOfEachLevelOfPC.keys()
        # object to store the maxDepth for each level that is used to balance the level of PC
        balancingDepthForEachLevel = dict()
        balancingNeededForEachLevel = dict()

        #print the level keys
        #print("Level Keys", levelKeys)
        # loop through the nodes of all levels
        for levelKey in levelKeys:
            #print the level key
            #print("Level Key", levelKey)
            # access the array of the children per level using levelKey
            children = self.childrenOfEachLevelOfPC[levelKey]
            # children shift register depth details
            shiftRegisterDepthOfChildren = list()
            # children that are balanced in a level
            balancedChildren = list()
            # using the children and find the depth of all the children
            for child in children:
                #print("The shift register depth of the child", child.shiftRegisterDepth)
                #print("The child input1 should be balanced or not", child.shouldInput1BeBalanced)
                #print("The child input2 should be balanced or not", child.shouldInput2BeBalanced)
                #print("The child input1 and input2 should be balanced or not", child.shouldInput1andInput2BeBalanced)

                # check whether the child input1 or input2 or input1 and input2 should be balanced or not
                if ((child.shouldInput1BeBalanced == True) or (child.shouldInput2BeBalanced == True) or (child.shouldInput1andInput2BeBalanced == True)):
                    #print("The level where some inputs are balanced", levelKey)
                    depth = child.shiftRegisterDepth
                    #print("The shift register depth of the child", depth)
                    #print("The child input1 should be balanced or not", child.shouldInput1BeBalanced)
                    #print("The child input2 should be balanced or not", child.shouldInput2BeBalanced)
                    #print("The child input1 and input2 should be balanced or not", child.shouldInput1andInput2BeBalanced)
                    # add the depth details to an array
                    shiftRegisterDepthOfChildren.append(depth)

                elif ((child.shouldInput1BeBalanced == False) and (child.shouldInput2BeBalanced == False) and (child.shouldInput1andInput2BeBalanced == False)):
                    #print("The level where some inputs are balanced", levelKey)
                    depth = child.delayOnTheLongestPath
                    #print("The shift register depth of the child", depth)
                    #print("The child input1 should be balanced or not", child.shouldInput1BeBalanced)
                    #print("The child input2 should be balanced or not", child.shouldInput2BeBalanced)
                    #print("The child input1 and input2 should be balanced or not", child.shouldInput1andInput2BeBalanced)
                    # add the children detail to the balanced children
                    balancedChildren.append(child)

                    # add the depth details to an array
                    shiftRegisterDepthOfChildren.append(depth)
                    
            if len(children) == len(balancedChildren):
                #print("The level that do not need balancing")
                balancingDepthForEachLevel[levelKey] = max(shiftRegisterDepthOfChildren)
                balancingNeededForEachLevel[levelKey] = False
                continue

            else:
                #print("The level still needs balancing, even though the some inputs of some nodes are balanced")
                balancingNeededForEachLevel[levelKey] = True

            # find the max from the shift register depth of children
            maxDepth = max(shiftRegisterDepthOfChildren)
            # update level key and max depth balancing for each level
            balancingDepthForEachLevel[levelKey] = max(shiftRegisterDepthOfChildren)

            # now loop through the same level children and find the child that is having shouldInput1andInput2BeBalanced set to true
            for child in children:
                if child.shouldInput1andInput2BeBalanced == True:
                    # check if the child shiftregsiter depth is less than the max depth
                    if child.shiftRegisterDepth < maxDepth:
                        # change or update the child shift register depth
                        child.shiftRegisterDepth = maxDepth
                    
                elif child.shouldInput1BeBalanced == True:
                    # check if the child shiftregsiter depth is less than the max depth
                    if child.shiftRegisterDepth < maxDepth:
                        # change or update the child shift register depth
                        child.shiftRegisterDepth = maxDepth
                    
                elif child.shouldInput2BeBalanced == True:
                    # check if the child shiftregsiter depth is less than the max depth
                    if child.shiftRegisterDepth < maxDepth:
                        # change or update the child shift register depth
                        child.shiftRegisterDepth = maxDepth
         
                    
                
        self.balancingDepthForEachLevelOfPC = balancingDepthForEachLevel
        self.balancingNeededOrNotForEachLevelOfPC = balancingNeededForEachLevel
        #print("Max Depth for levels of PC", self.balancingDepthForEachLevelOfPC)


        
        
    """
    # End: balance arithmetic nodes
    """

    """
    # Start: Remove Disabled Arithmetic Nodes
    """
    def removeDisabledArithmeticNodes(self):
        optimisedArithmeticNodes = self.arithmeticNodes.copy()
        for arithmeticNode in self.arithmeticNodes:
            if arithmeticNode.enable == False:
                optimisedArithmeticNodes.remove(arithmeticNode)
            
        self.optimisedArithmeticNodes = optimisedArithmeticNodes


    """
    # End: Remove Disabled Arithmetic Nodes
    """

    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()
    
    def process(self):
        super().process()

    def perform(self):
        super().process()

    def main(self):
        super().main()

    def run(self):
        self.main()

