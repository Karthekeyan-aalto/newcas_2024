#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  13 10:19:17 2021
@author: Karthekeyan Periasamy

"""

if __name__ == "__main__":
    from ProductNode import ProductNode
    productNode = ProductNode()
    productNode.number = 1
    productNode.dataType = 0
    productNode.operationMode = 1
    productNode.input1 = "1.0"
    productNode.input2 = "0.985"
    if  isinstance(productNode, ProductNode):
        print("The type of the custom object is of ProductNode")
        print("ProductNode VHDL weight Signal:", productNode.vhdlWeightSignal)
    else:
        print("The type of the custom object is of not ProductNode")
    if productNode.outputValue != None:
        print("OutputValue", productNode.outputValue)
    productNode.run()
        
        
            
        
                                 
