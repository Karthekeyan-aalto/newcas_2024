#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  18 13:16 2022

@author: Karthekeyan Periasamy
"""

import math


from Analysis.PCAnalysis import PCAnalysis
from Analysis.PCFloatAnalysis import PCFloatAnalysis

class PCPositAnalysis (PCAnalysis):
    
    
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
        # set the probability value to the connected and configured floatAnalysis object
        self.floatAnalysis.errorTolerance = self.errorTolerance
        # set the probability value to the connected and configured floatAnalysis object
        self.floatAnalysis.probabilityValue = self._probabilityValue
        # compute the required number of bits for posit number system
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
        self.mantissaBits = self.floatAnalysis.mantissaBits
        self.esBits = self.floatAnalysis.exponentBits
        # compute the regime bits for a given exponentBits
        regimeCode,esExponentValue = self.computeRegimeBits()
        regime_bits = self.create_regime_bits_string(regimeCode*(-1), "1")
        print("Posit Regime Bits", regime_bits)
        self.numberOfBits = self.floatAnalysis.numberOfBits
        # usually the regime bits and sign bits are added together to form the total number of bits
        self.numberOfBits = (self.numberOfBits-1) + (len(regime_bits) + 1)
        print("Posit Total Number of Bits", self.numberOfBits)
        return (self.mantissaBits,self.esBits,self.numberOfBits)
    
    # logic taken from Posit converter github Author: Raul Murillo
    def computeRegimeBits(self):
        # logic taken from Posit converter github
        self.fixedAnalysisNumberOfBits = self.floatAnalysis.fixedAnalysis.numberOfBits
        print("FixedAnalysis Number of bits", self.fixedAnalysisNumberOfBits)
        newfixedAnalysisNumberOfBits = -abs(int(self.fixedAnalysisNumberOfBits))
        print("NewfixedAnalysisNumberOfBits", newfixedAnalysisNumberOfBits)
        max_y = (2**self.esBits) -1
        print("Max y", max_y)
        c = 0
        while True:
            y = newfixedAnalysisNumberOfBits + (2**self.esBits) * c
            if (y >= 0 and y <= max_y):
                return (c*-1), y
            c = c + 1

    # code taken from the github posit_converter
    #Creates the binary string sequence to represent the regime section of the posit string
    #Refer to the posit reference paper (section 1.1) to see the "tally mark" approach adopted
    def create_regime_bits_string(self,regime_length, expo_sign_bit):
        reg_str = ""
        print("Expo sign bit", expo_sign_bit)
        print("Regime_length", regime_length)
        bit_to_add = 1-int(expo_sign_bit)
        for i in range(regime_length):
            reg_str += str(bit_to_add)
        reg_str += str(expo_sign_bit)
        return reg_str



    def connect(self):
        super().connect()
        # Intialise the PCFloatAnalysis object
        self.floatAnalysis = PCFloatAnalysis()

    def configure(self):
        """
        1. Set the properties with initial values
        """
        super().configure()
        self.floatAnalysis.configure()
        self._probabilityValue = float(0)
        self.esBits = 0
        self.fixedAnalysisNumberOfBits = 0
        self.numberSystem = 2
        

    def reset(self):
        """
        Reset the properties
        """
        super().reset()
        self._probabilityValue = float(0)
        self.esBits = 0
        self._probabilityValue = float(0)


        

    def main(self):
        """
        Main function of the PCPositAnalysis
        """
        # check whether a relative error or a absolute error needs to be performed
        if self.errorType == 1:
            # absolute error should be found for the probability value using the error tolerance
            pass
        elif self.errorType == 0:
            # relative error should be found for the probability value using the error tolerance
            # check the numberSystem
            if self.numberSystem == 2:
                print("Analysis for PCSystem Posit Type with min probability value", self._probabilityValue)
                self.computeRequiredNumberOfBits()

    def run(self):
        self.main()

