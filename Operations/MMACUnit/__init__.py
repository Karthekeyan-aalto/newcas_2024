#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:42:44 2022

@author: Karthekeyan Periasamy
"""
if __name__ == "__main__":
    from MMACUnit import MMACUnit
    maxNode = MMACUnit()
    maxNode.init()
    maxNode.number = 1
    maxNode.dataType = 0
    maxNode.input1 = "va0"
    maxNode.input2 = "vb0"
    maxNode.run()
    input()