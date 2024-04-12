#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:40:02 2022

@author: Karthekeyan Periasamy
"""
if __name__ == "__main__":
    from PCOperation import PCOperation
    operation = PCOperation()
    operation.run()
    
    
    from PCMMACUnitOperation import PCMMACUnitOperation
    operation = PCMMACUnitOperation()
    operation.run()
    
    #from PCOperation import PCMinOperation
    #operation = PCMinOperation()
    #operation.run()
    
    #from PCMaxOperation import PCMaxOperation
    #operation = PCMaxOperation()
    #operation.run()
