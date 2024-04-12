#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:40:28 2021

@author: Karthekeyan Periasamy
"""
from Port import Port
from NumberSystemPackages.POSITConverter.posit_converter import PositConverter


class ProductNode():
    
    """
    # Start - Default init Function
    """
    
    def __init__(self):
        
        """
        ============================================================
        Basic system properties 
        
        number: to represent the macAddress (number: member variable)
        input1: the input str  float to the productNode
        input2: second input str to the float of the productNode
        =============================================================
        
        """
        # the number is set in the equation parser when we peform an operation in the equation parser
        self.number = 0
        self._customName = None
        self._name = None
        self._input1 = None
        self._input2 = None
        self._output = None
        self.numberOfBits = 8
        self.exponentBits = 8
        self.mantissaBits = 8
        self.esBits = 8
        self.ports = list()
        self.portsInfo = dict()
        self._numberSystem = 0
        self._numberSystemName = None
        self.binaryStringConverter = None
        # property to know the index where the current product node is present in the arithmetic node category
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
        analysisMode = 0 PCMinOperation
        analysisMode = 1 PCOperation
        analysisMode = 2 PCMaxOperation
        
        """
        self.analysisMode = 0
        
        """
        ==========================================================================
        The below input1Value and input2Value are used to compute the real output
        when port values are set to a predefined values
        ===========================================================================
        """

        self._input1Value = None
        self._input2Value = None
        self._outputValue = None
        
        """
        ===========================================================
        Input port and weight related properties of the productNode
        ===========================================================
        """
        self._weight = None
        self._weightName = None
        
        self._vhdlWeightSignal = None
        self._vhdlInstance = None
       
   
        self.numberZero = 0
        
        self._numberSystem = 0
        self._numberSystemName = None
        self._binaryStringConverter = None
        self._tonumberSystemName = None
        # new property to store the port variable of the SPN
        self.portLetter = "v"

        # arithemtic node optimisation properties
        
        # equations of the product node
        self.equation = None
        # the drivers of the current productNode
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
    # Start: numberSystem setters and getters
    """
    
    @property
    def numberSystem(self):
        if self._numberSystem == None:
             self._numberSystem = 0
             return self._numberSystem
        return self._numberSystem
    
    
    @numberSystem.setter  
    def numberSystem(self,value):
        # set the numberSystem value
        self._numberSystem = value
        # set the converter object
        self.binaryStringConverter = PositConverter(self.numberOfBits,self.esBits,self.mantissaBits)
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
    # Start: customName getters and setters
    """

    @property
    def customName(self):
        if self._customName == None:
            if self.numberSystem == 0:
                self._customName = type(self).__name__ + "_" + "Fixed"
                return self._customName
            elif self.numberSystem == 1:
                self._customName = type(self).__name__ + "_" + "Float"
                return self._customName
            elif self.numberSystem == 2:
                if self.esBits > 3:
                    # set another POSIT custom name
                    self._customName = ("PositMult" + "_" + str(self.numberOfBits) + "_" + str(self.esBits) + "_" + "comb" + "_" + "uid" + "2")
                else:
                    # set another POSIT custom name
                    self._customName = ("PositMult" + "_" + str(self.numberOfBits) + "_" + str(self.esBits) + "_" + "F0" + "_" + "uid" + "2")           
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
    # Start: numberSystemName setters and getters
    """
    
    @property
    def numberSystemName(self):
        if self._numberSystemName == None:
            self._numberSystemName = "sfixed"
            return self._numberSystemName
        return self._numberSystemName
    
    
    @numberSystemName.setter  
    def numberSystemName(self,value):
        #print("To be set numberSystemName of the sumNode:",value)
        # set the numberSystemName value
        self._numberSystemName = value
        #print("The numberSystemName of the productNode:", self._numberSystemName)
        # set the tonumberSystemName
        # check the numberSystem, if its 2 the numberSystemTwoName is different than others
        if self.numberSystem == 2:
            self.tonumberSystemName = "to" + "_" + "stdlogicvector"
            return

        self.tonumberSystemName = "to"+ "_"+ self._numberSystemName
        # print the updated tonumberSystemName
       # print("Updated tonumberSystemName:", self.tonumberSystemName)
            
    """
    # End: numberSystemName setters and getters
    """
    
    """
    # Start: tonumberSystemName setters and getters
    """
    
    @property
    def tonumberSystemName(self):
        if self._tonumberSystemName == None:
            self._tonumberSystemName = "to"+ "_"+ "sfixed"
        return self._tonumberSystemName
    
    
    @tonumberSystemName.setter  
    def tonumberSystemName(self,value):
        # set the _tonumberSystemName value
        self._tonumberSystemName = value
            
    """
    # End: tonumberSystemName setters and getters
    """
    
    
    """
    # Start: input1 setters and getters
    """
    
    @property
    def input1(self):
        return self._input1
    
    
    @input1.setter  
    def input1(self,value):
        # set the input1 value
        self._input1 = value
        # set the input1Value member variable
        self.input1Value = value
            
            
    """
    # End: inpput1 setters and getters
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
            #print("The port letter of the productNode:", portLetter)
            # check the first portLetter is actually a porLetter or not
            if (portLetter == self.portLetter):
                print("Forming port at input 1 of the productNode")
                # then its a port
                # generate a port object and set its name
                port  = Port.Port()
                port.numberOfBits = self.numberOfBits
                port.numberSystem = self.numberSystem
                port.mantissaBits = self.mantissaBits
                port.exponentBits = self.exponentBits
                port.esBits = self.esBits
                port.name = self.input1
                self.ports.append(port)
                # add portname and the port number to portInfo dictionary
                self.portsInfo[port.name] = '1'
        else:
            # then the input1Float could be a weight signal
            # set the weightSignal
            self.weight = self.input1
            if self.analysisMode != 0:
                self._input1 = self.weightName
            
    """
    # End: _input1Value setters and getters
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
            self.output = self.name + str(self.number)\
                          + "Output" + "_" + str(self.arithmeticNodeNumber)
                                                
            
    
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
                print("Forming port at input 2 of the productNode")
                # then its a port
                # generate a port object and set its name
                port  = Port.Port()
                port.numberOfBits = self.numberOfBits
                port.numberSystem = self.numberSystem
                port.mantissaBits = self.mantissaBits
                port.exponentBits = self.exponentBits
                port.esBits = self.esBits
                port.name = self.input2
                self.ports.append(port)
                # add portname and the port number to portInfo dictionary
                self.portsInfo[port.name] = '2'
                
        else:
            # then the input2 could be a weight signal
            # set the weightSignal
            self.weight = self.input2
            if self.analysisMode != 0:
                self._input2 = self.weightName
            
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
        # print the input1Float answer
        #print("The input1 of the productNode is float or not, True or False:", input1Float)
        # print the input1Value
        #print("The input1Value of the productNode:", self.input1Value)
        input2Float = self.__isInput2Float()
        # print the input2Value
        #print("The input2Value of the productNode:", self.input2Value)
        # print the input2Float answer
        #print("The input2 of the productNode is float or not, True or False:", input2Float)
        if ((input1Float == True) and (input2Float == True)):
            # set the outputValue member variable by multiplying the two inputs
            self.outputValue = float(float(self.input1Value) * float(self.input2Value))
            return
        
        elif ((input1Float == False) and (self.input2 == self.weightName)):
            # check if there are ports or not
            if len(self.ports) > 0:
                # we can form the equation
                self.equation = "(" + str(self.weight) + "*" + str(self.input1) + ")"
                # set the equation to the receiver equation
                self.receiverEquation = self.equation
                #print("PN Type with Input1: A port and Input2: Weight"+"(" + str(self.weight) + "*" + str(self.input1) + ")")
            else:
                self.equation = "(" + str(self.weight) + "*" + str(self.input1) + ")"
                # check the length of input1 when split with underscore be 3
                if (len(self.input1.split("_")) == 3):
                    #then access the last part of the split array to access the driver details
                    driverNodeIndex = self.input1.split("_")[(len(self.input1.split("_"))-1)]
                    # add the driver node index to the drivers array
                    self.drivers["Input1"] = driverNodeIndex

                #print("PN Type with Input1:  Driven by another node and Input2: Weight"+"(" + str(self.weight) + "*" + str(self.input1) + ")")
        elif ((self.input1 == self.weightName) and (input2Float == False)):
            # check if there are ports or not
            if len(self.ports) > 0:
                # we can form the equation
                self.equation = "(" + str(self.weight) + "*" + str(self.input2) + ")"
                # set the equation to the receiver equation
                self.receiverEquation = self.equation
                #print("PN Type with Input1: Weight and Input2: A Port"+"(" + str(self.weight) + "*" + str(self.input2) + ")")
            else:
                # we can form the equation
                self.equation = "(" + str(self.input2) + "*" + str(self.weight) + ")"
                # check the length of input1 when split with underscore be 3
                if (len(self.input2.split("_")) == 3):
                    #then access the last part of the split array to access the driver details
                    driverNodeIndex = self.input2.split("_")[(len(self.input2.split("_"))-1)]
                    # add the driver node index to the drivers array
                    self.drivers["Input2"] = driverNodeIndex
                    #print("PN Type with Input1: Weight and Input2: Driven by another node"+"(" + str(self.input2) + "*" + str(self.weight) + ")")
            
        elif ((input1Float == False) and (self.input2 != self.weightName)):
            # check if there are ports or not
            if len(self.ports) > 0:
                # we can form the equation
                self.equation = "(" + str(self.input2) + "*" + str(self.input1) + ")"
                #print("PN Type with Input1 and Input2 is "+"(" + str(self.input2) + "*" + str(self.input1) + ")")
                
                if input2Float == False:
                    # check the length of input1 when split with underscore be 3
                    if (len(self.input2.split("_")) == 3):
                        #then access the last part of the split array to access the driver details
                        driverNodeIndex = self.input2.split("_")[(len(self.input2.split("_"))-1)]
                        # add the driver node index to the drivers array
                        self.drivers["Input2"] = driverNodeIndex

            else:
                # we can form the equation
                self.equation = "(" + str(self.input2) + "*" + str(self.input1) + ")"
                #print("PN Type with Input1 and Input2 is "+"(" + str(self.input2) + "*" + str(self.input1) + ")")
                
                
                # check the length of input1 when split with underscore be 3
                if (len(self.input1.split("_")) == 3):
                    #then access the last part of the split array to access the driver details
                    driverNodeIndex = self.input1.split("_")[(len(self.input1.split("_"))-1)]
                    # add the driver node index to the drivers array
                    self.drivers["Input1"] = driverNodeIndex

                
                # check the length of input1 when split with underscore be 3
                if (len(self.input2.split("_")) == 3):
                    #then access the last part of the split array to access the driver details
                    driverNodeIndex = self.input2.split("_")[(len(self.input2.split("_"))-1)]
                    # add the driver node index to the drivers array
                    self.drivers["Input2"] = driverNodeIndex

        elif  ((input2Float == False) and (self.input1 != self.weightName)):
            # check if there are ports or not
            if len(self.ports) > 0:
                # we can form the equation
                self.equation = "(" + str(self.input2) + "*" + str(self.input1) + ")"
                #print("PN Type with Input1 and Input2 is "+"(" + str(self.input2) + "*" + str(self.input1) + ")")
                
                
                if input1Float == False:
                    # check the length of input1 when split with underscore be 3
                    if (len(self.input1.split("_")) == 3):
                        #then access the last part of the split array to access the driver details
                        driverNodeIndex = self.input1.split("_")[(len(self.input1.split("_"))-1)]
                        # add the driver node index to the drivers array
                        self.drivers["Input1"] = driverNodeIndex

            else:
                # we can form the equation
                self.equation = "(" + str(self.input2) + "*" + str(self.input1) + ")"
                #print("PN Type with Input1 and Input2 is "+"(" + str(self.input2) + "*" + str(self.input1) + ")")
                
                # check the length of input1 when split with underscore be 3
                if (len(self.input1.split("_")) == 3):
                    #then access the last part of the split array to access the driver details
                    driverNodeIndex = self.input1.split("_")[(len(self.input1.split("_"))-1)]
                    # add the driver node index to the drivers array
                    self.drivers["Input1"] = driverNodeIndex

                
                # check the length of input1 when split with underscore be 3
                if (len(self.input2.split("_")) == 3):
                    #then access the last part of the split array to access the driver details
                    driverNodeIndex = self.input2.split("_")[(len(self.input2.split("_"))-1)]
                    # add the driver node index to the drivers array
                    self.drivers["Input2"] = driverNodeIndex

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
    # Start: weight setters and getters
    """
    
    @property
    def weight(self):
        return self._weight
    
    
    @weight.setter  
    def weight(self,value):
        # set the weight value
        self._weight = value
        # set the weightValue
        self.weightName = self._weight
            
    """
    # End: weight setters and getters
    """
    
    """
    # Start: weightName setters and getters
    """
    
    @property
    def weightName(self):
        if self._weightName == None:
            self._weightName = self.name + "weight"
        return self._weightName
    
    
    @weightName.setter  
    def weightName(self,value):
        # initially set the  _weightName
        self._weightName = value
        # modify the weightName
        # concatenate the string weight and number of the node to form the weightValue
        self._weightName = self.name + str(self.number) + "weight"
        #print the weightName
        #print("WeightName:", self._weightName)
        # generate a weightVHDL signal
        self.__generateVHDLWeightSignal()
            
    """
    # End: weightName setters and getters
    """
    
    """
    # Start: drivers
    """

    @property
    def drivers(self):
        if self._drivers == None:
            self._drivers = dict()
        return self._drivers
        
    @drivers.setter
    def drivers(self, value):
        self._drivers = value

    """
    # End: drivers 
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
        #print("DriverEquations of ProductNode",self._driverEquations)
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
    # Start: vhdlweightSignal setters and getters
    """
    
    @property
    def vhdlWeightSignal(self):
        return self._vhdlWeightSignal
    
    
    @vhdlWeightSignal.setter
    def vhdlWeightSignal(self,value):
        # set the vhdlPort value
        self._vhdlWeightSignal = value
            
    """
    # End: vhdlweightSignal setters and getters
    """
    
    
    """
    # End: End of custom getters and setters
    """
    
    
    """
    # Start: __generateVHDLInstance function
    """
    
    def __generateVHDLInstance(self):
        # append the string to form the vhdlInstance
        if self.numberSystem == 0:
            self.vhdlInstance = (self.name + str(self.number) + ":" + " " +"entity work"+"." \
                + self.name +"("+"rtl"+")" "\n" + "generic map" + "(" + "numberOfBits" + ")" + "\n" 
                + "port map" + "(" + str(self.input1) + "," \
                + str(self.input2) + ","+ self.output +")" + ";" + "\n" + "\n")
        elif self.numberSystem == 1:
            self.vhdlInstance = (self.name + str(self.number) + ":" + " " +"entity work"+"." \
                + self.name +"("+"rtl"+")" "\n" + "generic map" + "(" + "mantissaBits" + "," + "exponentBits" + ")" 
                + "\n" + "port map" + "(" + str(self.input1) + "," \
                + str(self.input2) + ","+ self.output +")" + ";" + "\n" + "\n")
        elif self.numberSystem == 2:
            self.vhdlInstance = (self.name + str(self.number) + ":" + " " +"entity work"+"." \
                + self.customName +"("+"arch"+")" "\n" 
                + "port map" + "(" + str(self.input1) + "," \
                + str(self.input2) + ","+ self.output +")" + ";" + "\n" + "\n")
    
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
        # append the string to form the vhdlInstance
        # check the numberSystem 
        if self.numberSystem == 0:
            self.vhdlOutputSignal = ("Signal" + " "
                                               + self.output \
                                               + ":" + " " + self.numberSystemName + " " + "("+ "0" \
                                               + " " +  "downto" + " " + str((1 - self.numberOfBits)) + ")" + ";" + "\n")
        elif self.numberSystem == 1:
            self.vhdlOutputSignal = ("Signal" + " "
                                               + self.output \
                                               + ":" + " " + self.numberSystemName + " " + "("+ str(self.exponentBits) \
                                               + " " +  "downto" + " " + str((1 - self.mantissaBits)) + ")" + ";" + "\n")
        elif self.numberSystem == 2:
            self.vhdlOutputSignal = ("Signal" + " "
                                               + self.output \
                                               + ":" + " " + self.numberSystemName + " " + "("+ str(self.numberOfBits-1) \
                                               + " " +  "downto" + " " + "0" + ")" + ";" + "\n")
            
        #print("VHDL Output Signal:", self._vhdlOutputSignal)
    
    """
    # End: __generateVHDLOutputSignal function
    """
    
    """
    # Start:  __generateVHDLWeightSignal function
    """
    def __generateVHDLWeightSignal(self):
        if self.numberSystem == 0:
            self.vhdlWeightSignal = ("Signal" + " "+ self.weightName \
                                               + " " + ":" + " " + self.numberSystemName \
                                               + " " + "(" + " " + "0" \
                                               + " " + "downto" \
                                               + " " + str((1-self.numberOfBits)) \
                                               + " " + ")" \
                                               + " " + ":=" \
                                               + " " + self.tonumberSystemName \
                                               + " " + "(" \
                                               + str(self.weight) \
                                               + "," + "0" + "," + str((1-self.numberOfBits)) + ")" + ";" + "\n")
        elif self.numberSystem == 1:
            self.vhdlWeightSignal = ("Signal" + " "+ self.weightName \
                                               + " " + ":" + " " + self.numberSystemName \
                                               + " " + "(" + " " + str(self.exponentBits) \
                                               + " " + "downto" \
                                               + " " + str((1-self.mantissaBits)) \
                                               + " " + ")" \
                                               + " " + ":=" \
                                               + " " + self.tonumberSystemName \
                                               + " " + "(" \
                                               + str(self.weight) \
                                               + "," + str(self.exponentBits) + "," + str((self.mantissaBits-1)) + ")" + ";" + "\n")
        elif self.numberSystem == 2:
            # convert the float weight to binary string using the binary converter
            binaryWeight = self.binaryStringConverter.convert_float_to_posit(float(self.weight))
            #if float(self.weight) != float(1.0):
                #binaryWeight = self.binaryStringConverter.convert_float_to_posit(float(self.weight))
            #else:
                # as per the numberOfbits update the ioPattern for ones
                #positOneWeightPartial = "01"
                #positZeroWeightPartial = "0"
                #positZeroWeight = "".join([positZeroWeightPartial]*(self.numberOfBits-2))
                #binaryWeight = positOneWeightPartial + positZeroWeight
                #print("POSIT One Weight:", binaryWeight)

            self.vhdlWeightSignal = ("Signal" + " "+ self.weightName \
                                               + " " + ":" + " " + self.numberSystemName \
                                               + " " + "(" + " " +  str((self.numberOfBits-1)) \
                                               + " " + "downto" \
                                               + " " + "0"\
                                               + " " + ")" \
                                               + " " + ":=" \
                                               + " " + "\"" + str(binaryWeight) + "\"" \
                                               + ";" + "\n")
                                               
            
        #print("VHDL Weight Signal:", self._vhdlWeightSignal)
    
    """
    # End: __generateVHDLWeightSignal function
    """
    
    """
    # Start: processDriverEquations
    """
    
    def processDriverEquations(self):

        if len(self.driverEquations) > 1:
            driverNode0Equation = self.driverEquations[0]
            driverNode1Equation = self.driverEquations[1]
            self.receiverEquation = "(" + driverNode1Equation + "*" + driverNode0Equation + ")"
        elif len(self.driverEquations) == 1:
            driverNode0Equation = self.driverEquations[0]
            #print("DriverNode Equation", driverNode0Equation)
            # check which key of the input is present in the drivers dictionary
            if "Input1" in self.drivers:
                # check whether the input2 is a float or not
                isInput2Float = self.__isInput2Float()
                if isInput2Float == True:
                    # input2 is a weight of the product node
                    self.receiverEquation = "(" + self.weight + "*" + driverNode0Equation + ")"
                else:
                    if len(self.ports) > 0:
                        # input2 is a port of the product node
                        self.receiverEquation = "(" + self.input2 + "*" + driverNode0Equation + ")"
                    else:
                        # input2 is a weight of the product node
                        self.receiverEquation = "(" + self.input2 + "*" + driverNode0Equation + ")"
            else:
                # check whether the input1 is a float or not
                isInput1Float = self.__isInput1Float()
                if isInput1Float == True:
                    # Input1 is a weight of the sum node
                    self.receiverEquation = "(" + driverNode0Equation + "*" + self.weight + ")"
                else:
                    if len(self.ports) > 0:
                        # input1 is a port of the product node
                        self.receiverEquation = "(" + driverNode0Equation + "*" + self.input1 + ")"
                    else:
                        # input1 is a weight of the product node
                        self.receiverEquation = "(" + driverNode0Equation + "*" + self.weight + ")"
    
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
