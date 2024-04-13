"""
Created on July 08 14:43 2023

@author: Karthekeyan Periasamy
"""

import sys
import os

def pcSystemModuleDirectory():
    
    path = os.getcwd()
    #print("Current Directory", path)
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    
    shiftRegisterPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("ShiftRegister Path:", shiftRegisterPath)
    
    operatorsPath = os.path.abspath(os.path.join(shiftRegisterPath, os.pardir))
    #print("Operators Path:", operatorsPath)
    
    pcSystemPath = os.path.abspath(os.path.join(operatorsPath, os.pardir))
    print("Hello PCSystem Path:", pcSystemPath)

    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)




if __name__ == "__main__":

    from Operators.ShiftRegisters.MBRightSHR.MBRightSHR import MBRightSHR

    #register = MBRightSHR()
    #print("Register",register)
    # add the configuration details of the register
    #register.configurationDetailsOfOperator = {"NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":1,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":23,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"NumberOfBits":23,"EsBits":6,"Depth":23,"Width":1,"ShiftDirection":"Right"}
    
    #print("Configuration Details that will be configured to the register operator",register.configurationDetailsOfOperator)
    # configure the logic
    #register.configure()
    # process the logic
    #register.run()

