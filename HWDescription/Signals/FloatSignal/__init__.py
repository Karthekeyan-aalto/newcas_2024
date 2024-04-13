"""
Created by Karthekeyan Periasamy
Edited on Jan 27 09:49
"""
import sys
import os

def pcSystemModuleDirectory():
    
    path = os.getcwd()
    signalPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("Signal Directory Path:", signalPath)

    #print(os.path.abspath(os.path.join(path, os.pardir)))
    hwDescriptionPath = os.path.abspath(os.path.join(signalPath, os.pardir))
    #print("HWDescription Directory Path:", hwDescriptionPath)
    
    pcSystemPath = os.path.abspath(os.path.join(hwDescriptionPath, os.pardir))
    #print("PCSystem Directory Path:", pcSystemPath)

    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)


if __name__ == "__main__":
    from FloatSignalVHDLDescription import FloatSignalVHDLDescription
    signalHWDescription = FloatSignalVHDLDescription()
    # add the configuration details of the LUT
    signalHWDescription.configurationDetails = {"Name":"floatOne","NumberOfBits":32, "MantissaBits":24, "ExponentBits":8, "ConstantSignalValue":1.0} 
    # configure the signal hw description
    signalHWDescription.configure()
    # process the signal hw description
    signalHWDescription.run()
