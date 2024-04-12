"""
Created by Karthekeyan Periasamy
Edited on Feb 1 2023 21:16
"""

import sys
import os
import re


def pcSystemModuleDirectory():
   
    
    flpPCOperationPath = os.getcwd()

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    operationsPath = os.path.abspath(os.path.join(flpPCOperationPath, os.pardir))
    #print("PCSystem Path:", pcSystemPath)

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPath = os.path.abspath(os.path.join(operationsPath, os.pardir))

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

def swOptimisersDirectory():
    
    pcSystemPath = pcSystemModuleDirectory()

    swOptimisersPath = pcSystemPath + "/SWOptimisers"
    
    return swOptimisersPath


def HWVHDLDescriptionDirectory():
    
    pcSystemPath = pcSystemModuleDirectory()

    hwDescriptionPath = pcSystemPath + "/HWDescription"
    
    return hwDescriptionPath


def createFile(fileLocation, fileName):

    pcSystemPath = pcSystemModuleDirectory()
    simulationPath = pcSystemPath + "/Simulation"
    vhdlPath = simulationPath + "/VHDL"

    path = fileLocation
    pathComponents = path.split("/")
    #print(pathComponents)

    # access the path Components
    for componentIndex, component in enumerate(pathComponents):
        #print("Component Index, Component", componentIndex, component)
        if component == "":
            continue

        # append the component with the vhdlPath and check whether the folder exists or not
        vhdlPath = vhdlPath + "/" + component
        if os.path.exists(vhdlPath) == True:
            #print("Exists", vhdlPath)
            continue
        else:
            # create the folder
            os.mkdir(vhdlPath)

    # create the file using the vhdlPath
    filePath = vhdlPath + "/" + fileName
    # check whether the file exists or not
    if os.path.isfile(filePath) == True:
        #print("File Exists")
        return filePath
    else:
        #print("File do not exist, create file")
        open(filePath, 'x')
        return filePath

def createVHDLCompileScriptFile(fileLocation, compileScriptFileName):

    pcSystemPath = pcSystemModuleDirectory()
    simulationPath = pcSystemPath + "/Simulation"
    #vhdlPath = simulationPath + "/VHDL"

    path = fileLocation
    pathComponents = path.split("/")
    #print(pathComponents)

    # access the path Components
    for componentIndex, component in enumerate(pathComponents):
        #print("Component Index, Component", componentIndex, component)
        if component == "":
            continue

        # append the component with the vhdlPath and check whether the folder exists or not
        vhdlPath = vhdlPath + "/" + component
        if os.path.exists(vhdlPath) == True:
            #print("Exists", vhdlPath)
            continue
        else:
            # create the folder
            os.mkdir(vhdlPath)

    # create the file using the vhdlPath
    filePath = vhdlPath + "/" + fileName
    # check whether the file exists or not
    if os.path.isfile(filePath) == True:
        #print("File Exists")
        return filePath
    else:
        #print("File do not exist, create file")
        open(filePath, 'x')
        return filePath


def readFromFile(fileLocation, fileName):
    pathOfCreatedFile = createFile(fileLocation, fileName)
    fileToRead = open(pathOfCreatedFile, 'r')
    return fileToRead

def writeToFile(fileLocation, fileName):
    pathOfCreatedFile = createFile(fileLocation, fileName)
    fileToWrite = open(pathOfCreatedFile, 'w')
    return fileToWrite




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

swOptimisersPath = swOptimisersDirectory()
sys.path.insert(3, swOptimisersPath)

hwDescriptionPath = HWVHDLDescriptionDirectory()
sys.path.insert(4, hwDescriptionPath)

portDirectoryPath = portDirectory()
sys.path.insert(5, portDirectoryPath)


if __name__ == "__main__":
    
    from FileSystem.PCFileSystem import PCFileSystem
    fileSystem = PCFileSystem()
    # set the pcsystemType
    # system type AC = 0, SPN = 1
    fileSystem.pcSystemType = 1
    # set teh pcSystemModel global property
    pcSystemModel = "msnbc"
    # set the modelName to the fileSystem PCSystemModel property
    fileSystem.pcSystemModel = pcSystemModel
    # set the fileSystemNumber
    fileSystem.pcSystemNumberSystem = 1
    fileSystem.pcSystemNumberOfBits = 22
    pcEquation = fileSystem.pcEquation
    #print("PCEquation", pcEquation)


    from Operations.FLPPCOperation.FLPPCOperation import FLPPCOperation
    #pcEquation = "((v0a*0.54)+(v0b*0.65))"
    #pcEquation = "((0.54*v1)+(0.65*v2))"
    #pcEquation = "((v5*((0.54*v4)*(0.65*v3)))+(((0.54*v1)*(0.65*v2))*v6))"
    #pcEquation = "((0.12*((0.54*v4)*(0.65*v3)))+(((0.54*v1)*(0.65*v2))*0.45))"
    #pcEquation = "((0.25*(0.54*v0a))+(0.32*(0.65*v0b)))"
    #pcEquation = "(((0.54*v1)*0.25)+((0.65*v2)*0.32))"
    #pcEquation = "((v3*(0.54*v1))+(v4*(0.65*v2)))"
    pcEquation = "(((0.54*v1)*v3)+((0.65*v2)*v4))"
    #pcEquation = "((0.54*v1)+((0.65*v2)*v3))"
    #pcEquation = "(((0.25*(v2*0.77))*(v3*0.99))+((0.35*(v1*0.54))*(v3*0.99)))"
    #pcEquation = "((0.25*((0.23*(v2*0.77))+(0.37*(v1*0.54))))+(0.6*((0.25*(v2*0.77))+(0.35*(v1*0.54)))))"
    #pcEquation = "((0.25*((0.23*(v2*0.77))+(0.37*(v1*0.54))))+(0.6*((0.23*(v2*0.77))+(0.37*(v1*0.54)))))"
    #pcEquation = "(((0.711743*(vb1))+(0.288257*v1))*((((0.756919*(vb2))+(0.243081*v2))*(((0.699091*(vb3))+(0.300909*v3))*(0.756090*(vb4))))+(((0.653649*(vb2))+(0.346351*v2))*(((0.999360*(vb3))+(0.000640*v3))*(0.243910*v4)))))"
    mantissaBits = 25
    exponentBits = 7
    # 7+15 is 22, but we set the number of bits to 21, as auto pc suggest mantissabits including the fixed 1, so reducing it is necessary to generate Flopoco HW
    numberOfBits = 32
    flopocoBits = 2
    frequency = 800

    operation = FLPPCOperation()
    operation.configurationDetailsOfOperation = {"Frequency":frequency,"MantissaBits":mantissaBits,"ExponentBits":exponentBits,"Equation":pcEquation,"NumberOfBits":numberOfBits, "FlopocoBits":flopocoBits}
    operation.configure()
    operation.run()

    from SWOptimisers.SWPCArithmeticNodesOptimiser.SWPCArithmeticNodesOptimiser import SWPCArithmeticNodesOptimiser
    pcArithmeticNodeOptimiser = SWPCArithmeticNodesOptimiser()
    pcArithmeticNodeOptimiser.configurationDetails = {"ArithmeticNodes":operation.arithmeticNodes, "ArithmeticNodeDuplicates":operation.arithmeticNodeIndicesWithTheirDuplicatesIndices,"DuplicatesOfArithmeticNodeWithTheirReceivers":operation.duplicatesOfArithmeticNodesWithTheirReceiverIndices}
    pcArithmeticNodeOptimiser.configure()
    pcArithmeticNodeOptimiser.run()
    
    arithmeticNodes = pcArithmeticNodeOptimiser.optimisedArithmeticNodes
    #print(len(arithmeticNodes))
    adders = pcArithmeticNodeOptimiser.totalNumberOfAdders
    #print(len(adders))
    multipliers = pcArithmeticNodeOptimiser.totalNumberOfMultipliers
    #print(len(multipliers))

    
    
    from SWSynthesisers.SWPCTreeSynthesiser.SWPCTreeSynthesiser import SWPCTreeSynthesiser
    pcTreeSynthesiser = SWPCTreeSynthesiser()
    #operation.configurationDetailsOfSynthesiser = {"ArithmeticNodes":pcArithmeticNodeOptimiser.arithmeticNodes,"TotalNumberOfArithmeticNodes":pcArithmeticNodeOptimiser.totalNumberOfArithmeticNodes,"TotalNumberOfAdders":pcArithmeticNodeOptimiser.totalNumberOfAdders, "TotalNumberOfMultipliers":pcArithmeticNodeOptimiser.totalNumberOfMultipliers}
    if pcArithmeticNodeOptimiser.isPCArithmeticNodesOptimisationEnabled == False:
        pcTreeSynthesiser.configurationDetailsOfSynthesiser = {"ArithmeticNodes":pcArithmeticNodeOptimiser.arithmeticNodes,"TotalNumberOfArithmeticNodes":pcArithmeticNodeOptimiser.totalNumberOfArithmeticNodes,"TotalNumberOfAdders":pcArithmeticNodeOptimiser.totalNumberOfAdders, "TotalNumberOfMultipliers":pcArithmeticNodeOptimiser.totalNumberOfMultipliers}
    else:
        pcTreeSynthesiser.configurationDetailsOfSynthesiser = {"ArithmeticNodes":pcArithmeticNodeOptimiser.optimisedArithmeticNodes,"TotalNumberOfArithmeticNodes":pcArithmeticNodeOptimiser.totalNumberOfArithmeticNodes,"TotalNumberOfAdders":pcArithmeticNodeOptimiser.totalNumberOfAdders, "TotalNumberOfMultipliers":pcArithmeticNodeOptimiser.totalNumberOfMultipliers}
    pcTreeSynthesiser.configure()
    pcTreeSynthesiser.run()
    #frequency = 400
    # flpAdd = 7
    # flpMult = 2
    #frequency = 800
    # flpAdd = 22
    # flpMult = 4

    #frequency = 800 # error = 10-6
    # mantissaBits = 24
    # exponentBits = 7
    #flpAdd = 24
    #flpMult = 9

    adderPipelineDepth = 24
    multiplierDepth = 9

    from SWOptimisers.SWPCTreeOptimiser.SWPCTreeOptimiser import SWPCTreeOptimiser
    optimiser = SWPCTreeOptimiser()
    if pcArithmeticNodeOptimiser.isPCArithmeticNodesOptimisationEnabled == True:
        optimiser.configurationDetails = {"ArithmeticNodes":pcArithmeticNodeOptimiser.optimisedArithmeticNodes,"TopArithmeticNode":pcTreeSynthesiser.topArithmeticNode,"AdderPipelineDepth":adderPipelineDepth,"MultiplierPipelineDepth":multiplierDepth}
    else:
        optimiser.configurationDetails = {"ArithmeticNodes":pcArithmeticNodeOptimiser.arithmeticNodes,"TopArithmeticNode":pcTreeSynthesiser.topArithmeticNode,"AdderPipelineDepth":adderPipelineDepth,"MultiplierPipelineDepth":multiplierDepth}

    optimiser.configure()
    optimiser.run()
    
    #print("Children Of Each Level Of PCTree", optimiser.childrenOfEachLevelOfPCTree)
    
    #for arithmeticNode in optimiser.arithmeticNodes:
        #if arithmeticNode.swOperator.isOperatorEnabled == False:
            #print(arithmeticNode)
            #print(arithmeticNode.swOperator)
            #print("ArithmeticNode Input1", arithmeticNode.input1)
            #print("ArithmeticNode Input2", arithmeticNode.input2)
            #print("ArithmeticNode Output", arithmeticNode.output)
            #print("ArithmeticNode Operator Disabled")
        #else:
            #pass
            
            #print(arithmeticNode)
            #print(arithmeticNode.swOperator)            
            #print("ArithmeticNode Input1", arithmeticNode.input1)
            #print("ArithmeticNode Input2", arithmeticNode.input2)
            #print("ArithmeticNode Output", arithmeticNode.output)
            #print("ArithmeticNode Operator Enabled")

    
    pythonHWOperatorGeneric = dict()
    pythonHWOperatorGeneric["MantissaBits"] = mantissaBits
    pythonHWOperatorGeneric["ExponentBits"] = exponentBits
    pythonHWOperatorGeneric["NumberOfBits"] = numberOfBits
    pythonHWOperatorGeneric["FlopocoBits"] = flopocoBits

    from Operators.Port.Port import Port
    from Operators.Port.FLPFlopocoPort.FLPFlopocoPort import FLPFlopocoPort

    
    outputPorts = list()
    # form the necessary input port details
    outputPortDetail = {"Name":"vout","MantissaBits":mantissaBits,"ExponentBits":exponentBits,"FlopocoBits":flopocoBits,"NumberOfBits":numberOfBits,"PortType":"Output","ConstantSignalValue":0}
    outputPort = FLPFlopocoPort()
    outputPort.configurationDetails = outputPortDetail
    # configure the port
    outputPort.configure()
    # process the port
    outputPort.process()
    outputPort.perform()
    outputPorts.append(outputPort)
    
    clockPortDetails = {"Name":"clk","NumberOfBits":1,"PortType":"Input","Frequency":frequency, "ConstantSignalValue":0}
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
    
    enablePortDetails = {"Name":"enable","NumberOfBits":1,"PortType":"Input", "ConstantSignalValue":0}
    enablePort = Port()
    enablePort.configurationDetails = enablePortDetails
    # configure the port
    enablePort.configure()
    # process the port
    enablePort.process()
    enablePort.perform()


   # from HWDescription.Systems.PCSystem.PCSystemVHDLDescription import PCSystemVHDLDescription
   # pcSystemVHDLDescription = PCSystemVHDLDescription()
   # pcSystemVHDLDescription.configurationDetailsOfHW = {"PythonHWEntity":{"Name":"PCSystem" + "_" + str(32),"NumberSystem":"Float","Number":32,"InputDataPorts":operation.operationPorts,"OutputDataPorts":outputPorts,"InputClockPort":clockPort, "InputResetPort":resetPort,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":pythonHWOperatorGeneric}},"PythonHWArchitecture":{"Name":"PCSystem" + "_" + str(32),"NumberSystem":"Float","Number":32,"InputDataPorts":operation.operationPorts, "OutputDataPorts":outputPorts,"InputClockPort":clockPort, "InputResetPort":resetPort,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":pythonHWOperatorGeneric},"ArithmeticNodes":optimiser.arithmeticNodes,"ChildrenOfEachLevelOfPCTree":optimiser.childrenOfEachLevelOfPCTree,"PythonHWProcess":{"SensitivityList":[clockPort.name,resetPort.name],"PythonHWProcessInfo":None,"NumberOfPipelineStages":4,"PythonHWClockProcessInfo":{"Frequency":400, "ClockPortName":clockPort.name,"ClockStimulusName":(clockPort.name + "Stimulus")},"PythonHWResetInfo":{"ResetPortName":resetPort.name},"PythonHWIOStimulusProcessInfo":{"PythonHWProcessVariablesInfo":[{"Name":"fileline","Type":"line","NumberOfBits":None},{"NumberOfBits":32,"Name":"inputBuffer","Type":"std_logic_vector"},{"Name":"commaBuffer","Type":"character","NumberOfBits":None}],"PythonHWProcessFileInfo":[{"Mode":"write_mode","Type":"text","Name":"outputfile","FileName":("Output" + "_" + "PCSystem" + "_" + str(32)),"FileExtension":"txt"},{"Mode":"read_mode","Type":"text","Name":"inputfile","FileName":("Input" + "_" + "PCSystem" + "_" + str(32)),"FileExtension":"txt"}],"InputDataPorts":operation.operationPorts,"OutputDataPorts":outputPorts}}}}
   # 
   # pcSystemVHDLDescription.configure()
   # pcSystemVHDLDescription.process()
   # pcSystemVHDLDescription.perform()

    #print("HWVHDL Description", pcSystemVHDLDescription.vhdlDescription)
    
    numberOfPipelineStages = 1


    from HWDescription.Systems.PCSystem.FLPPCSystem.FLPPCSystemVHDLDescription import FLPPCSystemVHDLDescription
    pcSystemVHDLDescription = FLPPCSystemVHDLDescription()
    pcSystemVHDLDescription.configurationDetailsOfHW = {"PythonHWEntity":{"Name":"PCSystem" + "_" + str(numberOfBits),"NumberSystem":"Float","Number":numberOfBits,"InputDataPorts":operation.operationPorts,"OutputDataPorts":outputPorts,"InputClockPort":clockPort, "InputResetPort":resetPort,"InputEnablePort":enablePort,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":pythonHWOperatorGeneric}},"PythonHWArchitecture":{"Name":"PCSystem" + "_" + str(numberOfBits),"NumberSystem":"Float","Number":numberOfBits,"InputDataPorts":operation.operationPorts, "OutputDataPorts":outputPorts,"InputClockPort":clockPort, "InputResetPort":resetPort,"InputEnablePort":enablePort,"PythonHWGeneric":{"GenericTypeName":"INTEGER","PythonHWGeneric":pythonHWOperatorGeneric},"ArithmeticNodes":optimiser.arithmeticNodes,"ChildrenOfEachLevelOfPCTree":optimiser.childrenOfEachLevelOfPCTree,"PythonHWProcess":{"SensitivityList":[clockPort.name,resetPort.name],"PythonHWProcessInfo":None,"NumberOfPipelineStages":numberOfPipelineStages,"PythonHWClockProcessInfo":{"Frequency":frequency, "ClockPortName":clockPort.name,"ClockStimulusName":(clockPort.name + "Stimulus")},"PythonHWResetInfo":{"ResetPortName":resetPort.name},"PythonHWEnableInfo":{"EnablePortName":enablePort.name},"PythonHWIOStimulusProcessInfo":{"PythonHWProcessVariablesInfo":[{"Name":"fileline","Type":"line","NumberOfBits":None},{"NumberOfBits":numberOfBits,"Name":"inputBuffer","Type":"std_logic_vector"},{"Name":"commaBuffer","Type":"character","NumberOfBits":None}],"PythonHWProcessFileInfo":[{"Mode":"write_mode","Type":"text","Name":"outputfile","FileName":("Output" + "_" + "PCSystem" + "_" + str(numberOfBits)),"FileExtension":"txt"},{"Mode":"read_mode","Type":"text","Name":"inputfile","FileName":("Input" + "_" + "PCSystem" + "_" + str(numberOfBits)),"FileExtension":"txt"}],"InputDataPorts":operation.operationPorts,"OutputDataPorts":outputPorts}}}}
    
    pcSystemVHDLDescription.configure()
    pcSystemVHDLDescription.process()
    pcSystemVHDLDescription.perform()

    #print("HWVHDL Description", pcSystemVHDLDescription.vhdlDescription)
    
    #vhdlFilePath = "/" + "SPN" + "/" + "msnbc" + "/" + "22" + "/" + "Float" + "/" +"PCSystem" + "/"
    #fileToWrite = writeToFile(vhdlFilePath,"PCSystem_22.vhd")
    #fileToWrite.write(pcSystemVHDLDescription.vhdlDescription)
    #fileToWrite.close()
    
    vhdlFilePath = "/" + "SPN" + "/" + "msnbc" + "/" + "32" + "/" + "Float" + "/" +"PCSystem" + "/"
    fileToWrite = writeToFile(vhdlFilePath,"PCSystem_32.vhd")
    fileToWrite.write(pcSystemVHDLDescription.vhdlDescription)
    fileToWrite.close()
    
    #vhdlFilePath = "/" + "AC" + "/" + "msnbc_tw5" + "/" + "32" + "/" + "Float" + "/" +"PCSystem" + "/"
    #fileToWrite = writeToFile(vhdlFilePath,"PCSystem_32.vhd")
    #fileToWrite.write(pcSystemVHDLDescription.vhdlDescription)
    #fileToWrite.close()


    
    #vhdlFilePath = "/" + "AC" + "/" + "msnbc_tw5" + "/" + "22" + "/" + "Float" + "/" +"PCSystem" + "/"
    #fileToWrite = writeToFile(vhdlFilePath,"PCSystem_22.vhd")
    #fileToWrite.write(pcSystemVHDLDescription.vhdlDescription)
    #fileToWrite.close()


    #fileToReadFrom = readFromFile(vhdlFilePath,"PCSystem_22.vhd")
    #fileContent = fileToReadFrom.read()
    #fileToReadFrom.close()
    #print("PCSystemVHDL Description", fileContent)
