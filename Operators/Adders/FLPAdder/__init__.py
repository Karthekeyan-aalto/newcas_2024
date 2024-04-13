"""
Created by Karthekeyan Periasamy
Edited on Dec 23 2023 14:41
"""

import sys
import os

def pcSystemModuleDirectory():
   
    
    flpAdderPath = os.getcwd()

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    addersPath = os.path.abspath(os.path.join(flpAdderPath, os.pardir))
    #print("PCSystem Path:", pcSystemPath)

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    operatorsPath = os.path.abspath(os.path.join(addersPath, os.pardir))

    print("Operators Path:", operatorsPath)
    
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(operatorsPath, os.pardir))

    print("PCSystem Path:", pcSystemPath)
    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)

if __name__ == "__main__":
    from Operators.Adders.FLPAdder.FLPAdder import FLPAdder
    adder = FLPAdder()
    # add the configuration details of the adder
    adder.configurationDetailsOfOperator = {"Name":"Adder","Frequency":400,"NumberSystem":"Float","Number":0,"ArithmeticNodeNumber":0,"MantissaBits":23,"ExponentBits":8,"NumberOfBits":32,"Augend":"v1", "Addend":"v2","InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":400, "ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input", "ConstantSignalValue":0}}
    # configure the adder
    adder.configure()
    # run the summation
    adder.run()
