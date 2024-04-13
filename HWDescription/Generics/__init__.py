"""
Created on June 20 14:27 2023

@author: Karthekeyan Periasamy
"""

import sys
import os

def pcSystemModuleDirectory():
    
    path = os.getcwd()
    #print("Current Directory", path)
    hwDescriptionPath = os.path.abspath(os.path.join(path, os.pardir))
    #print("HWDescription Path:", hwDescriptionPath)
    
    pcSystemPath = os.path.abspath(os.path.join(hwDescriptionPath, os.pardir))
    #print("Operators Path:", operatorsPath)


    return pcSystemPath

pcSystemDirectoryPath = pcSystemModuleDirectory()
sys.path.insert(0, pcSystemDirectoryPath)


if __name__ == "__main__":
    
    # set the generics dictionary and generate the VHDL generic hw description
    hwGenerics = dict()
    hwGenerics["numberOfBits"] = self.numberOfBits
    hwGenerics["esBits"] = self.esBits

    from HWDescription.Generics.GenericVHDLDescription import GenericVHDLDescription

    hwGenericVHDLDescription = GenericVHDLDescription()
    # add the configuration details of the mux
    hwGenericVHDLDescription.configurationDetailsOfHWGenerics = {"GenericTypeName":"INTEGER","PythonHWGeneric":hwGenerics}
    # configure the generics
    hwGenericVHDLDescription.configure()
    # process the logic
    hwGenericVHDLDescription.run()
