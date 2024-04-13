"""
Created by Karthekeyan Periasamy
Edited on Mar 14, 16.29 PM
"""

"""
The below code is necessary to set the package with the necessary path
This will help running the LUT object with in PCSystem
"""

import sys
import os

def pcSystemModuleDirectory():
    
    path = os.getcwd()
    #print("Current Directory", path)
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    logicPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("Operators Path:", operatorsPath)

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(logicPath, os.pardir))
    #print("PCSystem Path:", pcSystemPath)

    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)


if __name__ == "__main__":
    from Mux import Mux
    mux = Mux()
    # add the configuration details of the LUT
    mux.configurationDetailsOfLogic = {"NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":32,"PortType":"Input"},{"Name":"v2","NumberOfBits":32,"PortType":"Input"},{"Name":"v3","NumberOfBits":32,"PortType":"Input"},{"Name":"v4","NumberOfBits":32,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":32,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"NumberOfBits":32,"SelectSignalBits":2} 
    # configure the mux
    mux.configure()
    # process the mux
    mux.run()
