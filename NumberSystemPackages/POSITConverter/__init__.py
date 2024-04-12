#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:58:13 2022

@author: Karthekeyan Periasamy
"""
if __name__ == "__main__":
    from posit_converter import PositConverter
    num_bits = 26
    #num_frac_bits = 23
    es = 9
    #minValue = 0.000001
    #minValue = 1.0427426260518604e-17
    #minValue = 7.837161448684643e-20
    #minValue = 3.468209193661090e-75
    #minValue = 5
    #minValue = 4.239492018077885e-47
    #minValue = float(0.165)
    #minValue = float(0.1)
    #minValue = float(0.65)
    minValue = float(0.2)
    #minValue = float(0.75)
    #minValue = 3.9778359218187016e-47
    #minValue = 0.5
    positConverter = PositConverter(num_bits,es,num_bits)
    #positConverter.posit_num_bits
    positString = positConverter.convert_float_to_posit(minValue)
    print("The final POSIT string", positString)
    #positString = "00111111111011001100110011"
    #positString = "11000000000000100110010100"
    decimalString = positConverter.convert_posit_to_float(positString)
    print("The final decimal string", decimalString)
    #positString = "00111111111100011001100110"
    #decimalString = positConverter.convert_posit_to_float(positString)
    #print("The final decimal string", decimalString)
    #error = float(float(minValue) - float(decimalString)) / float(minValue)
    #print("RelativeError", error)
    positConverter.run()
        
