#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:36:30 2022

@author: 1003907
"""

if __name__ == "__main__":

    from PCSystemConfiguration import PCSystemConfiguration
    configuration = PCSystemConfiguration()
    # set all the above properties as configuration details for the operations package
    configuration.configurationDetailsOfSystemPackage = {"PCSystemInfo": {"NumberOfBits":[25,30,35],"MantissaBits":[20,25,30],"ExponentBits":6,"EsBits":5, "NumberSystem":"Posit", "SystemType":"SPN", "Model":"nltcs"}}
    
    from PCAnalysisConfiguration import PCAnalysisConfiguration
    analysisConfiguration = PCAnalysisConfiguration()
    # set all the above properties as configuration details for the operations package
    analysisConfiguration.configurationDetailsOfAnalysisPackage = {"AnalysisMode":1,"ErrorAnalysisType":0,"ActivateBitOptimisation":0, "ErrorTolerance":0.001}


