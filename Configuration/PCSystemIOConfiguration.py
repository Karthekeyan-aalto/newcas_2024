#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:49 2022

@author: Karthekeyan Periasamy
"""

import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)',text)]

class PCSystemIOConfiguration():
    
    def __init__(self):
        
        """
        # Start: Directory details
        """
        # a list to store the PCSystem ports
        self._ports = None
        # test data to generate PCSystem IO pattern, retrieved from the fileSystem
        self._testData = list()
        # IO patterns that will be used by the file System
        self.pattern = list()
        # a list to store the pcSystem port names
        self.portNames = list()
        # the port variables of the pcSystem is 
        self.numberOfPortVariables = 0
        # PCSystem model for now is of two types 0) AC 1) SPN
        self._systemType = 0
        # the portLetter for the PCSystem ports
        self.portLetter = "v"
        # port variable list, that will contain the portVariable for a given systemType
        self.pcSystemPortVariables = list()
        # port variable and categories map
        self.pcSystemPortVariablesAndCategories = dict()
        # portVariable categories
        self._portVariableCategories = None
        # port variable category startNumber
        self.portVariableCategoryStartNumber = 0
        # pcACIOPattern length required to manipulate the IOpattern
        self._pcSystemIOPatternLength = None
    
    
    @property
    def testData(self):
        return self._testData

    @testData.setter
    def testData(self,value):
        self._testData = value
        # generate the IO pattern for the ports
        # print the testData
        #print(self._testData)
        self.__generateIOPattern()
        
    
    @property
    def portVariableCategories(self):
        return self._portVariableCategories

    @portVariableCategories.setter
    def portVariableCategories(self,value):
        self._portVariableCategories = value
        # set the numberOfportVariables
        self.numberOfPortVariables = len(self._portVariableCategories)
    
    # custom setters and getters 
    @property
    def systemType(self):
        return self._systemType

    @systemType.setter
    def systemType(self,value):
        # set the value of the systemType
        self._systemType = value 
    
    @property
    def ports(self):
        return self._ports

    @ports.setter
    def ports(self,value):
        # set the ports
        self._ports = value
        # set the sortedPorts
        self._ports = self.sortPorts()
    
    
    
    @property
    def pcSystemIOPatternLength(self):
        """
        Property Getter to get the IOPatternList size. 
        The size is used the generateACIOPattern to generate a list and manipulate it to form the final IOPattern
        The final IOPattern is store in variable named self.pattern

        Returns
        -------
        an integer that will define the size of the IOPattern for one test data
        """

        if self._pcSystemIOPatternLength == None:
            ioPatternLength = 0
            for portVarialeCategory in self.portVariableCategories:
                # access the portVariableCategory as integer
                ioPatternLength = ioPatternLength + int(portVarialeCategory)
                #print(f'{ioPatternLength}')
                # check the length of the portNames
                #portNameLength = len(self.portNames)
                #print(f'{portNameLength}') 
            self._pcSystemIOPatternLength = ioPatternLength
                
        return self._pcSystemIOPatternLength
    
    @pcSystemIOPatternLength.setter
    def pcSystemIOPatternLength(self,value):
        # set the ports
        self._pcSystemIOPatternLength = value
        
   
    def __generateACPortVariableCategoryMap(self):
       # access the length of the pcSystemPortCategories
        # it help form the portVariables in an array
        for portIndex in range(0, len(self.portVariableCategories)):
            # form an array of strings by appending the portLetter and the portIndex
            portVariable = self.portLetter + str(portIndex)
            self.pcSystemPortVariables.append(portVariable)
            # set the categories and portVariable map
            self.pcSystemPortVariablesAndCategories[portVariable] = self.portVariableCategories[portIndex]
            
    
    def __generateSPNPortVariableCategoryMap(self):
        """
        Function to create a dictionary, keys being the category name and the values being the associated category representation that forms the portName
        """
        # access the length of the pcSystemPortCategories
        # it help form the portVariables in an array
        for portIndex in range(0, len(self.portVariableCategories)):
            # form an array of strings by appending the portLetter and the portIndex
            portVariable = self.portLetter + str(portIndex)
            self.pcSystemPortVariables.append(portVariable)
            # set the categories and portVariable map
            self.pcSystemPortVariablesAndCategories[portVariable] = self.portVariableCategories[portIndex]
            
        # generate the PCSystemPortIOconfiguration
        #print("PCSystemPortVariablesAndCategories",self.pcSystemPortVariablesAndCategories)

    def __generateIOPattern(self):
        # check for the system Type as based on the systemType form the port variable IO pattern
        if self.systemType == 0:
            #  generate AC port configuration
            self.__generateACIOPattern()
        elif self.systemType == 1:
            # call the pcSystem SPN to generate port configuration
            self.__generateSPNIOPattern()
    
   
    def __generateACIOPattern(self):
        """
        Funciton to generate IO pattern for the PCSystem containinig the AC model
        In general, SPN or AC model has portVariableCategories and its associated names dependent on the dataset

        Returns
        -------
        None.

        """
        # access all the test data
        pcSystemTestDataSet = self.testData
        counter = 0
        # loop through the two dimensional test data
        for pcSystemTestData in pcSystemTestDataSet:
            # portIOPattern list
            portIOPattern = ["0"] * self.pcSystemIOPatternLength
            counter = counter + 1
            currentPortVariableIndex = 0
            # set the pcSystemTestData to a locatlVariable
            pcSystemTestDataList = pcSystemTestData
            for pcSystemTestDataIndex, pcSystemTestData in enumerate(pcSystemTestDataList):
                # print the testData Index and pcSystemTestData
                #print("PCSystemTestDataIndex", pcSystemTestDataIndex)
                # access the index and access the associated index portVariable category
                portVariableCategory = self.portVariableCategories[pcSystemTestDataIndex]
                #print("CurrentPortVariableCategory", portVariableCategory)
                # change the string to an integer
                portVariableCategory = int(portVariableCategory)
                activeCategory = int(pcSystemTestData)
                # if the portVariableCategory is 2, the sorting of variables will be different so
                if portVariableCategory == 2:
                     # check the activeCategory from th e testdata
                     if activeCategory == 0:
                         #print("TestDataActiveCategory", pcSystemTestData)
                         portVariableInteger = int(pcSystemTestDataIndex) + 1
                         #print("PortVariableInteger", portVariableInteger)
                         # it means portName with "v" "b" is active and "0" means its "1" in the portnames
                         portName = self.portLetter + "b" + str(portVariableInteger)
                         # find the index of the portName
                         portNameIndex = self.portNames.index(portName)
                         # print the portNameIndex
                         #print("PortNameIndex", portNameIndex)
                         #print("PortName", portName)
                         #print("OriginalPortIOPattern", portIOPattern)
                         # add the value to 1 to the portNameIndex
                         portIOPattern[portNameIndex] = "1"
                         #print("UpdatedPortIOPattern", portIOPattern)
                         
                         portName = self.portLetter + str(portVariableInteger)
                         # find the index of the portName
                         portNameIndex = self.portNames.index(portName)
                         # print the portNameIndex
                         #print("PortNameIndex", portNameIndex)
                         #print("PortName", portName)
                         # add the value to 1 to the portNameIndex
                         #print("OriginalPortIOPattern", portIOPattern)
                         portIOPattern[portNameIndex] = "0"
                         #print("UpdatedPortIOPattern", portIOPattern) 
                         
                     elif activeCategory == 1:               
                         #print("TestDataActiveCategory", pcSystemTestData)
                         portVariableInteger = int(pcSystemTestDataIndex) + 1
                         #print("PortVariableInteger", portVariableInteger)                    
                         # it means portName with "v" and "1" means its "2" in the portnames
                         portName = self.portLetter + str(portVariableInteger)
                         # find the index of the portName
                         portNameIndex = self.portNames.index(portName)
                         # print the portNameIndex
                         #print("PortNameIndex", portNameIndex)
                         #print("PortName", portName)
                         # add the value to 1 to the portNameIndex
                         #print("OriginalPortIOPattern", portIOPattern)
                         portIOPattern[portNameIndex] = "1"
                         #print("UpdatedPortIOPattern", portIOPattern)
                         
                         portName = self.portLetter + "b" + str(portVariableInteger)
                         # find the index of the portName
                         portNameIndex = self.portNames.index(portName)
                         # print the portNameIndex
                         #print("PortNameIndex", portNameIndex)
                         #print("PortName", portName)
                         #print("OriginalPortIOPattern", portIOPattern)
                         # add the value to 1 to the portNameIndex
                         portIOPattern[portNameIndex] = "0"
                         #print("UpdatedPortIOPattern", portIOPattern)

                else:
                    # if the portVariableCategory is greater than 2, then variables will be arranged differently
                    # Variables will be arranged like v1, v2, v3 and so on
                    # loop through the range of portVariableCategory
                    for portVariableCategoryIndex in range(0,int(portVariableCategory)):
                        # print the portVariableCategoryIndex
                        #print("PortVariableCategoryIndex",portVariableCategoryIndex)
                        #print("PCSystemTestData",(int(pcSystemTestData) - self.categoryStartingPoint))
                        if portVariableCategoryIndex == (int(pcSystemTestData) - self.categoryStartingPoint):
                            #print("PCSystemTestData",pcSystemTestData)
                            #print("OriginalPortIOPattern", portIOPattern)
                            portIOPattern[currentPortVariableIndex+portVariableCategoryIndex] = "1"
                            #print("UpdatedPortIOPattern", portIOPattern)
                        else:
                            
                            #print("PCSystemTestData",pcSystemTestData)
                            #print("PCSystemTestDataIndex", pcSystemTestDataIndex)
                            #print("PortVariableCategoryIndex", portVariableCategoryIndex) 
                            #print("OriginalPortIOPattern", portIOPattern)
                            portIOPattern[currentPortVariableIndex+portVariableCategoryIndex] = "0"
                            #print("UpdatedPortIOPattern", portIOPattern)
   
                    
                    currentPortVariableIndex = int(portVariableCategory) - 1
                    
                    
            self.pattern.append(portIOPattern)
            #print("UpdatedLength", len(self.pattern))
            #print("UpdatedCounter", counter)
            
        #print("Finalcounter", counter)
        #print("FinalLength", len(self.pattern))
        #print("IOPattern", self.pattern)

    def __generateSPNIOPattern(self):
        """
        # access the number of active categories and loop through
        # now we have the access to a single category access the index of the element
        # check the category number and also access the total number of categories for that variable
        # loop through the total categories and set "1" only to the category that needs to be active. It is based on the index
        """
        # access the number of active categories and loop through
        for pcSystemSPNPortVariableActiveCategoryDataSet in self.testData:
            # hold IO pattern for the given DataSet
            pcSystemIOPatternForADataSet = list()
            #print("PCSystemSPNPortVariableActiveCategoryDataSet",pcSystemSPNPortVariableActiveCategoryDataSet)
            for pcSystemSPNPortVariableActiveCategoryIndex, pcSystemSPNPortVariableActiveCategoryNumber in enumerate(pcSystemSPNPortVariableActiveCategoryDataSet):
                # hold IO pattern for the given DataSet
                # pcSystemIOPatternForADataSet = list()
                #print("PCSystemSPNPortVariableActiveCategoryNumber",pcSystemSPNPortVariableActiveCategoryNumber)
                #print("PCSystemSPNPortVariableActiveCategoryIndex",pcSystemSPNPortVariableActiveCategoryIndex)
                # check the category number and also access the total number of categories for that variable
                totalPCSystemSPNPortVariableCategories = self.portVariableCategories[pcSystemSPNPortVariableActiveCategoryIndex]
                #print("TotalPCSystemSPNPortVariableCategories",totalPCSystemSPNPortVariableCategories)
                # loop through the total categories and set "1" only to the category that needs to be active. It is based on the index
                for pcSystemSPNPortVariableCategoryIndex in range(0, int(totalPCSystemSPNPortVariableCategories)):
                    #print("PCSystemSPNPortVariableCategoryIndex",pcSystemSPNPortVariableCategoryIndex)
                    if pcSystemSPNPortVariableCategoryIndex == int(pcSystemSPNPortVariableActiveCategoryNumber)-(self.portVariableCategoryStartNumber):
                        # set the respective index of list with "1"
                        pcSystemIOPatternForADataSet.append("1")
                        
                    else:
                        # set the respective index of list with "0" string
                        pcSystemIOPatternForADataSet.append("0")
                       
            self.pattern.append(pcSystemIOPatternForADataSet)
                      
        
        #print("PCSystemSPNIOPattern",self.pcSystemIOPattern)


    def sortPorts(self):
        """
        Function to sort the pcsystem ports based on the number in the names of the ports
        1. No parameters are given as everything in this is assumed to be of the hardware DUT form
        # First, access the name of the exisitng PCSystem ports, then use it to sort the portNames
        # use the sortedPortNames to sort the pcSystem ports object list and reassign back to the original self.pcSystemPorts
        Return: the sorted list of the PCSystem ports
        """
        # new systemPort list which will contain the sortedPCSystemPorts list
        ports = list()
        #print("OriginalPCSystemPorts",self.ports)
        for port in self.ports:
            self.portNames.append(port.name)
        self.portNames.sort(key=natural_keys)

        for portName in self.portNames:
            for port in self.ports:
                if port.name == portName:
                    ports.append(port)
                    break

        #print("PCSystemPortNames",self.portNames)
        #print("UpdatedPCSystemPorts",pcSystemPorts)
        # assign the updatedPCSystemPorts
        self._ports = ports
        #print("UpdatedPCSystemPorts",self._ports)

        #check whether the IOpattern length and the port length are same or not
        if len(self.pattern) == len(self.portNames):
            print("PCSystemPorts and generated PCSystemIOPattern are same")
        else:
            assert "PCSystemPorts and generated PCSystemIOPattern are not same"
        return self.ports 
