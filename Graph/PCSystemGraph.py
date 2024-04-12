#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:25:27 2022

@author: Karthekeyan Periasamy

"""

import math
import numpy as np
from FileSystem.PCFileSystem import PCFileSystem
from Configuration.PCAnalysisGraphConfiguration import PCAnalysisGraphConfiguration
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'Times New Roman'})
plt.rcParams.update({'font.size':12})
plt.rcParams.update({'font.weight':'bold'})




class PCSystemGraph():
    """
    PCSystemGraph object and member variables are used to plot graphs from the data stores in testfile for different analysis
    """
    
    def __init__(self):
        """
        Init function to have declaration and initialisation of necessary variables.
        For now, we do not have the concept of lazy loading so most of the member variables are initialised 
        during the initialisation of the PCAnalysis object
        
        """
        

        """
        Properties
        1. self.yAxisData stores the data in the form of array to be represented in the y axis of the graph
        2. self.xAxisData stores the data in the form of array to be represented in the x axis of the graph
        """
        self.graphTitle = None
        self._numberOfFigures = 1
        self._graphFigureYAxes = None
        self._graphAxes = None
        self._graphFigures = None
        self.fixedSystemMaxErrorValues = None
        self.floatSystemMaxErrorValues = None
        self.positSystemMaxErrorValues = None
        self.fixedSystemAvgErrorValues = None
        self.floatSystemAvgErrorValues = None
        self.positSystemAvgErrorValues = None


        """
        Graph configuration
        """
        self.graphConfiguration = PCAnalysisGraphConfiguration()
        
        self._yAxesData = None
        self._xAxesData = None
        self._yAxesLabel = None
        self._xAxesLabel = None

        """
        Analysis resutls properties
        """
        self.decimalBase = 10
        self.binaryBase = 2

        """
        FileSystem properties
        """
        self._fileSystem = None


        """
        PCSystem Properties
        """
        self._pcSystemInfo = None
        self._pcSystemNumberSystem = None

       
    """
    Custom property getters and setters
    """
   
    @property
    def graphFigures(self):        
        return self._graphFigures

    @graphFigures.setter
    def graphFigures(self,value):
        self._graphFigures = value
    

    
    @property
    def graphFiguresAxes(self):
        return self._graphFiguresAxes

    @graphFiguresAxes.setter
    def graphFiguresAxes(self,value):
        self._graphFiguresAxes = value
    
    
    @property
    def graphFiguresYAxes(self):
        return self._graphFiguresYAxes

    @graphFiguresYAxes.setter
    def graphFiguresYAxes(self,value):
        self._graphFiguresYAxes = value
        # set the graphFiguresYAxes to the configuration object
        self.graphConfiguration.graphFiguresYAxes = self._graphFiguresYAxes

        
    @property
    def numberOfFigures(self):
        return self._numberOfFigures

    @numberOfFigures.setter
    def numberOfFigures(self,value):
        self._numberOfFigures = value
        # set the numberOfFigures to the configuration object
        #self.graphConfiguration.numberOfGraphFigures = self._numberOfFigures
        # access the graphFigures from graphConfiguration
        #self.graphFigures = self.graphConfiguration.graphFigures
        #print("Configured Graph Figures", self.graphFigures)
        # access the graphAxes from graphConfiguration
        #self.graphFiguresAxes = self.graphConfiguration.graphFiguresAxes

         
    @property
    def pcSystemNumberSystem(self):
        return self._pcSystemNumberSystem

    @pcSystemNumberSystem.setter
    def pcSystemNumberSystem(self,value):
        self._pcSystemNumberSystem = value
        #self.graphFigure.title(self._pcSystemNumberSystem)
    
    @property
    def pcSystemModel(self):
        return self._pcSystemModel

    @pcSystemModel.setter
    def pcSystemModel(self,value):
        self._pcSystemModel = value
        self.graphTitle = self._pcSystemModel.upper()
        if self.pcSystemNumberSystem == 0:
            self.graphTitle =  self.graphTitle + " " + "AC"
        elif self.pcSystemNumberSystem == 1:
            self.graphTitle =  self.graphTitle + " " + "SPN"
        self.graphYAxisLabel = self._pcSystemModel

    
   
    @property
    def pcSystemInfo(self):
        if self._pcSystemInfo == None:
            self._pcSystemInfo = self.fileSystem.readPCSystemInfo()
            # access the number system of the PCSystem using the key 
            self.pcSystemNumberSystem = self._pcSystemInfo["NumberSystem"]
            
        return self._pcSystemInfo

    @pcSystemInfo.setter
    def pcSystemInfo(self,value):
        self._pcSystemInfo = value

        
    @property
    def yAxesData(self):
        if self._yAxesData == None:
            self._yAxesData = list()
        return self._yAxesData

    @yAxesData.setter
    def yAxesData(self,value):
        self._yAxesData = value
   
    @property
    def xAxesData(self):
        if self._xAxesData == None:
            self._xAxesData = list()
        return self._xAxesData

    @xAxesData.setter
    def xAxesData(self,value):
        self._xAxesData = value


    @property
    def yAxesLabel(self):
        if self._yAxesLabel == None:
            self._yAxesLabel = list()
        return self._yAxesLabel

    @yAxesLabel.setter
    def yAxesLabel(self,value):
        self._yAxesLabel = value
   
    @property
    def xAxesLabel(self):
        if self._xAxesLabel == None:
            self._xAxesLabel = list()
        return self._xAxesLabel

    @xAxesLabel.setter
    def xAxesLabel(self,value):
        self._xAxesLabel = value
           
          
    @property
    def fileSystem(self):
        if self._fileSystem == None:
            self._fileSystem = PCFileSystem()
          
        return self._fileSystem

    @fileSystem.setter
    def fileSystem(self,value):
        self._fileSystem = value

        
    def configure(self):
        """
        Initialise the values of the variables
        1. system based variables to store max, avg values are intialised
        2. The variables will be used to plot the graph
        """
        self.fixedPCSystemMaxErrorValues = None
        self.floatPCSystemMaxErrorValues = None
        self.positPCSystemMaxErrorValues = None


    """
    Function definitions
    """

    def __extractValuesToPlotErrorAnalysisGraph(self):
        # in total there are two analysis 1) maxError 2) averageError
        # extract the maxErrorxAxisData and maxErrorYAxisData
        maxErrroXAxisData, maxErrorYAxisData = self.__extractMaxErrorAnalysisValues()
        # extract the average error analysis
        averageErrorXAxisData, averageErrorYAxisData = self.__extractAverageErrorAnalysisValues()
        # access the graphAxes to set the xAxesData and yAxesData
        for graphFigureAxisIndex in range(0,len(self.graphFiguresAxes)):
            graphFigureAxis = self.graphFiguresAxes[graphFigureAxisIndex]
            # check the length of the graphFigureAxis by checking the length of the graphFigureAxis
            if len(graphFigureAxis) > 1:
                # then the figure of maxError and averageError will be merged
                # set the xAxes Label for both the graphs
                self.xAxesData.append([maxErrroXAxisData])
                # set the yAxes Label for both the graphs
                self.yAxesData.append([maxErrorYAxisData,averageErrorYAxisData])
                # set the xAxis Label
                self.xAxesLabel.append(["NumberOfBits"])
                # set the yAxes Label
                self.yAxesLabel.append(["Max Relative Error", "Average Relative Error"])

            else:
                # maxError and AverageError will not be merged rather two figures will be generated
                # set the xAxis Label
                self.xAxesData.append([maxErrroXAxisData])
                # set the yAxis Label
                self.yAxesData.append([maxErrorYAxisData])
                # set the xAxis Label
                self.xAxesLabel.append(["NumberOfBits"])
                # set the yAxes Label
                self.yAxesLabel.append(["Max Relative Error"])
                # set the xAxis Label
                self.xAxesData.append([averageErrorXAxisData])
                # set the yAxis Label
                self.yAxesData.append([averageErrorYAxisData])
                # set the xAxis Label
                self.xAxesLabel.append(["NumberOfBits"])
                # set the yAxes Label
                self.yAxesLabel.append(["Average Relative Error"])


    # function to extract the maxError Analysis values from the fileSystem 
    def extractMaxErrorAnalysisValues(self):
        # read the files from the fileSystem
        maxErrorAnalysisOutput = self.fileSystem.pcSystemMaxErrorAnalysis
        print("MaxErrorAnalysisOutput", maxErrorAnalysisOutput)
        xAxisData = list()
        yAxisData = list()
        # loop through output and also its a two dimentional array
        for maxErrorAnalysisData in maxErrorAnalysisOutput:
            # set the array to the maxErrorAnalysis property it will handle the making of x and y axis for the graph
            maxErrorAnalysisData = maxErrorAnalysisData
            # access the number of bits
            numberOfBits = maxErrorAnalysisData[0]
            # access the maxError value
            maxError = maxErrorAnalysisData[1]
            # add the numberOfBits to xAxesData 
            xAxisData.append(int(numberOfBits))
            #print(self.xAxesData)
            # add the maxError to the yAxis
            yAxisData.append(float(maxError)) 

        return (xAxisData, yAxisData)
    

    # function to extract the maxError Analysis values from the fileSystem 
    def extractAverageErrorAnalysisValues(self):
        #print("ModelName", self.fileSystem.fileConfiguration.modelName)
        # read the files from the fileSystem
        averageErrorAnalysisOutput = self.fileSystem.pcSystemAverageErrorAnalysis
        print("AverageErrorAnalysisOutput", averageErrorAnalysisOutput)
        xAxisData = list()
        yAxisData = list()
        # loop through output and also its a two dimentional array
        for averageErrorAnalysisData in averageErrorAnalysisOutput:
            # set the array to the maxErrorAnalysis property it will handle the making of x and y axis for the graph
            averageErrorAnalysisData = averageErrorAnalysisData
            # access the number of bits
            numberOfBits = averageErrorAnalysisData[0]
            # access the maxError value
            averageError = averageErrorAnalysisData[1]
            # add the numberOfBits to xAxesData 
            xAxisData.append(int(numberOfBits))
            #print(self.xAxesData)
            # add the averageError to the yAxis
            yAxisData.append(float(averageError)) 
        
        return (xAxisData, yAxisData)
    
    
    def __extractValuesToPlotHWSWAverageLikelihoodAnalysisGraph(self):
        # in total there are two analysis 1) maxError 2) averageError
        # extract the hwAverageLikelihoodXAxisData and hwAverageLikelihoodYAxisData
        hwAverageLikelihoodXAxisData, hwAverageLikelihoodYAxisData = self.__extractHWAverageLikelihoodAnalysisValues()
        # extract the swAverageLikelihoodXAxisData and swAverageLikelihoodXAxisData 
        swAverageLikelihoodXAxisData, swAverageLikelihoodYAxisData = self.__extractSWAverageLikelihoodAnalysisValues()
        # access the graphAxes to set the xAxesData and yAxesData
        for graphFigureAxisIndex in range(0,len(self.graphFiguresAxes)):
            graphFigureAxis = self.graphFiguresAxes[graphFigureAxisIndex]
            # check the length of the graphFigureAxis by checking the length of the graphFigureAxis
            if len(graphFigureAxis) > 1:
                # then the figure of maxError and averageError will be merged
                # set the xAxes Label for both the graphs
                self.xAxesData.append([hwAverageLikelihoodXAxisData])
                # set the yAxes Label for both the graphs
                self.yAxesData.append([hwAverageLikelihoodYAxisData,swAverageLikelihoodYAxisData])
                # set the xAxis Label
                self.xAxesLabel.append(["NumberOfBits"])
                # set the yAxes Label
                self.yAxesLabel.append(["Hardware Average Log Likelihood", "Software Average Log Likelihood"])
               

            else:
                # maxError and AverageError will not be merged rather two figures will be generated
                # set the xAxis Label
                self.xAxesData.append([hwAverageLikelihoodXAxisData])
                # set the yAxis Label
                self.yAxesData.append([hwAverageLikelihoodYAxisData])
                # set the xAxis Label
                self.xAxesLabel.append("NumberOfBits")
                # set the yAxes Label
                self.yAxesLabel.append("Hardware Average Likelihood")
                # set the xAxis Label
                self.xAxesData.append([swAverageLikelihoodXAxisData])
                # set the yAxis Label
                self.yAxesData.append([swAverageLikelihoodYAxisData])
                # set the xAxis Label
                self.xAxesLabel.append("NumberOfBits")
                # set the yAxes Label
                self.yAxesLabel.append("Software Average Likelihood")
                

    # function to extract the SW averagelikehood Analysis values from the fileSystem 
    def __extractSWAverageLikelihoodAnalysisValues(self):
        # read the files from the fileSystem
        swLikelihoodAnalysisOutput = self.fileSystem.pcSystemSWAverageLikelihoodAnalysis
        xAxisData = list()
        yAxisData = list()
        # loop through output and also its a two dimentional array
        for swLikelihoodAnalysisData in swLikelihoodAnalysisOutput:
            # set the array to the likelihoodAnalysisData property it will handle the making of x and y axis for the graph
            swAverageLikelihoodAnalysisData = swLikelihoodAnalysisData
            numberOfBits = swAverageLikelihoodAnalysisData[0]
            xAxisData.append(int(numberOfBits))
            # access the _averageLikelihood value
            swAverageLikelihood = swAverageLikelihoodAnalysisData[1]
            # add the averageLikelihood to the yAxis
            #if float(averageLikelihood) != 0.0:
                #averageLikelihood = math.log((1/float(averageLikelihood)),self.decimalBase)
            #print(averageLikelihood)
            #swAverageLikelihood = math.log(float(swAverageLikelihood),self.decimalBase)
            yAxisData.append(float(swAverageLikelihood))
            
        
        return (xAxisData, yAxisData)
    
    
    # function to extract the averagelikehood Analysis values from the fileSystem 
    def __extractHWAverageLikelihoodAnalysisValues(self):
        # read the files from the fileSystem
        hwLikelihoodAnalysisOutput = self.fileSystem.pcSystemHWAverageLikelihoodAnalysis
        xAxisData = list()
        yAxisData = list()
        # loop through output and also its a two dimentional array
        for hwLikelihoodAnalysisData in hwLikelihoodAnalysisOutput:
            # set the array to the likelihoodAnalysisData property it will handle the making of x and y axis for the graph
            hwAverageLikelihoodAnalysisData = hwLikelihoodAnalysisData
            numberOfBits = hwAverageLikelihoodAnalysisData[0]
            xAxisData.append(int(numberOfBits))
            # access the _averageLikelihood value
            hwAverageLikelihood = hwAverageLikelihoodAnalysisData[1]
            # add the averageLikelihood to the yAxis
            #if float(averageLikelihood) != 0.0:
                #averageLikelihood = math.log((1/float(averageLikelihood)),self.decimalBase)
            #print(averageLikelihood)
            #averageLikelihood = math.log((1/float(averageLikelihood)),self.decimalBase)
            if np.isinf(float(hwAverageLikelihood)):
                # access the last element of the array hwAverageLikelihood
                lastElement = hwLikelihoodAnalysisOutput[-1]
                # access the last element hardwareLikelihood
                lastElementHWAverageLikelihood = lastElement[1]
                # multiple the value by 100
                maxHWAverageLikelihood =  (float(lastElementHWAverageLikelihood) *5)
                print("Infinity AverageLikelihood",hwAverageLikelihood)
                print("Last Element AverageLikelihood",maxHWAverageLikelihood)
                # take average of maxHWAverageLikelihood
                maxHWAverageLikelihood = float ((float(lastElementHWAverageLikelihood) + float(maxHWAverageLikelihood)) / 2)
                yAxisData.append(float(maxHWAverageLikelihood))
                continue
            
            #hwAverageLikelihood = math.log(float(hwAverageLikelihood),self.decimalBase)
            yAxisData.append(float(hwAverageLikelihood))
            
        return (xAxisData, yAxisData)

      
    # function to extract the HWMannWhitneyUTestAnalysisValues from the fileSystem 
    def __extractPCSystemHWMannWhitneyUTestAnalysisValues(self):
        # read the files from the fileSystem
        pcSystemHWMannWhitneyUTestAnalysisOutput = self.fileSystem.pcSystemMannWhitneyUTestAnalysis
        xAxisData = list()
        yAxisData = list()
        # loop through output and also its a two dimentional array
        for pcSystemHWMannWhitneyUTestAnalysisData in pcSystemHWMannWhitneyUTestAnalysisOutput:
            numberOfBits = pcSystemHWMannWhitneyUTestAnalysisData[0]
            xAxisData.append(int(numberOfBits))
            # access the _averageLikelihood value
            mannWhitneyUTest = pcSystemHWMannWhitneyUTestAnalysisData[1]
            # add the averageLikelihood to the yAxis
            yAxisData.append(float(mannWhitneyUTest))
            
        return (xAxisData, yAxisData)
        
  
    def __plotGraph(self):
        # as there are subplots, we need to loop through to plot the subplots in a given graph figure
        for figureIndex in range (0, self.numberOfFigures):
            figure = self.graphFigures[figureIndex]
            figure.suptitle = self.graphTitle
            # access the graphFigure axes, that is also an array
            xyAxis = self.graphFiguresAxes[figureIndex]
            # check the xyAxis length
            if len(xyAxis) == 1:
                axis = self.graphFiguresAxes[figureIndex][0]
                # then we have one axis to control control both xAxis and yAxis
                # access the xAxis from xAxes
                xAxis = self.xAxesData[figureIndex][0]
                #print(xAxis)
                # access the yAxis from yAxes
                yAxis = self.yAxesData[figureIndex][0]
                # access and set the xAxis and yAxis labels
                axis.set_xlabel(self.xAxesLabel[figureIndex][0]) 
                axis.set_ylabel(self.yAxesLabel[figureIndex][0])
                if figureIndex == 0:
                    axis.set_yscale('log')
                    
                # plot the axis
                axis.plot(xAxis, yAxis, color = 'red')
                # show grid for the subplot
                axis.xaxis.grid(color = 'green', linestyle = '--', linewidth = 0.5)
                axis.yaxis.grid(color = 'green', linestyle = '--', linewidth = 0.5)
            
            elif len(xyAxis) > 1:

                # access the first axis to set the first x and y axis with data
                axis = self.graphFiguresAxes[figureIndex][0]
                # Y axis have two data to be plotted using twinx
                # then we have one axis to control control both xAxis and yAxis
                # access the xAxis from xAxes
                xAxis = self.xAxesData[figureIndex][0]
                #print(xAxis)
                # access the yAxis from yAxes
                yAxis = self.yAxesData[figureIndex][0]
                # access and set the xAxis and yAxis labels
                axis.set_xlabel(self.xAxesLabel[figureIndex][0]) 
                axis.set_ylabel(self.yAxesLabel[figureIndex][0])
                #axis.set_yscale('log') 
                #if figureIndex == 0:
                    #axis.set_yscale('log') 

                # plot the axis
                axis.plot(xAxis, yAxis, color = 'red', marker='o')
                #axis.set_ylim(top=0)
                # show grid for the subplot
                axis.xaxis.grid(color = 'green', linestyle = '--', linewidth = 0.5)
                axis.yaxis.grid(color = 'green', linestyle = '--', linewidth = 0.5)

                # set the second yaxis
                twinAxes = self.graphFiguresAxes[figureIndex][1]
                # check the length of the twinAxis
                twinAxis = twinAxes[0]
                # access the yAxis from yAxes
                twinYAxis = self.yAxesData[figureIndex][1]
                # access the twinYAxis with yAxesLabel
                twinAxis.set_ylabel(self.yAxesLabel[figureIndex][1])
                #twinAxis.set_yscale('log') 
                # plot the axis
                twinAxis.plot(xAxis, twinYAxis, color = 'black', linestyle='dotted', marker='x')
                #twinAxis.set_ylim(top=0)

        plt.show()
        
        
    def __plotHWSWAverageLikelihoodGraph(self):
        hwxAxis, hwyAxis = self.__extractHWAverageLikelihoodAnalysisValues()
        swxAxis, swyAxis = self.__extractSWAverageLikelihoodAnalysisValues()
        print(hwxAxis, swyAxis,hwyAxis)
        figure, axis = plt.subplots()
        axis.plot(hwxAxis, hwyAxis, color='red', label='HW ED', linewidth=1, marker='o')
        axis.plot(hwxAxis, swyAxis, color='black', linestyle='dotted', linewidth=1,label='SW ED', marker='o')
        plt.xlim(xmin= 0, xmax=40)
        #plt.ylim(ymax=0.0025)
        axis.set_yscale('log') 
        plt.title("Float PCSystem")
        axis.set_xlabel("Mantissa Bits")
        axis.set_ylabel("Eucilidean Distance")
        axis.legend(frameon=True, loc='upper center', ncol=2)
        # plot the axis
        axis.grid(color = 'green', linestyle = '--', linewidth = 0.5)
        plt.show()
       


    def plotAvgErrorAnalysisGraph(self):
        if self.fixedSystemAvgErrorValues != None:
            avgErrorXAxisData = self.fixedSystemAvgErrorValues[0]
        elif self.floatSystemAvgErrorValues != None:
            avgErrorXAxisData = self.floatSystemAvgErrorValues[0]
        elif self.positSystemAvgErrorValues != None:
            avgErrorXAxisData = self.positSystemAvgErrorValues[0]
        
        
        figure, axis = plt.subplots()

        if self.fixedSystemAvgErrorValues != None:
            # extract the fixedSystem avg error values
            fixedSystemAvgErrorValue = self.fixedSystemAvgErrorValues[1]
            axis.plot(avgErrorXAxisData, fixedSystemAvgErrorValue, color='red', label='Fixed', linewidth=1,marker='o')

        if self.floatSystemAvgErrorValues != None:
            # extract the floatSystem avg error values
            floatSystemAvgErrorValues = self.floatSystemAvgErrorValues[1]
            axis.plot(avgErrorXAxisData, floatSystemAvgErrorValues, color='black',  linewidth=1, label='Float', linestyle='dotted', marker='o')

        if self.positSystemAvgErrorValues != None:
            # extract the posit avg error values
            positSystemAvgErrorValues = self.positSystemAvgErrorValues[1]
            axis.plot(avgErrorXAxisData, positSystemAvgErrorValues, color='blue',  linewidth=1, label='Posit', linestyle='dotted', marker='o')

        axis.set_yscale('log')
        plt.ylim(ymin=0)
        self.graphTitle = self.graphTitle + " " + "PCSystem Avg Error"
        plt.title(self.graphTitle)
        plt.xlim(xmin= 20, xmax=60)
        #plt.xlim(xmin= 0)
        axis.set_xlabel("Total Number Of Bits")
        axis.set_ylabel("Avg Error")
        axis.legend(frameon=True, loc='best', ncol=2)
        # plot the axis
        axis.grid(color = 'green', linestyle = '--', linewidth = 0.5)
        plt.show()

            
        
    def plotMaxErrorAnalysisGraph(self):
        if self.fixedSystemMaxErrorValues != None:
            maxErrorXAxisData = self.fixedSystemMaxErrorValues[0]
        elif self.floatSystemMaxErrorValues != None:
            maxErrorXAxisData = self.floatSystemMaxErrorValues[0]
        elif self.positSystemMaxErrorValues != None:
            maxErrorXAxisData = self.positSystemMaxErrorValues[0]
        
        figure, axis = plt.subplots()

        if self.fixedSystemMaxErrorValues != None:
            # extract the fixedSystem max error values
            fixedSystemMaxErrorValues = self.fixedSystemMaxErrorValues[1]
            axis.plot(maxErrorXAxisData, fixedSystemMaxErrorValues, color='red', label='Fixed', linewidth=1,marker='o')
        if self.floatSystemMaxErrorValues != None:
            # extract the floatSystem max error values
            floatSystemMaxErrorValues = self.floatSystemMaxErrorValues[1]
            axis.plot(maxErrorXAxisData, floatSystemMaxErrorValues, color='black',  linewidth=1, label='Float', linestyle='dotted', marker='o')
        if self.floatSystemMaxErrorValues != None:
            # extract the posit max error values
            positSystemMaxErrorValues = self.positSystemMaxErrorValues[1]
            axis.plot(maxErrorXAxisData, positSystemMaxErrorValues, color='blue',  linewidth=1, label='Posit', linestyle='dotted', marker='*')

        axis.set_yscale('log') 
        plt.ylim(ymin=0)
        self.graphTitle = self.graphTitle + " " + "PCSystem Max Error"
        plt.title(self.graphTitle)
        plt.xlim(xmin= 10, xmax=50)
        #plt.xlim(xmin= 0)
        axis.set_xlabel("Total Number Of Bits")
        axis.set_ylabel("Max Error")
        axis.legend(frameon=True, loc='best', ncol=2)
        # plot the axis
        axis.grid(color = 'green', linestyle = '--', linewidth = 0.5)
        plt.show()

        
    
    def __plotMaxAverageErrorAnalysisGraph(self):
        # extract the fixedSystem max error values
        fixedSystemMaxErrorValues = self.fixedSystemMaxErrorValues[1]
        # extract the fixedSystem avg error values
        fixedSystemAvgErrorValue = self.fixedSystemAvgErrorValues[1]
        # extract the floatSystem max error values
        floatSystemMaxErrorValues = self.floatSystemMaxErrorValues[1]
        # extract the floatSystem avg error values
        floatSystemAvgErrorValues = self.floatSystemAvgErrorValues[1]
        # extract the posit max error values
        positSystemMaxErrorValues = self.positSystemMaxErrorValues[1]
        # extract the posit avg error values
        positSystemAvgErrorValues = self.positSystemAvgErrorValues[1]

        figure, axis = plt.subplots()
        axis.plot(maxErrroXAxisData, fixedSystemMaxErrorValues, color='red', label='MaxError', linewidth=1,marker='o')
        axis.plot(maxErrroXAxisData, floatSystemMaxErrorValues, color='black',  linewidth=1, label='MaxError', linestyle='dotted', marker='o')
        axis.plot(maxErrroXAxisData, positSystemMaxErrorValues, color='green',  linewidth=1, label='MaxError', linestyle='dotted', marker='o')

        axis.set_yscale('log') 
        plt.title("PCSystem")
        plt.ylim(ymin=0)
        plt.xlim(xmin= 0)
        #plt.xlim(xmin= 0, xmax=200)
        axis.set_xlabel("Total Number Of Bits")
        axis.set_ylabel("Max Error")
        axis.legend(frameon=True, loc='best', ncol=2)
        # plot the axis
        axis.grid(color = 'green', linestyle = '--', linewidth = 0.5)
        plt.show()
        
        
    def __plotHWMannWhitneyUTestAnalysisAverageGraph(self):
        hwxAxis, hwyAxis = self.__extractPCSystemHWMannWhitneyUTestAnalysisValues()
        swxAxis, swyAxis = self.__extractSWAverageLikelihoodAnalysisValues()
        #print(hwxAxis, swyAxis,hwyAxis)
        figure, axis = plt.subplots()
        axis.plot(hwxAxis, hwyAxis, color='red', label='HW ED', linewidth=1, marker='o')
        #axis.plot(hwxAxis, swyAxis, color='black', linestyle='dotted', linewidth=1,label='SW ED', marker='o')
        plt.xlim(xmin= 0, xmax=60)
        #plt.ylim(ymax=0.0025)
        #axis.set_yscale('log') 
        plt.title("Fixed PCSystem")
        axis.set_xlabel("Number Of Bits")
        axis.set_ylabel("MannWhitney UTest Pvalue")
        axis.legend(frameon=True, loc='best', ncol=2)
        # plot the axis
        axis.grid(color = 'green', linestyle = '--', linewidth = 0.5)
        plt.show()

    def configure(self):
        pass


    def connect(self):
        pass

    def main(self):
        #self.__extractValuesToPlotErrorAnalysisGraph()
        # clear xAxesData and yAxesData
        #self.xAxesData = None
        #self.yAxesData = None
        #self.__extractValuesToPlotHWSWAverageLikelihoodAnalysisGraph()
        # now plot the analysis Graph
        #self.__plotGraph()
        #self.__plotHWSWAverageLikelihoodGraph()
        #self.__plotHWMannWhitneyUTestAnalysisAverageGraph()
        self.__plotMaxAverageErrorAnalysisGraph()
    
    def run(self):
        self.main()
    
