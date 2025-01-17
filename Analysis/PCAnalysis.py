#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:25:27 2022

@author: Karthekeyan Periasamy

"""

import math
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu
import scipy.stats as stats
from scipy.special import rel_entr
from scipy.special import kl_div

class PCAnalysis():
    """
    PCAnalaysis object and member variables handle the analysis for different analysis mode of the PCEquationParser
    For instance, when the parser is in sensitivity analysis mode, the object and memeber variables of PCAnalysis,
    provide functionalities to analyse and output the corresponding results
    """
    
    def __init__(self):

        """
        Init function to have declaration and initialisation of necessary variables.
        For now, we do not have the concept of lazy loading so most of the member variables are initialised 
        during the initialisation of the PCAnalysis object
        
        """

        # configure the analysis parent module
        #self.configure()
               
    
    """
    Custom property getters and setters
    """
    
    # custom property setter and getter for errorTolerancePercentage
    
    # Useful to o compute few other member variables when the errorTolerancePercentage is set
    
    @property
    def errorTolerancePercentage(self):
        return self._errorTolerancePercentage
    
    @errorTolerancePercentage.setter
    def errorTolerancePercentage(self,value):
        self._errorTolerancePercentage = value
        # divide the error tolerance percentage by 100
        errorTolerance = self._errorTolerancePercentage / 100
        # set the error tolerance value
        self.errorTolerance = errorTolerance
    
    
    @property
    def errorTolerance(self):
        return self._errorTolerance
    
    @errorTolerance.setter
    def errorTolerance(self,value):
        self._errorTolerance = value
        
    
    @property
    def pcSystemSWOutput(self):
        return self._pcSystemSWOutput
    
    @pcSystemSWOutput.setter
    def pcSystemSWOutput(self,value):
        self._pcSystemSWOutput = value
               
    @property
    def pcSystemHWOutput(self):
        return self._pcSystemHWOutput
    
    @pcSystemHWOutput.setter
    def pcSystemHWOutput(self,value):
        self._pcSystemHWOutput = value
    
              
    """
    Function definition
    """   
    
    def computeRequiredNumberOfBits(self):
        pass

    
    def computePCSystemErrorBetweenSWAndHWOutput(self):
        """
        # read the software output from the likelihood csv file for the respective model
        # read the hardware decimal output from the DecimalOutput.txt file for the respective model

        # then, check whether the length of the SW and HW output are same. If not, raise an exception
        # if both the SW and HW length are same, choose the same index values and find the error, either relative or absoulte based on the error type of the system
        # error type of the system will be available from the PCSystemInfo property of the PCSystemIOProcessing
        # now switch to respective function handlers based on the error type

        Returns
        ---------
        An array of errorAnalysis results

        """
        if self.errorType == 0:
            maxErrorAndErrorAnalysisResutls = self.__computePCSystemRelativeErrorBetweenSWAndHWOutput()
            return maxErrorAndErrorAnalysisResutls
        else:
            return
        return
    
    
    def __computePCSystemHWSWDistributionSimilarity(self):
        """
        # compare the HWSW output distribution by performing Mann-whitney U test
        # Use the helper functions to access the results of it

        Returns
        ---------
        results
        """
        results = self.__comparePCSystemHWOutputDistributionWithSWOutput()
        return results


    def __computePCSystemRelativeErrorBetweenSWAndHWOutput(self):
        """
        # read the software output from the pcSystemSWOutput property 
        # read the hardware decimal output from the pcSystemHWOutput.

        # then, check whether the length of the SW and HW output are same. If not, raise an exception
        # if both the SW and HW length are same, choose the same index values and find the relative error of the system
        # sw output is the real value and the measured or inferred value is the HW output

        
        #. The found error array will be stored in a file for further analysis
        #. Finally, we need to find the maxError for the found error array
        
        Returns
        -------
        An array with the relative errors for each element of the HW and SW results

        """
        pcSystemSWOutputLikelihood = []
        # property to the relative error values
        relativeErrors = []
        # property to store the detailed errors including the SW, HW and Error tolerant details
        detailedErrors = []
        # property to store the HWOutputLikelihood
        pcSystemHWOutputLikelihood = list()
        # property to store the details of max error to numberOfBits
        maxError = dict()
        # property to store the averageError
        averageError = dict()
        # property to store the swError
        pcSystemSWOutputAverageLikelihood = dict()
        # property to averagelikelihood to numberOfBits
        pcSystemHWOutputAverageLikelihood = dict()
        # property to store the mannWhitneyUTest  to numberOfBits
        pcSystemMannWhitneyUTest = dict()

        #print("Length of PCSystemSWOutput",len(self.pcSystemSWOutput))
        #print("PCSystemHWOutput", self.pcSystemHWOutput)
        #print("Length of PCSystemHWOutput",len(self.pcSystemHWOutput))

        if (len(self.pcSystemHWOutput)) == (len(self.pcSystemSWOutput)):
            # retreive the one to one map from both the SW output and HW output
            for outputIndex in range(0, len(self.pcSystemHWOutput)):
                # access the SW output with the index
                swOutput = self.pcSystemSWOutput[outputIndex][0]
                # access the HW output with the index
                hwOutput = self.pcSystemHWOutput[outputIndex][0]
                # use euclidian distance scoring rule to find hwLikelihood
                hwOutputLikelihood = (((float(swOutput)-float(hwOutput))) ** 2) / (float(swOutput))
                pcSystemHWOutputLikelihood.append(float(hwOutputLikelihood))
        
                # use euclidian distance scoring rule to find hwLikelihood
                swOutputLikelihood = (((float(swOutput)-float(swOutput))) ** 2)
                pcSystemSWOutputLikelihood.append(float(swOutputLikelihood))
                # sw output is the real value and the measured or inferred value is the HW output
                # subtract the hw and sw output
                absoluteError = float((float(float(swOutput) - float(hwOutput))))
                #if outputIndex == 127 or outputIndex == 126:
                    #print("AbsoluteError",absoluteError,float(swOutput), float(hwOutput))
                    #print("Modulo Absolute Error", abs(absoluteError))
                    #print("Relative Error",abs(absoluteError)/float(swOutput))

                # divide the absoluteError by the swOutput
                relativeError = abs((float(float(absoluteError) / float(swOutput))))
                # modify relative error
                if relativeError < 0.01:
                    detailedError = swOutput + "," + hwOutput + "," + str (relativeError) + "," + "ErrorTolerance Achieved"
                else:
                    detailedError = swOutput + "," + str(hwOutput) + "," + str (relativeError) + "," + "ErrorTolerance Not Achieved"

                # add the relativeError to the array
                relativeErrors.append(relativeError)
                # add the detailed Error
                detailedErrors.append(detailedError)

            
            # add the numbefOfBits to maxError analysis
            maxError['NumberOfBits'] = self.numberOfBits
            # add the maxError 
            maxError['MaxError'] = str(max(relativeErrors))

            # find the average of HW errors
            sumOfErrors = float(sum(relativeErrors))
            # access the totalErrors
            totalErrors = len(relativeErrors)
            # add the numbefOfBits to averageError dict
            averageError['NumberOfBits'] = self.numberOfBits
            # add averageError value to AverageError key of the averageError dict
            averageError['AverageError'] = abs((float(sumOfErrors)/int(totalErrors)))
            
            # find the average of SW LikeliHood
            sumOfPCSystemSWOutputLikelihood = float(sum(pcSystemSWOutputLikelihood))
            # access the len of pcSystemSWOutputLikelihood
            totalPCSystemSWOutputLikelihood = len(pcSystemSWOutputLikelihood)
            # add the numbefOfBits to pcSystemSWOutputAverageLikelihood dict
            pcSystemSWOutputAverageLikelihood['NumberOfBits'] = self.numberOfBits
            # add the sw Error value to Software Error key of the swError dict
            pcSystemSWOutputAverageLikelihood['SWAverageLikelihood'] = (float(sumOfPCSystemSWOutputLikelihood)/int(totalPCSystemSWOutputLikelihood))

            # get the average value of the pcSystemAverageLikelihood
            # get the sum of the HWOutput
            pcSystemHWOutputSum = sum(pcSystemHWOutputLikelihood)
            # divide the HWOutput with the length of the pcSystemHWOutputLikelihood
            pcSystemHWOutputLength = len(pcSystemHWOutputLikelihood)
            # average likelihood
            pcSystemHWOutputAverageLikelihoodValue = float(float(pcSystemHWOutputSum) / int(pcSystemHWOutputLength))
            # print the averageLikelihoodValue
            print(pcSystemHWOutputAverageLikelihoodValue)
            # add the numberOfBits and averageLikelihoodValue to the dict
            pcSystemHWOutputAverageLikelihood['NumberOfBits'] = self.numberOfBits
            # add the averageLikelihoodValue to the dict
            pcSystemHWOutputAverageLikelihood['HWAverageLikelihood'] = pcSystemHWOutputAverageLikelihoodValue

            # find the maxError
            print("Max Relative Error", max(relativeErrors))
            if  max(relativeErrors) < 0.01:
                detailedError = str(max(relativeErrors)) + " " + "Max relative error less than errorTolerance"
                detailedErrors.append(detailedError)
            else:
                detailedError = str(max(relativeErrors)) + " " + "Max relative error greater than errorTolerance"
                detailedErrors.append(detailedError)

            mannWhitneyUTestResult = self.__computePCSystemHWSWDistributionSimilarity()
            # make a dictionary with number of bits and mannwhitneyUTest
            pcSystemMannWhitneyUTest["NumberOfBits"] = self.numberOfBits
            # make a dictionary with number of bits and mannwhitneyUTest
            pcSystemMannWhitneyUTest["MannWhitneyUTestPValue"] = mannWhitneyUTestResult
            # print the selected P value from the MannWhitneyUTest
            print("PCSystemMannWhitneyUTest", pcSystemMannWhitneyUTest)

            return (detailedErrors, maxError, pcSystemHWOutputAverageLikelihood, averageError, pcSystemSWOutputAverageLikelihood, pcSystemMannWhitneyUTest)

        else:
            #print("PCSystemSWOutput",self.pcSystemSWOutput)
            print("Length of PCSystemSWOutput",len(self.pcSystemSWOutput))
            #print("PCSystemHWOutput", self.pcSystemHWOutput)
            print("Length of PCSystemHWOutput",len(self.pcSystemHWOutput))
            # access the HWSW distribution similarity
            mannWhitneyUTestResult = self.__computePCSystemHWSWDistributionSimilarity()
            # make a dictionary with number of bits and mannwhitneyUTest
            pcSystemMannWhitneyUTest["NumberOfBits"] = self.numberOfBits
            # make a dictionary with number of bits and mannwhitneyUTest
            #pcSystemMannWhitneyUTest["MannWhitneyUTestPValue"] = mannWhitneyUTestResult
            # make a dictionary with number of bits and mannwhitneyUTest
            pcSystemMannWhitneyUTest["KLDivergence"] = mannWhitneyUTestResult
            # print the selected P value from the MannWhitneyUTest
            print("PCSystemMannWhitneyUTest", pcSystemMannWhitneyUTest)
            return (detailedErrors, maxError, pcSystemHWOutputAverageLikelihood, averageError, pcSystemSWOutputAverageLikelihood, pcSystemMannWhitneyUTest)


    def __processHWSWOutput(self):
        """
        To retrieve the exact values of SW and HW output from the member variables
        1. self.pcSystemHWOutput
        2. self.pcSystemSWOutput
        """
        # temprorary variables to store the retrieved HW and SW output
        pcSystemSWOutput = []
        pcSystemHWOutput = []
        if (len(self.pcSystemHWOutput)) == (len(self.pcSystemSWOutput)):
            # retreive the one to one map from both the SW output and HW output
            for outputIndex in range(0, len(self.pcSystemHWOutput)):
                # access the SW output with the index
                swOutput = self.pcSystemSWOutput[outputIndex][0]
                # add the swOutput to the pcSystemSWOutput
                pcSystemSWOutput.append(swOutput)
                # access the HW output with the index
                hwOutput = self.pcSystemHWOutput[outputIndex][0]
                # add the hwOutput to the pcSystemHWOutput
                pcSystemHWOutput.append(hwOutput)
                
            
        # return the processed output of HW and SW as tuple
        return (pcSystemHWOutput, pcSystemSWOutput)

    
    def __comparePCSystemHWOutputDistributionWithSWOutput(self):
        """
        Information from internet is written here for understanding

        # As we do not know the distribution of PCSystemHW output and SWOutput, we use Mann-Whitney-U-Test
        # It is used to find the stochastic dominance of the HW and SW output
        # process the software and hardware output from the pcSystemSWOutput properties 
        
        # Use pandas to run the mannwhitneyU test with dataframe as parameters 
        # Finally, we need to find the maxError for the found error array
        
        Returns
        -------
        Mann-whitney U test results

        """
        # property to store the SWHWOutput
        pcSystemHWSWOutput = self.__processHWSWOutput()
        pcSystemSWOutput = pcSystemHWSWOutput[1]
        pcSystemHWOutput = pcSystemHWSWOutput[0]
        #print("PCSystemSWOutput:", pcSystemSWOutput)
        #print("PCSystemHWOutput:", pcSystemHWOutput)

        #store the HWOutput and SWOutput as DF
        hwswOutputData = dict()
        # HWOutput stored to be added to a dataframe
        hwswOutputData["HWOutput"] = pcSystemHWOutput
        # SWOutput stored to be added to a dataframe
        hwswOutputData["SWOutput"] = pcSystemSWOutput
        # form the dataframe
        hwswDataFrame = pd.DataFrame(hwswOutputData)
        # print the dataframe of SWOutput
        #print("The HWdataframe", hwswDataFrame["SWOutput"])
        # print the dataframe of HWOutput
        #print("The HWdataframe", hwswDataFrame["HWOutput"])
        # perform the mannwhitneyutest
        #mannWhitneyUTestResults = mannwhitneyu(hwswDataFrame["SWOutput"], hwswDataFrame["HWOutput"])
        #mannWhitneyUTestResults = mannwhitneyu(pcSystemHWOutput, pcSystemSWOutput, use_continuity=False, alternative='two-sided')
        # do kl divergence test
        # change the string HWOutput to float
        hwOutput = list(map(float, hwswDataFrame["HWOutput"]))
        # change the string SWOutput to float
        swOutput = list(map(float, hwswDataFrame["SWOutput"]))
        klDivergenceResults = sum(kl_div(hwOutput, swOutput))
        # print the results
        print("KLDivergence Results", klDivergenceResults)
        # print the results
        #print("mannWhitneyUTestResults", mannWhitneyUTestResults)
        
        # return the results
        return klDivergenceResults      

    def connect(self):
        pass
 
    def configure(self):
        # constants to represent the base of the computation or analysis carried
        self.binaryBase = 2
        self.decimalBase = 10
        
        """
        Section: Properties to  store minimum values from sensitivity analysis
        
        """
        # float numberSystem property to store the value of PCAnalysis
        self._probabilityValue = float(0)
        
        
        """
        Section: Properties to store analysis constrains
        """
        # error type of the analysis
        self.errorType = 0
        # error tolerance is a private member variable calculated from the given error tolerance percentage
        self._errorTolerance = 0
        self._errorTolerancePercentage = 0
        
        
        """
        Section: Properties to store the relative error results
        """
        self.minRelativeErrorBound = 0
        self.maxRelativeErrorBound = 0
        
        """
        PCSystem Properties  
        # numberOfBits
        # state
        # Number system supported types 1) Fixed 2) Float 3) POSIT
        # pcSystemSWOutput
        # pcSystemHWOutput
        """
        self.numberOfBits = 0
        self.state = 0
        self.numberSystem = 0
        self._pcSystemHWOutput = None
        self._pcSystemSWOutput = None
       

        """
        Section: PCSystem analyis settings
        # Mode 0: PCMinOperation
        # Mode 1: PCOpertion
        # Mode 2: PCMaxOPeration
        """
        self.mode = 0


    def reset(self):
        # constants to represent the base of the computation or analysis carried
        self.binaryBase = 2
        self.decimalBase = 10
        
        """
        Section: Properties to  store minimum values from sensitivity analysis
        
        """
        # float numberSystem property to store the value of PCAnalysis
        self._probabilityValue = float(0)
        
        
        """
        Section: Properties to store analysis constrains
        """
        # error type of the analysis
        self.errorType = 0
        # error tolerance is a private member variable calculated from the given error tolerance percentage
        self._errorTolerance = 0
        self._errorTolerancePercentage = 0
        
        
        """
        Section: Properties to store the relative error results
        """
        self.minRelativeErrorBound = 0
        self.maxRelativeErrorBound = 0
        
        """
        PCSystem Properties  
        # numberOfBits
        # state
        # Number system supported types 1) Fixed 2) Float 3) POSIT
        # pcSystemSWOutput
        # pcSystemHWOutput
        """
        self.numberOfBits = 0
        self.state = 0
        self.numberSystem = 0
        self._pcSystemHWOutput = None
        self._pcSystemSWOutput = None
       

        """
        Section: PCSystem analyis settings
        # Mode 0: PCMinOperation
        # Mode 1: PCOpertion
        # Mode 2: PCMaxOPeration
        """
        self.mode = 0


    def main(self):
        pass

    def run(self):
        self.main()
    
