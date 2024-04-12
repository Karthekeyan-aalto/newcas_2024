#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  18 13:16 2022

@author: Karthekeyan Periasamy
"""

import math


from Analysis.PCAnalysis import PCAnalysis
from Analysis.PCFixedAnalysis import PCFixedAnalysis

class PCFloatAnalysis (PCAnalysis):
    
    
    def __init__(self):
        super().__init__()

        """
        Connnect the other necessary child modules/packages
        """
        self.connect()

        """
        Configure, the PCFloatAnalysis and other necessary child modules/packages
        """
        self.configure()
    
    
    
    # custom property setter and getter for the member variable value
    @property
    def probabilityValue(self):
        return self._probabilityValue

    @probabilityValue.setter
    def probabilityValue(self,value):
        """
        Purpose and logic
        ------------------
        Override the setter function to call the floatanalysis method
        """
        # set the value of the value to the property
        self._probabilityValue = value
        # set the fixedAnalysis errorTolerance
        self.fixedAnalysis.errorTolerance = self.errorTolerance
        # set the probability value to the connected and configured fixedAnalysis object
        self.fixedAnalysis.probabilityValue = self._probabilityValue
        # compute the required number of bits for floating point system
        self.computeRequiredNumberOfBits()
                  
    
    def computeRequiredNumberOfBits(self):
        """

        Purpose and Logic
        -------------------
        # The value of number of bits from the fixed analysis is stored as number of bits in float analysis as step 1
        # Then a decimal number for the number of bits is computed
        # Now normalise the decimal number by multiplying the decimal number by 2 for the total number of bits
        # Now access the minValue bits for single precision float and the double precision float 

        
        Returns
        -------
        A Tuple - exponentBits, MantissaBits, Number of bits for the float point representation based on either relative error or absolute error

        """
               
        precision = float(0.0)
        precision = self.errorTolerance * (10 ** -1)
        mantissaBits = math.ceil(math.log((1/precision),2))+1
        print("Final Mantissa bits", mantissaBits)

        # set the mantissabits variables with value
        self.mantissaBits = mantissaBits
        # set the exponentBits with value
        self.exponentBits = math.ceil(math.log((self.fixedAnalysis.numberOfBits),2))
        # final exponentBits
        print("Final ExponentBits", self.exponentBits)
        # updated total number of bits
        totalNumberOfBits = round(self.exponentBits + self.mantissaBits)
        # set the numberOfBits with value
        self.numberOfBits = round(totalNumberOfBits)
        print("Analysed Total number of bits from float analysis", totalNumberOfBits)
        return (totalNumberOfBits, self.exponentBits, self.mantissaBits)
    
    def connect(self):
        super().connect()
        # Intialise the PCFixedAnalysis object
        self.fixedAnalysis = PCFixedAnalysis()

    def configure(self):
        super().configure()
        """
        1. Set the properties with initial values
        """
        self.singlePrecisionFloatMinValue = float(1.175494e-38)
        self.doublePrecisionFloatMinValue = float(2.2250738585072014e-308)
        # float numberSystem property to store the value of PCAnalysis
        self._probabilityValue = float(0)
        self.exponentBits = 0
        self.mantissaBits = 0
        self.numberSystem = 1
        self.fixedAnalysis.errorTolerance = self.errorTolerance

    def reset(self):
        super().reset()
        """
        Reset the properties
        """
        self.singlePrecisionFloatMinValue = None
        self.doublePrecisionFloatMinValue = None
        # float numberSystem property to store the value of PCAnalysis
        self._probabilityValue = float(0)
        self.exponentBits = 0
        self.mantissaBits = 0


        

    def main(self):
        """
        Main function of the PCFloatAnalysis
        """
        # check whether a relative error or a absolute error needs to be performed
        if self.errorType == 1:
            # absolute error should be found for the probability value using the error tolerance
            pass
        elif self.errorType == 0:
            # relative error should be found for the probability value using the error tolerance
            # check the numberSystem
            if self.numberSystem == 1:
                print("Analysis for PCSystem Float Type with min probability value", self._probabilityValue)
                self.computeRequiredNumberOfBits()

    def run(self):
        self.main()

