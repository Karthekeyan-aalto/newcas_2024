#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 10:01:02 2022

@author: Karthekeyan Periasamy
"""

import os

class PCFileConfiguration():
    
    def __init__(self):


        """
        PCSystem Details
        """
        self._pcSystemNumberSystem = None
        
        """
        # Start: Directory details
        """
        self._parentDirectory = None
        
        """
        FolderName
        """

        self.pcSystemInfoFolderName = "SystemInfo"
        self.pcSystemVHDLFolderName = "VHDL"
        self.pcSystemLogFolderName = "Log"
        self._pcModelFolderName = None
        self._pcSystemNumberSystemFolderName = None
        self.pcSystemDataFolderName = "Data"
        self.pcSystemSimulationFolderName = "Simulation"
        self.pcSystemIOSimulationFolderName = "simulation"
        self.pcModelParentFolderName = "WhistleSoftware"
        self.pcSystemModelEquationAnalysisDataFolderName = "Analysis"
        self.pcSystemModelEquationErrorAnalysisFolderName = "ErrorAnalysis"
        self.pcSystemModelEquationDecimalOutputFolderName = "DecimalOutput"
        self.pcSystemModelEquationLikelihoodAnalysisFolderName = "LikelihoodAnalysis"
        self.pcSystemVHDLPackagesFolderName = "VHDLPackages"
        self.pcSystemProcessedDataFolderName = "ProcessedData"
        self.pcVHDLPOSITPackageFolderName = "POSITPackage"
        self.pcSystemPOSITSumNodeVHDLPackagesFolderName = "PositAdd"
        self.pcSystemPOSITProductNodeVHDLPackagesFolderName = "PositMult"

        """
        Files for the respective model equations, IO equations and etc:
        """
        # pcModel file
        self.pcModelFile = None
        self._pcModelMetaDataFile = None
        self._pcModelTestDataFile = None
        self._pcSystemSWLikeliHoodFile = None
        self._pcModelEquationFile = None
        self._pcSystemVHDLSimulationDoFile = None
        # pcVHDL file
        self._pcSystemVHDLFile = None
        # pcVHDLTestBench file
        self._pcSystemVHDLTestBenchFile = None
        # pcSystemVHDLCompile file
        self._pcSystemVHDLCompileFile = None
        # pcSystemVHDLSimulationDoFile file
        self._pcSystemVHDLSimulationDoFile = None
        # pcPorts file
        self._pcSystemPortsFile = None
        # PCSystemArithmeticNodes file
        self._pcSystemArithmeticNodesFile = None
        # pcSystemInfo  file 
        self._pcSystemInfoFile = None
        # pcSystemDecimalOutput  file 
        self._pcSystemHWOutputFile = None
        # pcSystemErrorAnalysis  file 
        self._pcSystemErrorAnalysisFile = None
        # pcSystemVHDLSimulationInputFile file
        self._pcSystemVHDLSimulationInputFile = None
        # pcSystemVHDLSimulationOutputFile file
        self._pcSystemVHDLSimulationOutputFile = None
        self._pcSystemMaxErrorAnalysisFile = None
        self._pcSystemAverageErrorAnalysisFile = None
        self._pcSystemHWAverageLikelihoodAnalysisFile = None
        self._pcSystemSWAverageLikelihoodAnalysisFile = None
        self._pcSystemMannWhitneyUTestFile = None



        """
        Folder Path
        """
        self._pcSystemDataFolder = None
        # when the model type is set, the pcSystemSPNDataFolder will be set
        self._pcSystemModelDataFolder = None
        self._pcSystemModelEquationDataFolder = None
        self._pcSystemNumberSystemFolder = None
        self._pcModelFolder = None
        self._pcVHDLPackagesFolder = None
        self._pcSystemModelEquationAnalysisDataFolder = None
        self._pcSystemModelEquationErrorAnalysisFolder = None
        self._pcSystemModelEquationDecimalOutputFolder = None
        self._pcSystemModelEquationLikelihoodAnalysisFolder = None
        self._pcSystemVHDLFolder = None
        self._pcModelParentFolder = None
        self._pcSystemSimulationFolder = None
        self._pcSystemInfoFolder = None
        self._pcSystemIOSimulationFolder = None
        self._pcSystemPOSITSumNodeVHDLPackagesFolder = None
        self._pcSystemPOSITProductNodeVHDLPackagesFolder = None
        self._pcVHDLPOSITPackageFolder = None


        """
        File format name including the IO, pcEquation and etc
        """
        # txt file format name
        self.textFileFormatName = ".txt"
        # csv file format name
        self.csvFileFormatName = ".csv"
        # xlsx file format name
        self.xlsxFileFormatName = ".xlsx"

        """
        PC Model name
        """
        # model type
        self._pcModelType = 0
        # model name
        self._pcModelName = None

        """
        File "Names"
        """
        # testdata file name (part of the whole filename) for any PC model
        self.testDataFileName = "testdata"
        self.metaDataFileName = "metadata"
        self.equationFileName = "equation"
        self.outputFileName = "Output"
        self.systemInfoFileName = "PCSystemInfo"
        self.likelihoodFileName = "likelihoods"
        self.errorAnalysisFileName = "ErrorAnalysis"
        self.maxErrorAnalysisFileName = "MaxErrorAnalysis"
        self.averageLikelihoodAnalysisFileName = "AverageLikelihoodAnalysis"
        self.averageErrorAnalysisFileName = "AverageErrorAnalysis"
        self.mannWhitneyUTestFileName = "MannWhitneyUTestFileName"
        self.portsFileName = "PCSystemPorts"
       
  
        """
        Filenames with extension for model read, IO read/write operations of the PCSystem
        """
        # make a textFile to store the PCPorts information
        self.pcSystemPortsFileName = "PCSystemPorts.txt"
        # make a textFile to store the PCArithmeticNodes information
        self.pcSystemArithmeticNodesFileName = "PCSystemArithmeticNodes.txt"
        # read the textFile to parser PCEquation information
        self.pcEquationFileName = "PCEquation.txt"
        # read the textFile to parser PCEquation information
        self.pcSystemVHDLFileName = "PCSystem.vhd"
        # read the textFile to parser PCEquation information
        self.pcSystemVHDLTestBenchFileName = "PCSystem_tb.vhd"
        # set the textfilename for the pcInputBinaryStringTextFileName equation
        self.pcSystemVHDLSimulationInputFileName = "Input.txt"
        self.pcSystemVHDLSimulationOutputFileName = "Output.txt"
        # set the textfilename for the PCSystem compile script
        self.pcSystemVHDLCompileFileName = "compile.sh"
        # set the textfilename for the PCSystem do script
        self.pcSystemVHDLSimulationDoFileName = "run_pcsystem.do"

        self._pcSystemErrorAnalysisFileName = None
        self._pcSystemMannWhitneyUTestFileName = None
        self._pcSystemInfoFileName = None
        self._pcSystemAverageErrorAnalysisFileName = None
        self._pcSystemMaxErrorAnalysisFileName = None
        self._pcSystemHWAverageLikelihoodAnalysisFileName = None
        self._pcSystemSWAverageLikelihoodAnalysisFileName = None


    @property
    def pcModelName(self):
        return self._pcModelName 

    @pcModelName.setter
    def pcModelName(self,value):
        self._pcModelName = value
        
    @property
    def pcSystemNumberSystem(self):
        return self._pcSystemNumberSystem

    @pcSystemNumberSystem.setter
    def pcSystemNumberSystem(self,value):
        self._pcSystemNumberSystem = value
        if self._pcSystemNumberSystem == 0:
            # set the numbersystem folder name
            self.pcSystemNumberSystemFolderName = "Fixed"
        elif self._pcSystemNumberSystem == 1:
            self.pcSystemNumberSystemFolderName = "Float"
        elif self._pcSystemNumberSystem == 2:
            self.pcSystemNumberSystemFolderName = "Posit"
    
    @property
    def pcSystemNumberSystemFolderName(self):
        return self._pcSystemNumberSystemFolderName

    @pcSystemNumberSystemFolderName.setter
    def pcSystemNumberSystemFolderName(self,value):
        self._pcSystemNumberSystemFolderName = value
        
    @property
    def pcModelFolderName(self):
        return self._pcModelFolderName

    @pcModelFolderName.setter
    def pcModelFolderName(self,value):
        self._pcModelFolderName = value
        # set the model folder using the folderName
        self.pcModelFolder = os.path.join(self.pcModelParentFolder, self._pcModelFolderName)



    @property
    def pcModelType(self):
        return self._pcModelType

    @pcModelType.setter
    def pcModelType(self,value):
        # set the modelType value
        self._pcModelType = value
        # set the model parent folder based on the systemType
        if self._pcModelType == 1:
            # set the SPN model parent file folder
            self.pcModelFolderName = "SPN"
        elif self._pcModelType == 0:
            # set the SPN model parent file folder
            self.pcModelFolderName = "AC"
    
    @property
    def pcSystemSumNodeName(self):
        return self._pcSystemSumNodeName

       
    @pcSystemSumNodeName.setter
    def pcSystemSumNodeName(self,value):
        # set the modelType value
        self._pcSystemSumNodeName = value
        # PCSystem SumNode Name
    
    @property
    def pcSystemProductNodeName(self):
        return self._pcSystemProductNodeName

       
    @pcSystemProductNodeName.setter
    def pcSystemProductNodeName(self,value):
        # set the modelType value
        self._pcSystemProductNodeName = value
    
    
    @property
    def pcSystemInfoFileName(self):
        if self._pcSystemInfoFileName == None:
            self._pcSystemInfoFileName = self.systemInfoFileName + self.textFileFormatName
        return self._pcSystemInfoFileName

       
    @pcSystemInfoFileName.setter
    def pcSystemInfoFileName(self,value):
        # set the modelType value
        self._pcSystemInfoFileName = value

    @property
    def pcSystemModelEquationDecimalOutputFileName(self):
        if self._pcSystemModelEquationDecimalOutputFileName == None:
            self._pcSystemModelEquationDecimalOutputFileName = self._pcSystemModelEquationDecimalOutputFileName + self.textFileFormatName

        return self._pcSystemModelEquationDecimalOutputFileName

       
    @pcSystemModelEquationDecimalOutputFileName.setter
    def pcSystemModelEquationDecimalOutputFileName(self,value):
        # set the modelType value
        self._pcSystemModelEquationDecimalOutputFileName = value


    @property
    def pcSystemErrorAnalysisFileName(self):
        if self._pcSystemErrorAnalysisFileName == None:
            self._pcSystemErrorAnalysisFileName = self.errorAnalysisFileName + self.textFileFormatName

        return self._pcSystemErrorAnalysisFileName

       
    @pcSystemErrorAnalysisFileName.setter
    def pcSystemErrorAnalysisFileName(self,value):
        # set the modelType value
        self._pcSystemModelEquationDecimalOutputFileName = value
        
    @property
    def pcSystemMaxErrorAnalysisFileName(self):
        if self._pcSystemMaxErrorAnalysisFileName == None:
            self._pcSystemMaxErrorAnalysisFileName = self.maxErrorAnalysisFileName + self.textFileFormatName

        return self._pcSystemMaxErrorAnalysisFileName

       
    @pcSystemMaxErrorAnalysisFileName.setter
    def pcSystemMaxErrorAnalysisFileName(self,value):
        # set the modelType value
        self._pcSystemMaxErrorAnalysisFileName = value
    
    
    @property
    def pcSystemMannWhitneyUTestFileName(self):
        if self._pcSystemMannWhitneyUTestFileName == None:
            self._pcSystemMannWhitneyUTestFileName = self.mannWhitneyUTestFileName + self.textFileFormatName

        return self._pcSystemMannWhitneyUTestFileName

       
    @pcSystemMannWhitneyUTestFileName.setter
    def pcSystemMannWhitneyUTestFileName(self,value):
        # set the modelType value
        self._pcSystemMannWhitneyUTestFileName = value


    @property
    def pcSystemHWAverageLikelihoodAnalysisFileName(self):
        if self._pcSystemHWAverageLikelihoodAnalysisFileName == None:
            self._pcSystemHWAverageLikelihoodAnalysisFileName = "HW" + self.averageLikelihoodAnalysisFileName + self.textFileFormatName
        return self._pcSystemHWAverageLikelihoodAnalysisFileName

       
    @pcSystemHWAverageLikelihoodAnalysisFileName.setter
    def pcSystemHWAverageLikelihoodAnalysisFileName(self,value):
        # set the modelType value
        self._pcSystemHWAverageLikelihoodAnalysisFileName = value
        return
    
    
    @property
    def pcSystemSWAverageLikelihoodAnalysisFileName(self):
        if self._pcSystemSWAverageLikelihoodAnalysisFileName == None:
            self._pcSystemSWAverageLikelihoodAnalysisFileName = "SW" + self.averageLikelihoodAnalysisFileName + self.textFileFormatName
        return self._pcSystemSWAverageLikelihoodAnalysisFileName

       
    @pcSystemSWAverageLikelihoodAnalysisFileName.setter
    def pcSystemSWAverageLikelihoodAnalysisFileName(self,value):
        # set the modelType value
        self._pcSystemSWAverageLikelihoodAnalysisFileName = value
    
    
    @property
    def pcSystemAverageErrorAnalysisFileName(self):
        if self._pcSystemAverageErrorAnalysisFileName == None:
            self._pcSystemAverageErrorAnalysisFileName = self.averageErrorAnalysisFileName + self.textFileFormatName
        return self._pcSystemAverageErrorAnalysisFileName

       
    @pcSystemAverageErrorAnalysisFileName.setter
    def pcSystemAverageErrorAnalysisFileName(self,value):
        # set the modelType value
        self._pcSystemAverageErrorAnalysisFileName = value


    @property
    def pcSystemVHDLSimulationOutputFileName(self):
        if self._pcSystemVHDLSimulationOutputFileName == None:
            self._pcSystemVHDLSimulationOutputFileName = self.outputFileName + self.textFileFormatName
        return self._pcSystemVHDLSimulationOutputFileName

       
    @pcSystemVHDLSimulationOutputFileName.setter
    def pcSystemVHDLSimulationOutputFileName(self,value):
        # set the modelType value
        self._pcSystemVHDLSimulationOutputFileName = value

    @property
    def parentDirectory(self):
        if self._parentDirectory == None:
            # if the parentDirectory is not set, set the parent Directory
            self._parentDirectory = os.path.abspath(os.path.join(__file__, "../.."))
            #print("Parent Directory", self.parentDirectory)
        return self._parentDirectory 

    @parentDirectory.setter
    def parentDirectory(self,value):
        self._parentDirectory = value
   
    
    @property
    def pcModelParentFolder(self):
        if self._pcModelParentFolder == None:
            self._pcModelParentFolder = os.path.join(self.parentDirectory, self.pcModelParentFolderName)
        return self._pcModelParentFolder
    
    @pcModelParentFolder.setter
    def pcModelParentFolder(self, value):
        self._pcModelParentFolder = value    
   
    @property
    def pcModelFolder(self):
        return self._pcModelFolder 

    @pcModelFolder.setter
    def pcModelFolder(self,value):
        self._pcModelFolder = value
   

    @property
    def pcSystemDataFolder(self):
        if self._pcSystemDataFolder == None:
            self._pcSystemDataFolder = os.path.join(self.parentDirectory, self.pcSystemDataFolderName)
        return self._pcSystemDataFolder 

    @pcSystemDataFolder.setter
    def pcSystemDataFolder(self,value):
        self._pcSystemDataFolder = value


    @property
    def pcSystemInfoFolder(self):
        if self._pcSystemInfoFolder == None:
            self._pcSystemInfoFolder = os.path.join(self.pcSystemDataFolder, self.pcSystemInfoFolderName)
            # configure the PCSystemModelEquationDataFolder folder
            isPCSystemInfoFolder = os.path.isdir(os.path.join(self.pcSystemDataFolder,self.pcSystemInfoFolderName))
            # check if isPCSystemInfoFolder is present or not
            if isPCSystemInfoFolder == False:
                # create the directory
                os.mkdir(self._pcSystemInfoFolder)

        return self._pcSystemInfoFolder 

    @pcSystemInfoFolder.setter
    def pcSystemInfoFolder(self,value):
        self._pcSystemInfoFolder = value


    @property
    def pcSystemLogFolder(self):
        if self._pcSystemLogFolder == None:
            self._pcSystemLogFolder = os.path.join(self.pcSystemDataFolder, self.pcSystemLogFolderName)
            # configure the PCSystemModelEquationDataFolder folder
            isPCSystemLogFolder = os.path.isdir(os.path.join(self.pcSystemDataFolder,self.pcSystemLogFolderName))
            # check if isPCSystemLogFolder is present or not
            if isPCSystemLogFolder == False:
                # create the directory
                os.mkdir(self._pcSystemLogFolder)
                return

            # configure the modelequation folder inside the logs folder
            #isPCSystemModelEquationLogFolder = os.path.isdir(os.path.join(self.pcSystemDataFolder,self.pcSystemLogFolderName))

        return self._pcSystemLogFolder 

    @pcSystemLogFolder.setter
    def pcSystemLogFolder(self,value):
        self._pcSystemLogFolder = value


    @property
    def pcSystemModelEquationDataFolder(self):
        if self._pcSystemModelEquationDataFolder == None:
            # configure the PCSystemModelEquationDataFolder folder
            isPCSystemModelEquationDataFolder = os.path.isdir(os.path.join(self.pcSystemModelDataFolder,self.pcModelName))
            self._pcSystemModelEquationDataFolder = os.path.join(self.pcSystemModelDataFolder,self.pcModelName)
            # check if isPCSystemModelEquationDataFolder is present or not
            if isPCSystemModelEquationDataFolder == False:
                # create the directory
                os.mkdir(self._pcSystemModelEquationDataFolder)
        return self._pcSystemModelEquationDataFolder 

    @pcSystemModelEquationDataFolder.setter
    def pcSystemModelEquationDataFolder(self,value):
        self._pcSystemModelEquationDataFolder = value



    @property
    def pcVHDLPOSITPackageFolder(self):
        if self._pcVHDLPOSITPackageFolder == None:
            self._pcVHDLPOSITPackageFolder =  os.path.join(self.pcVHDLPackagesFolder , self.pcVHDLPOSITPackageFolderName)
            
        return self._pcVHDLPOSITPackageFolder 


    @pcVHDLPOSITPackageFolder.setter
    def pcVHDLPOSITPackageFolder(self,value):
        self._pcVHDLPOSITPackageFolder = value


    @property
    def pcSystemSimulationFolder(self):
        if self._pcSystemSimulationFolder == None:
            self._pcSystemSimulationFolder =  os.path.join(self.parentDirectory, self.pcSystemSimulationFolderName)
        return self._pcSystemSimulationFolder
    
    
    @pcSystemSimulationFolder.setter
    def pcSystemSimulationFolder(self,value):
        self._pcSystemSimulationFolder =  value

    @property
    def pcSystemIOSimulationFolder(self):
        if self._pcSystemIOSimulationFolder == None:
            self._pcSystemIOSimulationFolder =  os.path.join(self.pcSystemSimulationFolder, self.pcSystemIOSimulationFolderName)
        return self._pcSystemIOSimulationFolder
    
    
    @pcSystemIOSimulationFolder.setter
    def pcSystemIOSimulationFolder(self,value):
        self._pcSystemIOSimulationFolder =  value


    @property
    def pcVHDLPackagesFolder(self):
        if self._pcVHDLPackagesFolder == None:
            self._pcVHDLPackagesFolder = os.path.join(self.parentDirectory, self.pcSystemVHDLPackagesFolderName)
        return self._pcVHDLPackagesFolder 

    @pcVHDLPackagesFolder.setter
    def pcVHDLPackagesFolder(self,value):
        self._pcVHDLPackagesFolder = value
    
    
    @property
    def pcSystemNumberSystemFolder(self):
        if self._pcSystemNumberSystemFolder == None:
            #print("PCSystemNumberSystemFolderName", self._pcSystemNumberSystemFolderName)
            # set the pcSystemModelEquationAnalysisDataFolder
            self._pcSystemNumberSystemFolder = os.path.join(self.pcSystemModelEquationDataFolder \
                , self._pcSystemNumberSystemFolderName)
            # print the path in which the folder will be created
            #print("PCSystemNumberSystemFolder:", self._pcSystemNumberSystemFolder)
            
            # configure the PCSystemNumberSystemFolder
            isPCSystemNumberSystemFolder = os.path.isdir(self._pcSystemNumberSystemFolder)
            #print("IsPCSystemNumberSystemFolder present in directory:", isPCSystemNumberSystemFolder)

            # check if PCSystemNumberSystemFolder is present or not
            if isPCSystemNumberSystemFolder == False:
                # print the path in which the folder will be created
                #print("NumberSystemFolder:", self._pcSystemNumberSystemFolder)
                # create the directory
                os.mkdir(self._pcSystemNumberSystemFolder)
      
        return self._pcSystemNumberSystemFolder 

    @pcSystemNumberSystemFolder.setter
    def pcSystemNumberSystemFolder(self,value):
        self._pcSystemNumberSystemFolder = value


    @property
    def pcSystemModelEquationAnalysisDataFolder(self):
        if self._pcSystemModelEquationAnalysisDataFolder == None:

            # set the pcSystemModelEquationAnalysisDataFolder
            self._pcSystemModelEquationAnalysisDataFolder = os.path.join(self.pcSystemNumberSystemFolder \
                , self.pcSystemModelEquationAnalysisDataFolderName)
            
            # configure the PCSystemModelEquationDataFolder folder
            isPCSystemModelEquationAnalysisDataFolder = os.path.isdir(self._pcSystemModelEquationAnalysisDataFolder)

            # check if isPCSystemModelEquationAnalysisDataFolder is present or not
            if isPCSystemModelEquationAnalysisDataFolder == False:
                # create the directory
                os.mkdir(self._pcSystemModelEquationAnalysisDataFolder)

        return self._pcSystemModelEquationAnalysisDataFolder 

    @pcSystemModelEquationAnalysisDataFolder.setter
    def pcSystemModelEquationAnalysisDataFolder(self,value):
        self._pcSystemModelEquationAnalysisDataFolder = value
       
    
    @property
    def pcSystemModelEquationErrorAnalysisFolder(self):
        if self._pcSystemModelEquationErrorAnalysisFolder == None:
            # set the error analysis folder
            self._pcSystemModelEquationErrorAnalysisFolder = os.path.join(self.pcSystemModelEquationAnalysisDataFolder, self.pcSystemModelEquationErrorAnalysisFolderName)
            
            isPCSystemModelEquationErrorAnalysisFolder = os.path.isdir(os.path.join(self.pcSystemModelEquationAnalysisDataFolder,self.pcSystemModelEquationErrorAnalysisFolderName))

            # check if isPCSystemModelEquationErrorAnalysisFolder is present or not
            if isPCSystemModelEquationErrorAnalysisFolder == False:
                # create the directory
                os.mkdir(self._pcSystemModelEquationErrorAnalysisFolder)

        return self._pcSystemModelEquationErrorAnalysisFolder 

    @pcSystemModelEquationErrorAnalysisFolder.setter
    def pcSystemModelEquationErrorAnalysisFolder(self,value):
        self._pcSystemModelEquationErrorAnalysisFolder = value
    
    
    @property
    def pcSystemModelEquationLikelihoodAnalysisFolder(self):
        if self._pcSystemModelEquationLikelihoodAnalysisFolder == None:
            # set the error analysis folder
            self._pcSystemModelEquationLikelihoodAnalysisFolder = os.path.join(self.pcSystemModelEquationErrorAnalysisFolder, self.pcSystemModelEquationLikelihoodAnalysisFolderName)
            print("LikelihoodAnalysisFolder",self._pcSystemModelEquationLikelihoodAnalysisFolder)
            
            isPCSystemModelEquationLikelihoodAnalysisFolder = os.path.isdir(os.path.join(self.pcSystemModelEquationErrorAnalysisFolder,self.pcSystemModelEquationLikelihoodAnalysisFolderName))

            # check if _pcSystemModelEquationLikelihoodAnalysisFolder is present or not
            if isPCSystemModelEquationLikelihoodAnalysisFolder == False:
                # create the directory
                os.mkdir(self._pcSystemModelEquationLikelihoodAnalysisFolder)
            
        return self._pcSystemModelEquationErrorAnalysisFolder 


    @pcSystemModelEquationLikelihoodAnalysisFolder.setter
    def pcSystemModelEquationLikelihoodAnalysisFolder(self,value):
        self._pcSystemModelEquationLikelihoodAnalysisFolder = value



    @property
    def pcSystemModelEquationDecimalOutputFolder(self):
        if self._pcSystemModelEquationDecimalOutputFolder == None:
             # set the ModelEquationDecimal folder
             self._pcSystemModelEquationDecimalOutputFolder = os.path.join(self.pcSystemModelEquationAnalysisDataFolder \
                , self.pcSystemModelEquationDecimalOutputFolderName)
             
             isPCSystemModelEquationDecimalOutputFolder = os.path.isdir(os.path.join(self.pcSystemModelEquationAnalysisDataFolder,self.pcSystemModelEquationDecimalOutputFolderName))
             # check if isPCSystemModelEquationDecimalOutputFolder is present or not
             if isPCSystemModelEquationDecimalOutputFolder == False:
                 # create the directory
                 os.mkdir(self._pcSystemModelEquationDecimalOutputFolder)
            
        return self._pcSystemModelEquationDecimalOutputFolder 

    @pcSystemModelEquationDecimalOutputFolder.setter
    def pcSystemModelEquationDecimalOutputFolder(self,value):
        self._pcSystemModelEquationDecimalOutputFolder = value


    @property
    def pcSystemModelEquationLikelihoodAnalysisFolder(self):
        if self._pcSystemModelEquationLikelihoodAnalysisFolder == None:
             # set the Likelihood Analysis folder
             self._pcSystemModelEquationLikelihoodAnalysisFolder = os.path.join(self.pcSystemModelEquationAnalysisDataFolder , self.pcSystemModelEquationLikelihoodAnalysisFolderName)
             
             isPCSystemModelEquationLikelihoodAnalysisFolder = os.path.isdir(os.path.join(self.pcSystemModelEquationAnalysisDataFolder,self.pcSystemModelEquationLikelihoodAnalysisFolderName))
             
             # check if _pcSystemModelEquationLikelihoodAnalysisFolder is present or not
             if isPCSystemModelEquationLikelihoodAnalysisFolder == False:
                 # create the directory
                 os.mkdir(self._pcSystemModelEquationLikelihoodAnalysisFolder)

        print("PCSystemModelEquationLikelihoodAnalysisFolder", self._pcSystemModelEquationLikelihoodAnalysisFolder)  
        return self._pcSystemModelEquationLikelihoodAnalysisFolder 

    @pcSystemModelEquationLikelihoodAnalysisFolder.setter
    def pcSystemModelEquationLikelihoodAnalysisFolder(self,value):
        self._pcSystemModelEquationLikelihoodAnalysisFolder = value


    @property
    def pcSystemModelDataFolder(self):
        if self._pcSystemModelDataFolder == None:
            # set the pcSystemModelEquationAnalysisDataFolder
            self._pcSystemModelDataFolder = os.path.join(self.pcSystemDataFolder \
                , self.pcModelFolderName)

            isPCSystemModelDataFolder = os.path.isdir(os.path.join(self.pcSystemDataFolder,self.pcModelFolderName))
            # check if isPCSystemModelDataFolder is present or not
            if isPCSystemModelDataFolder == False:
                # create the directory
                os.mkdir(self._pcSystemModelDataFolder)

        return self._pcSystemModelDataFolder 


    @pcSystemModelDataFolder.setter
    def pcSystemModelDataFolder(self,value):
        self._pcSystemModelDataFolder = value

    @pcSystemSimulationFolder.setter
    def pcSystemSimulationFolder(self,value):
        self._pcSystemSimulationFolder = value


    @property
    def pcSystemVHDLFolder(self):
        # check the pcSystemVHDLFolder
        if self._pcSystemVHDLFolder == None:
            self._pcSystemVHDLFolder = os.path.join(self.pcSystemSimulationFolderName, self.pcSystemVHDLFolderName)
            # check whether the folder is already there or not
            isPCSystemVHDLDirectoryAvailable = os.path.isdir(self._pcSystemVHDLFolder)
            if isPCSystemVHDLDirectoryAvailable == False: 
                os.mkdir(self._pcSystemVHDLFolder)

        return self._pcSystemVHDLFolder

       
    @pcSystemVHDLFolder.setter
    def pcSystemVHDLFolder(self,value):
        # set the modelType value
        self._pcSystemVHDLFolder = value


    @property
    def pcSystemPOSITSumNodeVHDLPackagesFolder(self):
        # check the pcSystemVHDLFolder
        if self._pcSystemPOSITSumNodeVHDLPackagesFolder == None:
            self._pcSystemPOSITSumNodeVHDLPackagesFolder = os.path.join(self.pcVHDLPOSITPackageFolder, self.pcSystemPOSITSumNodeVHDLPackagesFolderName)

        return self._pcSystemPOSITSumNodeVHDLPackagesFolder

       
    @pcSystemPOSITSumNodeVHDLPackagesFolder.setter
    def pcSystemPOSITSumNodeVHDLPackagesFolder(self,value):
        # set the modelType value
        self._pcSystemPOSITSumNodeVHDLPackagesFolder = value
   
    
    @property
    def pcSystemPOSITProductNodeVHDLPackagesFolder(self):
        # check the pcSystemVHDLFolder
        if self._pcSystemPOSITProductNodeVHDLPackagesFolder == None:
            self._pcSystemPOSITProductNodeVHDLPackagesFolder = os.path.join(self.pcVHDLPOSITPackageFolder, self.pcSystemPOSITProductNodeVHDLPackagesFolderName)

        return self._pcSystemPOSITProductNodeVHDLPackagesFolder

       
    @pcSystemPOSITProductNodeVHDLPackagesFolder.setter
    def pcSystemPOSITProductNodeVHDLPackagesFolder(self,value):
        # set the modelType value
        self._pcSystemPOSITProductNodeVHDLPackagesFolder = value


    @property
    def pcSystemProcessedDataFolder(self):
        # check the pcSystemVHDLFolder
        if self._pcSystemProcessedDataFolder == None:
            self._pcSystemProcessedDataFolder = os.path.join(self.pcSystemDataFolder, self.pcSystemProcessedDataFolderName)

        return self._pcSystemProcessedDataFolder

       
    @pcSystemProcessedDataFolder.setter
    def pcSystemProcessedDataFolder(self,value):
        # set the modelType value
        self._pcSystemProcessedDataFolder = value


    @property
    def pcSystemVHDLSimulationDoFile(self):
        if self._pcSystemVHDLSimulationDoFile == None:
            self._pcSystemVHDLSimulationDoFile =  os.path.join(self.pcSystemIOSimulationFolder , self.pcSystemVHDLSimulationDoFileName)
            
        return self._pcSystemVHDLSimulationDoFile 



    @pcSystemVHDLSimulationDoFile.setter
    def pcSystemVHDLSimulationDoFile(self,value):
        self._pcSystemVHDLSimulationDoFile = value


    @property
    def pcSystemVHDLCompileFile(self):
        if self._pcSystemVHDLCompileFile == None:
            self._pcSystemVHDLCompileFile =  os.path.join(self.pcSystemSimulationFolder , self.pcSystemVHDLCompileFileName)
        return self._pcSystemVHDLCompileFile 


    @pcSystemVHDLCompileFile.setter
    def pcSystemVHDLCompileFile(self,value):
        self._pcSystemVHDLCompileFile = value


    @property
    def pcSystemVHDLTestBenchFile(self):
        if self._pcSystemVHDLTestBenchFile == None:
            self._pcSystemVHDLTestBenchFile =  os.path.join(self.pcSystemVHDLFolder , self.pcSystemVHDLTestBenchFileName)
            
        return self._pcSystemVHDLTestBenchFile 


    @pcSystemVHDLTestBenchFile.setter
    def pcSystemVHDLTestBenchFile(self,value):
        self._pcSystemVHDLTestBenchFile = value


    @property
    def pcSystemSWLikeliHoodFile(self):
        if self._pcSystemSWLikeliHoodFile == None:
             # set the likelihood file name
            pcModelLikelihoodFileName = "/" + self.pcModelName + "/" \
                    + self.pcModelName + "_" + "likelihoods" + self.csvFileFormatName

            print("PCModelLikelihoodFileName Location:",pcModelLikelihoodFileName)

            self._pcSystemSWLikeliHoodFile = self.pcModelFolder + pcModelLikelihoodFileName
        return self._pcSystemSWLikeliHoodFile 


    @pcSystemSWLikeliHoodFile.setter
    def pcSystemSWLikeliHoodFile(self,value):
        self.pcSystemSWLikeliHoodFile = value


    @property
    def pcModelTestDataFile(self):
        if self._pcModelTestDataFile == None:
            # set the testData file name
            pcModelTestDataFileName = "/" + self._pcModelName + "/" \
                    + self._pcModelName + "_" + "testdata" + self.csvFileFormatName
                    
            # print the testModelFile
            print("PCModelTestdata Location:",self._pcModelTestDataFile)
            # set the pcModelTestDataFile
            self._pcModelTestDataFile = self.pcModelFolder + pcModelTestDataFileName
        return self._pcModelTestDataFile 


    @pcModelTestDataFile.setter
    def pcModelTestDataFile(self,value):
        self._pcModelTestDataFile = value


    @property
    def pcModelMetaDataFile(self):
        if self._pcModelMetaDataFile == None:
             # set the likelihood file name
            pcModelMetaDataFileName = "/" + self.pcModelName + "/" \
                    + self.pcModelName + "_" + "metadata" + self.csvFileFormatName
            # set the pcmodelmetadatafile
            self._pcModelMetaDataFile = self.pcModelFolder + pcModelMetaDataFileName
        return self._pcModelMetaDataFile 


    @pcModelMetaDataFile.setter
    def pcModelMetaDataFile(self,value):
        self._pcModelMetaDataFile = value


    @property
    def pcModelEquationFile(self):
        if self._pcModelEquationFile == None:
            # set the pcModelEquation file path
            pcModelEquationFileName = "/" + self.pcModelName \
                    + "/" + self.pcModelName + "_" + "equation" + self.textFileFormatName
            self._pcModelEquationFile = self.pcModelFolder + pcModelEquationFileName
        return self._pcModelEquationFile 

    @pcModelEquationFile.setter
    def pcModelEquationFile(self,value):
        self._pcModelEquationFile = value
       
    
    @property
    def pcSystemVHDLFile(self):
        if self._pcSystemVHDLFile == None:
            self._pcSystemVHDLFile = os.path.join(self.pcSystemVHDLFolder , self.pcSystemVHDLFileName)
        return self._pcSystemVHDLFile 

    @pcSystemVHDLFile.setter
    def pcSystemVHDLFile(self,value):
        self._pcSystemVHDLFile = value
    

    @property
    def pcSystemPortsFile(self):
        if self._pcSystemPortsFile == None:
            self._pcSystemPortsFile = os.path.join(self.pcSystemModelEquationDataFolder , self.pcSystemPortsFileName)
        return self._pcSystemPortsFile 

    @pcSystemPortsFile.setter
    def pcSystemPortsFile(self,value):
        self._pcSystemPortsFile = value
       
    
    @property
    def pcSystemArithmeticNodesFile(self):
        if self._pcSystemArithmeticNodesFile == None:
            self._pcSystemArithmeticNodesFile = os.path.join(self.pcSystemModelEquationDataFolder , self.pcSystemArithmeticNodesFileName)         
        return self._pcSystemArithmeticNodesFile 

    @pcSystemArithmeticNodesFile.setter
    def pcSystemArithmeticNodesFile(self,value):
        self._pcSystemArithmeticNodesFile = value
        
    
    @property
    def pcSystemInfoFile(self):
        if self._pcSystemInfoFile == None:
            self._pcSystemInfoFile = os.path.join(self.pcSystemInfoFolder , self.pcSystemInfoFileName)         
        return self._pcSystemInfoFile 

    @pcSystemInfoFile.setter
    def pcSystemInfoFile(self,value):
        self._pcSystemInfoFile = value
    
    
    @property
    def pcSystemHWOutputFile(self):
        if self._pcSystemHWOutputFile == None:
            self._pcSystemHWOutputFile = os.path.join(self.pcSystemModelEquationDecimalOutputFolder , self.pcSystemModelEquationDecimalOutputFolderName)
            print("HWOutputFile",self._pcSystemHWOutputFile)

        return self._pcSystemHWOutputFile 

    @pcSystemHWOutputFile.setter
    def pcSystemHWOutputFile(self,value):
        self._pcSystemHWOutputFile = value
    
    
    @property
    def pcSystemErrorAnalysisFile(self):
        if self._pcSystemErrorAnalysisFile == None:
            self._pcSystemErrorAnalysisFile = os.path.join(self.pcSystemModelEquationErrorAnalysisFolder , self.pcSystemErrorAnalysisFileName)

        return self._pcSystemErrorAnalysisFile 

    @pcSystemErrorAnalysisFile.setter
    def pcSystemErrorAnalysisFile(self,value):
        self._pcSystemErrorAnalysisFile = value
       
    
    
    @property
    def pcSystemMaxErrorAnalysisFile(self):
        if self._pcSystemMaxErrorAnalysisFile == None:
            self._pcSystemMaxErrorAnalysisFile = os.path.join(self.pcSystemModelEquationErrorAnalysisFolder , self.pcSystemMaxErrorAnalysisFileName)

        return self._pcSystemMaxErrorAnalysisFile 

    @pcSystemMaxErrorAnalysisFile.setter
    def pcSystemMaxErrorAnalysisFile(self,value):
        self._pcSystemMaxErrorAnalysisFile = value
    
    
    @property
    def pcSystemMannWhitneyUTestFile(self):
        if self._pcSystemMannWhitneyUTestFile == None:
            self._pcSystemMannWhitneyUTestFile = os.path.join(self.pcSystemModelEquationLikelihoodAnalysisFolder , self.pcSystemMannWhitneyUTestFileName)
            #print(self._pcSystemMannWhitneyUTestFile)

        return self._pcSystemMannWhitneyUTestFile 

    @pcSystemMannWhitneyUTestFile.setter
    def pcSystemMannWhitneyUTestFile(self,value):
        self._pcSystemMannWhitneyUTestFile = value
        
    
    @property
    def pcSystemHWAverageLikelihoodAnalysisFile(self):
        if self._pcSystemHWAverageLikelihoodAnalysisFile == None:
            self._pcSystemHWAverageLikelihoodAnalysisFile = os.path.join(self.pcSystemModelEquationLikelihoodAnalysisFolder , self.pcSystemHWAverageLikelihoodAnalysisFileName)

        return self._pcSystemHWAverageLikelihoodAnalysisFile 

    @pcSystemHWAverageLikelihoodAnalysisFile.setter
    def pcSystemHWAverageLikelihoodAnalysisFile(self,value):
        self._pcSystemHWAverageLikelihoodAnalysisFile = value
    
    
    @property
    def pcSystemSWAverageLikelihoodAnalysisFile(self):
        if self._pcSystemSWAverageLikelihoodAnalysisFile == None:
            self._pcSystemSWAverageLikelihoodAnalysisFile = os.path.join(self.pcSystemModelEquationLikelihoodAnalysisFolder , self.pcSystemSWAverageLikelihoodAnalysisFileName)

        return self._pcSystemSWAverageLikelihoodAnalysisFile 

    @pcSystemSWAverageLikelihoodAnalysisFile.setter
    def pcSystemSWAverageLikelihoodAnalysisFile(self,value):
        self._pcSystemSWAverageLikelihoodAnalysisFile = value
    
    
    @property
    def pcSystemAverageErrorAnalysisFile(self):
        if self._pcSystemAverageErrorAnalysisFile == None:
            self._pcSystemAverageErrorAnalysisFile = os.path.join(self.pcSystemModelEquationErrorAnalysisFolder , self.pcSystemAverageErrorAnalysisFileName)
#self._pcSystemAverageErrorAnalysisFile
        return self._pcSystemAverageErrorAnalysisFile 

    @pcSystemAverageErrorAnalysisFile.setter
    def pcSystemAverageErrorAnalysisFile(self,value):
        self._pcSystemAverageErrorAnalysisFile = value
            
    
    @property
    def pcSystemVHDLSimulationOutputFile(self):
        if self._pcSystemVHDLSimulationOutputFile == None:
            self._pcSystemVHDLSimulationOutputFile = os.path.join(self.pcSystemIOSimulationFolder , self.pcSystemVHDLSimulationOutputFileName)

        return self._pcSystemVHDLSimulationOutputFile 

    @pcSystemVHDLSimulationOutputFile.setter
    def pcSystemVHDLSimulationOutputFile(self,value):
        self._pcSystemVHDLSimulationOutputFile = value
    
    
    @property
    def pcSystemVHDLSimulationInputFile(self):
        if self._pcSystemVHDLSimulationInputFile == None:
            self._pcSystemVHDLSimulationInputFile = os.path.join(self.pcSystemIOSimulationFolder , self.pcSystemVHDLSimulationInputFileName)

        return self._pcSystemVHDLSimulationInputFile

    @pcSystemVHDLSimulationInputFile.setter
    def pcSystemVHDLSimulationInputFile(self,value):
        self._pcSystemVHDLSimulationInputFile = value
