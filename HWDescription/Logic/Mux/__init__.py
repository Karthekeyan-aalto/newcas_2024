"""
Created by Karthekeyan Periasamy
Edited on April 1 2023, 20:09
"""
import sys
import os

def pcSystemModuleDirectory():
    
    muxHWDescriptionPath = os.getcwd()
    #print("Current Directory", path)
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    logicHWDescriptionPath = os.path.abspath(os.path.join(muxHWDescriptionPath, os.pardir))
    #print("Operators Path:", operatorsPath)
    
    hwDescriptionPath = os.path.abspath(os.path.join(logicHWDescriptionPath, os.pardir))
    #print("HWDescription Path:", hwDescriptionPath)
    
    pcSystemPath = os.path.abspath(os.path.join(hwDescriptionPath, os.pardir))
    print("PCSystem Path:", pcSystemPath)


    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)


if __name__ == "__main__":
    from Logic.Mux.Mux import Mux
    mux = Mux()
   # add the configuration details of the LUT
    mux.configurationDetailsOfLogic = {"NumberSystem":"Posit","InputDataPorts":[{"Name":"v1","NumberOfBits":32,"PortType":"Input"},{"Name":"v2","NumberOfBits":32,"PortType":"Input"},{"Name":"v3","NumberOfBits":32,"PortType":"Input"},{"Name":"v4","NumberOfBits":32,"PortType":"Input"}],"OutputPorts":[{"Name":"vout","NumberOfBits":32,"PortType":"Output"}],"InputClockPort":{"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":100},"InputResetPort":{"Name":"rst","NumberOfBits":1,"PortType":"Input"},"NumberOfBits":32,"SelectSignalBits":2} 
    # configure the mux
    mux.configure()
    # process the mux
    mux.run()

    from HWDescription.Logic.Mux.MuxHWDescription import MuxHWDescription
    logicHWDescription = MuxHWDescription()
    # add the configuration details of the mux
    logicHWDescription.logicDetails = {"NumberSystem":mux.numberSystemName,"InputDataPorts":mux.inputDataPorts,"OutputPorts":mux.outputPorts,"InputClockPort":mux.clockPort,"InputResetPort":mux.resetPort,"NumberOfBits":mux.numberOfBits, "Name":mux.name,"SWMux":mux.pythonMUX} 
    # configure the logic
    logicHWDescription.configure()
    # process the logic
    logicHWDescription.run()
    
    from HWDescription.Logic.Mux.MuxVHDLDescription import MuxVHDLDescription
    logicVHDLDescription = MuxVHDLDescription()
    # add the configuration details of the mux
    logicVHDLDescription.logicDetails = {"NumberSystem":mux.numberSystemName,"InputDataPorts":mux.inputDataPorts,"OutputPorts":mux.outputPorts,"InputClockPort":mux.clockPort,"InputResetPort":mux.resetPort,"NumberOfBits":mux.numberOfBits, "Name":mux.name,"SWMux":mux.pythonMUX} 
    # configure the logic
    logicVHDLDescription.configure()
    # process the logic
    logicVHDLDescription.run()
