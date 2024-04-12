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
    from PCSystem import PCSystem
    # intialise the PCSystem object
    pcSystem = PCSystem()
    # configure the system
    # set the configuration details of the filesystem
    #pcSystem.configurationDetailsOfGraphPackage = {"PCSystemInfo":{"SystemType":"AC", "NumberSystems":["Fixed","Float","Posit"], "Model":"nltcs","Graph":"ErrorGraph"}}
    pcSystem.configurationDetailsOfGraphPackage = {"PCSystemInfo":{"SystemType":"SPN", "NumberSystems":["Float","Posit"], "Model":"dna80","Graph":"ErrorGraph"}}
    # configure graph  package
    pcSystem.configureGraphPackage()
    # process the data
    pcSystem.plotPCSystemGraph()
    

    #from PCSystemGraph import PCSystemGraph
    #graph = PCSystemGraph()
    #graph.graphFiguresYAxes = [[1,2]]
    #graph.numberOfFigures = 1 
    #graph.run()
