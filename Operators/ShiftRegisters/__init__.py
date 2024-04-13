"""
Created by Karthekeyan Periasamy
Edited on Apr 25, 2023, 12:53 PM
"""
import sys
import os

def pcSystemModuleDirectory():
    
    path = os.getcwd()
    #print("Current Directory", path)
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    operatorsPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("Operators Path:", operatorsPath)
    
    pcSystemPath = os.path.abspath(os.path.join(operatorsPath, os.pardir))
    #print("PCSystem Path:", pcSystemPath)

    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)

if __name__ == "__main__":
    from Operators.ShiftRegisters.ShiftRegister import ShiftRegister
    register = ShiftRegister()
    # add the configuration details of the register
    register.configurationDetailsOfOperator = {"NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":1,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":23,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"NumberOfBits":23,"Depth":23,"Width":1,"ShiftDirection":"Right","SensitivityList":["clk","rst"]} 
    # configure the logic
    register.configure()
    # process the logic
    register.run()


