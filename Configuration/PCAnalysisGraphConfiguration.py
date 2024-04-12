#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:25:27 2022

@author: Karthekeyan Periasamy

"""

import math
import matplotlib.pyplot as plt

class PCAnalysisGraphConfiguration():
    """
    PCAnalysisGraphConfiguration object and member variables are used to extend the existing attributes of the PCAnalysisGraph 
    """
    
    def __init__(self):
        """
        Init function to have declaration and initialisation of necessary variables.
        For now, we do have the concept of lazy loading for some of the member variables.Custom getters and setters of member variables support object lazy loading      
        """
        

        """
        Properties
        1. self.graphFiguresAxes stores the data in the form of dict to configure the xAxis and yAxis of a given figure to be represented in the x or y axis of the a figure in PCAnalysisGraph
        2. self._graphFigures stores the number of figures needed for the analysis graph object
        """
        self._numberOfGraphFigures = 0
        self._graphFiguresYAxes = None
        self.graphFiguresAxes = list()
        self.graphFigures = None
        # no subplots and figures are not configured, so when simpleGraph is set, numberOfFigures will be ignored
        self.simpleGraph = False

    
    """
    Custom getters and setters
    """

    @property
    def graphFiguresYAxes(self):
        return self._graphFiguresYAxes

    @graphFiguresYAxes.setter
    def graphFiguresYAxes(self,value):
        self._graphFiguresYAxes = value

    @property
    def graphFigures(self):
        return self._graphFigures

    @graphFigures.setter
    def graphFigures(self,value):
        self._graphFigures = value
        print(self._graphFigures)
                       
    @property
    def numberOfGraphFigures(self):
        return self._numberOfGraphFigures

    @numberOfGraphFigures.setter
    def numberOfGraphFigures(self,value):
        self._numberOfGraphFigures = value
        print("NumberOfGraphFigures:", self._numberOfGraphFigures)
        self.__generateGraphFiguresAndGraphAxes()


    def __generateGraphFiguresAndGraphAxes(self):
        # make an array object of graph figure
        graphFigures = list()
        # make an array object of graph axes
        graphFiguresAxes = list()
        # ignore the subplots
        # loop through the gaphFigures number and create multiple graphFigures object
        for graphFigureIndex in range (0, self.numberOfGraphFigures):
            # generate graph figure and axis accordingly
            graphFigure = None
            graphFigure, graphAxis = plt.subplots()
                      
            if self.numberOfGraphFigures == len(self.graphFiguresYAxes):
                # access the yaxis for a figure using the figure index
                numberOfYAxis = self.graphFiguresYAxes[graphFigureIndex][1]
                
                if numberOfYAxis > 1:
                    # loop through the numberOfYAxis
                    graphTwinAxes = list()
                    for yAxisIndex in range(0,numberOfYAxis-1):
                        # make twin axes
                        graphTwinAxis = graphAxis.twinx()
                        graphTwinAxes.append(graphTwinAxis)
                        
                    graphFiguresAxes.append([graphAxis,graphTwinAxes])

                elif numberOfYAxis == 1:
                    graphFiguresAxes.append([graphAxis])
                    
            graphFigures.append(graphFigure)

        self.graphFigures = graphFigures
        self.graphFiguresAxes = graphFiguresAxes
    

    def __generateGraphFiguresAndGraphAxes(self):
        # make an array object of graph figure
        graphFigures = list()
        # make an array object of graph axes
        graphFiguresAxes = list()
        # ignore the subplots
        # loop through the gaphFigures number and create multiple graphFigures object
        for graphFigureIndex in range (0, self.numberOfGraphFigures):
            # generate graph figure and axis accordingly
            graphFigure = None
            graphFigure, graphAxis = plt.subplots()
                      
            if self.numberOfGraphFigures == len(self.graphFiguresYAxes):
                # access the yaxis for a figure using the figure index
                numberOfYAxis = self.graphFiguresYAxes[graphFigureIndex][1]
                
                if numberOfYAxis > 1:
                    # loop through the numberOfYAxis
                    graphTwinAxes = list()
                    for yAxisIndex in range(0,numberOfYAxis-1):
                        # make twin axes
                        graphTwinAxis = graphAxis.twinx()
                        graphTwinAxes.append(graphTwinAxis)
                        
                    graphFiguresAxes.append([graphAxis,graphTwinAxes])

                elif numberOfYAxis == 1:
                    graphFiguresAxes.append([graphAxis])
                    
            graphFigures.append(graphFigure)

        self.graphFigures = graphFigures
        self.graphFiguresAxes = graphFiguresAxes

    def main(self):
        pass
            
    def run(self):
        self.main()
    
