"""
Created by Karthekeyan Periasamy
Edited on July 24 13:01
"""

from SWOperators.Driver.Driver import Driver
from SWOperators.Receiver.Receiver import Receiver
from Operators.Port.Port import Port

class SWOperator ():
    """
    This class is the base class for any type of Operator that will be constructed
    The purpose of this class is to hold the basic properties of any Operator but not including the HWDescription and HW Simulation object
    
    As Operator is part of AutoPC, it will follow the connect, configure, perform or process, reset process
    The idea of the four step process may not be intiutive, but it allows any package and its associated modules to be configured
    separately and tested accordingly.

    **However many other packages and modules in AutoPC are not made based on the four step process. Its lack of thought process which
    led that disaster happen while desgning those modules. So, it will be changed in the future and is recommended to follow the four step process
    """

    def __init__(self):
        self.connect()
    
    @property
    def input1(self):
        return self._input1

    @input1.setter
    def input1(self,value):
        self._input1 = value
        
    @property
    def input1Driver(self):
        return self._input1Driver

    @input1Driver.setter
    def input1Driver(self,value):
        self._input1Driver = value
        
    @property
    def input2(self):
        return self._input2

    @input2.setter
    def input2(self,value):
        self._input2 = value
    
    @property
    def input2Driver(self):
        return self._input2Driver

    @input2Driver.setter
    def input2Driver(self,value):
        self._input2Driver = value

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self,value):
        self._output = value

    @property
    def drivers(self):
        if self._drivers == None:
            self._drivers = list()
        return self._drivers

    @drivers.setter
    def drivers(self,value):
        self._drivers = value
    

    @property
    def receivers(self):
        if self._receivers == None:
            self._receivers = list()
        return self._receivers

    @receivers.setter
    def receivers(self,value):
        self._receivers = value
    
    @property
    def isInputDataModified(self):
        return self._isInputDataModified
    
    @isInputDataModified.setter
    def isInputDataModified(self,value):
        self._isInputDataModified = value

        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
    
    
    @property
    def isOutputModified(self):
        return self._isOutputModified
    
    @isOutputModified.setter
    def isOutputModified(self,value):
        self._isOutputModified = value

        # update the hwDescription of the operator
        # before that access the information of the updated ports
        # use the updated ports information to configure, process and perform the operations of the operator
    
    
    @property
    def numberSystemName(self):
        return self._numberSystemName

    @numberSystemName.setter
    def numberSystemName(self,value):
        self._numberSystemName = value
        # check the name and set the number system number accordingly
        # 0 is the integer for Fixed system
        # 1 is the integer for Float System
        # 2 is the integer for Posit System
        if self._numberSystemName == "Fixed":
            self.numberSystem = 0
        elif self._numberSystemName == "Float":
            self.numberSystem = 1
        elif self._numberSystemName == "Posit":
            self.numberSystem = 2
        elif self._numberSystemName == None:
            # when the numberSystemName is none, it means the numberSystem cannot be set
            # and is invalid.
            self.numberSystem = -1
    
    
    def configure(self):
        """
        This function will be called from outside of the class itself.
        The main purpose of this funciton to receive information via the configuraiton dictionary
        Use the information from the configurartion dictionary to set the properties of the object or configuring itself.
        """
        if self.configurationDetailsOfOperator == None:
            #print("The object is not configured and the behaviour of the object cannot be guaranteed")
            return

        configurationDetails = self.configurationDetailsOfOperator
        #print("Operator configurationDetails", configurationDetails)


        # check the configuration details has number system key or not
        if "NumberSystem" in configurationDetails:
            # access the number system information
            # set it to the number system variable
            self.numberSystemName = configurationDetails["NumberSystem"]
            
        # check the configuration details of the number of bits
        if "NumberOfBits" in configurationDetails:
            self.numberOfBits = configurationDetails["NumberOfBits"]

        if "MantissaBits" in configurationDetails:
            self.mantissaBits = configurationDetails["MantissaBits"]

        if "ExponentBits" in configurationDetails:
            self.exponentBits = configurationDetails["ExponentBits"]

        if "EsBits" in configurationDetails:
            self.esBits = configurationDetails["EsBits"]

        # check the configuration details of the name
        if "Name" in configurationDetails:
            self.name = configurationDetails["Name"]
    
    @property
    def shouldInput1BeBalanced(self):
        return self._shouldInput1BeBalanced
    
    @shouldInput1BeBalanced.setter
    def shouldInput1BeBalanced(self,value):
        self._shouldInput1BeBalanced = value
    
    @property
    def shouldInput2BeBalanced(self): 
        return self._shouldInput2BeBalanced
    
    @shouldInput2BeBalanced.setter
    def shouldInput2BeBalanced(self,value):
        self._shouldInput2BeBalanced = value    
    
    @property
    def shouldInput1AndInput2BeBalanced(self):
        return self._shouldInput1AndInput2BeBalanced
    
    
    @shouldInput1AndInput2BeBalanced.setter
    def shouldInput1AndInput2BeBalanced(self,value):
        self._shouldInput1AndInput2BeBalanced = value

    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        # dictionary to store the configuration details, which then will be used by the configure function to set the
        # properties of the Logic
        self.configurationDetailsOfOperator = dict()

        # property to store the number system
        # the number system property will be used the HW Description objects to generate appropriate VHDL syntax
        self.numberSytem = None

        # property to store the name of the LUT
        self.name = None

        # property to store the number system name
        # the name of the number system will be retreived from the configuration details
        # the custom getter and setters are used to use the number system name and set the corresponding number system
        self._numberSystemName = None

        # operational frequency of the LUT
        # for now, the LUT is not clock synchornised
        # its just a combinational block.
        self.frequency = None

        # property to store the numberOfBits
        # the number of bits will be used to configure the LUT numberOfBits
        # for an LUT the number of bits would be appropriate based on the input and output ports
        # the input port and output port number of bits will be configured using the configuration details
        self.numberOfBits = None

        # proeprty to store the required mantissaBits if the numberSystem is of Float
        self.mantissaBits = None

        # property to store the required exponent Bits if the number system is of Float
        self.exponentBits = None
        

        #property to store the required es bits if the number system is posit
        self.esBits = None

        # port information from the hardware are used to find the drivers         
        self._drivers = None
        
        # port information from the hardware are used to extract the information that will be used by receiver
        self._receivers = None

        # property to know whether the swoperator is enabled or not
        self.isOperatorEnabled = True

        #property to store the left child of the SWOperator (assuming the operators are all two port netwwork for now)
        self.leftChild = None

        #property to store the right child of the SWOperator
        self.rightChild = None
        
        # property to be used by optimisers, where input1 represents the operator property
        self._input1 = None

        #property to be used by optimisers, where input2 represents the port 2 
        self._input2 = None

        #property to mask the product
        self._output = None
        
        # property to mask the multiplier driver
        self._input1Driver = None

        # property to maske the multiplicand driver
        self._input2Driver = None
        
        # property to know that input data ports are updated or not
        # this property can be used to achieve the event driven architectures
        # however, for now, as the inputDataPorts property is not observable, we use this set and update mechanisms to update the inputdataports of an operator is updated
        # the vhdl description of the operator should be updated
        self._isInputDataModified = False


        # like the input data ports, output port when set to that it is modified.
        # Should be used to updated the VHDL Description of the operator itself
        # the outputPorts property is not observable for now, and it will updated by the object whoever modifies the output ports information
        self._isOutputModified = False

        # this property may be not appropriate for an operator
        # we will think about it soon how to achieve the same
        # property to store the level of the operator in a PCTree
        self.operatorLevelInAPCTree = None
        
        # property to know whether to attach a shiftRegister is needed to input1 or not
        self._shouldInput1BeBalanced = False
        
        # property to know whether to attach a shiftRegister is needed to input2 or not
        self._shouldInput2BeBalanced = False
        
        # property to know whether to attach a shiftRegister to both input1 and input2
        self._shouldInput1AndInput2BeBalanced = False
        
        #property to store the delay on the longestPathFromOperator
        self.delayOnTheLongestPathOfPCTreeFromOperator = None
        
        #initialise the input ports info dict
        self.inputDataPortsInfo = dict()





    def resetProperties(self):
        # dictionary to store the configuration details, which then will be used by the configure function to set the
        # properties of the Logic
        self.configurationDetailsOfOperator = dict()

        # property to store the number system
        # the number system property will be used the HW Description objects to generate appropriate VHDL syntax
        self.numberSytem = None

        # property to store the name of the LUT
        self.name = None

        # property to store the number system name
        # the name of the number system will be retreived from the configuration details
        # the custom getter and setters are used to use the number system name and set the corresponding number system
        self._numberSystemName = None


        # property to know that input data ports are updated or not
        # this property can be used to achieve the event driven architectures
        # however, for now, as the inputDataPorts property is not observable, we use this set and update mechanisms to update the inputdataports of an operator is updated
        # the vhdl description of the operator should be updated
        self._isInputDataModified = False


        # like the input data ports, output port when set to that it is modified.
        # Should be used to updated the VHDL Description of the operator itself
        # the outputPorts property is not observable for now, and it will updated by the object whoever modifies the output ports information
        self._isOutputModified = False


        # operational frequency of the LUT
        # for now, the LUT is not clock synchornised
        # its just a combinational block.
        self.frequency = None

        # property to store the numberOfBits
        # the number of bits will be used to configure the LUT numberOfBits
        # for an LUT the number of bits would be appropriate based on the input and output ports
        # the input port and output port number of bits will be configured using the configuration details
        self.numberOfBits = None

        # proeprty to store the required mantissaBits if the numberSystem is of Float
        self.mantissaBits = None

        # property to store the required exponent Bits if the number system is of Float
        self.exponentBits = None
        
        #property to store the required es bits if the number system is posit
        self.esBits = None
        
        # port information from the hardware are used to find the drivers
        self._drivers = None
        
        # port information from the hardware are used to extract the information that will be used by receiver
        self._receivers = None
        
        # property to know whether the swoperator is enabled or not
        self.isOperatorEnabled = True
        
        #property to store the left child of the SWOperator (assuming the operators are all two port netwwork for now)
        self.leftChild = None

        #property to store the right child of the SWOperator
        self.rightChild = None
        
        # property to be used by optimisers, where input1 represents the operator property
        self._input1 = None

        #property to be used by optimisers, where input2 represents the port 2 
        self._input2 = None

        #property to mask the product
        self._output = None
        
        # property to mask the multiplier driver
        self._input1Driver = None

        # property to maske the multiplicand driver
        self._input2Driver = None
        
        # property to know that input data ports are updated or not
        # this property can be used to achieve the event driven architectures
        # however, for now, as the inputDataPorts property is not observable, we use this set and update mechanisms to update the inputdataports of an operator is updated
        # the vhdl description of the operator should be updated
        self._isInputDataModified = False


        # like the input data ports, output port when set to that it is modified.
        # Should be used to updated the VHDL Description of the operator itself
        # the outputPorts property is not observable for now, and it will updated by the object whoever modifies the output ports information
        self._isOutputModified = False

        
        # this property may be not appropriate for an operator
        # we will think about it soon how to achieve the same
        # property to store the level of the operator in a PCTree
        self.operatorLevelInAPCTree = None
        
        # property to know whether to attach a shiftRegister is needed to input1 or not
        self._shouldInput1BeBalanced = False
        
        # property to know whether to attach a shiftRegister is needed to input2 or not
        self._shouldInput2BeBalanced = False
        
        # property to know whether to attach a shiftRegister to both input1 and input2
        self._shouldInput1AndInput2BeBalanced = False

        #property to store the delay on the longestPathFromOperator
        self.delayOnTheLongestPathOfPCTreeFromOperator = None
        
        #initialise the input ports info dict
        self.inputDataPortsInfo = dict()






    def process(self):
        pass
    
    def reset(self):
        self.resetProperties()        

    def main(self):
        # process the operator
        self.process()


    def run(self):
        self.main()

