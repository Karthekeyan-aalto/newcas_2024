#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:49 2022

@author: Karthekeyan Periasamy
"""

from FileSystem.PCFileSystem import PCFileSystem
from Analysis.PCAnalysis import PCAnalysis

class PCSystemIOData():
    
    def __init__(self):
        # configure
        self.configure()
    

    # custom setters and getters 
    @property
    def pcSystemOutput(self):
        return self._pcSystemOutput

    @pcSystemOutput.setter
    def pcSystemOutput(self,value):
        self._pcSystemOutput = value        
    
           
    @property
    def fileSystem(self):
        return self._fileSystem

    @fileSystem.setter
    def fileSystem(self,value):
        self._fileSystem = value
       
        self.pcSystemOutput = self._fileSystem.readPCSystemOutput()

        
    @property
    def pcSystemNumberOfBits(self):
        return self._pcSystemNumberOfBits

    @pcSystemNumberOfBits.setter
    def pcSystemNumberOfBits(self,value):
        self._pcSystemNumberOfBits = value
        
    
    @property
    def pcSystemEsBits(self):
        return self._pcSystemEsBits

    @pcSystemEsBits.setter
    def pcSystemEsBits(self,value):
        self._pcSystemEsBits = value

    @property
    def pcSystemExponentBits(self):
        return self._pcSystemExponentBits

    @pcSystemExponentBits.setter
    def pcSystemExponentBits(self,value):
        self._pcSystemExponentBits = value
        
    
    @property
    def pcSystemMantissaBits(self):
        return self._pcSystemMantissaBits

    @pcSystemMantissaBits.setter
    def pcSystemMantissaBits(self,value):
        self._pcSystemMantissaBits = value

    @property
    def pcSystemNumberSystem(self):
        return self._pcSystemNumberSystem

    @pcSystemNumberSystem.setter
    def pcSystemNumberSystem(self,value):
        self._pcSystemNumberSystem = value
        
    
    @property
    def pcSystemModel(self):
        return self._pcSystemModel

    @pcSystemModel.setter
    def pcSystemModel(self,value):
        self._pcSysteModel = value
    
    
    @property
    def pcSystemType(self):
        return self._pcSystemType

    @pcSystemType.setter
    def pcSystemType(self,value):
        self._pcSystemType = value


    @property
    def analysis(self):
        return self._analysis

    @analysis.setter
    def analysis(self,value):
        self._analysis = value

      
    def processPCSystemOutput(self):
        """
        Purpose and Logic
        ------
        Process the two dimensional output array store by switching it to 
        the appropriate switching handler based on the numberSystem
        1.Check the numberSystem using pcSystemNumberSystem property
        Returns
        --------
        None.
        """
        # check the numberSystem
        if self.pcSystemNumberSystem == None:
            assert "PCSystemNumberSystem not available from the PCSystemInfo file"
            return
        
    
    def convertPCSystemOutputDataToDecimal(self):
        """
        1. Retrieve each element and convert it to float using the FloatConverter function bit2float.
        2.

        Returns
        ---------
        One dimensional array of decimal output data
        """
        pass

    def processData(self):
        """
        Purpose
        -------
        1. To call processPCSystemOutputData handler to generate decimal output values of the PCSystemOutputData

        Returns
        -------
        None.
        """
        # call the handler to process the output
        self.processPCSystemOutput()

    def connect(self):
        pass

    def configure(self):
        """
        Purpose of PCSystemIODataProcessing attributes or properties or memberVariables
        ---------
        Processing of IO from the PCSystem will be done using the helper properties and functions of this class
        1. self.pcSystemNumberSystem
        2. self.pcSystemType
        3. self.pcSystemBits
        4. self._pcSystemMaxErrorAnalysis
        
        All the above properties will be set by the PCSystemInfo property

        self._fileSystem, property to read and write information "from and to" to respective files 
        self._analysis, property to do analysis on the SW and HW output based on the given systemInfo
        """

        self.pcSystemNumberSystem = None
        self.pcSystemType = None
        self.pcSystemNumberOfBits = None
        self.pcSystemModel = None
        self.pcSystemExponentBits = None
        self.pcSystemMantissaBits = None
        self._fileSystem = None
        self._analysis = None
        self.pcSystemOutput = None
        self.pcSystemInfo = None
        self.pcSystemEsBits = None
        self.pcSystemMaxErrorAnalysis = None

    def reset(self):
        self.pcSystemNumberSystem = None
        self.pcSystemType = None
        self.pcSystemNumberOfBits = None
        self.pcSystemModel = None
        self.pcSystemExponentBits = None
        self.pcSystemMantissaBits = None
        self._fileSystem = None
        self._analysis = None
        self.pcSystemOutput = None
        self.pcSystemInfo = None
        self.pcSystemEsBits = None
        self.pcSystemMaxErrorAnalysis = None


    def main(self):
        """
        Purpose
        ---------
        The main function to process IO of the PCSystem
        self.processData function handler is called when main function is called.
       
        Returns
        -------
        None.

        """
        self.processData()
               
    def run(self):
        self.main()





           
        





      
        
