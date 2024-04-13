"""
Created by Karthekeyan Periasamy
Created on Jan 21, 16.04 AM
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
    LUTsPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("Operators Path:", operatorsPath)

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    operatorsPath = os.path.abspath(os.path.join(LUTsPath, os.pardir))
    #print("PCSystem Path:", pcSystemPath)

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(operatorsPath, os.pardir))

    print("PCSystem Path:", pcSystemPath)
    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)


if __name__ == "__main__":
    from PositLUT import PositLUT
    lut = PositLUT()
    # add the configuration details of the LUT
    lut.configurationDetailsOfLUT = {"NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":1,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":23,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"NumberOfBits":23, "EsBits":6} 
    # configure the LUT
    lut.configure()
    # process the LUT
    lut.run()
