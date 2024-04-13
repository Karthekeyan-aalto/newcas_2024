"""
Created by Karthekeyan Periasamy
Edited on April 25, 2023 11-18 AM
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
    from DeMux import DeMux
    demux = DeMux()
    # add the configuration details of the demux
    demux.configurationDetailsOfLogic = {"NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":32,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":32,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"NumberOfBits":32,"SelectSignalBits":2} 
    # configure the demux
    demux.configure()
    # process the demux
    demux.run()



    # access the file system 
    from FileSystem.PCFileSystem import PCFileSystem
    fileSystem = PCFileSystem()
    fileSystem.writeMode = 1
    fileSystem.dataToWrite = None
    # form the location to write by accessing the file system file configurationn
    fileSystem.writeLocation = None

