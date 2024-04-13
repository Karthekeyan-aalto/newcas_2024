#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jan 18 08:52 2023

@author: Karthekeyan Periasamy
"""

import sys
import os

def pcSystemModuleDirectory():
    
    path = os.getcwd()
    #print("Current Directory", path)
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("Operators Path:", operatorsPath)

    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)




if __name__ == "__main__":
    from Operators.Operator import Operator
    operator = Operator()
    # add the configuration details of the mux
    operator.configurationDetailsOfOperator = {"NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":1,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":23,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"NumberOfBits":23} 
    # configure the logic
    operator.configure()
    # process the logic
    operator.run()
