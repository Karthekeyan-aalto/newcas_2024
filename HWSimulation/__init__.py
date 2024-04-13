"""
Created on June 22 10:46 2023

@author: Karthekeyan Periasamy
"""

import sys
import os

def pcSystemModuleDirectory():
    
    path = os.getcwd()
    #print("Current Directory", path)
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("Operators Path:", operatorsPath)

    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)


if __name__ == "__main__":
    
    # use package based ports present inside different hw description packages
    from Operators.Port.Port import Port
    
    inputPort = Port()
    inputPort.configurationDetails = {"Name":"v1","PortType":"Input","HWLanguageName":"VHDL","NumberOfBits":24}
    inputPort.configure()
    inputPort.process()

    outputPort = Port()
    outputPort.configurationDetails = {"Name":"vout","PortType":"Output","HWLanguageName":"VHDL","NumberOfBits":24}
    outputPort.configure()
    outputPort.process()
    
    clockPort = Port()
    clockPort.configurationDetails = {"Name":"clk","PortType":"Input","HWLanguageName":"VHDL","NumberOfBits":1,"Frequency":100}
    clockPort.configure()
    clockPort.process()
    
    resetPort = Port()
    resetPort.configurationDetails = {"Name":"rst","NumberOfBits":1,"HWLanguageName":"VHDL","PortType":"Input"}
    resetPort.configure()
    resetPort.process()
    
    from HWSimulation.HWSystemCompilation import HWSystemCompilation
    systemCompilation = HWSystemCompilation()
    systemCompilation.configurationDetails = {"HWDesignLibraries":["vlib","ieee_proposed"]}
    systemCompilation.configure()


    from HWSimulation.HWSystemSimulation import HWSystemSimulation
    systemSimulation = HWSystemSimulation()
    systemSimulation.configurationDetails = {"HWName":"Mux","InputDataPorts":[inputPort], "OutputDataPorts":[outputPort], "InputClockPort":clockPort, "InputResetPort":resetPort, "HWDesignLibraries":systemCompilation.hwDesignLibraries}
    systemSimulation.configure()
