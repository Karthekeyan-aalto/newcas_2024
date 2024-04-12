#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:58:13 2022

@author: Karthekeyan Periasamy
"""

import sys
import os

def numberSystemsPackagePathDirectory():
    
    path = os.getcwd()
    #print("Current Directory", path)
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    NumberSystemsPackagepath = os.path.abspath(os.path.join(path, os.pardir))
    #print("NumberSystemsPackage Path:", NumberSystemsPaackagepath)
    return NumberSystemsPackagepath


def pcSystemPackagePathDirectory():
    
    path = numberSystemsPackagePathDirectory()
    #print("Current Directory", path)
    #print(os.path.abspath(os.path.join(path, os.pardir)))
    pcSystemPackagePath = os.path.abspath(os.path.join(path, os.pardir))
    #print("PCSystemPackagePath Path:", pcSystemPackagePath)
    return pcSystemPackagePath

pcSystemPath = pcSystemPackagePathDirectory()
sys.path.insert(0, pcSystemPath)


if __name__ == "__main__":
    from NumberSystemPackages.FloatConverter.FloatConverter import FloatConverter
    floatConverter = FloatConverter()
    floatConverter.run()
