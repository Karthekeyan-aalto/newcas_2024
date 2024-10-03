"""
Created by Karthekeyan Periasamy
Edited on April 29, 2023
"""

from SWOptimisers.SWOptimiser import SWOptimiser
from Operators.Adders.Adder import Adder
from Operators.Multipliers.Multiplier import Multiplier

class SWPCArithmeticNodesOptimiser(SWOptimiser):

    def __init__(self):
        self.connect()

    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        super().connectProperties()
        self.isPCArithmeticNodesOptimisationEnabled = False
        # property to store duplicateArithmeticNodeWithTheirReceivers
        self.duplicateArithmeticNodesIndicesWithTheirReceiversIndices = None
        # property to store arithmeticNode Duplicates
        self.arithmeticNodeIndicesWithTheirDuplicatesIndices = None

    def configure(self):
        super().configure()
        
        if self.arithmeticNodes == None:
            return
        print("Length of ArithmeticNodes", len(self.arithmeticNodes))
        
        configurationDetails = self.configurationDetails
        if "DuplicatesOfArithmeticNodeWithTheirReceivers" in configurationDetails:
            self.duplicateArithmeticNodesIndicesWithTheirReceiversIndices = configurationDetails["DuplicatesOfArithmeticNodeWithTheirReceivers"]

        if "ArithmeticNodeDuplicates" in configurationDetails:
            self.arithmeticNodeIndicesWithTheirDuplicatesIndices = configurationDetails["ArithmeticNodeDuplicates"]            
        
    
    def updateDuplicateArithmeticNodesAndTheirReceiverInputs(self):

        if self.isPCArithmeticNodesOptimisationEnabled == False:
            return
        
        # access and copy the duplicateArithmeticNodesIndicesWithTheirReceiversIndices
        duplicateArithmeticNodesIndicesWithTheirReceiversIndices = self.duplicateArithmeticNodesIndicesWithTheirReceiversIndices.copy()

        # access the arithmeticNodeIndicesWithTheirDuplicatesIndices
        arithmeticNodeIndicesWithTheirDuplicatesIndices = self.arithmeticNodeIndicesWithTheirDuplicatesIndices.copy()

        # access the arithmeticNode and copy the list
        arithmeticNodes = self.arithmeticNodes.copy()


        # use for loop and access the keys from the arithmeticNodesIndicesWithTheirDuplicates
        for originalIndex in arithmeticNodeIndicesWithTheirDuplicatesIndices.keys():
            original = arithmeticNodes[int(originalIndex)]
            duplicatesIndices = arithmeticNodeIndicesWithTheirDuplicatesIndices[originalIndex]
            # use the duplicatesIndices to access the receiverIndices of the duplicates
            for duplicateIndex in duplicatesIndices:
                # access the duplicate arithmetic node
                duplicate = arithmeticNodes[duplicateIndex]
                receiverIndices = duplicateArithmeticNodesIndicesWithTheirReceiversIndices[str(duplicateIndex)]
                # access the receieverIndex
                for receiverIndex in receiverIndices:
                    # access the receiver node from the copy of the arithmetic node
                    receiver = arithmeticNodes[receiverIndex]
                    duplicate.swOperator.isOperatorEnabled = False
                    # access the receiver, check which input of the receiver is same as duplicate output
                    if receiver.input1 == duplicate.output:
                        #print("Receiver Input1", receiver.input1)
                        #print("Receiver Index", receiverIndex)
                        #print("Receiver Input1", receiver.input1)
                        #print("Duplicate Output", duplicate.output)
                        #print("Original Output", original.output)

                        #print("Original",receiver.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                        receiver.input1 = original.output
                        receiver.isInputDataPortsModified = True
                        #print("Updated", receiver.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)

                        #print("Receiver Input1", receiver.input1)
                        #print("Receiver Index", receiverIndex)
                        #print("Receiver Input1", receiver.input1)
                        #print("Duplicate Output", duplicate.output)
                        #print("Original Output", original.output)
                        
                    elif receiver.input2 == duplicate.output:
                        #print("Receiver Input2", receiver.input2)
                        #print("Receiver Index", receiverIndex)
                        #print("Receiver Input2", receiver.input2)
                        #print("Duplicate Output", duplicate.output)
                        #print("Original Output", original.output)
                        
                        #print("Original",receiver.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)
                        receiver.input2 = original.output
                        receiver.isInputDataPortsModified = True
                        #print("Updated", receiver.hwDescription.vhdlEntityDescription.vhdlEntityInstanceDefinition)

                        #print("Receiver Input2", receiver.input2)
                        #print("Receiver Index", receiverIndex)
                        #print("Receiver Input2", receiver.input2)
                        #print("Duplicate Output", duplicate.output)
                        #print("Original Output", original.output)
                
            
        self.optimisedArithmeticNodes = arithmeticNodes
    
    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()
        self.isPCArithmeticNodesOptimisationEnabled = False
        # property to store duplicateArithmeticNodeWithTheirReceivers
        self.duplicatesOfArithmeticNodesWithTheirReceiverIndices = None
        # property to store arithmeticNode Duplicates
        self.arithmeticNodeIndicesWithTheirDuplicatesIndices = None
    
    def process(self):
        super().process()

        if self.arithmeticNodes != None:
            if len(self.arithmeticNodeIndicesWithTheirDuplicatesIndices) > 0:
                self.isPCArithmeticNodesOptimisationEnabled = True
            else:
                print("There are no duplicate arithmeticNodes to optimise")
            

    def perform(self):
        self.updateDuplicateArithmeticNodesAndTheirReceiverInputs()

        if self.isPCArithmeticNodesOptimisationEnabled == False:
            
            for arithmeticNode in self.arithmeticNodes:
                if arithmeticNode.swOperator.isOperatorEnabled == True:
                    self.totalNumberOfArithmeticNodes = self.totalNumberOfArithmeticNodes + 1
                    if isinstance(arithmeticNode,Adder):
                        self.totalNumberOfAdders = self.totalNumberOfAdders + 1
                    elif isinstance(arithmeticNode, Multiplier):
                        self.totalNumberOfMultipliers = self.totalNumberOfMultipliers + 1
            
            print("Total number of arithmetic nodes", self.totalNumberOfArithmeticNodes)
            print("Total number of adder nodes", self.totalNumberOfAdders)
            print("Total number of multiplier nodes", self.totalNumberOfMultipliers)

            return

        for arithmeticNode in self.optimisedArithmeticNodes:
            if arithmeticNode.swOperator.isOperatorEnabled == True:
                self.totalNumberOfArithmeticNodes = self.totalNumberOfArithmeticNodes + 1
                if isinstance(arithmeticNode,Adder):
                    self.totalNumberOfAdders = self.totalNumberOfAdders + 1
                elif isinstance(arithmeticNode, Multiplier):
                    self.totalNumberOfMultipliers = self.totalNumberOfMultipliers + 1
        
        
        #print("Given Duplicate ArithmeticNode Information",self.duplicateArithmeticNodesIndicesWithTheirReceiversIndices)
        #print("Given ArithmeticNodeIndices With Their Duplicates",self.arithmeticNodeIndicesWithTheirDuplicatesIndices)
        #print("Optimised number of arithmetic nodes", self.totalNumberOfArithmeticNodes)
        #print("Optimised number of adder nodes", self.totalNumberOfAdders)
        #print("Optimised number of multiplier nodes", self.totalNumberOfMultipliers)


    def main(self):
        self.process()
        self.perform()
    
    def run(self):
        self.main()
