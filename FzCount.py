# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:07:53 2019

@author: sg
"""
"""
for j in range(len(arrayalpha)):
    x=arrayalpha[j]
    fz[x]=0
"""

arrayalpha=['a','b','f','g','d','s','h','z','l','i','b','n','c','a','c','d','c']
fz={}

for j in arrayalpha:
    fz[j]=0                     #assigning dictionary index values or key values

for i in range(len(arrayalpha)):
    fz[arrayalpha[i]]+=1
    
for x in sorted(fz.keys()):
    print("%s %d" %(x,fz[x]), end="\n")       #or just type "print(fz)"
