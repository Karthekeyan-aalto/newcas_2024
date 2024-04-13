#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 6  07:38:05 2023

@author: Karthekeyan Periasamy
"""

if __name__ == "__main__":
    from Driver import Driver
    driver = Driver()
        
    # set all the above properties as configuration details for the Driver package
    driver.configurationDetailsOfDriver = {}

    # configure the system package
    driver.configure()
    
    # process and perform the driver function
    system.run()

    
