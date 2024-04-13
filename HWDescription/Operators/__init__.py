"""
Created by Karthekeyan Periasamy
Edited on April 2, 2023
"""

import sys
import os

def pcSystemModuleDirectory():
    
    operatorsHWDescriptionPath = os.getcwd()
    #print("Current Directory", operatorsHWDescriptionPath)
 
    hwDescriptionPath = os.path.abspath(os.path.join(operatorsHWDescriptionPath, os.pardir))
    #print("HWDescription Path:", hwDescriptionPath)
    
    pcSystemPath = os.path.abspath(os.path.join(hwDescriptionPath, os.pardir))
    #print("PCSystemPath Path:", pcSystemPath)

    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)


if __name__ == "__main__":
    from HWDescription.Operators.OperatorHWDescription import OperatorHWDescription
    operatorHWDescription = OperatorHWDescription()
    # add the configuration details of the mux
    operatorHWDescription.configurationDetailsOfHW = {"NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":1,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":23,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"NumberOfBits":23} 
    # configure the logic
    operatorHWDescription.configure()
    # process the logic
    operatorHWDescription.run()
