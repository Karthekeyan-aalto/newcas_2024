"""
Edited on June 30 09:44

@author: Karthekeyan Periasamy
"""

import sys
import os

def pcSystemModuleDirectory():
    
    path = os.getcwd()
    print("Current Directory", path)

    hwDescriptionPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("HWDescription Path:", hwDescriptionPath)
    
    pcSystemPath = os.path.abspath(os.path.join(hwDescriptionPath, os.pardir))
    print("PCSystem Path", pcSystemPath)
    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)




if __name__ == "__main__":
    

    from HWDescription.Process.ProcessVHDLDescription import ProcessVHDLDescription
    processVHDLDescription = ProcessVHDLDescription()
    processVHDLDescription.configurationDetails = {"SensitivityList":["clk","rst"]}
    processVHDLDescription.configure()
    processVHDLDescription.run()
   
