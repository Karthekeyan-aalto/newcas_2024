#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:49:40 2022

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
    # set the configuration details of the filesystem
    pcSystem.configurationDetailsOfFileSystemPackage = {"ResetErrorAnalysisFile":0}
    # configure process data  package
    pcSystem.configureProcessDataPackage()
    # process the data
    pcSystem.processIOData()

    # configure the PCSystem object
    # set the processData object to the PCSystem
    # once the PCSystem gets the processData command
    # it uses its information to process the data and store the data in the respective location of the filesystem
    #from PCSystemIOData import PCSystemIOData
    #processIOData = PCSystemIOData()
    #processIOData.resetPCSystemErrorAnalysisFile = 0
    #processIOData.run()
    


