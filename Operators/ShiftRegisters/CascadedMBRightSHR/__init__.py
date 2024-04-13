"""
Created by Karthekeyan Periasamy
Edited on August 30, 01:27 PM
"""
import sys
import os

def pcSystemModuleDirectory():
    
    
    path = os.getcwd()
    #print("Current Directory", path)

    cascadeMBRightSHRPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("CascadedMBRightSHR Path:", cascadeMBRightSHRPath)

    operatorsPath = os.path.abspath(os.path.join(cascadeMBRightSHRPath, os.pardir))
    #print("Operator Path:", operatorsPath)

    pcSystemPath = os.path.abspath(os.path.join(operatorsPath, os.pardir))

    #print("PCSystem Path:", pcSystemPath)
    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)

if __name__ == "__main__":

    from Operators.ShiftRegisters.CascadedMBRightSHR.CascadedMBRightSHR import CascadedMBRightSHR
    
    cascadedMBRightSHR = CascadedMBRightSHR()
    # add the configuration details of the cascadedMBRightSHR
    cascadedMBRightSHR.configurationDetailsOfOperator = {"Name":"CascadedMBRightSHR","CascadeRegister":True,"NumberOfCascadeStage":2,"NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":23,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":23,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"ShiftRegisterResetType":"ASYNC","Depth":23, "Width":1,"ShiftDirection":"Right","NumberOfBits":23, "EsBits":6}
    # configure the mbRightSHR
    mbRightSHR.configure()
    # process the mbRightSHR
    mbRightSHR.run()

