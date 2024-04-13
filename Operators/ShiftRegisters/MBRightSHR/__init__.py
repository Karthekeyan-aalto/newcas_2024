"""
Created by Karthekeyan Periasamy
Edited on June 14, 09:22
"""
import sys
import os

def pcSystemModuleDirectory():
    
    
    path = os.getcwd()
    #print("Current Directory", path)

    mbRightSHRPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("MBRightSHR Path:", mbRightSHRPath)

    operatorsPath = os.path.abspath(os.path.join(mbRightSHRPath, os.pardir))
    #print("Operator Path:", operatorsPath)

    pcSystemPath = os.path.abspath(os.path.join(operatorsPath, os.pardir))

    #print("PCSystem Path:", pcSystemPath)
    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)

if __name__ == "__main__":

    from Operators.ShiftRegisters.MBRightSHR.MBRightSHR import MBRightSHR
    
    mbRightSHR = MBRightSHR()
    # add the configuration details of the mbRightSHR
    mbRightSHR.configurationDetailsOfOperator = {"Name":"MBRightSHR","NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":23,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":23,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"ShiftRegisterResetType":"ASYNC","Depth":23, "Width":1,"ShiftDirection":"Right","NumberOfBits":23, "EsBits":6}
    # configure the mbRightSHR
    mbRightSHR.configure()
    # process the mbRightSHR
    mbRightSHR.run()

