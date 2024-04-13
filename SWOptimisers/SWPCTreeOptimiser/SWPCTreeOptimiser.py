"""
Created by Karthekeyan Periasamy
Edited on December 25, 2023, 14:53
"""

from SWOptimisers.SWOptimiser import SWOptimiser
from Operators.Adders.Adder import Adder
from Operators.Multipliers.Multiplier import Multiplier


class SWPCTreeOptimiser(SWOptimiser):

    def __init__(self):
        super().__init__()
        self.connect()

    def connect(self):
        super().connect()
        self.connectProperties()
    

    def connectProperties(self):
        super().connectProperties()
                        
        # new property to store the height of the tree
        self.heightOfPCTree = 0
        
        # property to store multipliers on left side a a given arithmeticNode
        self.multipliersOnLeftSideOfArithmeticNode = 0
        # property to store the multiplier on right side of a given arithmetic node
        self.multipliersOnRightSideOfArithmeticNode = 0
        # property to store the adders on the left side of arithmetic node
        self.addersOnLeftSideOfArithmeticNode = 0
        # property to store the adders on the right side of arithmetic node
        self.addersOnRightSideOfArithmeticNode = 0


        # new property to store the levels of the PC
        self.numberOfLevelsOfPCTree = 0

        self.childrenOfEachLevelOfPCTree = None

        # property to store the number of children information for each level of PCTree
        self.numberOfChildrenForEachLevelOfPCTree = None
        
        # balancing depth informaton for each level of PCTree
        self.balancingDelayForEachLevelOfPCTree = None

        # balancing needed or not informaton for each level
        self.balancingNeededOrNotForEachLevelOfMMACUnit = None

        # property to store delay on the longest path of PC Tree
        self.delayOnLongestPathOfPCTree = 0
        
        # property to store the top arithmetic node
        self.topArithmeticNode = None
        
        self.copyOfArithmeticNodes = None





    def configure(self):
        super().configure()
        
        configurationDetails = self.configurationDetails

        if "ArithmeticNodes" in configurationDetails:
            #print(self.arithmeticNodes)
            self.copyOfArithmeticNodes = self.arithmeticNodes.copy()

        if "TopArithmeticNode" in configurationDetails:
            self.topArithmeticNode = configurationDetails["TopArithmeticNode"]
            #print(self.topArithmeticNode)
                
    
    """
    # Start: Function to find the longest path from the given arithmetic Node 
    """

    def longestPathFromArithmeticNode(self,currentNode):
        """
        Logic
        """

        if currentNode == None:
            #print("ArithmeticNode has no child")
            return []
        
        #print("ArithmeticNode HWInstance Name", currentNode.hwDescription.hwInstanceName)
        
        # print the left side arithmeticNodes length
        #print("Start Traversing Left Side of",currentNode.hwDescription.hwInstanceName)
           
        # recursively process the left  child of the currentNode
        leftSideArithmeticNodeList = self.longestPathFromArithmeticNode(currentNode.swOperator.leftChild)
        
        # print the left side arithmeticNodes length
        #print("Start Traversing Right Side of",currentNode.hwDescription.hwInstanceName)
        
        # recursively process the  right child of the current node
        rightSideArithmeticNodeList = self.longestPathFromArithmeticNode(currentNode.swOperator.rightChild)
        
        # print the left side arithmeticNodes length
        #print("The right side arithmetic nodes", len(rightSideArithmeticNodeList))
        
        # compare the left side arithmetic node list and right side arithmetic node list
        if (len(leftSideArithmeticNodeList) > len(rightSideArithmeticNodeList)):
            leftSideArithmeticNodeList.append(currentNode)
        else:
            rightSideArithmeticNodeList.append(currentNode)

        if (len(leftSideArithmeticNodeList) > len(rightSideArithmeticNodeList)):
            return leftSideArithmeticNodeList


        return rightSideArithmeticNodeList


             
    """
    # End:  Function to find the longest path from the given arithmetic Node 
    """
       
    """
    # Start: Function to find the height of the arithmetic Node using depth first traversal technique
    """

    def heightOfArithmeticNode(self,currentNode):
        """
        Logic
        """
        # depth first traversal method to find the each side height

        # check whether the string has the format defined to find the child of an arithmeticnode from the given array
        if currentNode == None:
            return 0
        
        #print("Height of ArithmeticNode function, CurrentNode is a", currentNode.name)

        # recursively process the left  child of the current node
        leftSideHeight = self.heightOfArithmeticNode(currentNode.swOperator.leftChild)
        
        # recursively process the  right child of the currentNode right child
        rightSideHeight = self.heightOfArithmeticNode(currentNode.swOperator.rightChild)
                
        
        # compare the left height and right side height and increament
        if leftSideHeight > rightSideHeight:
            # print the left side height
            #print("The left side height is > right side height", leftSideHeight+1)
            # print the right side height
            #print("The right side height", rightSideHeight)
            #leftSideHeight.append(currentNode)
            return leftSideHeight + 1
        else:
            # print the left side height
            #print("The left side height", leftSideHeight)
            # print the right side height
            #print("The right side height > left side height", rightSideHeight+1)
            return rightSideHeight + 1
             
    """
    # End: Function to find the height of the arithmetic Node using depth first traversal technique
    """    
       
    """
    # Start: Function to find the depth of the arithmetic Node using depth first traversal technique
    """

    def depthOfArithmeticNode(self, rootNode, currentNode):
        """
        Logic
        """        
        # check the rootNode has valid left and right child node or not 
        if ((rootNode == None)):
            return -1
        
        #print("RootNode Name", rootNode.name)
        #print("RootNode Input1", rootNode.input1)
        #print("RootNode Input2", rootNode.input2)
        #print("CurrentNode Name", currentNode.name)
        #print("CurrentNode Input1", currentNode.input1)
        #print("CurrentNode Input2", currentNode.input2)

        depth = -1
        
        # check whether the rootNode and the currentNode are same
        if ((currentNode.input1 == rootNode.input1) and (currentNode.input2 == rootNode.input2)):
            #print("Reached the CurrentNode from the root node")
            return depth + 1
        
        #print("The current depth", depth)leftChil
        
        # recursively process the left  child of the currentNode
        depth = self.depthOfArithmeticNode(rootNode.swOperator.leftChild,currentNode)
            
        # print the left side height
        #print("The left side depth from root node to current node", depth)
            
        #  check if the depth on the left side is greater than zero or not the left height and right side height and increament
        if depth >= 0:
            return depth + 1
        
        # recursively process the  right child of the currentNode
        depth = self.depthOfArithmeticNode(rootNode.swOperator.rightChild,currentNode)
        
        # print the right side height
        #print("The right side depth from root node to current node", depth)
        
        #  check if the depth on the left side is greater than zero or not the left height and right side height and increament
        if depth >= 0:
            #print("Depth is greater than 0")
            return depth + 1
            
        #print("The final depth", depth)
        return depth

    """
    # End: Function to find the depth of the arithmetic Node using depth first traversal technique
    """
    
    """
    # Start: Function to find levels of PCTree
    """

    def levelTraversePCTree(self,rootNode):
        """
        Logic
        """
        #print("Level Traverse PCTree, starting from root node", rootNode.name)
        
        # check if the rootNode is none or not
        if rootNode == None:
            return


        # property to find the levels, this property will be incremented
        self.numberOfLevelsOfPCTree = 1
        #initialise the children of level dict
        numberOfChildrenForEachLevelOfPCTree = dict()
        # property to store the children of the current level
        childrenOfCurrentLevelOfPCTree = None
        # property to store the children of all levels
        childrenOfAllLevelsOfPCTree = dict()
        
        # breadth first traversal method using queues to find the levels and the number of nodes per level
        # use list based queue
       
        # we can access the input 1 driver and input 2 driver add them to the queue
        # create a queue using list
        queue = list()

        # add the root node
        queue.append(rootNode)
        
        # access the length of the queue and update the children of level with respect to root node
        numberOfChildrenForEachLevelOfPCTree[str(self.numberOfLevelsOfPCTree)] = len(queue)

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
                # print the current node name
                #print("The current node name", currentNode.name)
                #print the current node input 1 and input 2
                #print("The current node input1", currentNode.input1)
                #print("The current node input2", currentNode.input2)


                # first check whether there is a valide left child and right child or not
                if currentNode.swOperator.leftChild == None and currentNode.swOperator.rightChild == None:
                    

                    # access the root node and find the depth of the current node
                    depthOfCurrentNode = self.depthOfArithmeticNode(rootNode, currentNode)
                    #print("CurrentNode Name", currentNode.name)
                    #print("The depth of the current node", depthOfCurrentNode)
                    
                    #if depthOfCurrentNode < 0:                        
                        # property to store the node depth, where the node is the current node
                        #depthOfCurrentNode = self.depthOfMMACUnitNode(rootNode.rightChild, currentNode)

                        #print("The depth of the CurrentNode", depthOfCurrentNode)
                        #print("Input1 of current node", currentNode.input1)
                        #print("Input2 of current node", currentNode.input2)


                    # check the difference between depth of the current node and height of PCTree
                    if (self.heightOfPCTree - depthOfCurrentNode) != 1:
                        #print("The height of PCTree", self.heightOfPCTree)
                        #print("Input1 is a port or weight, Input2 is a port or weight, or Input1 and Input2 both are ports and the DepthOfCurrentNode")
                        #print("Current Node Shift Register Delay", (int(self.heightOfPCTree-depthOfCurrentNode)-1))
                        # set the property of the shift register depth
                        currentNode.shiftRegisterDelay = (int(self.heightOfPCTree-depthOfCurrentNode)-1)
                        #print("The difference between height of PCTrree and Depth of CurrentNode", (int(self.heightOfPCTree-depthOfCurrentNode)-1))
                        currentNode.shouldAShiftRegisterBeAddedToInput1AndInput2 = True
                    else:
                        #print("Input1 is a port or weight, Input2 is a port or weight, or Input1 and Input2 both are ports and the DepthOfCurrentNode")
                        #print("Input1 of current node", currentNode.input1)
                        #print("Input2 of current node", currentNode.input2)
                        longestPathFromArithmeticNode = self.longestPathFromArithmeticNode(currentNode)

                        #print("LongestPathFromArithmeticNode", len(longestPathFromArithmeticNode))
                        #print("CurrentNode Input1", currentNode.input1)
                        #print("CurrentNode Input2", currentNode.input2)
                        
                        multipliersOnLongestPathFromArithmeticNode = 0
                        addersOnLongestPathFromArithmeticNode = 0
                        for arithmeticNode in longestPathFromArithmeticNode:
                            if isinstance(arithmeticNode, Multiplier):
                                multipliersOnLongestPathFromArithmeticNode = multipliersOnLongestPathFromArithmeticNode + 1
                            elif isinstance(arithmeticNode, Adder):
                                addersOnLongestPathFromArithmeticNode = addersOnLongestPathFromArithmeticNode + 1
                        
                        if isinstance(currentNode, Adder):
                            addersOnLongestPathFromArithmeticNode = addersOnLongestPathFromArithmeticNode - 1
                        elif isinstance(currentNode, Multiplier):
                            multipliersOnLongestPathFromArithmeticNode = multipliersOnLongestPathFromArithmeticNode - 1
                        
                        delayOnTheLongestPathOfPCTreeFromOperator = (((self.multiplierPipelineDepth*multipliersOnLongestPathFromArithmeticNode) + (self.adderPipelineDepth*addersOnLongestPathFromArithmeticNode)))
                        #print("Delay On the LongestPath From Operator with no children", delayOnTheLongestPathOfPCTreeFromOperator)
                        currentNode.swOperator.delayOnTheLongestPathOfPCTreeFromOperator = delayOnTheLongestPathOfPCTreeFromOperator


                    continue

                if currentNode.swOperator.leftChild != None and currentNode.swOperator.rightChild != None:
                    
                    longestPathFromArithmeticNode = self.longestPathFromArithmeticNode(currentNode)
                    #print("LongestPathFromArithmeticNode", len(longestPathFromArithmeticNode))
                    #print("CurrentNode Input1", currentNode.input1)
                    #print("CurrentNode Input2", currentNode.input2)
                        
                    multipliersOnLongestPathFromArithmeticNode = 0
                    addersOnLongestPathFromArithmeticNode = 0
                    for arithmeticNode in longestPathFromArithmeticNode:
                        if isinstance(arithmeticNode, Multiplier):
                            multipliersOnLongestPathFromArithmeticNode = multipliersOnLongestPathFromArithmeticNode + 1
                        elif isinstance(arithmeticNode, Adder):
                            addersOnLongestPathFromArithmeticNode = addersOnLongestPathFromArithmeticNode + 1
                        
                    if isinstance(currentNode, Adder):
                        addersOnLongestPathFromArithmeticNode = addersOnLongestPathFromArithmeticNode - 1
                    elif isinstance(currentNode, Multiplier):
                        multipliersOnLongestPathFromArithmeticNode = multipliersOnLongestPathFromArithmeticNode - 1
                        
                    delayOnTheLongestPathOfPCTreeFromOperator = (((self.multiplierPipelineDepth*multipliersOnLongestPathFromArithmeticNode) + (self.adderPipelineDepth*addersOnLongestPathFromArithmeticNode)))
                    #print("Delay On the LongestPath from operator with two children", delayOnTheLongestPathOfPCTreeFromOperator)
                    currentNode.swOperator.delayOnTheLongestPathOfPCTreeFromOperator = delayOnTheLongestPathOfPCTreeFromOperator

                
                # check if any one of the input do not have child
                #if (currentNode.swOperator.leftChild == None) or (currentNode.swOperator.rightChild == None):
                if (currentNode.swOperator.leftChild != None):
                    # access the input1 of the currentNode and access the next Node
                    decodedInput = currentNode.input1.split("_")
                    
                    # split the input string
                    #print("Decoded Input2 List",decodedInput)

                    # access the last index element to get the index which drives the input to the current node
                    inputNodeIndex = int(decodedInput[(len(decodedInput)-1)])

                    # using the inputNode Index we can access the driver of current Node
                    driverOfCurrentNode = self.copyOfArithmeticNodes[inputNodeIndex]
                    #print("Driver of Current Node is a ", driverOfCurrentNode.name)

                    # append the current node to the queue
                    queue.append(driverOfCurrentNode)

                elif (currentNode.swOperator.leftChild == None):
                    
                    # property to store the node depth, where the node is the current node
                    depthOfCurrentNode = self.depthOfArithmeticNode(rootNode, currentNode)      
                    #print("Depth of Current Node", depthOfCurrentNode, currentNode.input1)

                    # check the difference between depth and height of the current node
                    if (self.heightOfPCTree - depthOfCurrentNode) != 1:
                        # check the longest path from the current node and count the adders and multipliers in the longest path
                        # this would help multiply the shift regsiter factor to balance the paths effectively.
                        
                        longestPathFromArithmeticNode = self.longestPathFromArithmeticNode(currentNode)
                        #print("LongestPathFromArithmeticNode", len(longestPathFromArithmeticNode))
                        
                        multipliersOnLongestPathFromArithmeticNode = 0
                        addersOnLongestPathFromArithmeticNode = 0
                        for arithmeticNode in longestPathFromArithmeticNode:
                            if isinstance(arithmeticNode, Multiplier):
                                multipliersOnLongestPathFromArithmeticNode = multipliersOnLongestPathFromArithmeticNode + 1
                            elif isinstance(arithmeticNode, Adder):
                                addersOnLongestPathFromArithmeticNode = addersOnLongestPathFromArithmeticNode + 1
                        
                        if isinstance(currentNode, Adder):
                            addersOnLongestPathFromArithmeticNode = addersOnLongestPathFromArithmeticNode - 1
                        elif isinstance(currentNode, Multiplier):
                            multipliersOnLongestPathFromArithmeticNode = multipliersOnLongestPathFromArithmeticNode - 1
                        shiftRegisterDelay = (((self.multiplierPipelineDepth*multipliersOnLongestPathFromArithmeticNode) + (self.adderPipelineDepth*addersOnLongestPathFromArithmeticNode)))
                        #print("Shift Register Delay (Started from node's left child ", shiftRegisterDelay)
                        # set the property of the shift register delay
                        currentNode.shiftRegisterDelay = shiftRegisterDelay
                              
                        #add shift register to the input 2 of the current node
                        currentNode.shouldAShiftRegisterBeAddedToInput1 = True
                                               
                   
                if (currentNode.swOperator.rightChild != None):
                    
                    # access the input2 of the currentNode and access the next Node
                    decodedInput = currentNode.input2.split("_")
                    
                    # split the input string
                    #print("Decoded Input2 List",decodedInput)

                    # access the last index element to get the index which drives the input to the current node
                    inputNodeIndex = int(decodedInput[(len(decodedInput)-1)])

                    # using the inputNode Index we can access the driver of current Node
                    driverOfCurrentNode = self.copyOfArithmeticNodes[inputNodeIndex]
                    #print("Driver of Current Node is a ", driverOfCurrentNode.name)
                    
                    # append the driver of current node to the queue
                    queue.append(driverOfCurrentNode)
                
                elif (currentNode.swOperator.rightChild == None):
                    
                    # property to store the node depth, where the node is the current node
                    depthOfCurrentNode = self.depthOfArithmeticNode(rootNode, currentNode)
                    #print("RightChild != None: The depth of the currentNode", depthOfCurrentNode)
                    #print("Depth of Current Node", depthOfCurrentNode, currentNode.input2)
                        
                    # check the difference between depth and height of the current node
                    if (self.heightOfPCTree - depthOfCurrentNode) != 1:

                        longestPathFromArithmeticNode = self.longestPathFromArithmeticNode(currentNode)
                        #print("LongestPathFromArithmeticNode", len(longestPathFromArithmeticNode))
                        
                        multipliersOnLongestPathFromArithmeticNode = 0
                        addersOnLongestPathFromArithmeticNode = 0
                        for arithmeticNode in longestPathFromArithmeticNode:
                            if isinstance(arithmeticNode, Multiplier):
                                multipliersOnLongestPathFromArithmeticNode = multipliersOnLongestPathFromArithmeticNode + 1
                            elif isinstance(arithmeticNode, Adder):
                                addersOnLongestPathFromArithmeticNode = addersOnLongestPathFromArithmeticNode + 1
                        
                        if isinstance(currentNode, Adder):
                            addersOnLongestPathFromArithmeticNode = addersOnLongestPathFromArithmeticNode - 1
                        elif isinstance(currentNode, Multiplier):
                            multipliersOnLongestPathFromArithmeticNode = multipliersOnLongestPathFromArithmeticNode - 1
                        
                        shiftRegisterDelay = (((self.multiplierPipelineDepth*multipliersOnLongestPathFromArithmeticNode) + (self.adderPipelineDepth*addersOnLongestPathFromArithmeticNode)))
                        #print("Shift Register Delay (Started from node's right child ", shiftRegisterDelay)
                            
                        # set the property of the shift register delay
                        currentNode.shiftRegisterDelay = shiftRegisterDelay
                          
                        #print("The difference between height of PC and Depth of CurrentNode", (self.heightOfPC-depthOfCurrentNode))
                        #add shift register to the input 2 of the current node
                        currentNode.shouldAShiftRegisterBeAddedToInput2 = True
                          
                
                # add the current node to the children level dictionary
                childrenOfCurrentLevel.append(currentNode)

                #print the level based children detail
                #print("The level based children detail", childrenOfCurrentLevel)
                    
            # check the queue length
            if len(queue) == 0:
                print("The total levels of PCTree", self.numberOfLevelsOfPCTree)
                #print("Children Of All Levels", childrenOfAllLevels)
                self.childrenOfEachLevelOfPCTree = childrenOfAllLevelsOfPCTree
                print("Number of Children of each Level Dictionary", numberOfChildrenForEachLevelOfPCTree)
                #print("Global Children Of All Levels", self.childrenOfEachLevelOfMMACUnit)
                #print("Children Of Each Level Of PCTree", self.childrenOfEachLevelOfPCTree)
                return

            # update the levels count
            self.numberOfLevelsOfPCTree = self.numberOfLevelsOfPCTree + 1
            # print the level of the MMACUnit
            #print("The level of MMACUnit", self.numberOfLevelsOfMMACUnit)
            # access the length of the queue
            numberOfChildrenForEachLevelOfPCTree[str(self.numberOfLevelsOfPCTree)] = len(queue)
            # print the queue
            #print("The queue is", queue)
            # copy the queue to a new array or list
            childrenOfCurrentLevelOfPCTree = queue.copy()
            #print("Children Of Current Level", childrenOfCurrentLevel)
            # update the children of current level with the children of all levels dictionary
            childrenOfAllLevelsOfPCTree[str(self.numberOfLevelsOfPCTree)] = childrenOfCurrentLevelOfPCTree
            #print("Children Of All Levels", childrenOfAllLevels)
            # print the childen of levels with the number of children per level
            #print("Number of Children of each Level Dictionary", numberOfChildrenForEachLevelOfPCTree)
            #print("The current level of MMACUnit", self.levelsOfMMACUnit)
            
        #print("Number of Children of each Level Dictionary", numberOfChildrenForEachLevelOfPCTree)
        #print ("The total number of levels of PCTree", self.numberOfLevelsOfPCTree)
       
    """
    # End:  Function to find levels of a MMACUnit
    """
  
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

        # access the top arithmetic node
        topArithmeticNode = self.topArithmeticNode
        #print("The top arithmetic node", topArithmeticNode)
        print("The top arithmetic node is a", topArithmeticNode.name)

        # process the left child of the mmacunit top node
        self.heightOfPCTree = self.heightOfArithmeticNode(topArithmeticNode)        
        print("The height of PCTree", self.heightOfPCTree)
        
        # find the levels of the PCTree, so level traverse PCTree and update the depth of each node with respect to rootNode
        self.levelTraversePCTree(topArithmeticNode)
        
        # find the longest path on the left side of the top node
        longestPathFromArithmeticNode = self.longestPathFromArithmeticNode(topArithmeticNode)
        print("The length of the longest path on the from arithmetic top node is ",len(longestPathFromArithmeticNode))
        
        multipliersOnLongestPathFromArithmeticNode = 0
        addersOnLongestPathFromArithmeticNode = 0
        for arithmeticNode in longestPathFromArithmeticNode:
            if isinstance(arithmeticNode, Multiplier):
                multipliersOnLongestPathFromArithmeticNode = multipliersOnLongestPathFromArithmeticNode + 1
            elif isinstance(arithmeticNode, Adder):
                addersOnLongestPathFromArithmeticNode = addersOnLongestPathFromArithmeticNode + 1
                           
        self.delayOnTheLongestPathOfPCTree = ((self.multiplierPipelineDepth*multipliersOnLongestPathFromArithmeticNode) + (self.adderPipelineDepth*addersOnLongestPathFromArithmeticNode))
        print("The LongestPath of PCTree Delay", self.delayOnTheLongestPathOfPCTree)

       
    """
    # End: Process ArithmeticNodes 
    """
        
    """
    # Start: balance forward paths of arithmetic nodes
    """

    def performForwardPathBalancingOfArithmeticNodes(self):
        # access all the keys of the nodes of all levels object
        levelKeys = self.childrenOfEachLevelOfPCTree.keys()
        # object to store the maxDepth for each level that is used to balance the level of PC
        balancingDelayForEachLevel = dict()
        balancingNeededForEachLevel = dict()
        pcTreeShiftRegisterDelay = dict()

        #print the level keys
        #print("Level Keys", levelKeys)
        # loop through the nodes of all levels
        for levelKey in levelKeys:
            #print the level key
            #print("Level Key", levelKey)
            # access the array of the children per level using levelKey
            children = self.childrenOfEachLevelOfPCTree[levelKey]
            # children shift register delay details
            shiftRegisterDelayOfChildren = list()
            # children that are balanced in a level
            balancedChildren = list()
            # using the children and find the delay of all the children
            for child in children:
                # set the level of the arithmetic node
                child.swOperator.operatorLevelInAPCTree = int(levelKey)
                #print("The level of arithmeticNode",child.levelInMMACUnitTree)
                #print("The shift register depth of the child", child.shiftRegisterDelay)
                #print("The child input1 should be balanced or not", child.swOperator.shouldInput1BeBalanced)
                #print("The child input2 should be balanced or not", child.swOperator.shouldInput2BeBalanced)
                #print("The child input1 and input2 should be balanced or not", child.swOperator.shouldInput1AndInput2BeBalanced)

                # check whether the child input1 or input2 or input1 and input2 should be balanced or not
                if ((child.swOperator.shouldInput1BeBalanced == True) or (child.swOperator.shouldInput2BeBalanced == True) or (child.swOperator.shouldInput1AndInput2BeBalanced == True)):
                    #print("The level where some inputs are balanced", levelKey)
                    delay = child.shiftRegisterDelay
                    #print("The shift register depth of the child", depth)
                    #print("The child input1 should be balanced or not", child.shouldInput1BeBalanced)
                    #print("The child input2 should be balanced or not", child.shouldInput2BeBalanced)
                    #print("The child input1 and input2 should be balanced or not", child.shouldInput1andInput2BeBalanced)
                    # add the depth details to an array
                    shiftRegisterDelayOfChildren.append(delay)

                elif ((child.swOperator.shouldInput1BeBalanced == False) and (child.swOperator.shouldInput2BeBalanced == False) and (child.swOperator.shouldInput1AndInput2BeBalanced == False)):
                    #print("The level where some inputs are balanced", levelKey)
                    delay = child.swOperator.delayOnTheLongestPathOfPCTreeFromOperator
                    #print("The shift register delay of the child", delay)
                    #print("The child input1 should be balanced or not", child.shouldInput1BeBalanced)
                    #print("The child input2 should be balanced or not", child.shouldInput2BeBalanced)
                    #print("The child input1 and input2 should be balanced or not", child.shouldInput1andInput2BeBalanced)
                    # add the children detail to the balanced children
                    balancedChildren.append(child)

                    # add the delay details to an array
                    shiftRegisterDelayOfChildren.append(delay)
                    
            if len(children) == len(balancedChildren):
                #print("The level that do not need balancing")
                balancingDelayForEachLevel[levelKey] = max(shiftRegisterDelayOfChildren)
                balancingNeededForEachLevel[levelKey] = False
                continue

            else:
                #print("The level still needs balancing, even though the some inputs of some nodes are balanced")
                balancingNeededForEachLevel[levelKey] = True

            # find the max from the shift register depth of children
            maxDelay = max(shiftRegisterDelayOfChildren)
            # update level key and max depth balancing for each level
            balancingDelayForEachLevel[levelKey] = max(shiftRegisterDelayOfChildren)
            
            arithmeticNodeLevelBasedDelayDetails = list()
            # now loop through the same level children and find the child that is having shouldInput1andInput2BeBalanced set to true
            for child in children:
                arithmeticNodeDelayDetails = dict()
                if child.swOperator.shouldInput1AndInput2BeBalanced == True:
                    # check if the child shiftregsiter delay is less than the max delay
                    if child.shiftRegisterDelay < maxDelay:
                        # change or update the child shift register delay
                        child.shiftRegisterDelay = maxDelay
                    
                elif child.swOperator.shouldInput1BeBalanced == True:
                    #print the input1 name
                    #print("Child Input1 name", child.input1)
                    # check if the child shiftregsiter delay is less than the max delay
                    if child.shiftRegisterDelay < maxDelay:
                        # change or update the child shift register depth
                        child.shiftRegisterDelay = maxDelay
                    
                elif child.swOperator.shouldInput2BeBalanced == True:
                    #print the input2 name
                    #print("Child Input2 name", child.input2)
                    # check if the child shiftregsiter delay is less than the max delay
                    if child.shiftRegisterDelay < maxDelay:
                        # change or update the child shift register depth
                        child.shiftRegisterDelay = maxDelay

                arithmeticNodeDelayDetails[child.hwDescription.hwInstanceName] = child.shiftRegisterDelay
                arithmeticNodeLevelBasedDelayDetails.append(arithmeticNodeDelayDetails)     
                # add children hwInstance name and the shiftRegisterDelay based on the level to a separate dictionary
                pcTreeShiftRegisterDelay[levelKey] = arithmeticNodeLevelBasedDelayDetails

        self.balancingDelayForEachLevelOfPC = balancingDelayForEachLevel
        self.balancingNeededOrNotForEachLevelOfPC = balancingNeededForEachLevel
        print("Balancing Needed for each levels of PC", self.balancingNeededOrNotForEachLevelOfPC)
        print("Max Depth for levels of PC", self.balancingDelayForEachLevelOfPC)
        #print("PCTree Level Based ShiftRegister Details", pcTreeShiftRegisterDelay)
        # Add the level 1 that is the sum node to the children of each level of mmacunit dictionary
        # print the first object of the arithmetic node
        #print("ArithmeticNode Name",self.arithmeticNodes[len(self.arithmeticNodes)-1].name)

        # add the level details of the top arithmeticNode so it can be used by the VHDL Description to generate appropriate delays when needed
        self.copyOfArithmeticNodes[len(self.copyOfArithmeticNodes)-1].operatorLevelInAPCTree = 1
        self.childrenOfEachLevelOfPCTree["1"] = [self.copyOfArithmeticNodes[len(self.copyOfArithmeticNodes)-1]]        
        
    """
    # End: balance forwards paths of  arithmetic nodes
    """


    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()
        
        # new property to store the height of the tree
        self.heightOfPCTree = 0
        
        # property to store multipliers on left side a a given arithmeticNode
        self.multipliersOnLeftSideOfArithmeticNode = 0
        # property to store the multiplier on right side of a given arithmetic node
        self.multipliersOnRightSideOfArithmeticNode = 0
        # property to store the adders on the left side of arithmetic node
        self.addersOnLeftSideOfArithmeticNode = 0
        # property to store the adders on the right side of arithmetic node
        self.addersOnRightSideOfArithmeticNode = 0


        # new property to store the levels of the PC
        self.numberOfLevelsOfPCTree = 0

        self.childrenOfEachLevelOfPCTree = None

        # property to store the number of children information for each level of PCTree
        self.numberOfChildrenForEachLevelOfPCTree = None
        
        # balancing depth informaton for each level of PCTree
        self.balancingDelayForEachLevelOfPCTree = None

        # balancing needed or not informaton for each level
        self.balancingNeededOrNotForEachLevelOfMMACUnit = None

        # property to store delay on the longest path of PC Tree
        self.delayOnLongestPathOfPCTree = 0
        
        # property to store the top arithmetic node
        self.topArithmeticNode = None
        
        self.copyOfArithmeticNodes = None




    def perform(self):
        super().perform()
        # balance the arithmeticNodes with shift registers 
        self.performForwardPathBalancingOfArithmeticNodes()

        # set the copyOfArithmeticNodes back to arithmeticNodes
        self.arithmeticNodes = self.copyOfArithmeticNodes

    def process(self):
        super().process()
        self.processArithmeticNodes()

    def main(self):
        self.process()
        self.perform()

    def run(self):
        super().run()
