#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 23 15:23 2023

@author: Karthekeyan Periasamy
"""

class SWSynthesiser():
    
    def __init__(self):
        self.connect()
    
    @property
    def arithmeticNodes(self):
        return self._arithmeticNodes

    @arithmeticNodes.setter
    def arithmeticNodes(self,value):
        self._arithmeticNodes  = value

    
    def connect(self):
        self.connectProperties()
    
    def connectProperties(self):
        #property to store the arithmetic nodes
        self._arithmeticNodes = None

    def configure(self):
        if self.configurationDetailsOfSynthesiser == None:
            return

        configurationDetails = self.configurationDetailsOfSynthesiser

        if "ArithmeticNodes" in configurationDetails:
            self.arithmeticNodes = configurationDetails["ArithmeticNodes"]

    
    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        #property to store the arithmetic nodes
        self._arithmeticNodes = None

    def process(self):
        pass
   
    def perform(self):
        pass
    
    def main(self):
        self.process()
        self.perform()
    
    def run(self):
        self.main()
