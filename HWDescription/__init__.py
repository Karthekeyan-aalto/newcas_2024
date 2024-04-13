"""
Created on June 20 14:27 2023

@author: Karthekeyan Periasamy
"""

import sys
import os

def pcSystemModuleDirectory():
    
    path = os.getcwd()
    #print("Current Directory", path)
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(path, os.pardir))
    print("PCSystem Path:", pcSystemPath)

    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)




if __name__ == "__main__":

    # this function will be used to test the full HWDescription without the architecture definition
    # the architecture definiton of a HW is supported under differen HW Logic and Operators

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
    
    # set the generics dictionary and generate the VHDL generic hw description
    hwGenerics = dict()
    hwGenerics["numberOfBits"] = 23
    hwGenerics["esBits"] = 6
    
    #from HWDescription.Generics.GenericVHDLDescription import GenericVHDLDescription

    #hwGenericVHDLDescription = GenericVHDLDescription()
    # add the configuration details of the mux
    #hwGenericVHDLDescription.configurationDetailsOfHWGenerics = {"GenericTypeName":"INTEGER","PythonHWGeneric":hwGenerics}
    # configure the generics
    #hwGenericVHDLDescription.configure()
    # process the logic
    #hwGenericVHDLDescription.run()


    # geenrate the generics and signals

    from HWDescription.HWVHDLDescription import HWVHDLDescription
    hwVHDLDescription = HWVHDLDescription()
    # add the configuration details of the mux
    hwVHDLDescription.configurationDetailsOfHW = {"Name":"Mux","PythonHWEntity":{"Name":"Mux","PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":hwGenerics},"InputDataPorts":[inputPort], "OutputDataPorts":[outputPort], "InputClockPort":clockPort, "InputResetPort":resetPort},"PythonHWArchitecture":{"Name":"Mux","HWArchitectureTypeName":"RTL","InputDataPorts":[inputPort], "OutputDataPorts":[outputPort], "InputClockPort":clockPort, "InputResetPort":resetPort,"PythonHWProcess":{"SensitivityList":[clockPort.name,resetPort.name]}}
            ,"PythonHW":{}}

    # configure the logic
    hwVHDLDescription.configure()
    # process the logic
    hwVHDLDescription.run()
