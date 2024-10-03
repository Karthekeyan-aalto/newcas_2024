#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:38:57 2022

@author: Karthekeyan Periasamy
"""
import os
import sys



def pcSystemParentDirectoryPath():
    currentDirectoryPath = os.getcwd()
    #print("Current Directory", currentDirectoryPath)
    parentDirectoryPath = os.path.abspath(os.path.join(currentDirectoryPath, os.pardir))
    #print("Parent Directory", parentDirectoryPath)
    pcSystemParentDirectoryPath = parentDirectoryPath
    #pcSystemParentDirectoryPath = currentDirectoryPath
    return pcSystemParentDirectoryPath

sys.path.insert(1,pcSystemParentDirectoryPath())

if __name__ == "__main__":

    #from PCAnalysis import PCAnalysis
    #analysis = PCAnalysis()
    # set the error type
    #analysis.errorType = 0
    # set the probabilityValue for which the analysis needs to be done
    #analysis.probabilityValue = None
    #analysis.run()
    
    #from PCFixedAnalysis import PCFixedAnalysis
    #fixedAnalysis = PCFixedAnalysis()
    # set the error tolerance
    #fixedAnalysis.errorTolerance = 0.001
    # set the error type
    #fixedAnalysis.errorType = 0
    # set the number system
    #fixedAnalysis.numberSystem = 0
    # set the probabilityValue for which the analysis needs to be done
    #fixedAnalysis.probabilityValue = 1.0427426260518604e-17
    #fixedAnalysis.probabilityValue = 7.509617279803402e-20
    #fixedAnalysis.probabilityValue = 0.00010016448852046429

    #floatAnalysis.probabilityValue = 4.904384938037399e-27
    #fixedAnalysis.run()    
    
    from PCFloatAnalysis import PCFloatAnalysis
    floatAnalysis = PCFloatAnalysis()
    # set the error tolerance
    floatAnalysis.errorTolerance = 0.1
    # set the error type
    floatAnalysis.errorType = 0
    # set the number system
    floatAnalysis.numberSystem = 1
    # set the probabilityValue for which the analysis needs to be done
    #floatAnalysis.probabilityValue = 7.104628366926888e-14    
    #floatAnalysis.probabilityValue = 1.0427426260518604e-17
    #floatAnalysis.probabilityValue = 1.8053167581036416e-13
    #floatAnalysis.probabilityValue = 4.248901926502472e-07
    #floatAnalysis.probabilityValue = 0.000651836016686902
    #floatAnalysis.probabilityValue = 0.0028269015418692367
    #floatAnalysis.probabilityValue = 5.883831685811427e-39
    #floatAnalysis.probabilityValue = 1.9173831685811427e-39


    floatAnalysis.run()
    
    
    #from PCPositAnalysis import PCPositAnalysis
    #positAnalysis = PCPositAnalysis()
    # set the error tolerance
    #positAnalysis.errorTolerance = 0.001
    # set the error type
    #positAnalysis.errorType = 0
    # set the number system
    #positAnalysis.numberSystem = 2
    # set the probabilityValue for which the analysis needs to be done
    #positAnalysis.probabilityValue = 7.104628366926888e-14    
    #positAnalysis.probabilityValue = 1.0427426260518604e-17
    #positAnalysis.run()

    #from PCAnalysisGraph import PCAnalysisGraph
    #graph = PCAnalysisGraph()
    #graph.graphFiguresYAxes = [[1,2]]
    #graph.numberOfFigures = 1 
    #graph.run()
