#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:56:09 2021

@author: Karthekeyan Periasamy
"""

class EquationParser():
    
    """
    Notes: Equation parser object to support parsing equations that are balanced
    1. Primarily, the object will help parse AC equation, SPN equation, still it could be used to parse any other balanced equation
    2. For now, the equation parser can only support addition and multiplication operation without operator precedence
    3. The parser works well only on bracket precedence
    """
    
    """
    # Start: Function definitions

    """
    
    """
    #Start : Default init function
    """
    
    def __init__(self):
        
        #declare a variable to store the closing bracket
        self.closingBracket = ")"
        #declare a variable to store the opening bracket
        self.openingBracket = "("
        # declare a variable to store the multiplication operator
        self.multiplicationOperator = "*"
        # declare a variable to store the addition operator
        self.additionOperator = "+"
        # declare the addition operations counter
        self.additionOperation = 0
        # declare the addition operations counter
        self.multiplicationOperation = 0
        # set the current operator with which the operation will be performed
        self.currentOperator = None
        # set the current number of operations to be performed with the current operator
        self.currentNumberOfOperators = None
       
        # declare the equation
        self.equationString = "(((0.6*(0.3))+(0.4*0.5))*0.5)"
        # conver the equationString string into an array with characters in it
        self.equation = list(self.equationString)
        # declare an empty list to store the brackets and operands
        self.bracketsAndOperatorStack = list()
        # declare an empty list to store the elements of the operandValue
        self.operandElementStack = list ()
        # declare an empty list to store the operandValues
        self.operandValueStack = list()
        # initialise the object as we have the spnEquation and its associated list
        self.init()
    
    """
    #End - Default init Function
    """
    
    
    
    """
    #Start: custom init function
    """
    def init(self):
        pass
    
    """
    #End: custom init function
    """
    
    
    """
    #Start: Stack:  BracketsAndOperator
    """
    
    
    """
    # Start: pushIntoBracketsAndOperatorStack function
    
    1. It pushes or add the retrieved bracket or the operator
       to the bracketsAndOperatorStack list: The parameter is "wordy" so its readable and understandable.
       
    2. The parameter is operatororBracketToBePushed
       
    """
    
    def pushIntoBracketsAndOperatorStack(self,operatorOrBracketToBePushed):
        # check the passed parameter is not None.
        # if None, print error message using the else statement
        if operatorOrBracketToBePushed is not None:
            # print the array to understand before adding the element
            #print("OriginalOperatorAndBracketsQueue",self.bracketsAndOperatorStack)
            # check whether the pushed element is an operator or bracket
            # add the operatorOrBracketToBePushed to the stack or list
            self.bracketsAndOperatorStack.append(operatorOrBracketToBePushed)
            # print the array to understand where the added element is
            #print("UpdatedOperatorAndBracketsQueue",self.bracketsAndOperatorStack)
        else:
            #print("Error: The passed argument operatorOrBracketToBePushed is None")
            return
        return
    
    """
    #End: pushIntoBracketsAndOperatorStack function
    """
    
    
    """
    # Start: popBracketsAndOperatorStack function
    1. It pops the last elements of the queue.
    2. This function will be called when an opertion or multiple operations are done
    """
    
    def popBracketsAndOperatorStack(self):
        # print the Queue
        #print("OriginalbracketsAndOperatorStack",self.bracketsAndOperatorStack)
        # remove the last element of the bracketsAndOperatorStack
        # pop the last element that entered the queue last
        self.bracketsAndOperatorStack.pop(len(self.bracketsAndOperatorStack)-1) 
        # print the udpated Queue
        #print("UpdatedbracketsAndOperatorStack",self.bracketsAndOperatorStack)
    
    """
    # End:popBracketsAndOperatorStack function
    """
    
    """
    # Start: popOperatorsFrombracketsAndOperatorStack function
    1. It pops the operators based on the number of operators that is passed as parameter.
    2. This function will be called once performOpertion is done
    """
    
    def popOperatorsFrombracketsAndOperatorStack(self, numberOfOperators):
        #print("Total operators to be popped:", numberOfOperators)
        #print("OriginalOperatorAndBracketsQueue",self.bracketsAndOperatorStack)
        startIndex = len(self.bracketsAndOperatorStack)-1
        totalToBePopppedOPerators = numberOfOperators
        #closingBracket = None
        while totalToBePopppedOPerators != 0:
            # closingBracket = self.bracketsAndOperatorStack[startIndex]
            #print("The operator:", closingBracket)
            totalToBePopppedOPerators = totalToBePopppedOPerators - 1
            #print("Number of operators left to be poped:", totalToBePopppedOPerators)
            self.bracketsAndOperatorStack.pop(startIndex)
            startIndex = startIndex-1
            #closingBracket = self.bracketsAndOperatorStack[startIndex]
        
        #print("UpdatedbracketsAndOperatorStack",self.bracketsAndOperatorStack)
    
    """
    # End:popOperatorsFrombracketsAndOperatorStack function
    """
    
    
    """
    # Start: topElementOfBracketsAndOperatorStack function
    
    1. Access the last element of the Queue, mostly it should be an operator  
    2. The return value is topElementOfBracketsAndOperatorStack
       
    """
    
    def topElementOfBracketsAndOperatorStack(self):
        # print the stack to know what is the state of the stack before accessing the elements
        #print("OriginalOperatorAndBracketsQueue :",self.bracketsAndOperatorStack)
        # access the topElementOfBracketsAndOperatorStack
        topElementOfBracketsAndOperatorStack = self.bracketsAndOperatorStack[-1]
        # print the array to understand where the added element is
        #print("OriginalOperatorAndBracketsQueue :",self.bracketsAndOperatorStack)
        return topElementOfBracketsAndOperatorStack
    
    """
    #End: topElementOfBracketsAndOperatorStack function
    """
    
    
    
    """
    # Start: topElementIndexOfBracketsAndOperatorStack function
    
    1. Access the last elementIndex of the Queue.  
    2. The return value is an integer
       
    """
    
    def topElementIndexOfBracketsAndOperatorStack(self):
        # print the stack length
        #print("LengthOfOriginalOperatorAndBracketsQueue :",len(self.bracketsAndOperatorStack))
        # access the topElementIndexOfBracketsAndOperatorStack
        topElementIndexOfBracketsAndOperatorStack = len(self.bracketsAndOperatorStack)-1
        # print the array to understand where the added element is
        #print("AccessedIndexOperatorAndBracketsQueue :",topElementIndexOfBracketsAndOperatorStack)
        return topElementIndexOfBracketsAndOperatorStack
    
    """
    #End: topElementIndexOfBracketsAndOperatorStack function
    """
    
    
    """
    #End: Stack:  BracketsAndOperator
    """
    
    
    """
    # Start: Stack: OperandElement
       
    """
    
    
    """
    # Start: pushIntoOperandElementStack function
    
    1. It pushes or add the sensed element
       to the operandElementStack: The parameter is wordy for the purpose of understanding the code.
       
    2. The parameter is operandElementToBePushed
       
    """
    
    def pushIntoOperandElementStack(self,operandElementToBePushed):
        # check the passed parameter is not None.
        # if None, print error message using the else statement
        if operandElementToBePushed is not None:
            # print the stack to know what is the state of the stack before adding the element
            #print("OriginalOperandElementStack",self.operandElementStack)
            # add the equationElementToBePushed to the stack or list
            self.operandElementStack.append(operandElementToBePushed)
            # print the array to understand where the added element is
            #print("UpdatedOperandElementStack",self.operandElementStack)
        else:
            #print("Error: The passed argument: equationElementToBePushed is None")
            return
        return
    
    """
    #End: pushIntoOperandElementStack function
    """
    
    
    """
    # Start: popOperandElementStack function
    1. It pops all the elements of the stack and return the appended operandValue
    """
    
    def popOperandElementStack(self):
        # print the stack to know what is the state of the stack before poping all the elements
        #print("OriginalOperandElementStack",self.operandElementStack)
        # append the existing elements of the operandElementStack
        # as its a stack LIFO retreival scheme should be followed to correctly represent the string
        operandValue = None
        for indexOfOperandElement, operandElement in reversed(list(enumerate(self.operandElementStack))):
            # print the indeOfOperandElement and operandElement
            #print("IndexOfOperandElement: ", indexOfOperandElement, " OperandElement: ", operandElement)
            # check the indexOfOperandElement, if its 0 we need to set the operandElement to the operandValue
            if indexOfOperandElement == (len(self.operandElementStack)-1):
                operandValue = operandElement
            else:
                # concatenate the operandValue with th operandElement
                operandValue = operandValue + operandElement
        # print the operandValue
        #print("The OperandValue :", operandValue)
        # remove all the operands from the operandElementStack
        self.operandElementStack.clear()     
        # print the udpated stack
        #print("UpdatedOperandElementStack",self.operandElementStack)
        return operandValue
    
    """
    # End:popOperandElementStack function
    """
    
    """
    # End: Stack: OperandElement
       
    """
    
    
    """
    # Start: Stack: OperandValue
       
    """
    
    
    """
    # Start: pushIntoOperandValueStack function
    
    1. It pushes or add the retrieved operandValue
       to the operandValueStack: The parameter is wordy for the purpose of understanding the code.
       
    2. The parameter is operandValueTobePushed
       
    """
    
    def pushIntoOperandValueStack(self,operandValueTobePushed):
        # check the passed parameter is not None.
        # if None, print error message using the else statement
        if operandValueTobePushed is not None:
            # print the stack to know what is the state of the stack before adding the element
            #print("OriginalOperaValueStack",self.operandValueStack)
            # add the equationElementToBePushed to the stack or list
            self.operandValueStack.append(operandValueTobePushed)
            # print the array to understand where the added element is
            #print("UpdatedOperatorValueStack",self.operandValueStack)
        else:
            #print("Error: The passed argument: operandValueTobePushed is None")
            return
        return
    
    """
    #End: pushIntoOperandValueStack function
    
    """
    
    """
    # Start: popOperandValueStack function
    
    1. It pushes or add the retrieved operandValue
       to the operandValueStack: The parameter is wordy for the purpose of understanding the code.
    2. The parameter is operandValueTobePushed
       
    """
    
    def popOperandValueStack(self, startRange, stopRange):
        # loop through the range of operandValues that needs to be poped
        for indexOfOperandValue in range(startRange,stopRange,-1):
            self.operandValueStack.pop(indexOfOperandValue)
        return
    
    """
    #End: popOperandValueStack function
    
    """
    
    """
    # Start: Stack: OperandValue
       
    """
    
    
    
    """
    # Start: findNumberOfOperatorsBetweenBrackets function
    """
    
    def findNumberOfOperatorsBetweenBrackets(self):
        startIndex = len(self.bracketsAndOperatorStack)-1
        closingBracket = None
        numberOfOperators = 0
        while closingBracket != self.closingBracket:
            closingBracket = self.bracketsAndOperatorStack[startIndex]
            if (closingBracket == self.closingBracket):
                #print("The operator:", closingBracket)
                continue
            #print("The operator:", closingBracket)
            numberOfOperators = numberOfOperators + 1
            #print("The number of operators:", numberOfOperators)
            startIndex = startIndex-1
        return numberOfOperators
    """
    # End: findNumberOfOperatorsBetweenBrackets function 
    """
    
    
    
    
    """
    # Start: performOperation function
    1. It performs the operation with the values of the operandValueStack

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
                operationValue = float(operandValue)
                # print the final operationValue
                #print( "The updated operationValue: ", operationValue)
            else:
                # Then check the operator, for now two operations are supported
                # 1. Multiplication 
                # 2. Addition
                if self.currentOperator is self.multiplicationOperator:
                    # do multiplication
                    # increase the multiplication operation counter
                    self.multiplicationOperation = self.multiplicationOperation + 1
                    # make a productNode object with two inputs
                    operationValue = operationValue * float(operandValue)
                elif self.currentOperator is self.additionOperator:
                    # do addition
                    # increase the addition operation counter
                    self.additionOperation = self.additionOperation + 1
                    operationValue = operationValue + float(operandValue)
                    
                    
        # print the final operationValue
        #print( "The updated operationValue: ", operationValue)
        # pop the operandValueStack
        self.popOperandValueStack(startRange, stopRange)
        # push the calculated new operandValues into operandValueStack
        self.pushIntoOperandValueStack(operationValue)
        # pop the operator or operators from the bracketsAndOperatorStack
        self.popOperatorsFrombracketsAndOperatorStack(numberOfOperators)
        return True
    
    
    """
    # End: performOperation function
    """
    
    
    """
    # Start: ProcessOperation
    
    1. The function will be called whenever we encounter an oeprator
    2. During the event of an operator, we need some information and process information from stacks
    3. This function serves the purpose of doing some primitive information processing in 
       operandElement stack and bracketsAndOperatorStack
    
    4. The function returns a operandValue and operator after processing the above two stacks
    """
    def processOperation(self):
        # print the event
        #print("Function call: Processing operation")
        # before pushing the operator to the bracketsAndOperatorStack, we need to concatenate the StringElements
        # together to form the equationValue to be operated on the operator
        operandValue = self.popOperandElementStack()
        # Now, push the equationValue into the operandValueStack
        self.pushIntoOperandValueStack(operandValue)
        # access the top element, that is an operator from the bracketsAndOperatorStack
        operator = self.topElementOfBracketsAndOperatorStack()
        return operandValue, operator
    """
    # End: process operation
    """
    
    """
    # Start: processOpeningBracket operation
    """
    
    def processOpeningBracket(self, openingBracket):
        # print the event
        #print("Found an opening bracket \n")
        # access the top element of the bracketsAndOperatorStack
        topOperator = self.topElementOfBracketsAndOperatorStack()
        #print("Opening Bracket call: The last element of the operandAndBracketsStack: \n", topOperator)
        # check whether its an operator or not
        if ((topOperator in self.additionOperator) or (topOperator in self.multiplicationOperator)):
            # print the operator
            #print("Opening Bracket call: The operator: \n", topOperator)
            # check whether there are operandElements in operandElement stack by checking the length of the stack
            operandElementStackLength = len(self.operandElementStack)
            if operandElementStackLength > 0:
                if (topOperator is self.multiplicationOperator):
                    #print("Open bracket multiplication operation call")
                    self.performMultiplicationOperation(openingBracket)
                else:
                    # pop the operandElementStack
                    operandValue = self.popOperandElementStack()
                    # push the operandValue to the operandValueStack
                    self.pushIntoOperandValueStack(operandValue)
            
            # access the numberOfOperators and perform the left over operation
            numberOfOperators = self.findNumberOfOperatorsBetweenBrackets()
            if numberOfOperators > 0:
                #print("The total number of operators between opening and closing brackets are:", numberOfOperators)
                # access the top element of the bracketsAndOperatorStack
                operandValueStackLength = len(self.operandValueStack)
                # if the length of the operandValueStack is less than 2
                #print("Available operandValues:", operandValueStackLength)
                topOperator = self.topElementOfBracketsAndOperatorStack()
                # set the topOperator to be the currentOperator
                self.currentOperator = topOperator
                # set the number of operators to currentNumberOfOperators
                self.currentNumberOfOperators = numberOfOperators
                # perform the operation on operandValueStack
                self.performOperation()
                
        # if the numberOfOperators are zero, remove the opening and closing bracket pair
        self.popBracketsAndOperatorStack()
        return
    
    """
    End: processOpeningBracket
    """
    
    
    """
    # Start: Perform addition operation
    """
    def performAdditionOperation(self, operator):
        # set the equation element string
        equationElementString = self.additionOperator
        # set the numberOfMultiplicationOperation
        numberOfAdditionOperation = 1
        # print the event
        #print("Found Addition operator")
        operandValue,topOperator = self.processOperation()
        #print("The operandValue before performing addition operation:", operandValue)
        #print("The top operator:", topOperator)
        # check whether which operator it is
        if (topOperator in self.multiplicationOperator):
            # print the event
            #print("Found different top operator, Multiplication operator is present before addition operator")
            # pop the operandElementStack
            operandValue = self.popOperandElementStack()
            #print("Poped operandValue :", operandValue)
            # if the operandValue is none, try to use the operandValues in operandValueStack to complete the operation
            if operandValue != None:
                # push the operandValue to the operandValueStack
                self.pushIntoOperandValueStack(operandValue)
                
            # set the topOperator to be the currentOperator
            self.currentOperator = topOperator
            # set the number of operators to currentNumberOfOperators
            self.currentNumberOfOperators = numberOfAdditionOperation
            # perform the operation on operandValueStack
            self.performOperation()
        # push the operator to the bracketsAndOperatorStack
        self.pushIntoBracketsAndOperatorStack(equationElementString)
        
    """
    # End: Perform Addition operation
    """
    
    """
    # Start: Perform multiplication operation
    """
    def performMultiplicationOperation(self, operator):
        # print the event
        #print("Function call: Perform multiplication operation using the parameter: Operator")
        # set the numberOfMultiplicationOperation
        numberOfMultiplicationOperation = 1
        # set the local "multiplicationOperator" with the multiplication operation string
        multiplicationOperator = self.multiplicationOperator
        operandValue,topOperator = self.processOperation()
        # check whether its an addition operator or not
        if (topOperator in self.additionOperator):
            # print the operator
            #print("Found different operator: Addition before multiplication")
            # pop the operandElementStack
            operandValue = self.popOperandElementStack()
            # if the operandValue is none, try to use the operandValues in operandValueStack to complete the operation
            if operandValue != None:
                # push the operandValue to the operandValueStack
                self.pushIntoOperandValueStack(operandValue)
        elif (topOperator in multiplicationOperator): 
            # print the operator
            #print("Found Multiplication operator")
            # set the topOperator to be the currentOperator
            self.currentOperator = topOperator
            # set the number of operators to currentNumberOfOperators
            self.currentNumberOfOperators = numberOfMultiplicationOperation
            # perform the previous multiplication operation first, then push the current multiplication operator
            isOperationSuccessFul = self.performOperation()
            if isOperationSuccessFul:
                #print("Top multiplication operation successful")
                # check the current operator element of the operatorBracketsStack again
                if (operator in self.multiplicationOperator):
                    self.pushIntoBracketsAndOperatorStack(multiplicationOperator)
                return
        elif (topOperator in self.openingBracket):
            # print the operator
            #print("Found opening bracket as top operator")
            # set the topOperator to be the currentOperator
            self.currentOperator = topOperator
            # set the number of operators to currentNumberOfOperators
            self.currentNumberOfOperators = numberOfMultiplicationOperation
            # perform the previous multiplication operation first, then push the current multiplication operator
            isOperationSuccessFul = self.performOperation()
            if isOperationSuccessFul:
                #print("Previous multiplication operation successful: Now opening bracket and closing bracket should be removed")
                return

        # push the operator to the bracketsAndOperatorStack
        self.pushIntoBracketsAndOperatorStack(multiplicationOperator)
        
    """
    # End: Perform multiplication operation
    """
    
   
    """
    # Start: parseEquation function
    """
    def parseEquation(self):
        """
        Loop procedure
        
        1. Loop through the array till we reach the first element of the array
        2. use "for" loop to reverse loop the equation in the reverse order
        3. Check whether the retireved element is a opening bracket, closing bracket,operand or operator
        4. Upon every check we perform the necessary steps (explained inside each function to compute the output of the parser)
        
        """
        # reverse loop the equation
        for indexOfEquationElement, equationElementString \
            in reversed(list(enumerate(self.equation))):
                #print the index and equationElement
                #print("IndexOfEquationElement :", indexOfEquationElement, "EquationElementString: ",equationElementString)
                # It is expected to have "(" at the end of the equation
                # So check the ")" or closing bracket
                if (equationElementString in self.closingBracket):
                    # print event
                    #print("Event: closing bracket")
                    # As we retrieved a closing bracket, we need to store it in bracketsAndOperatorStack
                    # push the closing bracket into the bracketsAndOperand stack
                    self.pushIntoBracketsAndOperatorStack(equationElementString)
                # check whether the retrieved equationStringElement is an operator or not
                elif ((equationElementString in self.multiplicationOperator)):
                    # perform multiplication operation
                    #print("Event: Multiplication operator")
                    self.performMultiplicationOperation(equationElementString)
                elif ((equationElementString in self.additionOperator)):
                    # perform addition operation
                    self.performAdditionOperation(equationElementString)
                elif (equationElementString in self.openingBracket):
                    # process opening bracket
                    self.processOpeningBracket(equationElementString)
                else:
                    # print the event
                    #print("Event: Operand:", equationElementString)
                    # the retrieved equationStringElement is part of the operand
                    # push into the operandElementStack
                    self.pushIntoOperandElementStack(equationElementString)
                    # However to form the operand value, we need to retrieve all the operands
                    # Once we retrieve all the operand, we need to append the elements.
                    # The above scenario will happen once we receive the operator
                    # The previous steps are handled inside the operator elif condition
                    
        #print("Equation fully parsed: successfully or not still needs to be verified using the generated log or text file")
        # print the total number of multiplication operation
        #print("Total number of addition operations: ", self.additionOperation)
        # print the totalnumber of addition operation
        #print("Total number of multiplication operations: ", self.multiplicationOperation)
        return
    
    """
    # End: parseEquation function
    """
    """
    # Start: resetEquationParser
    """
    def resetEquationParser(self):
        # declare the addition operations counter
        self.additionOperation = 0
        # declare the addition operations counter
        self.multiplicationOperation = 0
        # set the current operator with which the operation will be performed
        self.currentOperator = None
        # set the current number of operations to be performed with the current operator
        self.currentNumberOfOperators = None
        # declare an empty list to store the brackets and operands
        self.bracketsAndOperatorStack = list()
        # declare an empty list to store the elements of the operandValue
        self.operandElementStack = list ()
        # declare an empty list to store the operandValues
        self.operandValueStack = list()
    
    """
    # End: resetEquationParser
    """
                    
    """
    #Start: Main function
    """
    def main(self):
        self.parseEquation()
    
    """
    #End: Main function
    """
    
    
    """
    #Start: Run function
    """
    def run(self):
        # call the main function
        self.main()
    
    """
    #End: Run function
    """
