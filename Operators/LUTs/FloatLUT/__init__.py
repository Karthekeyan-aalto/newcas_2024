"""
Created by Karthekeyan Periasamy
Edited on Jan 26 13:15 (Today is India's 74th Republic Day)
"""


import sys
import os

def pcSystemModuleDirectory():
    
    path = os.getcwd()
    #print("Current Directory", path)
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    lutPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("Operators Path:", operatorsPath)

    operatorsPath = os.path.abspath(os.path.join(lutPath, os.pardir))
    print("Operators Path:", operatorsPath)

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(operatorsPath, os.pardir))
    print("PCSystem Path:", pcSystemPath)

    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)


if __name__ == "__main__":
    from FloatLUT import FloatLUT
    lut = FloatLUT()
    # add the configuration details of the LUT
    lut.configurationDetailsOfLUT = {"NumberSystem":"Float","InputDataPorts":[{"Name":"v1","NumberOfBits":1,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":32,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"NumberOfBits":32, "MantissaBits":24, "ExponentBits":8, "Name":"FloatLUT"} 
    # configure the LUT
    lut.configure()
    # process the LUT
    lut.run()


