"""
Created by Karthekeyan Periasamy
Edited on Feb 1 2023 21:16
"""

import sys
import os

def pcSystemModuleDirectory():
   
    
    ffPath = os.getcwd()

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    logicPath = os.path.abspath(os.path.join(ffPath, os.pardir))
    #print("PCSystem Path:", pcSystemPath)

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(logicPath, os.pardir))

    #print("PCSystem Path:", pcSystemPath)
    return pcSystemPath

def operatorsDirectory():
    
    pcSystemPath = pcSystemModuleDirectory()

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    operatorsPath = pcSystemPath + "/Operators"

    #print("Operators Path:", operatorsPath)
    return operatorsPath

def fileSystemDirectory():
    
    pcSystemPath = pcSystemModuleDirectory()

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    fileSystemPath = pcSystemPath + "/FileSystem"

    #print("FileSystem Path:", fileSystemPath)
    return fileSystemPath



def HWVHDLDescriptionDirectory():
    
    pcSystemPath = pcSystemModuleDirectory()

    hwDescriptionPath = pcSystemPath + "/HWDescription"
    
    return hwDescriptionPath


def portDirectory():
    
    pcSystemPath = pcSystemModuleDirectory()

    portDirectoryPath = pcSystemPath + "/Operators/Port"
    
    return portDirectoryPath


pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)

operatorsDirectoryPath = operatorsDirectory()
sys.path.insert(1, operatorsDirectoryPath)

fileSystemDirectoryPath = fileSystemDirectory()
sys.path.insert(2, fileSystemDirectoryPath)

hwDescriptionPath = HWVHDLDescriptionDirectory()
sys.path.insert(3, hwDescriptionPath)

portDirectoryPath = portDirectory()
sys.path.insert(4, portDirectoryPath)






if __name__ == "__main__":
    
    from FileSystem.PCFileSystem import PCFileSystem
    fileSystem = PCFileSystem()
    # set the pcsystemType
    fileSystem.pcSystemType = 0
    # set teh pcSystemModel global property
    pcSystemModel = "4ip"
    # set the modelName to the fileSystem PCSystemModel property
    fileSystem.pcSystemModel = pcSystemModel
    # set the fileSystemNumber
    fileSystem.pcSystemNumberSystem = 1
    fileSystem.pcSystemNumberOfBits = 32
    pcEquation = fileSystem.pcEquation
    #print("PCEquation", pcEquation)


       
    pythonHWOperatorGeneric = dict()
    pythonHWOperatorGeneric["MantissaBits"] = 23
    pythonHWOperatorGeneric["ExponentBits"] = 8

    from Operators.Port.Port import Port
    
    outputPorts = list()
    # form the necessary input port details
    outputPortDetail = {"Name":"vout","NumberOfBits":32,"PortType":"Output","ConstantSignalValue":0}
    outputPort = Port()
    outputPort.configurationDetails = outputPortDetail
    # configure the port
    outputPort.configure()
    # process the port
    outputPort.process()
    outputPort.perform()
    outputPorts.append(outputPort)
    
    clockPortDetails = {"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":400, "ConstantSignalValue":0}
    clockPort = Port()
    clockPort.configurationDetails = clockPortDetails
    # configure the port
    clockPort.configure()
    # process the port
    clockPort.process()
    clockPort.perform()

    resetPortDetails = {"Name":"rst","NumberOfBits":1,"PortType":"Input", "ConstantSignalValue":0}
    resetPort = Port()
    resetPort.configurationDetails = resetPortDetails
    # configure the port
    resetPort.configure()
    # process the port
    resetPort.process()
    resetPort.perform()
