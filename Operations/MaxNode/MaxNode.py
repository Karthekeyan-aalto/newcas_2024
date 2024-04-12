#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:23:08 2022

@author: Karthekeyan Periasamy
"""
from Port import Port

class MaxNode():
    
    """
    # Start - Default init Function
    """
    
    def __init__(self):
        # the number is set in the equation parser when we peform an operation in the equation parser
        
        """
        ===========================================================================
        Basic properites of the MaxNode, that describes the ports: input and output
        ===========================================================================
        """
        self.number = 0
        self._input1 = None
        self._input2 = None
        self._output = None
        self.ports = list()
        self.portsInfo = dict()
        self.numberOfBits = 8
        self.portLetter = "v"
        self._numberSystem = 0
        self._numberSystemName = None
        
        """
        operation Mode = 1 its a mode to generate VHDL
        operation Mode = 0 its a mode to do realtime calculation
        """
        self.operationMode = 0
        
        """
        analysisMode = 0 its VHDL creation mode - default
        analysisMode = 1 its sensitivity analysis
        analysisMode = 2 its MPE inference
        analysisMode = 3 Expression Solving
        
        """
        self.analysisMode = 0
        
        
        """
        ========================================================================
        Values of input1, input2, and output are used to generate VHDL instances
        ========================================================================
        """
        self._input1Value = None
        self._input2Value = None
        self._outputValue = None
      
        
        """
        ==============================
        VHDL properties of the MaxNode
        ==============================
        """
        self._vhdlInstance = None
        self._vhdlOutputSignal = None
       
        """
        Miscellaneous properties
        """
        self.numberZero = 0
    
    """
    # End - Default init Function
    """

    """
    # Start: Custom setters and getters
    """
    
    """
    # Start: numberSystem setters and getters
    """
    
    @property
    def numberSystem(self):
        return self._numberSystem
    
    
    @numberSystem.setter  
    def numberSystem(self,value):
        # set the numberSystem value
        self._numberSystem = value
        # according to the value of the numberSystem
        # we set the numberSystem name
        if int(self._numberSystem) == 0:
            # set the numberSystem to be fixed
            self.numberSystemName = "sfixed"
        elif int(self._numberSystem) == 1:
            # set the numberSystem to be float
            self.numberSystemName = "float"
        elif int(self._numberSystem) == 2:
            # set the numberSystem to be POSIT
            self.numberSystemName = "posit"
            
    """
    # End: numberSystem setters and getters
    """
    
    """
    # Start: numberSystemName setters and getters
    """
    
    @property
    def numberSystemName(self):
        return self._numberSystemName
    
    
    @numberSystemName.setter  
    def numberSystemName(self,value):
        # set the numberSystemName value
        self._numberSystemName = value
       
    """
    # End: numberSystemName setters and getters
    """
    
    """
    # Start: input1 setters and getters
    """
    
    @property
    def input1(self):
        return self._input1
    
    
    @input1.setter  
    def input1(self,value):
        # set the input2 value
        self._input1 = value
        # set the input1Value member variable
        self.input1Value = value
        
    """
    # End: input1 setters and getters
    """
    
    """
    # Start: input1Value setters and getters
    """
    
    @property
    def input1Value(self):
        return self._input1Value
    
    
    @input1Value.setter  
    def input1Value(self,value):
        # set the input2 value
        self._input1Value = value
        # check the input1 value is a port or not
        input1Float = self.__isInput1Float()
        # then update the ports array
        if input1Float == False:
            # check the string name
            portLetter = self._input1Value[self.numberZero]
            # check the first portLetter is actually a porLetter or not
            if (portLetter == self.portLetter):
                # then its a port
                # generate a port object and set its name
                port  = Port.Port()
                port.numberOfBits = self.numberOfBits
                port.numberSystem = self.numberSystem
                port.name = self.input1
                self.ports.append(port)
                # add portname and the port number to portInfo dictionary
                self.portsInfo[port.name] = '1'
            
    """
    # End: input1Value setters and getters
    """
    
    """
    # Start: input2 setters and getters
    """
    
    @property 
    def input2(self):
        return self._input2
        
    
    @input2.setter 
    def input2(self,value):
        # set the input2 value
        self._input2 = value
        # set the input2Value member variable
        self.input2Value = value
        # customise the input1 and _inoput2 value to form the outputvariable
        if self._input1 != None:
            self.output = type(self).__name__ \
                          + str(self.number)\
                          + "Output"
            
    
    """
    # End: input2 setters and getters
    """
    
    """
    # Start: input2Value setters and getters
    """
    
    @property
    def input2Value(self):
        return self._input2Value
    
    
    @input2Value.setter  
    def input2Value(self,value):
        # set the _input2Value value
        self._input2Value = value
        # check the input2 is a port or not
        input2Float = self.__isInput2Float()
        # then update the ports array
        if input2Float == False:
            # check the string name
            portLetter = self._input2Value[self.numberZero]
            # check the first portLetter is actually a porLetter or not
            if (portLetter == self.portLetter):
                # then its a port
                # generate a port object and set its name
                port  = Port.Port()
                port.numberOfBits = self.numberOfBits
                port.numberSystem = self.numberSystem
                port.name = self.input2
                self.ports.append(port)
                # add portname and the port number to portInfo dictionary
                self.portsInfo[port.name] = '2'
            
    """
    # End: input2Value setters and getters
    """
        
    """
    # Start: Output setters and getters
    """
    
    @property
    def output(self):
        return self._output
    
    
    @output.setter  
    def output(self,value):
        # set the _output value
        self._output = value
        # check whether the first and second input are of tupe float
        input1Float = self.__isInput1Float()
        input2Float = self.__isInput2Float()
        if ((input1Float == True) and (input2Float == True)):
            # set the outputValue member variable by finding the max of two input values
            maxValue = max(float(self.input1Value), float(self.input2Value))
            self.outputValue = float(maxValue)
            return
        # generate the vhdlInstance of the productNode with the output
        self.__generateVHDLInstance()
            
    """
    # End: Output setters and getters
    """
    
    """
    # Start: OutputValue setters and getters
    """
    
    @property
    def outputValue(self):
        return self._outputValue
    
    
    @outputValue.setter  
    def outputValue(self,value):
        # set the _output value
        self._outputValue = value
            
    """
    # End: outputValue setters and getters
    """
    
    
    """
    # Start: vhdlInstance setters and getters
    """
    
    @property
    def vhdlInstance(self):
        return self._vhdlInstance
    
    
    @vhdlInstance.setter
    def vhdlInstance(self,value):
        # set the _vhdlInstance value
        self._vhdlInstance = value
            
    """
    # End: vhdlInstance setters and getters
    """
        
    """
    # Start: vhdlPort setters and getters
    """
    
    @property
    def vhdlOutputSignal(self):
        return self._vhdlOutputSignal
    
    
    @vhdlOutputSignal.setter
    def vhdlOutputSignal(self,value):
        # set the vhdlPort value
        self._vhdlOutputSignal = value
            
    """
    # End: vhdlPort setters and getters
    """
    
    """
    # End: End of custom getters and setters
    """
    
    
    """
    # Start: __generateVHDLInstance function
    """
    
    def __generateVHDLInstance(self):
        # append the string to form the vhdlInstance
        self._vhdlInstance = type(self).__name__ \
                                               + str(self.number) + ":"+ " " +"entity work"+"." \
                                               + type(self).__name__+"("+"rtl"+")" "\n" \
                                               + "port map" + "(" + self.input1 + ","  \
                                               + self.input2 + ","+ self.output +")" + ";" + "\n" + "\n"
        #print("VHDL Instance:", self._vhdlInstance)
        # generate the signal of the ProductNode
        self.__generateVHDLOutputSignal()
        
    
        
    """
     # End: __generateVHDLInstance function
    """
    
    
    """
    # Start:  __generateVHDLOutputSignal function
    """
    def __generateVHDLOutputSignal(self):
        self._vhdlOutputSignal = ("Signal" + " "
                                           + self.output \
                                           + ":" + " " + self.numberSystemName + " " + "("+ "0" \
                                           + " " +  "downto" + " " + str((1-self.numberOfBits)) + ")" + ";" + "\n")
            
        #print("VHDL Output Signal:", self._vhdlOutputSignal)
    
    """
    # End: __generateVHDLOutputSignal function
    """
    
    """
    # Start:  isInput1Float function
    
    """
    def __isInput1Float(self):
        try:
            float(self.input1)
            return True
        except ValueError:
            return False
    
    """
    # End: isInput1Float function
    """
    
    """
    # Start:  isInpu21Float function
    
    """
    def __isInput2Float(self):
        try:
            float(self.input2)
            return True
        except ValueError:
            return False
    
    """
    # End: isInpu21Float function
    """
                            
    
    """
    #Start: Main function
    """
    def main(self):
        pass
    
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