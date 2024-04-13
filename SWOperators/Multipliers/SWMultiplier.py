"""
Created by Karthekeyan Periasamy
Edited on November 22 12:39
"""

from SWOperators.SWOperator import SWOperator
from SWOperators.Multipliers.Driver.Driver import Driver
from SWLogic.Memory.Weight.Weight import Weight

class SWMultiplier(SWOperator):

    """
    Class to have blueprint of the different types of multipliers
    In general a multiplier will have a LUT, Input Converter, A Multiplier, Output Converter.
    Based on the number systems, we may or may not have the converters, but for sure we will have LUTs.
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
    def multiplicand(self):
        return self._multiplicand

    @multiplicand.setter
    def multiplicand(self,value):
        self._multiplicand = value
        # build a driver object of the multiplicand if the multiplicand is not a port
        self.multiplicandDriver = Driver()
        self.multiplicandDriver.configurationDetailsOfDriver = {"Name":self._multiplicand}
        self.multiplicandDriver.configure()
        if self.multiplicandDriver.isDriverAWeight == True:
            self.weight = Weight()
            self.weight.configureDetailsOfWeight = {"Weight":self.multiplicandDriver.name}
            self.weight.configure()
        elif self.multiplicandDriver.isDriverAnArithmeticNode == True:
            # update the drivers
            self.drivers.append(self.multiplicandDriver)
            # update the driversInfo
            self.driversInfo[self._multiplicand] = self.multiplicandDriver
        
        #print("SWMultiplier Multiplicand", self._multiplicand)
        
    @property
    def multiplier(self):
        return self._multiplier

    @multiplier.setter
    def multiplier(self,value):
        self._multiplier = value
        # build a driver object of the multiplicand if the multiplicand is not a port
        self.multiplierDriver = Driver()
        self.multiplierDriver.configurationDetailsOfDriver = {"Name":self._multiplier}
        self.multiplierDriver.configure()
        if self.multiplierDriver.isDriverAWeight == True:
            self.weight = Weight()
            self.weight.configureDetailsOfWeight = {"Weight":self.multiplierDriver.name}
            self.weight.configure()
        elif self.multiplierDriver.isDriverAnArithmeticNode == True:
            # update the drivers
            self.drivers.append(self.multiplierDriver)
            # update the driversInfo
            self.driversInfo[self._multiplier] = self.multiplierDriver
        
        #print("SWMultiplier Multiplier", self._multiplier)

   
    
    @property
    def product(self):
        if self._product == None:
            #print("Multiplier", self.multiplier)
            #print("Multiplicand", self.multiplicand)
            if (self.multiplicandDriver and self.multiplierDriver) != None:
                # build the computed equation
                if ((self.multiplicandDriver.isDriverAWeight == True) and (self.multiplierDriver.isDriverAPort == True)):
                    self.equation = "(" + self.multiplier + "*" + self.multiplicand + ")"
                    # set the product expression with the equation
                    #print("SWMultiplier Equation", self.equation)
                    self._product = self.equation
                elif ((self.multiplierDriver.isDriverAWeight == True) and (self.multiplicandDriver.isDriverAPort == True)):
                    self.equation = "(" + self.multiplicand + "*" + self.multiplier + ")"
                    # set the product expression with the equation
                    #print("SWMultiplier Equation", self.equation)
                    self._product = self.equation
                else:
                    self._product = None
        
        return self._product

    @product.setter
    def product(self,value):
        self._product = value
    
    @property
    def input1(self):
        self._input1 = self.multiplicand
        return self._input1

    @input1.setter
    def input1(self,value):
        #print("SW Multiplier Value", value)
        #print("SW Multiplier Input1", self._input1)
        if self._input1 != None:
            if self.isInputDataModified == False:
                # remove the multiplicand driver from the drivers
                multiplicandDriver = self.driversInfo[self.multiplicand]
                # remove the multiplicand port from the inputDataPorts
                self.drivers.remove(multiplicandDriver)
                #print("Length of Drivers", len(self.drivers))
                del self.driversInfo[self._input1]
            self._input1 = value
        elif self._input1 == None:
            if self.multiplicand != None:
                self._input1 = self.multiplicand
                if self.isInputDataModified == False:
                    # remove the multiplicand driver from the drivers
                    multiplicandDriver = self.driversInfo[self.multiplicand]
                    # remove the multiplicand port from the inputDataPorts
                    self.drivers.remove(multiplicandDriver)
                    #print("Length of Drivers", len(self.drivers))
                    del self.driversInfo[self._input1]
                    self._input1 = value
            else:
                self._input1 = value
                
    @property
    def input2(self):
        self._input2 = self.multiplier
        return self._input2

    @input2.setter
    def input2(self,value):
        #print("SW Multiplier Value", value)
        #print("SW Multiplier Input2", self._input2)
        if self._input2 != None:
            if self.isInputDataModified == False:
                # remove the multiplicand driver from the drivers
                multiplierDriver = self.driversInfo[self.multiplier]
                # remove the multiplier driver from the drivers
                self.drivers.remove(multiplierDriver)
                del self.driversInfo[self._input2]
                
            self._input2 = value
        elif self._input2 == None:
            if self.multiplier != None:
                self._input2 = self.multiplier
                if self.isInputDataModified == False:
                    # remove the multiplicand driver from the drivers
                    multiplierDriver = self.driversInfo[self.multiplier]
                    # remove the multiplier driver from the drivers
                    self.drivers.remove(multiplierDriver)
                    del self.driversInfo[self._input2]
                    #print("Length of Drivers", len(self.drivers))
                    self._input2 = value 
            else:
                self._input2 = value
    
    @property
    def output(self):
        self._output = self.product
        return self._output

    @output.setter
    def output(self,value):
        self._output = value
        self.product = value
        
    @property
    def input1Driver(self):
        self._input1Driver = self.multiplicandDriver
        return self._input1Driver

    @input1Driver.setter
    def input1Driver(self,value):
        self._input1Driver = value
    
    
    @property
    def input2Driver(self):
        self._input2Driver = self.multiplierDriver
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
            #print("Driver Equations of SWMultiplier", self._driverEquations)
            if self.equation == None:
                if len(self._driverEquations) == 2:

                    driverNode0Equation = self.driverEquations[0]
                    driverNode1Equation = self.driverEquations[1]
                    self.equation = "(" + driverNode0Equation + "*" + driverNode1Equation + ")"
                    #print("Multiplier Equation", self.equation)
                
                elif len(self._driverEquations) == 1:
                    driverNode0Equation = self.driverEquations[0]
               
                    # check which key of the input is present in the drivers dictionary
                    if self.multiplicand in self.driversInfo:
                        # check whether the multiplier is a weight or not is a float or not
                        if self.multiplierDriver.isDriverAWeight == True:
                            # input2 is a weight of the product node
                            self.equation = "(" + driverNode0Equation + "*" + self.weight.name + ")"
                        elif self.multiplierDriver.isDriverAPort == True:
                            # multiplier is a port of the product node
                            self.equation = "(" + driverNode0Equation + "*" + self.multiplier + ")"

                    elif  self.multiplier in self.driversInfo:
                        # check whether the multiplicand is a weight or not is a float or not
                        if self.multiplicandDriver.isDriverAWeight == True:
                            # input1 is a weight of the product node
                              self.equation = "(" + self.weight.name + "*" + driverNode0Equation + ")"
                        elif self.multiplicandDriver.isDriverAPort == True:
                            # multiplier is a port of the product node
                            self.equation = "(" + self.multiplicand + "*" + driverNode0Equation + ")"
                                        
        # set the product expression with the equation
        #print("SWMultiplier Equation", self.equation)
        self.product = self.equation

    
                    
    def connect(self):
        self.connectProperties()
    
    def connectProperties(self):
        super().connectProperties()
       
        #property to store the arithemetic number
        # the arithmetic number property is the number of current multiplier based on the arithmeticNode Number
        # assigned by any PCOperation
        self.arithmeticNodeNumber = 0

  
        # property to store the multiplicand
        # this is equivalent of inpu1 of the two port multiplier
        self._multiplicand = None

        # property to store the multiplier
        # the property to store the second input of the two port multiplier
        self._multiplier = None

        #property to store the partial products
        # this property will be used when we implement the python based float, fixed or posit multipliers
        self.partialProduct = None

        # property to store the product of the multiplicand and the multiplier
        # the property to store the product or the output of the multiplier entity
        self._product = None

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

        
        #property to store the weight of the multiplier
        # this is a weight object which will contain the infomration of the weight and the name of the weight
        self.weight = None

        self._product = None

        #property to store the driver of multiplicand driver
        self.multiplicandDriver = None

        #property to store the driver of multiplier driver
        self.multiplierDriver = None
        
        # update the driversInfo
        self._driversInfo = None

        self.equation = None


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

  
        # property to store the multiplicand
        # this is equivalent of inpu1 of the two port multiplier
        self._multiplicand = None

        # property to store the multiplier
        # the property to store the second input of the two port multiplier
        self._multiplier = None

        #property to store the partial products
        # this property will be used when we implement the python based float, fixed or posit multipliers
        self.partialProduct = None

        # property to store the product of the multiplicand and the multiplier
        # the property to store the product or the output of the multiplier entity
        self._product = None

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

        
        #property to store the weight of the multiplier
        # this is a weight object which will contain the infomration of the weight and the name of the weight
        self.weight = None

        self._product = None

        #property to store the driver of multiplicand driver
        self.multiplicandDriver = None

        #property to store the driver of multiplier driver
        self.multiplierDriver = None
        
        # update the driversInfo
        self._driversInfo = None

        self.equation = None



    def process(self):
        pass
   
    def perform(self):
        pass
  
    def main(self):
        pass

    def run(self):
        pass




