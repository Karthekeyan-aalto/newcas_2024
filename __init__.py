#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:49:40 2022

@author: Karthekeyan Periasamy
"""

if __name__ == "__main__":
    from PCSystem import PCSystem
    system = PCSystem()

    # set the default total numberOfBits
    # set the default exponentBits
    # set the default exponentBits
    # set the default esBits
    # numberSystem 0 = fixed, 1 = float, 2 = posit
    # systemType = 1, the pcSystem uses one of the SPN PC; systemType = 0, the pcSystem uses one of the AC PC
    # set the model name

    #msnbc 
    #AC: 22 Float
    #SPN: 22 Float
    #AC: 23,6 Posit
    #SPN: 24 Posit

    
    # set all the above properties as configuration details for the operations package
    system.configurationDetailsOfSystemPackage = {"PCSystemInfo": {"NumberOfBits":22,"MantissaBits":15,"ExponentBits":7,"EsBits":6, "NumberSystem":"Float", "SystemType":"AC", "Model":"nltcs_a", "OptimisePCANToRemoveDuplicatePCAN":True}}

    # configure the system package
    system.configure()
    
    # analysis mode is to decide, whether we need to normal PCOperation or PCMAxOperation
    # PCMaxOperation is used to do inference.
    # if the analysis.mode is set to 1, means normal parsing of the equation to form the PCSystemVHDL
    # if the system and its analysis mode is set, the errorType will be used to do absolute error or relative error based on the type of the error
    # numberSystem 0 = fixed, 1 = float, 2 = posit

    # set the configuration details for the analysis package
    # Activate Bit Optimisation when set to 1, AutoPC will analyse the number of bits required by itself. But, when set to 0, the above PCsystem info object details will be used as per the set number system
    system.configurationDetailsOfAnalysisPackage = {"AnalysisMode":1,"ErrorAnalysisType":"RelativeError","ActivateBitOptimisation":1, "ErrorTolerance":0.001}
    # configure the analysis package
    system.configureAnalysisPackage()
    
    # run the PCSystem
    system.run()
