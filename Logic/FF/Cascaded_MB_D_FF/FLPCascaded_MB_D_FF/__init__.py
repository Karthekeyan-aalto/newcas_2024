"""
Created by Karthekeyan Periasamy
Edited on Feb 1 2023 21:16
"""

import sys
import os

def pcSystemModuleDirectory():
   
    
    flpcascadedffPath = os.getcwd()

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    cascadedffPath = os.path.abspath(os.path.join(flpcascadedffPath, os.pardir))
    #print("PCSystem Path:", pcSystemPath)
    
    ffPath = os.path.abspath(os.path.join(cascadedffPath, os.pardir))
    
    logicPath = os.path.abspath(os.path.join(ffPath, os.pardir))

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(logicPath, os.pardir))

    print("PCSystem Path:", pcSystemPath)
    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)





if __name__ == "__main__":
       
    pythonHWOperatorGeneric = dict()
    pythonHWOperatorGeneric["MantissaBits"] = 23
    pythonHWOperatorGeneric["ExponentBits"] = 8

    from Logic.FF.Cascaded_MB_D_FF.FLPCascaded_MB_D_FF.FLPCascaded_MB_D_FF import FLPCascaded_MB_D_FF
    
    cascaded_MB_D_FF = FLPCascaded_MB_D_FF()
    cascaded_MB_D_FF.configurationDetailsOfLogic = {"Name":"Cascaded_MB_D_FF","Frequency":400,"InputDataPorts":[{"Name":("cascadedMB_D_FF" + "0" + "_" + "0" + "Input"),"NumberOfBits":23,"PortType":"Input", "ConstantSignalValue":0}],"Number":"0","CascadeRegisters":True,"NumberSystem":"Float","NumberOfCascadeStages":1,"FFResetType":"ASYNC","Width":23,"NumberOfBits":23, "EsBits":6,"MantissaBits":14, "ExponentBits":7}
    cascaded_MB_D_FF.configure()
    cascaded_MB_D_FF.process()
    cascaded_MB_D_FF.perform()
