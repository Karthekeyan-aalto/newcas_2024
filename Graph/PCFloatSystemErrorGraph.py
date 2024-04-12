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


class PCFloatSystemErrorGraph(PCSystemGraph):
    
    def __init__(self):
        super().__init__()
    


    """
    Function definitions
    """

    def extractValuesToPlotErrorAnalysisGraph(self):
        # in total there are two analysis 1) maxError 2) averageError
        # extract the maxErrorxAxisData and maxErrorYAxisData
        maxErrroXAxisData, maxErrorYAxisData = self.extractMaxErrorAnalysisValues()
        #print("Values of FloatSystemMaxErrorValue Y axis", maxErrorYAxisData)
        #print("Length of FloatSystemMaxErrorValue Y axis", len(maxErrorYAxisData))
        # set the maxError value to fixedMaxErrorValues property
        self.floatSystemMaxErrorValues =  (maxErrroXAxisData, maxErrorYAxisData)
        # extract the average error analysis
        averageErrorXAxisData, averageErrorYAxisData = self.extractAverageErrorAnalysisValues()
        # set the maxError value to fixedMaxErrorValues property
        self.floatSystemAvgErrorValues =  (averageErrorXAxisData, averageErrorYAxisData)
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
        plt.title("Float PCSystem")
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
    
