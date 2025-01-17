#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 10:12:40 2021

@author: Karthekeyan Periasamy
"""

from Port import Port

class SumNode():
    
    """
    # Start - Default init Function
    """
    
    def __init__(self):
        # the number is set in the equation parser when we peform an operation in the equation parser
        
        """
        ===========================================================================
        Basic properites of the SumNode, that describes the ports: input and output
        ===========================================================================
        """
        self.number = 0
        self._customName = None
        self._input1 = None
        self._name = None
        self._input2 = None
        self._output = None
        self.ports = list()
        self.portsInfo = dict()
        self.numberOfBits = 8
        self.exponentBits = 8
        self.mantissaBits = 8
        self.esBits = 2
        self.portLetter = "v"
        self._numberSystem = 0
        self._numberSystemName = None
        
        # property to know the index where the current sum node is present in the arithmetic node category
        self.arithmeticNodeNumber = 0

        
        """
        ==========================================================================================
        Property: operationMode
        
        operationMode 0: Entity will parser the equation from a given text file and do the analysis
        based on the set analysis mode
        ==========================================================================================
        """
        # different operationMode  will be used to reset the starting state and procedures to be done initially
        # for now, there is only one operationMode
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
        VHDL properties of the sumNode
        ==============================
        """
        self._vhdlInstance = None
        self._vhdlOutputSignal = None
       
        """
        Miscellaneous properties
        """
        self.numberZero = 0
        
        
        # arithmetic node optimisation properties

        self.equation = None
        # the drivers of the current sumNode
        self._drivers = None
        # the driver equation is the driver which drives one of the input of the productNode
        self._driverEquations = None
        # the receiver equation will be used by the receiver of this product node (or whichever node the current produt node drives)
        self.receiverEquation = None
    
    """
    # End - Default init Function
    """
    
    
    """
    # Start: Custom setters and getters
    """

    """
    # Start: name getters
    """
    @property
    def name(self):
        if self._name == None:
            if self.numberSystem == 0:
                self._name = type(self).__name__ + "_" + "Fixed"
                return self._name
            elif self.numberSystem == 1:
                self._name = type(self).__name__ + "_" + "Float"
                return self._name
            elif self.numberSystem == 2:
                self._name = type(self).__name__ + "_" + "POSIT"
                return self._name
        else:
            return self._name
        
    @name.setter
    def name(self, value):
        self._name = value
    
    
    """
    # Start: customName getters
    """
    @property
    def customName(self):
        if self._customName == None:
            if self.numberSystem == 0:
                self._customName = type(self).__name__ + "_" + "Fixed"
                return self._name
            elif self.numberSystem == 1:
                self._customName = type(self).__name__ + "_" + "Float"
                return self._customName
            elif self.numberSystem == 2:
                # set another POSIT custom name
                # check for the esBits
                # if the esBits is greater than 2, make a new custom Name
                if self.esBits == 2:
                    # set another POSIT custom name
                    self._customName = ("PositAdd" + str(self.esBits) + "_" + str(self.numberOfBits) + "_" + str(self.esBits) + "_" + "F0" + "_" + "uid" + "2")
                elif (self.esBits == 0 or self.esBits == 1):
                    self._customName = ("PositAdd")
                
                elif (self.esBits == 6 and self.numberOfBits == 27) or (self.esBits == 6 and self.numberOfBits == 18) or (self.esBits == 6 and self.numberOfBits == 28) or (self.esBits == 6 and self.numberOfBits == 32) or (self.esBits == 6 and self.numberOfBits == 35) or (self.esBits == 6 and self.numberOfBits == 38) or  (self.esBits == 6 and self.numberOfBits == 42) or (self.esBits == 6 and self.numberOfBits == 45) or (self.esBits == 6 and self.numberOfBits == 48):
                    # set another POSIT custom name
                    self._customName = ("PositAdd" + "_" + str(self.numberOfBits) + "_" + str(self.esBits) + "_" + "comb" + "_" + "uid" + "2")

                elif self.esBits > 2:
                    # set another POSIT custom name
                    self._customName = ("PositAdd" + "_" + str(self.numberOfBits) + "_" + str(self.esBits) + "_" + "F0" + "_" + "uid" + "2")
                return self._customName
        else:
            return self._customName
        
    @customName.setter
    def customName(self, value):
        self._customName = value

    
    """
    # End: customName setters and getters
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
            self.numberSystemName = "std_logic_vector"
            
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
                port.mantissaBits = self.mantissaBits
                port.exponentBits = self.exponentBits
                port.esBits = self.esBits
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
            self.output = self.name + str(self.number) + "Output" + "_" + str(self.arithmeticNodeNumber)
            
    
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
                port.mantissaBits = self.mantissaBits
                port.exponentBits = self.exponentBits
                port.esBits = self.esBits
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
            # set the outputValue member variable by adding the two inputs
            self.outputValue = float(float(self.input1Value) + float(self.input2Value))
            return
        
        else:

            self.equation = "(" + str(self.input2) + "+" + str(self.input1) + ")"
            
            # check the length of input1 when split with underscore be 3
            if (len(self.input1.split("_")) == 3):
                #then access the last part of the split array to access the driver details
                driverNodeIndex = self.input1.split("_")[(len(self.input1.split("_"))-1)]
                # add the driver node index to the drivers dictionary
                self.drivers["Input1"] = driverNodeIndex
                
            # check the length of input1 when split with underscore be 3
            if (len(self.input2.split("_")) == 3):
                #then access the last part of the split array to access the driver details
                driverNodeIndex = self.input2.split("_")[(len(self.input2.split("_"))-1)]
                # add the driver node index to the drivers dictionary
                self.drivers["Input2"] = driverNodeIndex
                #print("SN Type with Input1:  Driven by another node and Input2:  Driven by another node"+"(" + str(self.input2) + "+" + str(self.input1) + ")")

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
    # Start: drivers getter
    """

    @property
    def drivers(self):
        if self._drivers == None:
            self._drivers = dict()
        return self._drivers

    @drivers.setter
    def drivers(self,value):
        self._drivers = value
        
    """
    # End: drivers setter
    """
    
    """
    # Start: driverEquations setters and getters
    """
    
    @property
    def driverEquations(self):
        if self._driverEquations == None:
            self._driverEquations = list()
        return self._driverEquations
    
    
    @driverEquations.setter  
    def driverEquations(self,value):
        # set the driverEquations value
        self._driverEquations = value
        self.processDriverEquations()
    """
    # End: driverEquations setters and getters
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
        # select the numberSystem 
        if self.numberSystem == 0:
            self._vhdlInstance = (self.name + str(self.number) + ":"+ " " +"entity work"+"." \
                                       + self.name +"("+"rtl"+")" "\n" \
                                       + "generic map" + "(" + "numberOfBits" + ")" + "\n" \
                                       + "port map" + "(" + self.input1 + ","  \
                                       + self.input2 + ","+ self.output +")" + ";" + "\n" + "\n")
        elif self.numberSystem == 1:
            self._vhdlInstance = (self.name + str(self.number) + ":"+ " " +"entity work"+"." \
                                       + self.name +"("+"rtl"+")" "\n" \
                                       + "generic map" + "(" + "mantissaBits" + "," + "exponentBits" + ")" + "\n" \
                                       + "port map" + "(" + self.input1 + ","  \
                                       + self.input2 + ","+ self.output +")" + ";" + "\n" + "\n")
        
        elif self.numberSystem == 2:
            self._vhdlInstance = (self.name + str(self.number) + ":"+ " " +"entity work"+"." \
                                       + self.customName +"("+"arch"+")" "\n" \
                                       + "port map" + "(" + self.input1 + ","  \
                                       + self.input2 + ","+ self.output +")" + ";" + "\n" + "\n")



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
        if self.numberSystem == 0:
            self._vhdlOutputSignal = ("Signal" + " "
                                           + self.output \
                                           + ":" + " " + self.numberSystemName + " " + "("+ "0" \
                                           + " " +  "downto" + " " + str((1-self.numberOfBits)) + ")" + ";" + "\n")
        elif self.numberSystem == 1:
            self._vhdlOutputSignal = ("Signal" + " "
                                           + self.output \
                                           + ":" + " " + self.numberSystemName + " " + "("+ str(self.exponentBits) \
                                           + " " +  "downto" + " " + str((1-self.mantissaBits)) + ")" + ";" + "\n")
        
        elif self.numberSystem == 2:
            self._vhdlOutputSignal = ("Signal" + " "
                                           + self.output \
                                           + ":" + " " + self.numberSystemName + " " + "("+ str(self.numberOfBits-1) \
                                           + " " +  "downto" + " " + "0" + ")" + ";" + "\n")



            
        #print("VHDL Output Signal:", self._vhdlOutputSignal)
    
    """
    # End: __generateVHDLOutputSignal function
    """
    
    """
    # Start: processDriverEquations
    """
    
    def processDriverEquations(self):

        if len(self.driverEquations) > 1:
            driverNode0Equation = self.driverEquations[0]
            #print("DriverNode0Equation", driverNode0Equation)
            driverNode1Equation = self.driverEquations[1]
            #print("DriverNode1Equation", driverNode1Equation)
            self.receiverEquation = "(" + driverNode1Equation + "+" + driverNode0Equation + ")"
        elif len(self.driverEquations) == 1:
            driverNode0Equation = self.driverEquations[0]
            # check which key of the input is present in the drivers dictionary
            if "Input1" in self.drivers:
                # input2 is a port of the sum node
                self.receiverEquation = "(" + self.input2 + "+" + driverNode0Equation + ")"
            else:
                # Input1 is a port of the sum node
                self.receiverEquation = "(" + driverNode0Equation + "+" + self.input1 + ")"
    
    """
    # End: processDriverEquations
    """
    
    """
    # Start: performHWGeneration
    """

    def performHWGeneration(self):
        """
        This function will be called when the input 1 or input 2 of the product node is updated or optmised after perform the PCOperation
        """
        # update the VHDL instance
        self.__generateVHDLInstance()
        # update the weight instance
        #self.__generateVHDLWeightSignal()

    """
    # End: performHWGeneration
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
