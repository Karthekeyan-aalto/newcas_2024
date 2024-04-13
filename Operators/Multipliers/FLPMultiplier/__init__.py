"""
Created by Karthekeyan Periasamy
Edited on Feb 1 2023 21:16
"""

import sys
import os

def pcSystemModuleDirectory():
   
    
    flpMultiplierPath = os.getcwd()

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    multiplierPath = os.path.abspath(os.path.join(flpMultiplierPath, os.pardir))
    #print("PCSystem Path:", pcSystemPath)

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    operatorsPath = os.path.abspath(os.path.join(multiplierPath, os.pardir))

    print("Operators Path:", operatorsPath)
    
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(operatorsPath, os.pardir))

    print("PCSystem Path:", pcSystemPath)
    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)


if __name__ == "__main__":
    from Operators.Multipliers.FLPMultiplier.FLPMultiplier import FLPMultiplier
    multiplier = FLPMultiplier()
    # add the configuration details of the multiplier
    multiplier.configurationDetailsOfOperator = {"Name":"Multiplier","Frequency":400,"NumberSystem":"Float","Number":0,"ArithmeticNodeNumber":0,"MantissaBits":23,"ExponentBits":8,"NumberOfBits":32,"Multiplicand":"0.54", "Multiplier":"v1","InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":400, "ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input", "ConstantSignalValue":0}}
    # configure the multiplier
    multiplier.configure()
    # run the multiplication
    multiplier.run()
