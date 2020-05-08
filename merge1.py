#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:15:46 2020

@author: akashkumar
"""

s = "AABCAAADA"
n = 3
at = []
temp = ""
l = len(s)
for i in range(0,l,n):
    j = i
    for k in range(n):
        at.append(s[j])
        j += 1
    at = list(dict.fromkeys(at))
    for e in at:
        temp += e
    print(temp)
    at = []
    temp = ""
    
    
    
    
    
    
l = []
def wrap(string, max_width):
    k = max_width
    for i in range(0,len(string),max_width):
        l.append(string[slice(i,k)])
        k += max_width
    return l
