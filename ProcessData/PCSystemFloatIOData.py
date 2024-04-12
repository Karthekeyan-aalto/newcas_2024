#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:49 2022

@author: Karthekeyan Periasamy
"""

import csv
import numpy as np
import torch
from torch import nn
from FileSystem.PCFileSystem import PCFileSystem
from Analysis.PCAnalysis import PCAnalysis
from ProcessData.PCSystemIOData import PCSystemIOData
from NumberSystemPackages.FloatConverter.FloatConverter import FloatConverter


class PCSystemFloatIOData(PCSystemIOData):
    
    def __init__(self):
        super().__init__()

       
    def processPCSystemOutput(self):
        """
        Purpose and Logic
        ------
        Process the two dimensional output array store by switching it to the appropriate switching handler based on the numberSystem
        1.Check the numberSystem using pcSystemNumberSystem property
        2.Check the numberSystem type and call appropriate handlers. For instance, converting the fixedOutput to Decimal value is handled by convertPCSystemOutputDataFromFixedToDecimal

        Returns
        --------
        None.
        """
        # check the numberSystem
        if self.pcSystemNumberSystem == None:
            assert "PCSystemNumberSystem not available from the PCSystemInfo file"
            return
                
        if self.pcSystemNumberSystem == 1:
            self.__processFloatPCSystemOutput()


    
    def __processFloatPCSystemOutput(self):
        print("Start: conversion of output data to decimal")
        decimalOutput = self.convertPCSystemOutputDataToDecimal()
        print("End: conversion of output data to decimal")
        # set the decimalOutputData of the pcSystemOutput to the fileSystem
        # custom setter is establised to write to the fileSystem when the pcSystemDecimalOutput is set
        self.fileSystem.pcSystemHWOutput = decimalOutput
        # read the pcSystemSWResults and set it to analysis property
        self.analysis.pcSystemSWOutput = self.fileSystem.pcSystemSWOutput
        # read again the previously stored decimal output HW resutls
        self.analysis.pcSystemHWOutput = self.fileSystem.pcSystemHWOutput
        # now analyse the pcSystemError
        maxErrorAndErrorAnalysisResults = self.analysis.computePCSystemErrorBetweenSWAndHWOutput()
        # check the errorAnalysisResults
        if maxErrorAndErrorAnalysisResults != None:
            # write the error analysis array to the fileSystem
            errorAnalysisResults = maxErrorAndErrorAnalysisResults[0]
            self.fileSystem.pcSystemErrorAnalysis = errorAnalysisResults
            # write the max error analysis to the fileSystem
            maxErrorAnalysisResults = maxErrorAndErrorAnalysisResults[1]
            self.fileSystem.pcSystemMaxErrorAnalysis = maxErrorAnalysisResults
            # write the averagelikeli hood analysis to the fileSystem
            hwAverageLikelihoodAnalysisResults = maxErrorAndErrorAnalysisResults[2]
            self.fileSystem.pcSystemHWAverageLikelihoodAnalysis = hwAverageLikelihoodAnalysisResults
            # write the averageError analysis to the fileSystem
            averageErrorAnalysisResults = maxErrorAndErrorAnalysisResults[3]
            self.fileSystem.pcSystemAverageErrorAnalysis = averageErrorAnalysisResults
            # write the swErrorAnalysisResults analysis to the fileSystem
            swAverageLikeliHoodAnalysisResults = maxErrorAndErrorAnalysisResults[4]
            self.fileSystem.pcSystemSWAverageLikelihoodAnalysis = swAverageLikeliHoodAnalysisResults
        
    def convertPCSystemOutputDataToDecimal(self):
        """
        1. Retrieve each element and convert it to float using the FloatConverter function bit2float.
        2.

        Returns
        ---------
        One dimensional array of decimal output data
        """
        #Initialise the converter object
        print("State 3: Converter object initialised")
        converter = FloatConverter()
        # variable to store the decimal output
        decimalOutput = []
        # loop through the pcSystemOutput
        print("State 3: Conversion to decimal started")
        for outputData in self.pcSystemOutput:
            # access the first index "0" of the outputData
            # print the data of the output
            #print("HW binary output:", outputData[0])
            # store locally to strip the ":" of the outputData
            output=outputData[0]
            output=output.replace(":", "")
            decimalOutputData = converter.bit2float(torch.Tensor([[int(f) for f in list(output.strip())]]),
                    num_e_bits=self.pcSystemExponentBits,
                    num_m_bits=((self.pcSystemMantissaBits-1)), bias= (((2 ** self.pcSystemExponentBits)/2)-1))
            decimalOutput.append(decimalOutputData.item())
            
        #print the length of the decimal output data
        #print("Length of the Decimal Output",len(decimalOutput))
        print("State 3: Complete, Conversion to decimal output from fixed output data")
        return decimalOutput
    
   
    def processData(self):
        """
        Purpose
        -------
        1. To call processPCSystemOutputData handler to generate decimal output values of the PCSystemOutputData

        Returns
        -------
        None.
        """
        #super().processData()
        # call the handler to process the output
        self.processPCSystemOutput()

    def configure(self):
        super().configure()


    def main(self):
        """
        Purpose
        ---------
        The main function to process IO of the PCSystem
        self.processData function handler is called when main function is called.
       
        Returns
        -------
        None.

        """
        self.processData()
               
    def run(self):
        self.main()





           
        





      
        
