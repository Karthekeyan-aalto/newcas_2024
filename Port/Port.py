#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 14:08:43 2021

@author: Karthekeyan Periasamy
"""

class Port():
    
    """
    # Start - Default init Function
    """
    
    def __init__(self):
        # the name of the port
        self._name = None
        self._numberSystem = 0
        self._numberSystemName = None
        self._vhdlPort = None
        self._vhdlPortSignal = None
        self._vhdlOutputPortSignal = None
        self.numberOfBits = 0
        self.exponentBits = 0
        self.esBits = 2
        self.mantissaBits = 0
        self._vhdlOutputPort = None
        self.portLetter = "v"
        self.init()
    
    """
    # End - Default init Function
    """
    
    """
    # Start: name setters and getters
    """
    
    @property
    def name(self):
        if self._name == None:
            # generate name i.e output port name
            self.__generateVHDLOutputPortName()
        return self._name
    
    @name.setter
    def name(self,value):
        # set the _vhdlInstance value
        self._name = value
        # generate the VHDL port
        self.__generateVHDLPort()
        # generate the std_logic_port signal
        self.__generateVHDLPortSignal()
            
    """
    # End: name setters and getters
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
        #print("To be set numberSystemName of the sumNode:",value)
        # set the numberSystemName value
        self._numberSystemName = value
        #print("The numberSystemName of the productNode:", self._numberSystemName)
        # set the tonumberSystemName
        self.tonumberSystemName = "to"+ "_"+ self._numberSystemName
        # print the updated tonumberSystemName
       # print("Updated tonumberSystemName:", self.tonumberSystemName)
            
    """
    # End: numberSystemName setters and getters
    """
 
    
    """
    # Start: vhdlPort setters and getters
    """
    
    @property
    def vhdlPort(self):
        return self._vhdlPort
    
    
    @vhdlPort.setter
    def vhdlPort(self,value):
        # set the vhdlPort value
        self._vhdlPort = value
            
    """
    # End: vhdlPort setters and getters
    """
    
    """
    # Start: vhdlPortSignal setters and getters
    """
    
    @property
    def vhdlPortSignal(self):
        return self._vhdlPortSignal
    
    
    @vhdlPortSignal.setter
    def vhdlPortSignal(self,value):
        # set the vhdlPort value
        self._vhdlPortSignal = value
            
    """
    # End: vhdlPortSignal setters and getters
    """

    
    
    """
    # Start: vhdlOutputPortSignal setters and getters
    """
    
    @property
    def vhdlOutputPortSignal(self):
        if self._vhdlOutputPortSignal == None:
            self.__generateVHDLOutputPortSignal()
            return self._vhdlOutputPortSignal
        else:
            return self._vhdlOutputPortSignal    
    
    
    @vhdlOutputPortSignal.setter
    def vhdlOutputPortSignal(self,value):
        # set the _vhdlOutputPortSignal value
        self._vhdlOutputPortSignal = value
            
    """
    # End: vhdlOutputPortSignal setters and getters
    """
    
    
    """
    # Start: vhdlOutputPort setters and getters
    """
    
    @property
    def vhdlOutputPort(self):
         self._vhdlOutputPort = self.__outputPort()
         return self._vhdlOutputPort
    
    
    @vhdlOutputPort.setter
    def vhdlOutputPort(self,value):
        # set the _vhdlOutputPort value
        self._vhdlOutputPort = value
            
    """
    # End: vhdlOutputPort setters and getters
    """

    
    
    """
    # Start: custom init function
    """
    def init(self):
        #print("ProductNode initialised")
        pass
    
    """
    # End: custom init function
    """
    
    """
    # Start: __generateVHDLPort function
    """
    
    def __generateVHDLPort(self):
        # append the string to form the vhdlInstance
        # check the numberSystem
        if self.numberSystem == 0:
            self._vhdlPort = (self._name + " " + ":" + " " + "in" \
                                                + " " + self.numberSystemName \
                                                + " " + "("+ "0" \
                                                + " " +  "DOWNTO" + " " + str((1-self.numberOfBits)) + ")")
        elif self.numberSystem == 1:
            self._vhdlPort = (self._name + " " + ":" + " " + "in" \
                                                + " " + self.numberSystemName \
                                                + " " + "("+ str(self.exponentBits) \
                                                + " " +  "DOWNTO" + " " + str((1-self.mantissaBits)) + ")")
        elif self.numberSystem == 2:
            self._vhdlPort = (self._name + " " + ":" + " " + "in" \
                                                + " " + self.numberSystemName \
                                                + " " + "("+ str(self.numberOfBits-1) \
                                                + " " +  "DOWNTO" + " " + "0" + ")")


        #print("VHDL Port:", self._vhdlPort)
        
    
        
    """
     # End: __generateVHDLPort function
    """
    
    """
    # Start: __outputPort function
    """
    
    def __outputPort(self):
        # append the string to form the vhdlInstance
        if self.numberSystem == 0:
            # append the string to form the vhdlInstance
            return (self.portLetter + "out" + " " + ":" + " " + "out" \
                                                + " " + self.numberSystemName \
                                                + " " + "("+ "0" \
                                                + " " +  "DOWNTO" + " " + str((1-self.numberOfBits))  + ")")
        elif self.numberSystem == 1:
            # append the string to form the vhdlInstance
            return (self.portLetter + "out" + " " + ":" + " " + "out" \
                                                + " " + self.numberSystemName \
                                                + " " + "("+ str(self.exponentBits) \
                                                + " " +  "DOWNTO" + " " + str((1-self.mantissaBits))  + ")")
        elif self.numberSystem == 2:
            # append the string to form the vhdlInstance
            return (self.portLetter + "out" + " " + ":" + " " + "out" \
                                                + " " + self.numberSystemName \
                                                + " " + "("+ str(self.numberOfBits-1) \
                                                + " " +  "DOWNTO" + " " + "0"  + ")")


        
    
        
    """
    # End: __outputPort function
    """
    
    """
    # Start: __generateVHDLPortSignal function
    """

    def __generateVHDLPortSignal(self):
        if self.numberSystem == 0:
            self._vhdlPortSignal = ("SIGNAL" + " " + self.name + ":" + self.numberSystemName + "(" + "0" \
                                                + " " + "DOWNTO" + " " + str((1-self.numberOfBits)) \
                                                + ")" + ":=" + "(" + "others" + "=>" + '\'0\'' + ")" + ";" + "\n")
        elif self.numberSystem == 1:
            self._vhdlPortSignal = ("SIGNAL" + " " + self.name + ":" + self.numberSystemName + "(" + str(self.exponentBits) \
                                                + " " + "DOWNTO" + " " + str((1-self.mantissaBits)) \
                                                + ")" + ":=" + "(" + "others" + "=>" + '\'0\'' + ")" + ";" + "\n")
        elif self.numberSystem == 2:
            self._vhdlPortSignal = ("SIGNAL" + " " + self.name + ":" + self.numberSystemName + "(" + str(self.numberOfBits-1) \
                                                + " " + "DOWNTO" + " " + "0" \
                                                + ")" + ":=" + "(" + "others" + "=>" + '\'0\'' + ")" + ";" + "\n")


                                                
    """
    # End: __generateVHDLPortSignal function
    """
    
    """
    # Start: __generateVHDLPortSignal function
    """
    
    def __generateVHDLOutputPortSignal(self): 
        if self.numberSystem == 0:
            # append the string to form the vhdlInstance
            self._vhdlOutputPortSignal = ("SIGNAL" + " " + self.portLetter + "out" + ":" \
            + self.numberSystemName + "(" + "0" + " " \
            + "DOWNTO" + " " + str((1-self.numberOfBits))+ ")" + ":=" + "(" + "others" + "=>" + "\'0\'" + ")" + ";" + "\n")
        elif self.numberSystem == 1:
            # append the string to form the vhdlInstance
            self._vhdlOutputPortSignal = ("SIGNAL" + " " + self.portLetter + "out" + ":" \
            + self.numberSystemName + "(" + str(self.exponentBits) + " " \
            + "DOWNTO" + " " + str((1-self.mantissaBits))+ ")" + ":=" + "(" + "others" + "=>" + "\'0\'" + ")" + ";" + "\n")
        elif self.numberSystem == 2:
            # append the string to form the vhdlInstance
            self._vhdlOutputPortSignal = ("SIGNAL" + " " + self.portLetter + "out" + ":" \
            + self.numberSystemName + "(" + str(self.numberOfBits-1) + " " \
            + "DOWNTO" + " " + "0" + ")" + ":=" + "(" + "others" + "=>" + "\'0\'" + ")" + ";" + "\n")


                                                
    """
    # End: __generateVHDLOutputPortSignal function
    """
    
    """
    # Start: __generateVHDLOutputPortName function
    """
    
    def __generateVHDLOutputPortName(self): 
        # append the string to form the vhdlInstance
         self._name = self.portLetter + "out"                                                
    """
    # End: __generateVHDLOutputPortName function
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
    
