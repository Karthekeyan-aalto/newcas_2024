#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:49:19 2022

@author: Karthekeyan Periasamy
"""

from Analysis.PCAnalysis import PCAnalysis
from Analysis.PCFixedAnalysis import PCFixedAnalysis
from Analysis.PCFloatAnalysis import PCFloatAnalysis
from Analysis.PCPositAnalysis import PCPositAnalysis
from FileSystem.PCFileSystem import PCFileSystem
from Configuration.PCSystemIOConfiguration import PCSystemIOConfiguration
from Configuration.PCSystemConfiguration import PCSystemConfiguration
from Operations.PCOperation import PCOperation
from Operations.PCMaxOperation import PCMaxOperation
from Operations.PCMinOperation import PCMinOperation
from ProcessData.PCSystemFixedIOData import PCSystemFixedIOData
from ProcessData.PCSystemFloatIOData import PCSystemFloatIOData
from ProcessData.PCSystemPOSITIOData import PCSystemPOSITIOData
from Graph.PCSystemGraph import PCSystemGraph
from Graph.PCFixedSystemErrorGraph import PCFixedSystemErrorGraph
from Graph.PCFloatSystemErrorGraph import PCFloatSystemErrorGraph
from Graph.PCPositSystemErrorGraph import PCPositSystemErrorGraph
from Port.Port import Port


class PCSystem ():
    
    def __init__(self):
        
        # connect other necessary packages
        self.connect()

        # PCSystem configuartion detail dictionary
        self.configurationDetailsOfSystemPackage = None
        
        # PCAnalysisPackage configuration detail dictionary
        self.configurationDetailsOfAnalysisPackage = None
        
        # PCProcessData configuration detail dictionary
        self.configurationDetailsOfProcessDataPackage = None
        
        # PCFileSystem configuartion detail dictionary
        self.configurationDetailsOfFileSystemPackage = None

        #PCSystemGraph configuration detail dictionary
        self.configurationDetailsOfGraphPackage = None
            
    """
    Custom property getters and setters
    """

    @property
    def numberOfBits(self):
        return self._numberOfBits
    
    @numberOfBits.setter
    def numberOfBits(self,value):
        self._numberOfBits = value
        # set the systemOutputPort bits
        self.outputPort.numberOfBits = self._numberOfBits
        # check the info is not None
        if self.info == None:
            # as the info object is None, we cannot set the details
            return
        # add the numberOfBits to the system info
        self.info["NumberOfBits"] = self._numberOfBits

    
    @property
    def exponentBits(self):
        return self._exponentBits
    
    @exponentBits.setter
    def exponentBits(self,value):
        self._exponentBits = value
        # set the exponent bits
        self.outputPort.exponentBits = self._exponentBits
        # check the info is not None
        if self.info == None:
            # as the info object is None, we cannot set the details
            return
        # set the exponent bits
        self.info["ExponentBits"] = self._exponentBits

   

    @property
    def mantissaBits(self):
        return self._mantissaBits
    
    @mantissaBits.setter
    def mantissaBits(self,value):
        self._mantissaBits = value
        # set the mantissaBits
        self.outputPort.mantissaBits = self._mantissaBits
        # check the info is not None
        if self.info == None:
            # as the info object is None, we cannot set the details
            return

        # set the mantissa bits
        self.info["MantissaBits"] = self._mantissaBits

    
    @property
    def esBits(self):
        return self._esBits
    
    @esBits.setter
    def esBits(self,value):
        self._esBits = value
        # set the mantissaBits
        self.outputPort.esBits = self._esBits
        # check the info is not None
        if self.info == None:
            # as the info object is None, we cannot set the details
            return
        # set the exponent bits
        self.info["EsBits"] = self._esBits



    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self,value):
        self._model = value
        print("ModelName", self._model)
        # set the model
        self.fileSystem.pcSystemModel = self._model
        # set the pcEquation variable after the setting the model name
        self.pcEquation = self.fileSystem.pcEquation
        # check the info is not None
        if self.info == None:
            # as the info object is None, we cannot set the details
            return
        # add the modelname
        self.info["Model"] = self._model


       
    @property
    def numberSystem(self):
        return self._numberSystem
    
    @numberSystem.setter
    def numberSystem(self,value):
        self._numberSystem = value
        # set the system OutputPort bits
        self.outputPort.numberSystem = self._numberSystem
        # check the info is not None
        if self.info == None:
            # as the info object is None, we cannot set the details
            return

        # add the numberSystem
        if self._numberSystem == 0:
            self.info["NumberSystem"] = "Fixed"
        elif self._numberSystem == 1:
            self.info["NumberSystem"] = "Float"
        elif self._numberSystem == 2:
            self.info["NumberSystem"] = "Posit"

    @property
    def ports(self):
        return self._ports

    @ports.setter
    def ports(self,value):
        # sort the given ports
        self._ports = value
        #print(self._ports)
        # set the pcSystemPorts to the pcSystemIOPattern
        self.ioConfiguration.ports = self._ports
        # set the sortedPorts
        self._ports = self.ioConfiguration.ports
        # set the metaData to know the portVariableCategories and category start number
        portVariableCategoriesAndStartNumber = self.fileSystem.pcSystemModelMetaData
        self.ioConfiguration.portVariableCategories = portVariableCategoriesAndStartNumber[0]
        # set the category start number
        self.ioConfiguration.portVariableCategoryStartNumber = portVariableCategoriesAndStartNumber[1]
        # set the testData 
        self.ioConfiguration.testData = self.fileSystem.pcSystemTestData
        # set the metaData to the IO
        # set the IO pattern to the fileSystem
        self.fileSystem.pcSystemIOPattern = self.ioConfiguration.pattern
        # check the info is not None
        if self.info == None:
            # as the info object is None, we cannot set the details
            return

        # add the numberOfPorts to the info object
        self.info["NumberOfPorts"] = len(self._ports)

     
    
    @property
    def arithmeticNodes(self):
        return self._arithmeticNodes

    @arithmeticNodes.setter
    def arithmeticNodes(self,value):
        # set the arithmeticNodes
        self._arithmeticNodes = value
        # check the info is not None
        if self.info == None:
            # as the info object is None, we cannot set the details
            return

        # add the _arithmeticNodes to the info object
        self.info["NumberOfAirthmeticNodes"] = len(self._arithmeticNodes)
    
    
    @property
    def shouldPCANBeOptimisedToRemoveDuplicatePCAN(self):
        return self._shouldPCANBeOptimisedToRemoveDuplicatePCAN

    @shouldPCANBeOptimisedToRemoveDuplicatePCAN.setter
    def shouldPCANBeOptimisedToRemoveDuplicatePCAN(self,value):
        # set the value of the systemType
        self._shouldPCANBeOptimisedToRemoveDuplicatePCAN = value
        # check the info is not None
        if self.info != None:
            self.info["OptimisatisePCANToRemoveDuplicatePCAN"] = self._shouldPCANBeOptimisedToRemoveDuplicatePCAN 
    
    
    @property
    def systemType(self):
        return self._systemType

    @systemType.setter
    def systemType(self,value):
        # set the value of the systemType
        self._systemType = value
        # set  the category number name map
        # set the fileSystem systemType
        if self._systemType == 0:
            self.ioConfiguration.systemType = 0
            self.fileSystem.pcSystemType = self._systemType
            # check the info is not None
            if self.info != None:
                self.info["SystemType"] = "AC"
        elif self._systemType == 1:
            self.ioConfiguration.systemType = 1
            self.fileSystem.pcSystemType = self._systemType
            # check the info is not None
            if self.info != None:
                self.info["SystemType"] = "SPN"

    """
    # Start: connectOperationsPackage
    """
    def connectOperationsPackage(self):
        """
        # Start: Properties to handle different operations of the PCSystem
        1. The operation or PCOperations are different for different states of the PCSystem
        """
        self.pcOperation = PCOperation()
        self.pcMaxOperation = PCMaxOperation()
        self.pcMinOperation = PCMinOperation()


    """
    # End: connectOperationsPackage
    """

    """
    # Start: connectProcessDataPackage
    """
    def connectProcessDataPackage(self):
        """
        1. Connect the necessary modules of the processData package
        """
        self.ioData = PCSystemFixedIOData()
        self.ioData = PCSystemFloatIOData()
        self.ioData = PCSystemPOSITIOData()

    """
    # End: connectProcessDataPackage
    """

    """
    # Start: connectConfigurationPackage
    """
    def connectConfigurationPackage(self):
        """
        PCSystem IO properties
        """
        self.configuration = PCSystemConfiguration()
        self.ioConfiguration = PCSystemIOConfiguration()

    """
    # End: connectConfigurationPackage
    """
    
    """
    # Start: connectFileSystemPackage
    """
    def connectFileSystemPackage(self):
        """
        # Start: Properties of the PCSystem to read and write file
        1. PCSystem needs PCEquation, that is accessed using the PCFileSystem
        2. PCSystem read and write synthesisable VHDL hardware files using PCFileSystem
        """
        self.fileSystem = PCFileSystem()
    """
    # End: connectFileSystemPackage
    """
    
    """
    # Start: connectAnalysisPackage
    """
    def connectAnalysisPackage(self):
        """
        Connect Analysis Package 
        1. when needed connect the fixedAnalysis module
        2. when needed connect the floatAnalysis module
        3. when needed connect the positAnalysis module
        """
        self.analysis = PCAnalysis()
        
    
    """
    # End: connectAnalysisPackage
    """
    
    """
    # Start: connectGraphPackage
    """
    def connectGraphPackage(self):
        """
        Connect Graph Package 
        """
        self.pcSystemMaxErrorGraph = PCSystemGraph()
        self.pcSystemAvgErrorGraph = PCSystemGraph()
        self.fixedPCSystemErrorGraph = None
        self.floatPCSystemErrorGraph = None
        self.positPCSystemErrorGraph = None
        
    
    """
    # End: connectAnalysisPackage
    """

    
    """
    # Start: connectPortPackage
    """
    def connectPortPackage(self):
        """
        Connect port Package 
        """
        self.outputPort = Port()
        
    """
    # End: connectPortPackage
    """
      
    """
    # Start: configureProcessDataPackage
    """
    
    def configureProcessDataPackage(self):
        # read the systemInfo using fileSystemInfo object
        pcSystemInfo = self.fileSystem.readPCSystemInfo()
        # access the pcSystemInfo
        if pcSystemInfo == None:
            assert "There is no available PCSystem Info to process the output data"
            print("Configuration of ProcessData package failed")
            return 


        self.configurationDetailsOfSystemPackage = pcSystemInfo
        # configure the system package
        self.configure()

        # configure the analysis package by setting the configuration details
        # set the configuration details for the operations package
        self.configurationDetailsOfAnalysisPackage = {"AnalysisMode":1,"ErrorAnalysisType":0,"ActivateBitOptimisation":0, "ErrorTolerance":0.001}

        # configure the analysis package
        self.configureAnalysisPackage()

        # configure the fileSystem package
        self.configureFileSystemPackage()

        # configure the processData package modules and properties
        if self.numberSystem == 0:
            self.ioData = PCSystemFixedIOData()
        elif self.numberSystem == 1:
            self.ioData = PCSystemFloatIOData()
        elif self.numberSystem == 2:
            self.ioData = PCSystemPOSITIOData()

        # set the total number of bits
        self.ioData.pcSystemNumberOfBits = self.numberOfBits
        # set the mantissa bits
        self.ioData.pcSystemMantissaBits = self.mantissaBits
        # set the exponential bits
        self.ioData.pcSystemExponentBits = self.exponentBits
        # set the es bits
        self.ioData.pcSystemEsBits = self.esBits
        # set the numberSystem bits
        self.ioData.pcSystemNumberSystem = self.numberSystem
        # set the systemType
        self.ioData.pcSystemSystemType = self.systemType
        # set the modelName
        self.ioData.pcSystemModel = self.model
        
        print("FileObject", self.fileSystem)
        # set the file system object
        self.ioData.fileSystem = self.fileSystem
        # set the analysis object
        self.ioData.analysis = self.analysis
            
    """
    # End: configureProcessDataPackage
    """
    
    """
    # Start: configureFileSystemPackage
    """
    
    def configureFileSystemPackage(self):
        # check whether the configuration details of the file system is set or not
        if self.configurationDetailsOfFileSystemPackage != None:
            print("ConfigurationOfFileSystemPackage is missing")
            print("Use the system package details and other package details to configure the fileSystem")
            # set the analysis file reset status
            self.fileSystem.resetPCSystemErrorAnalysisFile = self.configurationDetailsOfFileSystemPackage["ResetErrorAnalysisFile"]

        # set the pcsystemType
        self.fileSystem.pcSystemType = self.systemType 
        # set the filesystem with the modelName
        self.fileSystem.pcSystemModel = self.model
        # set the fileSystemNumber
        self.fileSystem.pcSystemNumberSystem = self.numberSystem
       
                       
    """
    # End: configureFileSystemPackage
    """
    
    """
    # Start: configureGraphPackage
    """
    
    def configureGraphPackage(self):
        # check whether the configuration details of the graph is set or not
        if self.configurationDetailsOfGraphPackage == None:
            print("Configuration details of the graph package is missing")
            return

        configurationDetail = self.configurationDetailsOfGraphPackage["PCSystemInfo"]

        if configurationDetail["SystemType"] == "AC":
            self.pcSystemMaxErrorGraph.pcSystemNumberSystem = 0
            self.pcSystemAvgErrorGraph.pcSystemNumberSystem = 0
        elif configurationDetail["SystemType"] == "SPN":
            self.pcSystemMaxErrorGraph.pcSystemNumberSystem = 1
            self.pcSystemAvgErrorGraph.pcSystemNumberSystem = 1
        
        self.pcSystemMaxErrorGraph.pcSystemModel = configurationDetail["Model"]
        self.pcSystemAvgErrorGraph.pcSystemModel = configurationDetail["Model"]

        # check the number of numberSystems
        numberSystems = configurationDetail["NumberSystems"]
        
        for numberSystem in numberSystems:
            if numberSystem == "Fixed":
                configurationDetail["NumberSystem"] = "Fixed"
                self.configurationDetailsOfSystemPackage = {"PCSystemInfo":configurationDetail}
                # set the configuration details of the system package
                self.configurationDetailsOfSystemPackage["NumberSystem"] = "Fixed"
                # set the configuration details of the system package
                self.configurationDetailsOfSystemPackage["SystemType"] = configurationDetail["SystemType"]
                # set the configuration details of the system package
                self.configurationDetailsOfSystemPackage["Model"] = configurationDetail["Model"]
                # configure the system package
                self.configure()

                # connect the fileSystem package
                self.connectFileSystemPackage()
                # configureFile system package
                self.configureFileSystemPackage()

                self.fixedPCSystemErrorGraph = PCFixedSystemErrorGraph()
                # set the number system for system error graph
                self.fixedPCSystemErrorGraph.pcSystemNumberSystem = self.numberSystem
                # set the fileSystem
                self.fixedPCSystemErrorGraph.fileSystem = self.fileSystem
                # set the pcsystemType
                self.fixedPCSystemErrorGraph.fileSystem.pcSystemType = self.systemType 
                # set the filesystem with the modelName
                self.fixedPCSystemErrorGraph.fileSystem.pcSystemModel = self.model
                # set the fileSystemNumber
                self.fixedPCSystemErrorGraph.fileSystem.pcSystemNumberSystem = self.numberSystem
                # extract the error values of the fixedMaxAverageErrorAnalysisGraph
                self.fixedPCSystemErrorGraph.extractValuesToPlotErrorAnalysisGraph()
                # plot the fixedPCSystemErrorGraph
                #self.fixedPCSystemErrorGraph.plotMaxAverageErrorAnalysisGraph()

                # reset the fileSystem package
                self.resetFileSystemPackage()

            elif numberSystem == "Float":
                configurationDetail["NumberSystem"] = "Float"
                self.configurationDetailsOfSystemPackage = {"PCSystemInfo":configurationDetail}
                # set the configuration details of the system package
                self.configurationDetailsOfSystemPackage["NumberSystem"] = "Float"
                # set the configuration details of the system package
                self.configurationDetailsOfSystemPackage["SystemType"] = configurationDetail["SystemType"]
                # set the configuration details of the system package
                self.configurationDetailsOfSystemPackage["Model"] = configurationDetail["Model"]


                # connect the fileSystem package
                self.connectFileSystemPackage()

                # configure the system package
                self.configure()

                # configureFile system package
                self.configureFileSystemPackage()

                # initialise a global variable to
                self.floatPCSystemErrorGraph = PCFloatSystemErrorGraph()
                # set the number system for system error graph
                self.floatPCSystemErrorGraph.pcSystemNumberSystem = self.numberSystem
                # set the fileSystem
                self.floatPCSystemErrorGraph.fileSystem = self.fileSystem
                # set the pcsystemType
                self.floatPCSystemErrorGraph.fileSystem.pcSystemType = self.systemType 
                # set the filesystem with the modelName
                self.floatPCSystemErrorGraph.fileSystem.pcSystemModel = self.model
                # set the fileSystemNumber
                self.floatPCSystemErrorGraph.fileSystem.pcSystemNumberSystem = self.numberSystem
                # extract the error values of the fixedMaxAverageErrorAnalysisGraph
                self.floatPCSystemErrorGraph.extractValuesToPlotErrorAnalysisGraph()
                # plot the fixedPCSystemErrorGraph
                #self.floatPCSystemErrorGraph.plotMaxAverageErrorAnalysisGraph()
                
                # reset the fileSystem package
                self.resetFileSystemPackage()


            elif numberSystem == "Posit":
                configurationDetail["NumberSystem"] = "Posit"
                self.configurationDetailsOfSystemPackage = {"PCSystemInfo":configurationDetail}
                # set the configuration details of the system package
                self.configurationDetailsOfSystemPackage["NumberSystem"] = "Posit"
                # set the configuration details of the system package
                self.configurationDetailsOfSystemPackage["SystemType"] = configurationDetail["SystemType"]
                # set the configuration details of the system package
                self.configurationDetailsOfSystemPackage["Model"] = configurationDetail["Model"]

                
                # connect the fileSystem package
                self.connectFileSystemPackage()

                # configure the system package
                self.configure()

                # configureFile system package
                self.configureFileSystemPackage()

                # initialise a global variable to
                self.positPCSystemErrorGraph = PCPositSystemErrorGraph()
                # set the number system for system error graph
                self.positPCSystemErrorGraph.pcSystemNumberSystem = self.numberSystem
                # set the fileSystem
                self.positPCSystemErrorGraph.fileSystem = self.fileSystem
                # set the pcsystemType
                self.positPCSystemErrorGraph.fileSystem.pcSystemType = self.systemType 
                # set the filesystem with the modelName
                self.positPCSystemErrorGraph.fileSystem.pcSystemModel = self.model
                # set the fileSystemNumber
                self.positPCSystemErrorGraph.fileSystem.pcSystemNumberSystem = self.numberSystem
                # extract the error values of the fixedMaxAverageErrorAnalysisGraph
                self.positPCSystemErrorGraph.extractValuesToPlotErrorAnalysisGraph()
                # plot the fixedPCSystemErrorGraph
                #self.positPCSystemErrorGraph.plotMaxAverageErrorAnalysisGraph()
                
                # reset the fileSystem package
                self.resetFileSystemPackage()

                              
    """
    # End: configureGraphPackage
    """

    def plotPCSystemGraph(self):
        # now initialise the systemGraph
        # assign the fixedAvgt error values, floatAvg error values, positAvg error values
        if self.positPCSystemErrorGraph != None:
            print(self.pcSystemAvgErrorGraph.positSystemAvgErrorValues) 
            self.pcSystemAvgErrorGraph.positSystemAvgErrorValues = self.positPCSystemErrorGraph.positSystemAvgErrorValues
        if self.floatPCSystemErrorGraph != None:
            self.pcSystemAvgErrorGraph.floatSystemAvgErrorValues = self.floatPCSystemErrorGraph.floatSystemAvgErrorValues
        if self.fixedPCSystemErrorGraph != None:
            self.pcSystemAvgErrorGraph.fixedSystemAvgErrorValues = self.fixedPCSystemErrorGraph.fixedSystemAvgErrorValues
        self.pcSystemAvgErrorGraph.plotAvgErrorAnalysisGraph()
        
        # assign the fixedAvgt error values, floatAvg error values, positAvg error values
        if self.positPCSystemErrorGraph != None:
            self.pcSystemMaxErrorGraph.positSystemMaxErrorValues = self.positPCSystemErrorGraph.positSystemMaxErrorValues
        if self.floatPCSystemErrorGraph != None:
            self.pcSystemMaxErrorGraph.floatSystemMaxErrorValues = self.floatPCSystemErrorGraph.floatSystemMaxErrorValues
        if self.fixedPCSystemErrorGraph != None:
            self.pcSystemMaxErrorGraph.fixedSystemMaxErrorValues = self.fixedPCSystemErrorGraph.fixedSystemMaxErrorValues
        self.pcSystemMaxErrorGraph.plotMaxErrorAnalysisGraph()
    
    """
    # Start: configureAnalysisPackage
    """
    
    def configureAnalysisPackage(self):
        # check the configuration details object
        if self.configurationDetailsOfAnalysisPackage == None:
            print("Analysis package cannot be configured")
            return

        # read the configuration details dictionary
        configurationDetails = self.configurationDetailsOfAnalysisPackage
        # check whether the bitoptimisation is set or not
        activateBitOptimisation = configurationDetails["ActivateBitOptimisation"]

        # check the number system of the PCSystem 
        # Then, connect the appropriate Analysis module
        # numberSystem 0 = fixed, 1 = float, 2 = posit

        if self.numberSystem == 0:
            # set the analysis as the fixedAnalysis
            self.analysis = PCFixedAnalysis()
            # set the analysis numberSystem
            self.analysis.numberSystem = self.numberSystem
            self.analysis.errorTolerance = configurationDetails["ErrorTolerance"]

        elif self.numberSystem == 1:
            # set the analysis as floatAnalysis 
            self.analysis = PCFloatAnalysis()
            # set the analysis numberSystem
            self.analysis.numberSystem = self.numberSystem
            self.analysis.errorTolerance = configurationDetails["ErrorTolerance"]

        elif self.numberSystem == 2:
            # set the analysis as floatAnalysis
            self.analysis = PCPositAnalysis()
            # set the analysis numberSystem
            self.analysis.numberSystem = self.numberSystem
            self.analysis.errorTolerance = configurationDetails["ErrorTolerance"]
            print("Posit Analysis ErrorTolerance", self.analysis.errorTolerance)
            

        # check the errorType from the systemInfo
        if configurationDetails["ErrorAnalysisType"] == "RelativeError":
            self.analysis.errorType = 0
            self.info["ErrorAnalysisType"] = "RelativeError"
        elif configurationDetails["ErrorAnalysisType"] == "AbsoluteError":
            self.analysis.errorType = 1
            self.info["ErrorAnalysisType"] = "AbsoluteError"


        # check the activateBitOptimisation
        if activateBitOptimisation == 1:
            # if bit optimisation is true, set the analysisMode as 0, that signifies operation is PCMinOperation
            self.analysis.mode = 0
            # configure the PCMinOperation
            self.configurePCMinOperation()
            # processPCEquation the PCMinOperation
            self.__performPCMinOperation()
            # set the analysis mode and return as it can help in processPCEquationing other operations based on the given analysis mode
            self.analysis.mode = configurationDetails["AnalysisMode"]
            return


        # analysis mode is to decide, whether we need to normal PCOperation or PCMAxOperation
        # PCMaxOperation is used to do inference.
        # if the analysis.mode is set to 1, means normal parsing of the equation to form the PCSystemVHDL
        # if the system and its analysis mode is set, the errorType will be used to do absolute error or relative error based on the type of the error

        self.analysis.mode = configurationDetails["AnalysisMode"]
        # check the numberSystem and set the analysis numberOfBits, manitssaBits, exponentBits, esBits
        if self.numberSystem == 0:
            # set the total number of bits
            self.analysis.numberOfBits = self.numberOfBits
            # set the mantissa bits
            self.analysis.mantissaBits = self.mantissaBits
        elif self.numberSystem == 1:
            # set the total number of bits
            self.analysis.numberOfBits = self.numberOfBits
            # set the mantissa bits
            self.analysis.mantissaBits = self.mantissaBits
            # set the exponential bits
            self.analysis.exponentBits = self.exponentBits
        elif self.numberSystem == 2:
            # set the total number of bits
            self.analysis.numberOfBits = self.numberOfBits
            # set the mantissa bits
            self.analysis.mantissaBits = self.mantissaBits
            # set the exponential bits
            self.analysis.exponentBits = self.exponentBits
            # set the es bits
            self.analysis.esBits = self.esBits
    
    """
    # End: configureAnalysisPackage
    """



    """
    # Start: configurePCOperation
    """
    
    def configurePCOperation(self):
        # reset the resetPCOperation
        self.pcOperation.resetPCOperation()
        # set the pcEquation to the pcOperation
        self.pcOperation.equation = self.pcEquation
        # set the pcOperation analysisMode
        self.pcOperation.analysisMode = self.analysis.mode
        # set the number of bits
        self.pcOperation.numberOfBits = self.numberOfBits
        # set the exponent bits
        self.pcOperation.exponentBits = self.exponentBits
        # set the mantissa  bits
        self.pcOperation.mantissaBits = self.mantissaBits
        # set the es bits
        self.pcOperation.esBits = self.esBits
        # set property to PC Operation to optimise the generate arithmetic nodes
        self.pcOperation.optimisePCANToRemoveDuplicatePCAN = self.shouldPCANBeOptimisedToRemoveDuplicatePCAN


        # set the pcOperation numberSystem
        self.pcOperation.numberSystem = self.numberSystem
        # first check whether there are any ports
        if len(self.pcOperation.ports) > 0:
            # the configuration is possible
            # access the ports
            for port in self.pcOperation.ports:
                # set the portName as a key and set the value of the key to 1 in a global dictionary
                self.pcOperation.inputToPorts[port.name] = "1"
            #print("The pcOperation.inputToPorts are:", self.pcOperation.inputToPorts)
 
        # set the current operation variable with the pcOperation object
        self.currentPCSystemOperation = self.pcOperation
    
    
    """
    # End: configurePCOperation
    """

    """
    # Start: configurePCMinOperation
    """
    
    def configurePCMinOperation(self):
        # reset the EquationParser and PCEquationParser
        self.pcMinOperation.resetPCMinOperation()
        # set the pcEquation to the pcMinOperation
        self.pcMinOperation.equation = self.pcEquation
        
        # first check whether there are any ports
        if len(self.pcMinOperation.ports) > 0:
            # the configuration is possible
            # access the ports
            for port in self.pcMinOperation.ports:
                # set the portName as a key and set the value of the key to 1 in a global dictionary
                self.pcMinOperation.inputToPorts[port.name] = "1"
            # once the inputToPorts are set, configuration for sensitivity analysis is complete
            # set the inputPort
        #print("The inputToPorts are:", self.inputToPorts)
        # set the current operation variable with the pcMinOperation object
        self.currentPCSystemOperation = self.pcMinOperation
    
    
    """
    # End: configurePCMinOperation
    """
    
    """
    # Start: configurePCMaxOperation
    """
    
    def configurePCMaxOperation(self):
        # reset the resetPCOperation
        self.pcMaxOperation.resetPCOperation()
        # set the pcEquation to the pcOperation
        self.pcMaxOperation.equation = self.pcEquation
        # first check whether there are any ports
        if len(self.pcOperation.ports) > 0:
            # the configuration is possible
            # access the ports
            for port in self.pcOperation.ports:
                # set the portName as a key and set the value of the key to 1 in a global dictionary
                self.pcOperation.inputToPorts[port.name] = "1"
            #print("The pcOperation.inputToPorts are:", self.pcOperation.inputToPorts)
        # set the current operation variable with the pcMinOperation object
        self.currentPCSystemOperation = self.pcMaxOperation
    
    
    """
    # End: configurePCMaxOperation
    """
    
    def configurePCFileSystem(self):
        # set the pcSystem type to the file system
        self.fileSystem.pcSystemType = self.systemType
        # set the ports
        self.fileSystem.pcSystemPorts = self.ports
        # set the arithmeticNodes
        self.fileSystem.pcSystemArithmeticNodes = self.arithmeticNodes
        # set the output node of the PCSystem to the PCFileSystem
        self.fileSystem.pcSystemOutputPort = self.outputPort
        #print("OutputPort ExponentBits:", self.outputPort.exponentBits)
        # set the fileSytem 
        self.fileSystem.pcSystemNumberSystem = self.numberSystem
        # set the pcSystem Info
        self.fileSystem.pcSystemInfo = {"PCSystemInfo" :self.info}
        
    
    def writeToPCFileSystem(self):
        # write the PCSystemInfo
        self.fileSystem.writePCSystemInfo()
        # write the PCSystemPorts of the respective analysis in a file
        self.fileSystem.writePCSystemPorts()
        # write the PCSystemArithmeticNodes of the respective analysis in a file
        self.fileSystem.writePCSystemArithmeticNodes()
        # set the fileSystem
        self.fileSystem.writePCSystemInputBinaryString()
        # write the ports of the respective analysis in a file
        self.fileSystem.writePCSystemVHDL()
        # write the PCSystemVHDLTestBench
        self.fileSystem.writePCSystemVHDLTestBench()        
        
    
    def processPCEquation(self):
        """
        Function to processPCEquation the analysis based on the set analysisMode.
        For any state of the PCSystem, we use this analysis mode to route, configure, reset and process the information for the respecitve operations of the PCSystem
        Returns
        -------
        None.
        """
        # processPCEquation the respective operation based on the set analysis mode
        if self.analysis.mode == 1:
            # configure the PCOperation
            self.configurePCOperation()
           
            # processPCEquation PCOperation
            print("\n\n ********* Start analysis: PCOperation ******** \n")
            self.pcOperation.performPCOperation()
            # access the arithmeticNodes and set it to PCSystem property
            self.arithmeticNodes = self.pcOperation.arithmeticNodes
            print("The total number of PCSystem ArithmeticNodes:", len(self.arithmeticNodes))


            # check if the optimisation flag is set or not
            if self.shouldPCANBeOptimisedToRemoveDuplicatePCAN == True:
                # access the optimised arithmetic nodes from the pcOperation arithmetic node optimiser
                self.optimisedArithmeticNodes = self.pcOperation.pcArithmeticNodeOptimiser.optimisedArithmeticNodes
                # set the optmised arithmetic nodes to the arithmetic nodes
                self.arithmeticNodes = self.optimisedArithmeticNodes

            # access the ports of PCOperation and set it to PCSystem property
            self.ports = self.pcOperation.ports
            print("\n\n *********  End analysis: PCOperation ******** \n")
            
            #print the printPCSystemInformation
            self.printPCSystemInformation()
            # confifgure the PCFileSystem
            self.configurePCFileSystem()
            # write to PCFileSystem
            self.writeToPCFileSystem()
        
        elif self.analysis.mode == 2:
            # configure the PCMaxOperation
            self.configurePCMaxOperation()
            # set the number of bits
            self.pcOperation.numberOfBits = self.numberOfBits
            
            # processPCEquation PCOperation
            print("\n\n ********* Start analysis: PCMaxOperation ******** \n")
            self.pcMaxOperation.performPCMaxOperation()
            # access the arithmeticNodes and set it to PCSystem property
            self.arithmeticNodes = self.pcMaxOperation.arithmeticNodes
            # access the ports of PCMaxOperation and set it to PCSystem property
            self.ports = self.pcMaxOperation.ports
            print("\n\n *********  End analysis: PCMaxOperation ******** \n")
            
            #print the printPCSystemInformation
            self.printPCSystemInformation()
            # confifgure the PCFileSystem
            self.configurePCFileSystem()
            # write to PCFileSystem
            self.writeToPCFileSystem()
            
        
    
    def __performPCMinOperation(self):
        """
        Function to processPCEquation the analysis based on the set analysisONOFF property.
        For any analysis mode of the PCSystem, we use this analysisONOFF to understand whether minAnalysis is needed or not to route, configure, reset and process the information
        Returns
        -------
        None.
        """
        
        print("\n\n ********* Start Analysis:  Bit optimisation analysis ******** \n")

       
        print("\n\n ********* Start analysis: PCMinOperation ******** \n")
        # processPCEquation PCMinOperation
        self.pcMinOperation.performPCMinOperation()
        print("\n\n *********  End analysis: PCMinOperation ******** \n")
        
        print("ErrorTolerance",self.analysis.errorTolerance)

        # access the minValue of pcMinOperation and set the min value to the probability value of the analysis object
        self.analysis.probabilityValue = self.pcMinOperation.minValue
   
        # check the pcSystem numberSystem type
        if self.numberSystem == 0:
            # set the total number of bits
            self.numberOfBits = self.analysis.numberOfBits
        elif self.numberSystem == 1:
            # set the total number of bits
            self.numberOfBits = self.analysis.numberOfBits
            # set the mantissa bits
            self.mantissaBits = self.analysis.mantissaBits
            # set the exponential bits
            self.exponentBits = self.analysis.exponentBits
        elif self.numberSystem == 2:
            # set the total number of bits
            self.numberOfBits = self.analysis.numberOfBits
            # set the mantissa bits
            self.mantissaBits = self.analysis.mantissaBits
            # set the es bits
            self.esBits = self.analysis.esBits

        print("\n\n ********* End Analysis: Bit Optimisation analysis ******** \n")
               
    


    def processIOData(self):
        # access the ioData object and call processData function
        self.ioData.processData()


    def printPCSystemInformation(self):
        
        print("The total number of PCSystem bits:", self.numberOfBits)
        print("The min value of PCSystem:", self.pcMinOperation.minValue)
        
        print("the number of ports:", len(self.ports))
        
        print("PCOperartion total number of nodes.....")
        
        print("the number of ProductNodes:", len(self.pcOperation.productNodes))
        print("the number of SumNodes:", len(self.pcOperation.sumNodes))
        
        print("PCMinOperation total number of nodes.....")
        
        print("the number of PCMInOperation ProductNodes:", len(self.pcMinOperation.productNodes))
        print("the number of PCMInOperation MinNodes:", len(self.pcMinOperation.minNodes))
        
        print("PCMaxOperation total number of nodes.....")
        
        print("the number of ProductNodes:", len(self.pcMaxOperation.productNodes))
        print("the number of MaxNodes:", len(self.pcMaxOperation.maxNodes))
        
        if self.shouldPCANBeOptimisedToRemoveDuplicatePCAN == True:
            print("The total number of PCSystem Optimised ArithmeticNodes:", len(self.pcOperation.pcArithmeticNodeOptimiser.optimisedArithmeticNodes))
        print("The total number of PCSystem MMACUnitOperationsPerformed:", self.mmacUnitOperationsPerformed)
        print("The total number of PCSystem MMACUnits:", len(self.mmacUnits))

    
    
    def connect(self):
        # connect the analysis package
        self.connectAnalysisPackage()

        # connect the FileSystem Package
        self.connectFileSystemPackage()
        
        # connect the Configuration Package, especially IOConfiguration module
        self.connectConfigurationPackage()

        # connect the processData package, especially connect all the modules
        self.connectProcessDataPackage()

        # connect the operations package, especially connect all the modules
        self.connectOperationsPackage()

        # connect the Graph package
        self.connectGraphPackage()

        # connect port package
        self.connectPortPackage()

    
    
    # configure the PCSystem
    def configure(self):

        # check the configuration details of the PCSystem
        if self.configurationDetailsOfSystemPackage == None:
            #print("Configuration details for system package is missing")
            return

        # access the configuration details of the PCSystem
        configurationDetails = self.configurationDetailsOfSystemPackage["PCSystemInfo"]

        # configure the PCSystem from the configuration details
        
        # number of bits for the PCSystem
        # the variable will be set afer execution of PCMinOperation object and analysis processPCEquationed by PCAnalysis object
        # the exponentBits of the PCSystem, this will be used when the numberSystem is 2
        # the manitssaBits of the PCSystem, this will be used in the future to represent the numberSystem 2, that is Float
        # the esBits of the PCSystem, this will be used to represent the numberSystem 3, that is POSIT
        # numberSystem of the PCSystem
        # systemType 0) AC 1) SPN
        # error analysis type 0) relative error 1) absolute error
        # the variable will have custom setter to update the analysis object
        
        # property to store the information about the PCSystem in the form of a dictionary
        self.info = dict()
        #print("ConfigurationDetails",configurationDetails)
        # check whether the key NumberOfBits is present or not
        if "NumberOfBits" in configurationDetails:
            # set the number of bits
            self.numberOfBits = configurationDetails["NumberOfBits"]
        
        # check whether the key ExponentBits is present or not
        if "ExponentBits" in configurationDetails:
            # set the exponent bits
            self.exponentBits = configurationDetails["ExponentBits"]

        # check whether the key MantissaBits is present
        if "MantissaBits" in configurationDetails:
            # set the exponent bits
            self.mantissaBits = configurationDetails["MantissaBits"]
        
        # check whether the key EsBits is present
        if "EsBits" in configurationDetails:
            # set the esBits 
            self.esBits = configurationDetails["EsBits"]
        
        
        # check whether the key NumberSystem is present
        if "NumberSystem" in configurationDetails:
            # set the system number system
            pcSystemNumberSystem = configurationDetails["NumberSystem"]
            if pcSystemNumberSystem == "Fixed":
                self.numberSystem = 0
                print(self.numberSystem)
            elif pcSystemNumberSystem == "Float":
                self.numberSystem = 1
            elif pcSystemNumberSystem == "Posit":
                self.numberSystem = 2

        # check whether the key SystemType is present
        if "SystemType" in configurationDetails:
            pcSystemType = configurationDetails["SystemType"]
            # set the system type 
            if pcSystemType == "SPN":
                self.systemType = 1
            elif pcSystemType == "AC":
                self.systemType = 0
        
        # check whether the key NumberSystem is present
        if "Model" in configurationDetails:
            # set the model name
            self.model = configurationDetails["Model"]
           
        
        # check whether the key for port optimistation is present or not
        # if port optimistation is present, a single bit port is expected else a multi bit port is expected.
        if "OptimisePCANToRemoveDuplicatePCAN" in configurationDetails:
            # check the configuration details whether PCAN duplicate optimistaion is present in configuration details or not
            self.shouldPCANBeOptimisedToRemoveDuplicatePCAN = configurationDetails["OptimisePCANToRemoveDuplicatePCAN"]


        """
        Properties of PCSystem that needs to be configured
        """
        # new property to store the system ports
        self._ports = list()
        # inputToPorts, a dictionary to set the value of an input port
        self.inputToPorts = dict()
        # property to store the current number of MMACUnitOperationsPerformed
        self.mmacUnitOperationsPerformed = 0
        # property to store the systemMMACUnits
        self.mmacUnits = list()
        # new property to store both the arithmetic nodes
        self._arithmeticNodes = list()

        """
        Properties that make configuring analysis package possible
        """
        # expected to be a dictionary to store the details for configuring analysis package
        self.configurationDetailsOfAnalysisPackage = None
               
        # property to know the current operaiton of the PCSystem
        self.currentPCSystemOperation = None
    
    """
    # Start: reset PCSystem function
    """
    def reset(self):
        # reset all the operations
        self.pcOperation.resetPCOperation()
        self.pcMinOperation.resetPCMinOperation()
        # reset the PCSystem Info object
        self.info = None
        
    """
    # End: reset PCSystem function
    """
    
    """
    # Start: resetFileSystemPackage
    """
    def resetFileSystemPackage(self):
        self.fileSystem = None
               
    """
    # End: resetFileSystemPackage
    """
    
    """
    # Start: resetAnalysisPackage
    """
    def resetAnalysisPackage(self):
        self.analysis = None
               
    """
    # End: resetAnalysisPackage
    """



    def main(self):
        """
        The main funcationality of the main function is to parser the equation
        For parsing the equation will call the object PCOperation
        However, based on the analysis Mode different PCOperation child class functions will be called to processPCEquation the state functions

        Returns
        -------
        None.

        """
        # configure packages
        # check whether the pcEquation member variable is not empty
        if len(self.pcEquation) == 0:
            assert 'Empty PCEquation String: No PCEquation found in FileSystem'
            return
        self.processPCEquation()
        
    def run(self):
        self.main()
        
        
