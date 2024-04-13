"""
Created by Karthekeyan Periasamy
Edited on Jan 23 2023 21:16
"""

import sys
import os

def pcSystemModuleDirectory():
   
    
    flpMultiplierPath = os.getcwd()

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    mb_d_ffPath = os.path.abspath(os.path.join(flpMultiplierPath, os.pardir))
    #print("MB_D_FF Path:", mb_d_ffPath)

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    ffPath = os.path.abspath(os.path.join(mb_d_ffPath, os.pardir))
    
    logicPath = os.path.abspath(os.path.join(ffPath, os.pardir))

    print("Logic Path:", logicPath)
    
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(logicPath, os.pardir))

    print("PCSystem Path:", pcSystemPath)
    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)


if __name__ == "__main__":
    from Logic.FF.MB_D_FF.FLPMB_D_FF.FLPMB_D_FF import FLPMB_D_FF
    flpMB_D_FF = FLPMB_D_FF()
    # add the configuration details of the multiplier
    flpMB_D_FF.configurationDetailsOfLogic = {"Name":"MB_D_FF","Frequency":400,"NumberSystem":"Float","Number":0, "InputDataPorts":[{"Name":("mb_D_FF" + "0" + "_" + "0" + "Input"),"NumberOfBits":23,"PortType":"Input", "ConstantSignalValue":0}],"OutputPorts":[{"Name":("mb_D_FF" + "0" + "_" + "0" + "Output"),"NumberOfBits":23,"PortType":"Output","ConstantSignalValue":0}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":400,"ConstantSignalValue":0},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0}, "InputEnablePort":{"Name":"enable","NumberOfBits":1,"PortType":"Input","ConstantSignalValue":0},"ShiftRegisterResetType":"ASYNC","Width":23,"NumberOfBits":23, "EsBits":6, "MantissaBits":15, "ExponentBits":8}   
    flpMB_D_FF.configure()
    # run the multiplication
    flpMB_D_FF.run()
