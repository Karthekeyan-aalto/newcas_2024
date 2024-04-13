"""
Created by Karthekeyan Periasamy
Edited on November 26 11:59:49
"""

from SWOperators.SWOperator import SWOperator
from SWOperators.Adders.Driver.Driver import Driver

class SWAdder(SWOperator):

    """
    Class to have blueprint of the different types of multipliers
    Based on the number systems, we may or may not have the converters.
    """

    def __init__(self):
        self.connect()    
    

    @property
    def drivers(self):
        if self._drivers == None:
            self._drivers = list()

        return self._drivers


    @drivers.setter
    def drivers(self,value):
        self._drivers = value
    
    
    
    @property
    def driversInfo(self):
        if self._driversInfo == None:
            self._driversInfo = dict()

        return self._driversInfo


    @driversInfo.setter
    def driversInfo(self,value):
        self._driversInfo = value
    
    @property
    def augend(self):
        return self._augend

    @augend.setter
    def augend(self,value):
        self._augend = value
        # build a driver object of the multiplicand if the multiplicand is not a port
        self.augendDriver = Driver()
        self.augendDriver.configurationDetailsOfDriver = {"Name":self._augend}
        self.augendDriver.configure()
        if self.augendDriver.isDriverAnArithmeticNode == True:
            # update the drivers
            self.drivers.append(self.augendDriver)
            # update the driversInfo
            self.driversInfo[self._augend] = self.augendDriver
        #print("SWAdder Augend", self._augend)
    
    @property
    def addend(self):
        return self._addend

    @addend.setter
    def addend(self,value):
        self._addend = value
        # build a driver object of the multiplicand if the multiplicand is not a port
        self.addendDriver = Driver()
        self.addendDriver.configurationDetailsOfDriver = {"Name":self._addend}
        self.addendDriver.configure()
        if self.addendDriver.isDriverAnArithmeticNode == True:
            # update the drivers
            self.drivers.append(self.addendDriver)
            # update the driversInfo
            self.driversInfo[self._addend] = self.addendDriver
        #print("SWAdder Addend", self._addend)
    
    @property
    def summation(self):
        if self._summation == None:
            if (self.augendDriver and self.addendDriver) != None:
                # build the computed equation
                if ((self.augendDriver.isDriverAPort == True) and (self.addendDriver.isDriverAPort == True)):
                    self.equation = "(" + self.augend + "+" + self.addend + ")"
                    # set the product expression with the equation
                    # set the summation expression with the equation
                    #print("SWAdder Equation", self.equation)
                    self._summation = self.equation
                
                elif ((self.augendDriver.isDriverAPort == True) and (self.addendDriver.isDriverAPort == True)):
                    self.equation = "(" + self.addend + "+" + self.augend + ")"
                    # set the summation expression with the equation
                    #print("SWAdder Equation", self.equation)
                    self._summation = self.equation
                else:
                    self._summation = None
        
        return self._summation

    @summation.setter
    def summation(self,value):
        self._summation = value
     
    @property
    def input1(self):
        self._input1 = self.augend
        return self._input1

    @input1.setter
    def input1(self,value):
        if self._input1 != None:
            if self.isInputDataModified == False:
                # remove the augend driver from the drivers
                augendDriver = self.driversInfo[self.augend]
                # remove the augend driver from the drivers
                self.drivers.remove(augendDriver)

        self._input1 = value
        
        
    @property
    def input2(self):
        self._input2 = self.addend
        return self._input2

    @input2.setter
    def input2(self,value):
        if self._input2 != None:
            if self.isInputDataModified == False:
                # remove the addend driver from the drivers
                addendDriver = self.driversInfo[self.addend]
                # remove the addend driver from the drivers
                self.drivers.remove(addendDriver)
        
        self._input2 = value
    
    @property
    def output(self):
        self._output = self.summation
        return self._output

    @output.setter
    def output(self,value):
        self._output = value
    
    
    @property
    def input1Driver(self):
        self._input1Driver = self.augendDriver
        return self._input1Driver

    @input1Driver.setter
    def input1Driver(self,value):
        self._input1Driver = value
    
    
    @property
    def input2Driver(self):
        self._input2Driver = self.addendDriver
        return self._input2Driver

    @input2Driver.setter
    def input2Driver(self,value):
        self._input2Driver = value
    
    
    @property
    def driverEquations(self):
        return self._driverEquations
    
    
    @driverEquations.setter
    def driverEquations(self,value):
        if value != None:
            self._driverEquations = value
            #print("DriverEquations", self._driverEquations)
            if self.equation == None:
                if len(self._driverEquations) == 2:

                    driverNode0Equation = self.driverEquations[0]
                    driverNode1Equation = self.driverEquations[1]
                    self.equation = "(" + driverNode0Equation + "+" + driverNode1Equation + ")"
                
                elif len(self._driverEquations) == 1:
                    driverNode0Equation = self.driverEquations[0]
                    #print("DriverNode Equation", driverNode0Equation)
                    # check which key of the input is present in the drivers dictionary
                    if self.augend in self.driversInfo:
                        if self.augendDriver.isDriverAPort == True:
                            # augend is a port of the adder
                            self.equation = "(" + self.augend + "+" + driverNode0Equation + ")"
                    else:
                        if self.addendDriver.isDriverAPort == True:
                            # addend is a port of the adder
                            self.equation = "(" +  driverNode0Equation + "+" + self.addend + ")"
        
        # set the product expression with the equation
        #print("SWAdder Equation", self.equation)
        self.summation = self.equation

    def connect(self):
        self.connectProperties()
    
    def connectProperties(self):
        super().connectProperties()
       
        #property to store the arithemetic number
        # the arithmetic number property is the number of current multiplier based on the arithmeticNode Number
        # assigned by any PCOperation
        self.arithmeticNodeNumber = 0

  
        # property to store the augend
        # this is equivalent of augend of the two port multiplier
        self._augend = None

        # property to store the addend
        # the property to store the second input of the two port multiplier
        self._addend = None

        # property to store the summation of the augend and the addend
        # the property to store the product or the output of the Adder Entity
        self._summation = None

        # property to store the dictionary info of the drivers of multiplier
        # Multiplier can be driven at both the ends or one of the input is driven by a memory which gives information about weight
        self._drivers = None
        
        # the driver equation is the driver which drives the inputs of the productNode
        # the driver equations property will have max two driver equation, that is a string, stored in the form of an array
        self._driverEquations = None

        # this equation represents the equation of the mutiplier, that is formed based on the given input
        # or combining the driver equations would give the equation a value that can be used
        # the equation will be used by the receiver (or whichever node the current produt node drives)
        self.equation = None

        #property to store the driver of augend driver
        self.augendDriver = None

        #property to store the driver of addend driver
        self.addendDriver = None
        
        # update the driversInfo
        self._driversInfo = None
        
        # property to be used by optimisers, where input1 represents the augend property
        self._input1 = None

        #property to be used by optimisers, where input2 represents the addend property
        self._input2 = None

        # property to mask the summation as output
        self._output = None




    def configure(self):
        # check if the configuration details of the multiplier is set or not
        if self.configurationDetailsOfOperator == None:
            return
        super().configure()


    def reset(self):
        self.resetProperties()
    
    def resetProperties(self):
        super().resetProperties()
        #property to store the arithemetic number
        # the arithmetic number property is the number of current multiplier based on the arithmeticNode Number
        # assigned by any PCOperation
        self.arithmeticNodeNumber = 0


        # property to store the augend
        # this is equivalent of augend of the two port adder
        self._augend = None

        # property to store the addend
        # the property to store the addend input of the two port adder
        self._addend = None


        # property to store the summation of the augend and the adder
        # the property to store the summation or the output of the adder entity
        self._summation = None
        
        # property to store the dictionary info of the drivers of adder
        self._drivers = None
        
        # the driver equation is the driver which drives the inputs of the Adder
        # the driver equations property will have max two driver equation, that is a string, stored in the form of an array
        self._driverEquations = None

        # this equation represents the equation of the mutiplier, that is formed based on the given input
        # or combining the driver equations would give the equation a value that can be used
        # the equation will be used by the receiver (or whichever node the current produt node drives)
        self.equation = None
                
        #property to store the driver of augend driver
        self.augendDriver = None

        #property to store the driver of addend driver
        self.addendDriver = None
        
        # update the driversInfo
        self._driversInfo = None
        
        # property to be used by optimisers, where input1 represents the augend property
        self._input1 = None

        #property to be used by optimisers, where input2 represents the addend property
        self._input2 = None

        # property to mask the summation as output
        self._output = None


        

    def process(self):
        pass
    
   
    def perform(self):
        pass
  
    def main(self):
        pass

    def run(self):
        pass




