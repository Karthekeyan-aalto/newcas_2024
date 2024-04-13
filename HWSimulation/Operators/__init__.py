"""
Created by Karthekeyan Periasamy
Edited on Jan 30 20:34
"""

import sys
import os

def pcSystemModuleDirectory():
    
    
    path = os.getcwd()
    #print("Current Directory", path)
    operatorsPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("Operators Path:", operatorsPath)

    hwSimulationPath = os.path.abspath(os.path.join(operatorsPath, os.pardir))
    #print("HWSimulation Path:", hwSimulationPath)

    pcSystemPath = os.path.abspath(os.path.join(hwSimulationPath, os.pardir))

    print("PCSystem Path:", pcSystemPath)
    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)

if __name__ == "__main__":
    from HWSimulation.ShiftRegisters.MBRightSHR.MBRightSHRHWSimulation import MBRightSHRHWSimulation
    mbRightSHR = MBRightSHR()
    # add the configuration details of the mbRightSHR
    mbRightSHR.configurationDetailsOfOperator = {"NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":23,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":23,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"ShiftDirection":"Right","NumberOfBits":23, "EsBits":6} 
    # configure the mbRightSHR
    mbRightSHR.configure()
    # process the mbRightSHR
    mbRightSHR.run()

