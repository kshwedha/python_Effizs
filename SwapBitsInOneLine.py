# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def Swap_bits(x):    
    return  (x & 0b10101010) >> 1 | (x & 0b01010101) << 1
even=Swap_bits(4)
odd=Swap_bits(5)
evenb=Swap_bits(10000100)
oddb=Swap_bits(10000101)
print(even)
print(odd)
print(evenb)
print(oddb)