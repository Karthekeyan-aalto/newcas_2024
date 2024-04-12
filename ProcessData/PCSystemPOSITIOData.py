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
from NumberSystemPackages.POSITConverter.posit_converter import PositConverter

class PCSystemPOSITIOData(PCSystemIOData):
    
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
        super().processPCSystemOutput()
        # check the numberSystem                
        if self.pcSystemNumberSystem == 2:
            self.__processPositPCSystemOutput()
    
    def __processPositPCSystemOutput(self):
        print("Start: conversion of output data to decimal")
        decimalOutput = self.convertPCSystemOutputDataToDecimal()
        print("End: conversion of output data to decimal")
        # set the decimalOutputData of the pcSystemOutput to the fileSystem
        # custom setter is establised to write to the fileSystem when the pcSystemDecimalOutput is set
        # the custom setter will set the writeMode of the fileSystem
        self.fileSystem.pcSystemHWOutput = decimalOutput
        # set the readMode of the fileSystem before reading
        self.fileSystem.readMode = 1
        # print the HWOutput results
        #print("The Length PCSystem HWOutput:", len(self.fileSystem.pcSystemHWOutput))
        # print the SWOutput results
        #print("The Length PCSystem SWOutput:", len(self.fileSystem.pcSystemSWOutput))
        # read the pcSystemSWResults and set it to analysis property
        self.analysis.pcSystemSWOutput = self.fileSystem.pcSystemSWOutput
        # set again the readMode to 1 to futher read, as the read function once read, will reset the readMode
        self.fileSystem.readMode = 1
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
            # access the results of the mann-whitney U - test
            mannWhitneyUTestResults = maxErrorAndErrorAnalysisResults[5]
            # print the mannWhitneyUTestResults
            print("U Test results", mannWhitneyUTestResults)
            # set the pcSystemSWAverageLikelihoodAnalysis
            self.fileSystem.pcSystemMannWhitneyUTestAnalysis = mannWhitneyUTestResults
    
    def convertPCSystemOutputDataToDecimal(self):
        """
        1. Retrieve each element and convert it to decimal using the PositConvert function convert posit to float.
        
        Returns
        ---------
        One dimensional array of decimal output data
        """
         #Initialise the converter object
        print("State 3: Converter object initialised")
        converter = PositConverter(self.pcSystemNumberOfBits,self.pcSystemEsBits,self.pcSystemMantissaBits)
        # variable to store the decimal output
        decimalOutput = []
        # loop through the pcSystemOutput
        print("State 3: Conversion to decimal started")
        for outputData in self.pcSystemOutput:
            # access the first index "0" of the outputData
            # print the data of the output
            #print("HW binary output:", outputData[0])
            decimalOutputData = converter.convert_posit_to_float(outputData[0])
            decimalOutput.append(decimalOutputData)
            
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
        # call the handler to process the output
        self.processPCSystemOutput()


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





           
        





      
        
