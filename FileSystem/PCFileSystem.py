#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:17:30 2022

@author: Karthekeyan Periasamy
"""

from Configuration.PCFileConfiguration import PCFileConfiguration
from Configuration.PCSystemVHDLConfiguration import PCSystemVHDLConfiguration
from Operations.ProductNode import ProductNode
from Operations.SumNode import SumNode
from NumberSystemPackages.POSITConverter.posit_converter import PositConverter
import itertools
import os
import csv
import openpyxl
import pandas as pd
import json
import shutil


class PCFileSystem():
    
    def __init__(self):
         
        """
        Properties to handle the files
        1. A PCSytem needs PCFileSystem to manage access, create different files
        2. The PCFileSystem access PCFileConfiguration to modify and store data and files at the said location
        """
        self.fileConfiguration = PCFileConfiguration()
        self._pcSystemModel = None

        """
        Properties to handle VHDL configuration of PCs
        """
        self.pcSystemVHDLConfiguration = PCSystemVHDLConfiguration()
                
        """
        Properties set by PCSystem to write to the PCFileSystem
        """
        # pcSystem SumNode name
        self._pcSystemSumNodeName = None
        # pcSystem ProductNode name
        self._pcSystemProductNodeName = None

        # the output port of the system
        self._pcSystemOutputPort = None
        # the total available pcSystemPorts
        self.pcSystemPorts = None
        # the pcSystemNumbersystem, it is used to write correct and necessary content to the files based on the numberSystem type of the PCSystem
        self._pcSystemNumberSystem = None
        # the total available pcSystemArithmeticNodes
        self._pcSystemArithmeticNodes = None
        # pcSystemIOPattern
        self.pcSystemIOPattern = None
        # pcSystemType
        self._pcSystemType = 0
        # _pcSystemTestData
        self._pcSystemTestData = None
        # pcSystemModelMetaData a two dimensional array that holds the port variable categories and category start number
        self._pcSystemModelMetaData = None
        # pcSystemInfo
        self.pcSystemInfo = None
        # pcSystemDecimalOutput property
        self._pcSystemDecimalOutput = None
        # self.pcSystemHWOutput property
        self._pcSystemHWOutput = None
        # self.pcSystemSWOutput property
        self._pcSystemSWOutput = None
        # property to store the pcSystemMaxError
        self._pcSystemMaxErrorAnalysis = None
        # property to store the pcSystemHWAverageLikelihoodAnalysis
        self._pcSystemHWAverageLikelihoodAnalysis = None
        # property to store the pcSystemHWAverageLikelihoodAnalysis
        self._pcSystemSWAverageLikelihoodAnalysis = None
        # property to store the pcSystemAverageError
        self._pcSystemAverageErrorAnalysis = None
        # property to store the pcSystemManWhitneyUTestAnalysis
        self._pcSystemMannWhitneyUTestAnalysis = None

        """
        PCSystem Details
        """
        self.pcSystemNumberOfBits = 0
        self.pcSystemEsBits = 0
        self.pcSystemMantissaBits = 0

        """
        Properties set by PCSystemIODataProcessing to write to the PCFileSystem
        """
        # if the reset flag is to 0, we need to write to the next line of the existing file
        # else, we can rewrite the file
        self.resetPCSystemErrorAnalysisFile = 0


        """
        Properties to be used while writing or reading a file using the fileName
        1. These properties would be common to the fileSystem, can be set from other modules too.
        """
        self.writeMode = 0
        self.readMode = 0
        self.dataToWrite = None
        self._pcSystemWriteData = None
        self.dataToRead = None
        self.fileToWriteOn = None
        # there are two writeData type 1) Array 2) Dictionary
        # if Dictionary, we need to have the keys in writeDataKeys and there are only two keys are supported
        self.writeDataKeys = list()
        self.writeDataType = 0
        self.fileToReadFrom = None

    """
    Custom getters and setters
    """
    
    @property
    def pcSystemOutputPort(self):
        return self._pcSystemOutputPort

       
    
    @pcSystemOutputPort.setter
    def pcSystemOutputPort(self,value):
        # sort the given ports
        self._pcSystemOutputPort = value
        #print(self._ports)
        # set the numberOfBits and exponentBits to the VHDLConfiguration object
        self.pcSystemVHDLConfiguration.numberOfBits = self._pcSystemOutputPort.numberOfBits
        # print the exponentBits
        #print("The PCSystemOutputPort exponent bits:", self._pcSystemOutputPort.exponentBits)
        # set the exponentBits to the VHDLConfiguration object
        self.pcSystemVHDLConfiguration.exponentBits = self._pcSystemOutputPort.exponentBits
        # set the mantissaBits to the VHDLConfiguration object
        self.pcSystemVHDLConfiguration.mantissaBits = self._pcSystemOutputPort.mantissaBits
        # set the mantissaBits to the VHDLConfiguration object
        self.pcSystemVHDLConfiguration.esBits = self._pcSystemOutputPort.esBits
        # print the number of bits
        #print("The PCSystemOutputPort number of bits:", self._pcSystemOutputPort.numberOfBits)
    

    @property
    def pcSystemNumberSystem(self):
        return self._pcSystemNumberSystem

       
    
    @pcSystemNumberSystem.setter
    def pcSystemNumberSystem(self,value):
        # sort the given ports
        self._pcSystemNumberSystem = value
        self.fileConfiguration.pcSystemNumberSystem = self._pcSystemNumberSystem
        print("PCSystemNumberSystemFolderName", self.fileConfiguration.pcSystemNumberSystemFolderName)

                 

    @property
    def pcSystemArithmeticNodes(self):
        return self._pcSystemArithmeticNodes

    
    @pcSystemArithmeticNodes.setter
    def pcSystemArithmeticNodes(self,value):
        # sort the given ports
        self._pcSystemArithmeticNodes = value
        # set the pcSystemNumberOfBits
        self.pcSystemNumberOfBits = self._pcSystemArithmeticNodes[0].numberOfBits
        # set the pcSystemEsBits
        self.pcSystemEsBits = self._pcSystemArithmeticNodes[0].esBits
                

    @property
    def pcSystemType(self):
        return self._pcSystemType

       
    @pcSystemType.setter
    def pcSystemType(self,value):
        # sort the given ports
        self._pcSystemType = value
        # set the file configuration object with the systemType
        self.fileConfiguration.pcModelType = self._pcSystemType
    
       

    @property
    def pcSystemModel(self):
        return self._pcSystemModel

       
    @pcSystemModel.setter
    def pcSystemModel(self,value):
        # systemModel
        self._pcSystemModel = value
        # set the file configuration object with the pcSystemModel
        self.fileConfiguration.pcModelName = self._pcSystemModel
        # read the pcEquation
        # set the readMode of the fileSystem to read
        self.readMode = 1
        # set the fileName to be read using fileConfiguration object
        self.fileToReadFrom = self.fileConfiguration.pcModelEquationFile 
        # the based on the information type to be read
        # use the readFunction of the information type to access the PCEquation
        self.pcEquationString = self.readPCEquation()
        #self.pcEquationString = "((0.0179874213836478*(v7b*1.0))+(0.0220125786163522*(v7a*1.0)))"
        # print the accessed PCEquationString
        #print(self.pcEquationString)
        # set the equation variable with the read equationString
        self.pcEquation = list(self.pcEquationString)


    @property
    def pcSystemSumNodeName(self):
        if self._pcSystemSumNodeName == None:
            self._pcSystemSumNodeName = None
        return self._pcSystemSumNodeName

    @pcSystemSumNodeName.setter
    def pcSystemSumNodeName(self,value):
        self._pcSystemSumNodeName = value        
    
    @property
    def pcSystemProductNodeName(self):
        if self._pcSystemProductNodeName == None:
            self._pcSystemProductNodeName = None
        return self._pcSystemProductNodeName


    @pcSystemProductNodeName.setter
    def pcSystemProductNodeName(self,value):
        self._pcSystemProductNodeName = value

    @property
    def pcSystemTestData(self):
        if self._pcSystemTestData == None:
            # read the pcSystemTestData
            self._pcSystemTestData = self.readPCSystemTestData()
            return self._pcSystemTestData
        else:
            return self._pcSystemTestData

    @pcSystemTestData.setter
    def pcSystemTestData(self,value):
        self._pcSystemTestData = value
        
    
    @property
    def pcSystemModelMetaData(self):
        if self._pcSystemModelMetaData == None:
            # read the pcSystemTestData
            self._pcSystemModelMetaData = self.readPCSystemModelMetaData()
            # set the port variable categories and category starting value
            return self._pcSystemModelMetaData
        else:
            return self._pcSystemModelMetaData

    @pcSystemModelMetaData.setter
    def pcSystemModelMetaData(self,value):
        self._pcSystemModelMetaData = value
        
        
    @property
    def pcSystemHWOutput(self):
        # set the readMode
        self.readMode = 1
        # set the file to be read from 
        self.fileToReadFrom = self.fileConfiguration.pcSystemHWOutputFile
        # call the function readCSVData
        self._pcSystemHWOutput = self.readArrayData()
        return self._pcSystemHWOutput

    @pcSystemHWOutput.setter
    def pcSystemHWOutput(self,value):
        self._pcSystemHWOutput = value
        # set the write flag
        self.writeMode = 1
        # set the data to write
        self.pcSystemWriteData = self._pcSystemHWOutput
        # set the file to write on
        self.fileToWriteOn = self.fileConfiguration.pcSystemHWOutputFile
        # write the data to the file system
        self.writeArrayData()
    
    
    @property
    def pcSystemSWOutput(self):
        # set the readMode
        self.readMode = 1
        # set the file to be read from 
        self.fileToReadFrom = self.fileConfiguration.pcSystemSWLikeliHoodFile
        # call the function readCSVData
        self._pcSystemSWOutput = self.readCSVData()
        # print the retrieved sw output
        #print("The PCSystem SWOutput", self._pcSystemSWOutput)
        return self._pcSystemSWOutput

    @pcSystemSWOutput.setter
    def pcSystemSWOutput(self,value):
        self._pcSystemSWOutput = value
        # set the write flag
        self.writeMode = 1
        # set the data to write
        self.writeData = self._pcSystemSWOutput
        # set the file to write on
        self.fileToWriteOn = self.fileConfiguration.pcSystemSWLikeliHoodFile
        # write the data to the file system
        self.writeArrayData()

    @property
    def pcSystemErrorAnalysis(self):
        # set the readMode
        self.readMode = 1
        # set the file to be read from 
        self.fileToReadFrom = self.fileConfiguration.pcSystemErrorAnalysisFile
        # call the function readCSVData
        self._pcSystemErrorAnalysis = self.readCSVData()

        return self._pcSystemErrorAnalysis

    @pcSystemErrorAnalysis.setter
    def pcSystemErrorAnalysis(self,value):
        print("State 5: Initialised the PCSystemOutputData writing process")
        self._pcSystemErrorAnalysis = value
        # set the writeMode 
        self.writeMode = 1
        # set the file to be write on
        self.fileToWriteOn = self.fileConfiguration.pcSystemErrorAnalysisFile
        # set the pcSystemWriteData
        self.pcSystemWriteData = self._pcSystemErrorAnalysis
        # as the data is in the form of array, call the writeArrayData function
        self.writeArrayData()
        
    @property
    def pcSystemMaxErrorAnalysis(self):
        # set the readMode
        self.readMode = 1
        # set the file to be read from 
        self.fileToReadFrom = self.fileConfiguration.pcSystemMaxErrorAnalysisFile
        # call the function readCSVData
        self._pcSystemMaxErrorAnalysis = self.readCSVData()
        return self._pcSystemMaxErrorAnalysis

    @pcSystemMaxErrorAnalysis.setter
    def pcSystemMaxErrorAnalysis(self,value):
        self._pcSystemMaxErrorAnalysis = value
        # print the pcSystemMaxErrorAnalysis
        print("PCSystem max error analysis",self._pcSystemMaxErrorAnalysis)
        # set the writeMode 
        self.writeMode = 1
        # set the file to be write on
        self.fileToWriteOn = self.fileConfiguration.pcSystemMaxErrorAnalysisFile
        print("MaxErrorWriteFile", self.fileToWriteOn)
        # set the writeDataType
        self.writeDataType = 2
        # set the key of the dictionary data to be written
        self.writeDataKeys = ["NumberOfBits","MaxError"]
        # set the pcSystemWriteData
        self.pcSystemWriteData = self._pcSystemMaxErrorAnalysis
        # as the data is in the form of array, call the writeArrayData function
        self.writeDictionaryData()
        
    
    @property
    def pcSystemSWAverageLikelihoodAnalysis(self):
        # set the readMode
        self.readMode = 1
        # set the file to be read from 
        self.fileToReadFrom = self.fileConfiguration.pcSystemSWAverageLikelihoodAnalysisFile
        # call the function readCSVData
        self._pcSystemSWAverageLikelihoodAnalysis = self.readCSVData()
        return self._pcSystemSWAverageLikelihoodAnalysis

    @pcSystemSWAverageLikelihoodAnalysis.setter
    def pcSystemSWAverageLikelihoodAnalysis(self,value):
        self._pcSystemSWAverageLikelihoodAnalysis = value
        # set the writeMode 
        self.writeMode = 1
        # set the file to be write on
        self.fileToWriteOn = self.fileConfiguration.pcSystemSWAverageLikelihoodAnalysisFile
        # set the writeDataType
        self.writeDataType = 2
        # set the key of the dictionary data to be written
        self.writeDataKeys = ["NumberOfBits","SWAverageLikelihood"]
        # set the pcSystemWriteData
        self.pcSystemWriteData = self._pcSystemSWAverageLikelihoodAnalysis
        # as the data is in the form of array, call the writeArrayData function
        self.writeDictionaryData()
        

    @property
    def pcSystemHWAverageLikelihoodAnalysis(self):
        # set the readMode
        self.readMode = 1
        # set the file to be read from 
        self.fileToReadFrom = self.fileConfiguration.pcSystemHWAverageLikelihoodAnalysisFile
        # call the function readCSVData
        self._pcSystemHWAverageLikelihoodAnalysis = self.readCSVData()
        return self._pcSystemHWAverageLikelihoodAnalysis

    @pcSystemHWAverageLikelihoodAnalysis.setter
    def pcSystemHWAverageLikelihoodAnalysis(self,value):
        self._pcSystemHWAverageLikelihoodAnalysis = value
        # set the writeMode 
        self.writeMode = 1
        # set the file to be write on
        self.fileToWriteOn = self.fileConfiguration.pcSystemHWAverageLikelihoodAnalysisFile
        # set the writeDataType
        self.writeDataType = 2
        # set the key of the dictionary data to be written
        self.writeDataKeys = ["NumberOfBits","HWAverageLikelihood"]
        # set the pcSystemWriteData
        self.pcSystemWriteData = self._pcSystemHWAverageLikelihoodAnalysis
        # as the data is in the form of array, call the writeArrayData function
        self.writeDictionaryData()
        
        
    @property
    def pcSystemAverageErrorAnalysis(self):
        # set the readMode
        self.readMode = 1
        # set the file to be read from 
        self.fileToReadFrom = self.fileConfiguration.pcSystemAverageErrorAnalysisFile
        # call the function readCSVData
        self._pcSystemAverageErrorAnalysis = self.readCSVData()
        return self._pcSystemAverageErrorAnalysis

    @pcSystemAverageErrorAnalysis.setter
    def pcSystemAverageErrorAnalysis(self,value):
        self._pcSystemAverageErrorAnalysis = value
        # set the writeMode 
        self.writeMode = 1
        # set the file to be write on
        self.fileToWriteOn = self.fileConfiguration.pcSystemAverageErrorAnalysisFile
        # set the writeDataType
        self.writeDataType = 2
        # set the key of the dictionary data to be written
        self.writeDataKeys = ["NumberOfBits","AverageError"]
        # set the pcSystemWriteData
        self.pcSystemWriteData = self._pcSystemAverageErrorAnalysis
        # as the data is in the form of array, call the writeArrayData function
        self.writeDictionaryData()
        
    
    @property
    def pcSystemMannWhitneyUTestAnalysis(self):
        # set the readMode
        self.readMode = 1
        # set the file to be read from 
        self.fileToReadFrom = self.fileConfiguration.pcSystemMannWhitneyUTestFile
        # call the function readCSVData
        self._pcSystemMannWhitneyUTestAnalysis = self.readCSVData()

        return self._pcSystemMannWhitneyUTestAnalysis

    @pcSystemMannWhitneyUTestAnalysis.setter
    def pcSystemMannWhitneyUTestAnalysis(self,value):
        self._pcSystemMannWhitneyUTestAnalysis = value
        # set the writeMode 
        self.writeMode = 1
        # set the file to be write on
        self.fileToWriteOn = self.fileConfiguration.pcSystemMannWhitneyUTestFile
        # set the writeDataType
        self.writeDataType = 2
        # set the key of the dictionary data to be written
        self.writeDataKeys = ["NumberOfBits","MannWhitneyUTestPValue"]
        # set the pcSystemWriteData
        self.pcSystemWriteData = self._pcSystemMannWhitneyUTestAnalysis
        # as the data is in the form of array, call the writeArrayData function
        self.writeDictionaryData()
        
    
    @property
    def pcSystemWriteData(self):
        return self._pcSystemWriteData

    @pcSystemWriteData.setter
    def pcSystemWriteData(self,value):
        self._pcSystemWriteData = value
           
           
    # read PCEquation
    def readPCEquation(self):
        # print the file path along with that name
        #print("PCModelEquationFile:",self.fileConfiguration.pcModelEquationFile)
        # open the equationTextFile in readMode
        with open(self.fileConfiguration.pcModelEquationFile,'r') as file:
           # read the equationString from text File
           equationString = file.read()
           #print(equationString)
        return equationString


    def readCSVData(self):
        """
        Function to read data the form of CSV
        1. Checks whether the readMode of the fileSystem is set or not
        2. If set, uses the property of fileSystem, fileToBeReadFrom to read
        Returns
        -------
        An array that will have the read data form the given fileToBeReadFrom
        """

        # check the readState of the fileSystem, if the readState is set to 0, return without reading
        if self.readMode == 0:
            # print the readState of the FileSystem is not set
            print("FileSystem is not readMode, so reading the of the file is not possible:", self.fileToReadFrom)
            return

        # open the csv file
        csvFile = open(self.fileToReadFrom, 'r')
        # use the reader function of csv
        csvDataReader = csv.reader(csvFile)
        # as the first line of the csvData is the header  
        csvDataHeader = []
        # read header
        csvDataHeader = next(csvDataReader)
        # assign a local list variable to store the testData
        csvData = list()
        # loop through the csvDataReader
        for csvDataRows in csvDataReader:
            csvData.append(csvDataRows)
        
        # close the csvFile
        csvFile.close()
        # reset the readMode
        self.readMode = 0
        # return the retrieved data
        # print the retreieved data
        #print ("The retreived data:", self.csvData)
        return csvData
    
    def readArrayData(self):
        """
        Function to read data the form of Array, mainly used to read the HWOutput txt file
        1. Checks whether the readMode of the fileSystem is set or not
        2. If set, uses the property of fileSystem, fileToBeReadFrom to read
        Returns
        -------
        An array that will have the read data form the given fileToBeReadFrom
        """

        # check the readState of the fileSystem, if the readState is set to 0, return without reading
        if self.readMode == 0:
            # print the readState of the FileSystem is not set
            print("FileSystem is not readMode, so reading the of the file is not possible:", self.fileToReadFrom)
            return

        # open the csv file
        csvFile = open(self.fileToReadFrom, 'r')
        # use the reader function of csv
        csvDataReader = csv.reader(csvFile)
        # assign a local list variable to store the testData
        csvData = list()
        # loop through the csvDataReader
        for csvDataRows in csvDataReader:
            csvData.append(csvDataRows)
        
        # close the csvFile
        csvFile.close()
        # reset the readMode
        self.readMode = 0
        # return the retrieved data
        # print the retreieved data
        #print ("The retreived data:", self.csvData)
        return csvData

    def writeArrayData(self):
        """
        Function to write the data in the form of an array
        1. Checks whether the writeMode of the fileSystem is set or not
        2. If set, uses the property of fileSystem, fileToWriteOn to write the information
        Returns
        -------
        None
        """

        # check the writeState of the fileSystem, if the writeState is set to 0, return without reading
        if self.writeMode == 0:
            # print the writeState of the FileSystem is not set
            print("FileSystem is not writeMode, so writing on to the file is not possible:", self.fileToWriteOn)
            return

        #print("fileToWriteOn", self.fileToWriteOn)
        writeFile = open(self.fileToWriteOn,"w")
        # loop through the decimalOutputData
        for writeData in self.pcSystemWriteData:
            # write the pcSystemDecimalOutput
            writeFile.write(str(writeData) + "\n")
        
        # close the file
        writeFile.close()
        # reset the writeMode
        self.writeMode = 0
        
    
    
    def writeDictionaryData(self):
        """
        Function to write the data in the form of an array
        1. Checks whether the writeMode of the fileSystem is set or not
        2. If set, uses the property of fileSystem, fileToWriteOn to write the information
        Returns
        -------
        None
        """

        # check the writeState of the fileSystem, if the writeState is set to 0, return without reading
        if self.writeMode == 0:
            # print the writeState of the FileSystem is not set
            print("FileSystem is not writeMode, so writing on to the file is not possible:", self.fileToWriteOn)
            return


        #print("fileToWriteOn", self.fileToWriteOn)
        # variable to store the file of the pcSystemMaxErrorAnalysis
        writeFile = None
        if self.resetPCSystemErrorAnalysisFile == 0:
            # use the same file and access the nextNewLine
            writeFile = open(self.fileToWriteOn,"a")
        else:
            #print("fileToWriteOn", self.fileToWriteOn)
            # overwrite the file and its associated contents
            writeFile = open(self.fileToWriteOn,"w")
        
        key1 = self.writeDataKeys[0]
        key2 = self.writeDataKeys[1]
        value1 = self.pcSystemWriteData[key1]
        value2 = self.pcSystemWriteData[key2]
        # write the dictionary data
        writeFile.write(str(value1) + "," + str(value2) + "\n")
        # close the file
        writeFile.close()
        # reset the writeMode
        self.writeMode = 0

    # read testData
    def readPCSystemTestData(self):
        """
        TestData of a given model allows us to know the active port variable and its associated categories for a given port variable
        1. It is currently available as part of the "Whistle-software" gitlab repo
        2. First, we will use the file configuration to locate the file location in the respective gitlab
        3. Then, use the file name to read the testData csv file of the respective model 

        Returns
        --------
        A list object that contains the testData in the form of a two dimenstional list. This list forms the IOPattern for the DUT or the PCSystem

        """
        # print the file path along with that name
        #print("PCModelTestDataFile:",self.fileConfiguration.pcModelTestDataFile)
        # open the testData csv file
        testDataFile = open(self.fileConfiguration.pcModelTestDataFile)
        # read the testData csv file
        testDataReader = csv.reader(testDataFile)
        # set a list to store the header
        testDataHeader = []
        # read header
        testDataHeader = next(testDataReader)
        # assign a local list variable to store the testData
        testData = list()
        # loop through the testDataReader
        for testDataRows in testDataReader:
            testData.append(testDataRows)
        # set the length of the testData multiplied by 10 ns for simulation run time
        self.pcSystemVHDLConfiguration.simulationRunTime = str((len(testData) * 5))
        return testData
    
    
    # readPCSystemModelMetaData metaData
    def readPCSystemModelMetaData(self):
        """
        MetaData of a given model allows us to know the total port variable and its associated categories 
        1. It is currently available as part of the "Whistle-software" gitlab repo
        2. First, we will use the file configuration to locate the file location in the respective gitlab
        3. Then, use the file name to read the metadata csv file of the respective model 

        Returns
        --------
        A list object that contains the metaData in the form of a one dimenstional list

        """
        # print the metaDataFile
        #print("PCModelMetaDataFile:",self.fileConfiguration.pcModelMetaDataFile)

        # open the metaData csv file
        metaDataFile = open(self.fileConfiguration.pcModelMetaDataFile)
        # read the metaData csv file
        metaDataReader = csv.reader(metaDataFile)
        # set a list to store the header
        metaDataHeader = []
        # readReader and set header
        metaDataHeader = next(metaDataReader)
        # assign a local list variable to store the metaData
        metaData = list()
        # loop through the testDataReader
        for metaDataIndex, metaDataRow in enumerate(metaDataReader):
            # first row or index 0 is portVariable categories
            # second row or index 1 is category start number
            if metaDataIndex == 0:
                # set the portVariable categories
                #portVariableCategories = metaDataRow
                #print("Meta DataRow PortVariable Categories:", metaDataRow)
                metaData.append(metaDataRow)
            elif metaDataIndex == 1:
                # access the metaDataRow
                # access the second element of metaDataRow
                categoryStartNumber = metaDataRow[1]
                #print("MetaData CategoryStartNumber:", categoryStartNumber)
                metaData.append(int(categoryStartNumber))
                               
        #print("PCModel Meta Data:", metaData)
        return metaData
    
    
    # readPCSystemModelMetaData metaData
    def readPCSystemModelMetaDataExcel(self):
        """
        MetaData of a given model allows us to know the total port variable and its associated categories 
        1. It is currently available as part of the "Whistle-software" gitlab repo
        2. First, we will use the file configuration to locate the file location in the respective gitlab
        3. Then, use the file name to read the metadata excel file of the respective model 

        Returns
        --------
        A list object that contains the metaData in the form of a one dimenstional list

        """
        # print the metaDataFile
        #print("PCModelMetaDataFile:",self.fileConfiguration.pcModelMetaDataFile)

        # open the metaData xlsx file
        metaDataFile = self.fileConfiguration.pcModelMetaDataFile
        # read the metaDataExcel file
        metaDataExcel = pd.read_excel(metaDataFile, engine='openpyxl', sheet_name=0, header=None, index_col=False)
        # check the dataframe shape is valid or not
        if metaDataExcel.shape[1] == 0:
            print("MetaData might not contain the cat_start dictionary as second row")
        # read the portVariable Categories
        portVariableCategoriesDF = metaDataExcel.iloc[[0]]
        # flatten the df
        portVariableCategories = portVariableCategoriesDF.values.flatten()
        # print the portVariable Categories
        print("PortVariable Categories:", portVariableCategories)
        # check the dataframe number of rows, if the rows are more than 1,then we have start_cat as dict in dataframe
        if len(metaDataExcel.index) == 1:
            print("MetaData might not contain the cat_start dictionary as second row")
            # mannually set the start point of the ctegorues to 0
            categoryStartNumber = 0
            # make the metaData
            metaData = list()
            metaData.append(portVariableCategories)
            metaData.append(categoryStartNumber)
            return metaData


        # access the category start number can be either 0 or 1
        categoryStartNumberDF = metaDataExcel.iloc[[1]]
        # flatten the df
        categoryStartNumberList = categoryStartNumberDF.values.flatten()
        # access the 1st index in the list
        categoryStartNumber = int(categoryStartNumberList[1])
        # print the category start number
        #print("Category start Number:", categoryStartNumber)

        # flatten the metaDataExcel into list
        metaData = list()
        metaData.append(portVariableCategories)
        metaData.append(categoryStartNumber)
        # print the metaData
        #print("PCModel MetaData:", metaData)
        #print(f'{metaDataExcel}')
        return metaData


   
    def readPCSystemSWOutput(self):
        """
        Read the likelihood data from the likelihood csv file
        1. The read data is the SW results data of the PCSystem
        2. Every row in the likelihood data is one to one mapped with the decimalOutput text file
        3. Once read, we need to find the relative error of one to one mapped HW and SW results
        4. The found error array will be stored in a file for further analysis
        5. Also, we need to find the maxError for the found error array
        
        Returns
        -------
        An array with the relative errors for each element of the HW and SW results

        """
        # access the fileName using the fileconfiguration object
        pcSystemSWOutputFileName = self.fileConfiguration.pcSystemSWLikeliHoodFile
        # print the SWOutput fileName
        #print("PCSystem SWOutput FileName:", pcSystemSWOutputFileName)
        # open the file
        pcSystemSWOutputFile = open(pcSystemSWOutputFileName)
        # read the file
        pcSystemSWOutputReader = csv.reader(pcSystemSWOutputFile)
        # store the header
        pcSystemSWOutputFileHeader = []
        # read header
        pcSystemSWOutputFileHeader = next(pcSystemSWOutputReader)
        # read the file and store the SWResults in an array
        pcSystemSWOutputResults = []
        for pcSystemSWOutputData in pcSystemSWOutputReader:
            pcSystemSWOutputResults.append(pcSystemSWOutputData)
            
        # print the testData
        return pcSystemSWOutputResults
    
    
    
    def readPCSystemOutput(self):
        """
        Read the PCSystemOoutput from the Output.txt file
        1. Use the fileconfiguration object to retrieve the output file
        2. Use csv to read the output file values and store in an array

        Returns
        ----------
        A two dimensional array containing the outputData
        """
        # access the output file
        outputFile = self.fileConfiguration.pcSystemVHDLSimulationOutputFile
        # open the file
        outputFileHeader = open(outputFile)
        # use the csv reader
        outputFileCSVReader = csv.reader(outputFileHeader)
        # loop through the csv reader
        # assign a list to append the read output data
        outputData = []
        for outputFileData in outputFileCSVReader:
            outputData.append(outputFileData)
        #print("PCSystemOutputData:", outputData)
        return outputData
    
    def readPCSystemInfo(self):
        """
        Logic
        -------
        Read the PCSystemInfo from the PCSystemInfo.txt file
        1. Use the fileconfiguration object to retrieve the PCSystemInfo.txt file
        2. Then, use json framework  to read the PCSystemInfo file values and store in a dict

        Purpose
        --------
        To read Info of a PCSystem and use the info to process the output data
        Returns
        ----------
        Dictionary containing the PCSystemInfo
        """
        # access the output file
        pcSystemInfoFile = self.fileConfiguration.pcSystemInfoFile
        # open the file
        pcSystemInfoFileReference = open(pcSystemInfoFile,'r')
        # use the reference pointer to read the contents of the file
        psSystemInfo = json.load(pcSystemInfoFileReference)
        # return the pcSystemInfo dictionary
        return psSystemInfo
    
    """
    # Start: writePCSystemPorts function
    """
    def writePCSystemPorts(self):
        # print the file path
        #print("PCPortsFile file location", self.fileConfiguration.pcPortsFile)
        pcPortsFile = open(self.fileConfiguration.pcSystemPortsFile, "w")
        # check the numberSystem
        if self.pcSystemNumberSystem == 0:
            pcPortsFile.write(self.pcSystemVHDLConfiguration.fixedPCSystemVHDLLibrariesSyntax)
        elif self.pcSystemNumberSystem == 1:
            pcPortsFile.write(self.pcSystemVHDLConfiguration.floatPCSystemVHDLLibrariesSyntax)
        elif self.pcSystemNumberSystem == 2:
            pcPortsFile.write(self.pcSystemVHDLConfiguration.positPCSystemVHDLLibrariesSyntax)

        
        pcPortsFile.write("entity PCSystem is \n \n")

        if self.pcSystemNumberSystem == 0:
             pcPortsFile.write(self.pcSystemVHDLConfiguration.fixedPCSystemGenericsVHDLSyntax)
        elif self.pcSystemNumberSystem == 1:
            pcPortsFile.write(self.pcSystemVHDLConfiguration.floatPCSystemGenericsVHDLSyntax)
        elif self.pcSystemNumberSystem == 2:
            pcPortsFile.write(self.pcSystemVHDLConfiguration.positPCSystemGenericsVHDLSyntax)
            
        pcPortsFile.write("port( \n")
        
        for port in self.pcSystemPorts:
            pcPortsFile.write(port.vhdlPort+ ";" + "\n")
        
        pcPortsFile.write(self.pcSystemOutputPort.vhdlOutputPort)
        pcPortsFile.write("); \n \n")
        pcPortsFile.write("end PCSystem; \n")
        
        pcPortsFile.close()
        return
    """
    # End: writePCSystemPorts function
    """
    
    
    """
    # Start: writePCSystemInputBinaryString function
    """
    def writePCSystemInputBinaryString(self):
        binaryStringConverter = PositConverter(self.pcSystemNumberOfBits,self.pcSystemEsBits,self.pcSystemMantissaBits)
        # open the Input.txt file
        pcSystemInputBinaryStringTextFile = open(self.fileConfiguration.pcSystemVHDLSimulationInputFile, "w")
        # print the pcSystemPortsIO
        #print("PCSystemIOPattern", self.pcSystemIOPattern)
        for ioPatterns in self.pcSystemIOPattern:
            for ioPattern in ioPatterns:
                # check the numberSystem
                if self.pcSystemNumberSystem == 2:
                    # check input iOPattern
                    if ioPattern == "0":
                        # as per the numberofBits update the ioPattern for zeros
                        #ioPattern = binaryStringConverter.convert_float_to_posit(float(0))
                        ioPattern = "".join([ioPattern]*self.pcSystemNumberOfBits)
                    elif ioPattern == "1":
                        # use the converter to convert the "1" to POSIT 1 based on the number of es bits 
                        # and number of bits
                        ioPattern = binaryStringConverter.convert_float_to_posit(float(1))
                        # as per the numberOfbits update the ioPattern for ones
                        #ioPositOnePattern = "01"
                        #ioPositZeroPattern = "0"
                        #ioPositZeroPattern = "".join([ioPositZeroPattern]*(self.pcSystemNumberOfBits-2))
                        #ioPattern = ioPositOnePattern + ioPositZeroPattern
                        #print("POSIT 1 IOPattern:", ioPattern)
                pcSystemInputBinaryStringTextFile.write(ioPattern + ",")

            pcSystemInputBinaryStringTextFile.write("\n")
            
        pcSystemInputBinaryStringTextFile.close()
        return
    """
    # End: writePCSystemInputBinaryString function
    """
    
    
    """
    # Start: writePCSystemArithmeticNodes function
    """
    
    def writePCSystemArithmeticNodes(self):
        # print the file path
        #print("PCArithmeticNodes file location", self.fileConfiguration.pcArithmeticNodesFile)
        pcSystemArithmeticNodesFile = open(self.fileConfiguration.pcSystemArithmeticNodesFile, "w")
        
        pcSystemArithmeticNodesFile.write("architecture rtl of PCSystem is \n \n")
        
        
        for arithmeticNode in self.pcSystemArithmeticNodes:
            if isinstance(arithmeticNode, SumNode.SumNode):
                if self.pcSystemNumberSystem == 2:
                    self.pcSystemSumNodeName = arithmeticNode.customName
                else:
                    self.pcSystemSumNodeName = arithmeticNode.name

            if isinstance(arithmeticNode, ProductNode.ProductNode):
                if self.pcSystemNumberSystem == 2:
                    self.pcSystemProductNodeName = arithmeticNode.customName
                else:
                    self.pcSystemProductNodeName = arithmeticNode.name

                if (arithmeticNode.vhdlWeightSignal != None):
                    pcSystemArithmeticNodesFile.write(arithmeticNode.vhdlWeightSignal)
                    pcSystemArithmeticNodesFile.write("\n")
                     
            pcSystemArithmeticNodesFile.write(arithmeticNode.vhdlOutputSignal)
            
        pcSystemArithmeticNodesFile.write("\n \n")
        pcSystemArithmeticNodesFile.write("begin \n")
        
        for arithmeticNode in self.pcSystemArithmeticNodes:
            pcSystemArithmeticNodesFile.write(arithmeticNode.vhdlInstance)
        
        arithmeticNode = self.pcSystemArithmeticNodes[len(self.pcSystemArithmeticNodes)-1]
        finalOutput = arithmeticNode.output
        pcSystemArithmeticNodesFile.write("vout <= " + finalOutput + ";" + "\n \n")
        
        # write the end architecture to the pcSystemArithmeticNodesFile
        pcSystemArithmeticNodesFile.write("end architecture" + ";" + "\n")
        # close the pcSystemArithmeticNodesFile
        pcSystemArithmeticNodesFile.close()
        return
    
    """
    # End: writePCSystemArithmeticNodes function
    """


    """
    # Start: writePCSystemInfo Function
    """

    def writePCSystemInfo(self):
        """
        Purpose
        --------
        The currentPCSystem object will be store its information in a text file inside the "File-System" folder.
        1. The stored information will be used by the DataProcessing modules to process the PCSystemOutput data

        Logic
        --------
        1. Access the file using the fileconfiguration object
        2. Open the file in write mode 
        """
        # access and open the PCSystemInfo file using the fileconfiguration object
        pcSystemInfoFile = open(self.fileConfiguration.pcSystemInfoFile,"w") 
        # write the pcSystem Information using JSON
        json.dump(self.pcSystemInfo,pcSystemInfoFile)
        
    
    """
    # End: writePCSystemInfo Function
    """
            
    """
    # Start: writePCSystemVHDL function
    """
    
    def writePCSystemVHDL(self):
        # print the file path
        #print("PCSystemVHDLFile file location", self.fileConfiguration.pcVHDLFile)
        # open the file in write mode
        pcVHDLFile = open(self.fileConfiguration.pcSystemVHDLFile, "w")
        
        # Opening ports file and scanning each line
        # from ports file and start writing in output file
        with open(self.fileConfiguration.pcSystemPortsFile, "r") as scan:
            pcVHDLFile.write(scan.read())
        
        pcVHDLFile.write("\n")
        with open (self.fileConfiguration.pcSystemArithmeticNodesFile,"r") as scan:
            pcVHDLFile.write(scan.read())
                
        # Closing the pcVHDLFile file
        pcVHDLFile.close()
        return
    
    """
    # End: writePCSystemVHDL function
    """
    
    """
    # Start: writePCSystemVHDLTestBench function
    """
    
    def writePCSystemVHDLTestBench(self):
       # print the file path
        #print("PCPortsFile file location", self.fileConfiguration.pcPortsFile)
        
        pcVHDLTestBenchFile = open(self.fileConfiguration.pcSystemVHDLTestBenchFile, "w")
        if self.pcSystemNumberSystem == 0:
            pcVHDLTestBenchFile.write(self.pcSystemVHDLConfiguration.fixedPCSystemVHDLTestBenchLibrariesSyntax)
        elif self.pcSystemNumberSystem == 1:
            pcVHDLTestBenchFile.write(self.pcSystemVHDLConfiguration.floatPCSystemVHDLTestBenchLibrariesSyntax)
        elif self.pcSystemNumberSystem == 2:
            pcVHDLTestBenchFile.write(self.pcSystemVHDLConfiguration.positPCSystemVHDLTestBenchLibrariesSyntax)
       
        pcVHDLTestBenchFile.write("ENTITY PCSystem_tb IS \n")
        pcVHDLTestBenchFile.write("END PCSystem_tb; \n \n")
   
        pcVHDLTestBenchFile.write("ARCHITECTURE behavioural of PCSystem_tb IS \n \n")
        
        if self.pcSystemNumberSystem == 0:
            pcVHDLTestBenchFile.write(self.pcSystemVHDLConfiguration.fixedPCSystemConstantsVHDLSyntax)
        elif self.pcSystemNumberSystem == 1:
            pcVHDLTestBenchFile.write(self.pcSystemVHDLConfiguration.floatPCSystemConstantsVHDLSyntax)
        elif self.pcSystemNumberSystem == 2:
            pcVHDLTestBenchFile.write(self.pcSystemVHDLConfiguration.positPCSystemConstantsVHDLSyntax)

        for port in self.pcSystemPorts:
            pcVHDLTestBenchFile.write(port.vhdlPortSignal)
        
        pcVHDLTestBenchFile.write(self.pcSystemOutputPort.vhdlOutputPortSignal + "\n")
        pcVHDLTestBenchFile.write("BEGIN" + "\n\n")
        pcVHDLTestBenchFile.write("pcSystem: ENTITY work.PCSystem(rtl)"+ "\n\n")
        
        if self.pcSystemNumberSystem == 0:
            pcVHDLTestBenchFile.write(self.pcSystemVHDLConfiguration.fixedPCSystemGenericMapVHDLSyntax)
        elif self.pcSystemNumberSystem == 1:
            pcVHDLTestBenchFile.write(self.pcSystemVHDLConfiguration.floatPCSystemGenericMapVHDLSyntax)

        pcVHDLTestBenchFile.write("PORT MAP (")
        
        for port in self.pcSystemPorts:
            pcVHDLTestBenchFile.write(port.name + "=>" + port.name + "," + "\n")

        pcVHDLTestBenchFile.write(self.pcSystemOutputPort.name + "=>" + self.pcSystemOutputPort.name + ");" + "\n\n")

        # write the testbench IO stimulus process
        pcVHDLTestBenchFile.write("ioStimulus  : PROCESS IS" + "\n\n")

        pcVHDLTestBenchFile.write("VARIABLE fileline     : line" + ";" + "\n")
        if self.pcSystemNumberSystem == 0:
            pcVHDLTestBenchFile.write("VARIABLE inputBuffer  : integer" + ";" + "\n")
        elif self.pcSystemNumberSystem == 1:
            pcVHDLTestBenchFile.write("VARIABLE inputBuffer  : integer" + ";" + "\n")
        elif self.pcSystemNumberSystem == 2:
            pcVHDLTestBenchFile.write("VARIABLE inputBuffer  : bit_vector" + "(" \
                    + str(self.pcSystemNumberOfBits-1)+ " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n")

        pcVHDLTestBenchFile.write("VARIABLE commaBuffer  : character" + ";" + "\n")

        pcVHDLTestBenchFile.write("FILE inputfile  : text OPEN read_mode is" + " " + "\"Input.txt\"" + ";" + "\n")
        pcVHDLTestBenchFile.write("FILE outputfile : text OPEN write_mode is" + " " + "\"Output.txt\"" + ";" + "\n\n")
        
        pcVHDLTestBenchFile.write("BEGIN \n\n")
        pcVHDLTestBenchFile.write("WHILE NOT endfile (inputfile) LOOP" + "\n\n")
        pcVHDLTestBenchFile.write("readline (inputfile, fileline);" + "\n")
     
        for port in self.pcSystemPorts:
            pcVHDLTestBenchFile.write("read (fileline, inputBuffer)" + ";" + "\n")

            if self.pcSystemNumberSystem == 0:
                pcVHDLTestBenchFile.write(port.name + "<=" + "to_" + port.numberSystemName + "(" + "inputBuffer" + "," + "0" + "," + str((1-port.numberOfBits))+ ")" + ";" + "\n\n")
            elif self.pcSystemNumberSystem == 1:
                pcVHDLTestBenchFile.write(port.name + "<=" + "to_" + port.numberSystemName + "(" + "inputBuffer" + "," + str(port.exponentBits) + "," + str((port.mantissaBits-1))+ ")" + ";" + "\n\n")
            elif self.pcSystemNumberSystem == 2:
                pcVHDLTestBenchFile.write(port.name + "<="  + "to_stdlogicvector" + "(" + "inputBuffer" + ")" + ";" + "\n\n")
            
            pcVHDLTestBenchFile.write("read (fileline, commaBuffer)" + ";" + "\n")
       
        pcVHDLTestBenchFile.write("WAIT FOR" + " " + "5 ns" + ";" + "\n\n")
        if self.pcSystemNumberSystem == 0:
            pcVHDLTestBenchFile.write("write (fileline, " + self.pcSystemOutputPort.name + ")" + ";" + "\n")
        elif self.pcSystemNumberSystem == 1:
            pcVHDLTestBenchFile.write("write (fileline, " + self.pcSystemOutputPort.name + ")" + ";" + "\n")
        elif self.pcSystemNumberSystem == 2:
            pcVHDLTestBenchFile.write("write (fileline, " + "to_bitvector" + "(" + self.pcSystemOutputPort.name + ")" + ")" + ";" + "\n")

        pcVHDLTestBenchFile.write("writeline (outputfile, fileline)" + ";" + "\n\n")

        pcVHDLTestBenchFile.write("END LOOP" + ";" + "\n\n")
        pcVHDLTestBenchFile.write("file_close (inputfile);" +"\n") 
        pcVHDLTestBenchFile.write("file_close (outputfile);" +"\n\n") 
        pcVHDLTestBenchFile.write("WAIT;" +"\n\n")
        pcVHDLTestBenchFile.write("END PROCESS ioStimulus" + ";" + "\n\n")
        pcVHDLTestBenchFile.write("END ARCHITECTURE behavioural" + ";" + "\n\n")

        pcVHDLTestBenchFile.close()

        # write the PCSystem compile script
        self.writePCSystemVHDLCompileScript()
        # write the PCSystem simulation script
        self.writePCSystemVHDLSimulationScript()

    
    """
    # End: writePCSystemVHDLTestBench function
    """
    
    """
    # Start: writePCSystemVHDLCompileScript function
    """
    
    def writePCSystemVHDLCompileScript(self):
        # check if the number system is POSIT, if so, then retrieve the files from the POSITAdd, POSITMult
        # folders by appending the dynamics names of the POSITAdd and POSITMult using the information of the PCSystem
        if self.pcSystemNumberSystem == 2:
            self.__copyPositSumProductNodeFilesFromSourceFolderToDestinationPCSystemVHDLFolder()

        # open the pcSystemVHDLCompileFile file
        pcSystemVHDLCompileFile = open(self.fileConfiguration.pcSystemVHDLCompileFile, "w")

        #print(pcInputBinaryStringTextFile)
        pcSystemVHDLCompileFile.write("cd $PWD/simulation" + "\n")
        # for posit avoid compiling the library ieee_proposed
        if self.pcSystemNumberSystem != 2:
            pcSystemVHDLCompileFile.write("vlib ieee_proposed" + "\n")
        pcSystemVHDLCompileFile.write("vlib work" + "\n")

        if self.pcSystemNumberSystem == 0:
            pcSystemVHDLCompileFile.write(self.pcSystemVHDLConfiguration.fixedPCSystemVHDLCompileScriptSyntax)
        elif self.pcSystemNumberSystem == 1:
            pcSystemVHDLCompileFile.write(self.pcSystemVHDLConfiguration.floatPCSystemVHDLCompileScriptSyntax)
       
        if self.pcSystemNumberSystem == 0:
            pcSystemVHDLCompileFile.write("vcom -work work $PWD/vhdl/"+ self.pcSystemSumNodeName + ".vhd" + "\n")
            pcSystemVHDLCompileFile.write("vcom -work work $PWD/vhdl/"+ self.pcSystemProductNodeName + ".vhd" + "\n")
        elif self.pcSystemNumberSystem == 1:
           pcSystemVHDLCompileFile.write("vcom -work work $PWD/vhdl/" + self.pcSystemProductNodeName + ".vhd" + "\n")
           pcSystemVHDLCompileFile.write("vcom -work work $PWD/vhdl/" + self.pcSystemSumNodeName + ".vhd" + "\n")
        elif self.pcSystemNumberSystem == 2:
           #print("ProductNodeName:", self.pcSystemProductNodeName)
           pcSystemVHDLCompileFile.write("vcom -work work $PWD/vhdl/" + self.pcSystemProductNodeName + ".vhd" + "\n")
           pcSystemVHDLCompileFile.write("vcom -work work $PWD/vhdl/" + self.pcSystemSumNodeName + ".vhd" + "\n")

        pcSystemVHDLCompileFile.write("vcom -work work $PWD/vhdl/PCSystem.vhd" + "\n")
        pcSystemVHDLCompileFile.write("vcom -work work $PWD/vhdl/PCSystem_tb.vhd" + "\n")

        pcSystemVHDLCompileFile.close()
    
    """
    # End: writePCSystemVHDLCompileScript function
    """
    
    """
    # Start: __copyPositSumProductNodeFilesToVHDLFolder function
    """

    def __copyPositSumProductNodeFilesFromSourceFolderToDestinationPCSystemVHDLFolder(self):

        # check if the number system is POSIT, if so, then retrieve the files from the POSITAdd, POSITMult
        # folders by appending the dynamics names of the POSITAdd and POSITMult using the information of the PCSystem

        # make the fileName for the Flopoco VHDL of PositAdd
        flopocoPositSumNodeVHDLPackagesFolder = os.path.join(self.fileConfiguration.pcSystemPOSITSumNodeVHDLPackagesFolder, "PositAdd" + "_" + str(self.pcSystemNumberOfBits) + "_" + str(self.pcSystemEsBits))
        # make the fileName for the Flopoco VHDL of PositMult
        flopocoPositProductNodeVHDLPackagesFolder = os.path.join(self.fileConfiguration.pcSystemPOSITProductNodeVHDLPackagesFolder, "PositMult" + "_" + str(self.pcSystemNumberOfBits) + "_" + str(self.pcSystemEsBits))


        # make the flopocoPOSITSumNodeVHDLFileName
        flopocoPositProductNodeVHDLSourceFile = flopocoPositProductNodeVHDLPackagesFolder + "/flopoco.vhdl"
        # make the flopocoPOSITSumNodeVHDLFileName
        flopocoPositSumNodeVHDLSourceFile = flopocoPositSumNodeVHDLPackagesFolder + "/flopoco.vhdl"

        # make the flopocoPOSITSumNode VHDL move to the Destination Folder
        flopocoPositSumNodeVHDLDestinationFolder = self.fileConfiguration.pcSystemVHDLFolder + "/" + self.pcSystemSumNodeName + ".vhd"
        # make the flopocoPOSITSumNodeVHDLFileName
        flopocoPositProductNodeVHDLDestinationFolder = self.fileConfiguration.pcSystemVHDLFolder + "/" + self.pcSystemProductNodeName + ".vhd"


        #copy the file sumNode from source to destination
        shutil.copy(flopocoPositSumNodeVHDLSourceFile,flopocoPositSumNodeVHDLDestinationFolder)
        
        #copy the file productNode from source to destination
        shutil.copy(flopocoPositProductNodeVHDLSourceFile,flopocoPositProductNodeVHDLDestinationFolder)
    
    """
    # End: __copyPositSumProductNodeFilesToVHDLFolder function
    """
    
    """
    # Start: writePCSystemVHDLSimulationScript function
    """
    
    def writePCSystemVHDLSimulationScript(self):
       
        # open the pcSystemVHDLCompileFile file
        pcSystemVHDLSimulationDoFile = open(self.fileConfiguration.pcSystemVHDLSimulationDoFile, "w")

        #print(pcInputBinaryStringTextFile)
        pcSystemVHDLSimulationDoFile.write("vlib ieee_proposed" + "\n")
        pcSystemVHDLSimulationDoFile.write("vlib work" + "\n")

        if self.pcSystemNumberSystem == 0:
            pcSystemVHDLSimulationDoFile.write(self.pcSystemVHDLConfiguration.pcSystemVHDLSimulationScript)
        elif self.pcSystemNumberSystem == 1:
            pcSystemVHDLSimulationDoFile.write(self.pcSystemVHDLConfiguration.pcSystemVHDLSimulationScript)
            
      
        if self.pcSystemNumberSystem == 0:
            pcSystemVHDLSimulationDoFile.write("vcom -work work vhdl/SumNode_Fixed.vhd" + "\n")
            pcSystemVHDLSimulationDoFile.write("vcom -work work vhdl/ProductNode_Fixed.vhd" + "\n")
        elif self.pcSystemNumberSystem == 1:
           pcSystemVHDLSimulationDoFile.write("vcom -work work vhdl/SumNode_Float.vhd" + "\n")
           pcSystemVHDLSimulationDoFile.write("vcom -work work vhdl/ProductNode_Float.vhd" + "\n")
        elif self.pcSystemNumberSystem == 2:
           pcSystemVHDLSimulationDoFile.write("vcom -work work vhdl/" + self.pcSystemProductNodeName + ".vhd" + "\n")
           pcSystemVHDLSimulationDoFile.write("vcom -work work vhdl/" + self.pcSystemSumNodeName + ".vhd" + "\n")

        pcSystemVHDLSimulationDoFile.write("vcom -work work vhdl/PCSystem.vhd" + "\n")
        pcSystemVHDLSimulationDoFile.write("vcom -work work vhdl/PCSystem_tb.vhd" + "\n\n")
        pcSystemVHDLSimulationDoFile.write("vsim -work work PCSystem_tb" + "\n")
        #pcSystemVHDLSimulationDoFile.write("add wave -r *" + "\n")'
        #pcSystemVHDLSimulationDoFile.write("exit" + "\n")
        pcSystemVHDLSimulationDoFile.write(self.pcSystemVHDLConfiguration.simulationRunTime)
        pcSystemVHDLSimulationDoFile.write("exit" + "\n")


        pcSystemVHDLSimulationDoFile.close()
    
    """
    # End: writePCSystemVHDLSimulationScript function
    """
    
    def main(self):
        pass
    
    def run(self):
        self.main()


        

