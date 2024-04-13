"""
Created by Karthekeyan Periasamy
Edited on Feb 1 2023 21:16
"""

import sys
import os

def pcSystemModuleDirectory():
   
    
    multipliersPath = os.getcwd()

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    operatorsPath = os.path.abspath(os.path.join(multipliersPath, os.pardir))
    #print("PCSystem Path:", pcSystemPath)

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(operatorsPath, os.pardir))

    print("PCSystem Path:", pcSystemPath)
    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)


if __name__ == "__main__":
    from Multiplier import Multiplier
    multiplier = Multiplier()
    # add the configuration details of the multiplier
    multiplier.configurationDetailsOfMultiplier = {"NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":1,"PortType":"Input"},{"Name":"v2","NumberOfBits":32,"PortType":"Input"},{"Name":"v3","NumberOfBits":32,"PortType":"Input"},{"Name":"weight","NumberOfBits":32,"PortType":"Input"}],"InputDataSelect":{"Name":"inputSelect","NumberOfBits":32,"PortType":"Input"},"OutputPorts":[{"Name":"vout","NumberOfBits":23,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"NumberOfBits":23, "EsBits":6} 
    # configure the multiplier
    multiplier.configure()
    # process the multiplier
    multiplier.run()
