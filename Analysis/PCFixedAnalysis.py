#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  18 13:16 2022

@author: Karthekeyan Periasamy
"""

import math

from Analysis.PCAnalysis import PCAnalysis

class PCFixedAnalysis (PCAnalysis):
    
    
    def __init__(self):
        super().__init__()

        # connect other packages
        self.connect()
        
        """
        Configure, the PCFixedAnalysis and other necessary child modules/packages
        """
        self.configure()
    
    
    # custom property setter and getter for the member variable value
    @property
    def probabilityValue(self):
        return self._probabilityValue
    
    
    @probabilityValue.setter
    def probabilityValue(self,value):
        # set the value of the value to the property
        self._probabilityValue = value
        # check whether a relative error or a absolute error needs to be performed
        if self.errorType == 1:
            # absolute error should be found for the probability value using the error tolerance
            pass
        elif self.errorType == 0:
            # do the analysis
            self.computeRequiredNumberOfBits()

    #overriding the properties
    def computeRequiredNumberOfBits(self):
        """

        Purpose and Logic
        -------------------

        # to find the number of bits using 991ms calculator
        # formula to find number of bits for a given quantum, number of bits = log (1/quantum) / log (2)
        # for instance if the quanutm is 1.18e-10 the number of bits using the above formula would give 32.9, round it to 33 bits
        # howerver, when back convert the minimum number represented using the 33 bits using the forumula = (1/2^N), where N = numberOfBits = 1.161 e-10
        # so when reverse representing the minValue using the number of bits, the maximum error between the real value and the converted value should be less than (convertedvalue / 2)
        # the above (convertedvalue / 2) is a rule to understand the rounding off errors in bits. so if we have so less bits to represent the original quantum while reverse conversion, 
        # the difference between the converted value and the original (quantum or real value) may exceed the (convertedvalue / 2) bounds. 
        # the above condition first should be met to even start the relative error analysis to make sure the round off is right

        # usually, the above condition on (converted value / 2) quantisation error is represented and sorted using the error tolerance
        # so if the relative error or erroTolerance bounds, i.e ((maxValue - minValue) / 2) is greater than than (convertedValue / 2) form above, the required bits (N) would be mostly higher than 
        # the  number of bits = log (1/quantum) / log (2)
        # if in case the erroTolerance based quantization error is lesser than the actualQuantiztion error, we can return the initial numberOfBits

        # now use the errorTolerance based quantization error to check whether that is lesser than thn minBoundValue (based on the error tolerance)
        # if so, then the errorTolerance based quantization error is the value for which we need to find the final numberOfBits

        # Quantum is the minValue or real Value
        # Min and Max Bound Value base on error tolerance formula: Min/MaxToleratedValue = (1 (+-) 0.01) * (real or min value or quantum)

        Returns
        -------
        Number of bits for the fixed point representation based on either relative error or absolute error

        """
   
        # check if the quantum is greater than 0
        if self.probabilityValue <= 0:
            # then return default 16 bits to run the system
            self.numberOfBits = 90
            self.exponentBits = 8
            return self.numberOfBits

        # so, the quantum is > 0, now we proceed to find the right number of bits to represent the fixed PCSystem
        # first check the errorType
        if self.errorType == 0:

            # we need to find the number of bits based on the relative error concept
            numberOfBits = math.ceil(math.log((1/float(self.probabilityValue)),self.binaryBase))
            # unadjustedNumberOfBits
            self.unadjustedNumberOfBits = numberOfBits
            #print("Unadjusted NumberOfBits", self.unadjustedNumberOfBits)

            actualQuantum = float(1/ 2 ** numberOfBits)
            actualQuantizationError = float(actualQuantum / 2)
            #actualQuantizationError = abs(float(quantum - actualQuantum))
            #print(self.probabilityValue)

            minBoundValue = float((1-self.errorTolerance) * self.probabilityValue)
            maxBoundValue = float((1+self.errorTolerance) * self.probabilityValue)
            errorBasedQuantizationError = float((maxBoundValue - minBoundValue) / 2)
            #print("ErrorBasedQuantisation Error",errorBasedQuantizationError)
            #print("Error Tolerance",self.errorTolerance)


            # now check whether the errorBasedQuantizationError is less than actualQuantizationError
            if actualQuantizationError >= errorBasedQuantizationError:
                # now find the numberOfBits again and that is the final numberOfBits required to run the system
                numberOfBits = math.ceil(math.log(1/float(errorBasedQuantizationError),self.binaryBase))
                # if so, the numberOfBits can be the previously calculated one
                # set the local numberOfBits to global one
                self.numberOfBits = numberOfBits
                print("Analysed Number of bits from fixed analysis:",self.numberOfBits)
                #self.numberOfBits = 22
                return self.numberOfBits
            else:
                # if so, the numberOfBits can be the previously calculated one
                # set the local numberOfBits to global one
                self.numberOfBits = (numberOfBits)                
                return self.numberOfBits
                
    def connect(self):
        pass

    def configure(self):
        super().configure()
        """
        1. Set the properties with initial values
        """
        # fixed numberSystem properties
        self._probabilityValue = float(0)
        self.numberOfBits = 0
        self.unadjustedNumberOfBits = 0

    def reset(self):
        super().reset()
        """
        1. Set the properties with initial values
        """
        # fixed numberSystem properties
        self._probabilityValue = float(0)
        self.numberOfBits = 0


    def main(self):
        # check whether a relative error or a absolute error needs to be performed
        if self.errorType == 1:
            # absolute error should be found for the probability value using the error tolerance
            pass
        elif self.errorType == 0:
            # do the analysis
            self.computeRequiredNumberOfBits()

    def run(self):
        self.main()

