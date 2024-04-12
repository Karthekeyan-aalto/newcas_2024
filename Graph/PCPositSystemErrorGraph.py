#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:25:27 2022

@author: Karthekeyan Periasamy

"""

import math
import numpy as np
from Graph.PCSystemGraph import PCSystemGraph
import matplotlib.pyplot as plt


class PCPositSystemErrorGraph(PCSystemGraph):
     
    def __init__(self):
        super().__init__()
               
    
    """
    Function definitions
    """

    def extractValuesToPlotErrorAnalysisGraph(self):
        # in total there are two analysis 1) maxError 2) averageError
        # extract the maxErrorxAxisData and maxErrorYAxisData
        maxErrroXAxisData, maxErrorYAxisData = self.extractMaxErrorAnalysisValues()
        # set the maxError value to fixedMaxErrorValues property
        self.positSystemMaxErrorValues =  (maxErrroXAxisData, maxErrorYAxisData)
        #print("Values of PositSystemMaxErrorValue Y axis", maxErrorYAxisData)
        #print("Length of PositSystemMaxErrorValue Y axis", len(maxErrorYAxisData))
        # extract the average error analysis
        averageErrorXAxisData, averageErrorYAxisData = self.extractAverageErrorAnalysisValues()
        #print("Length of PositSystemAvgErrorValue Y axis", len(averageErrorYAxisData))
        # set the maxError value to fixedMaxErrorValues property
        self.positSystemAvgErrorValues =  (averageErrorXAxisData, averageErrorYAxisData)
        return (maxErrroXAxisData, maxErrorYAxisData, averageErrorXAxisData, averageErrorYAxisData)


        
        
    def plotMaxAverageErrorAnalysisGraph(self):
        # extract the maxErrorxAxisData and maxErrorYAxisData
        maxErrroXAxisData, maxErrorYAxisData = self.extractMaxErrorAnalysisValues()
        # extract the average error analysis
        averageErrorXAxisData, averageErrorYAxisData = self.extractAverageErrorAnalysisValues()
        print(maxErrroXAxisData, maxErrorYAxisData,averageErrorYAxisData)
        figure, axis = plt.subplots()
        axis.plot(maxErrroXAxisData, maxErrorYAxisData, color='red', label='MaxError', linewidth=1,marker='o')
        axis.plot(maxErrroXAxisData, averageErrorYAxisData, color='black',  linewidth=1, label='AverageError', linestyle='dotted', marker='o')
        axis.set_yscale('log') 
        plt.title("Posit PCSystem")
        plt.xlim(xmin= 0, xmax=70)
        axis.set_xlabel("Total Number Of Bits")
        axis.set_ylabel("Max and Average Error")
        axis.legend(frameon=True, loc='best', ncol=2)
        # plot the axis
        axis.grid(color = 'green', linestyle = '--', linewidth = 0.5)
        plt.show()
        
        
   
    def main(self):
        self.plotMaxAverageErrorAnalysisGraph()
    
    def run(self):
        self.main()
    
