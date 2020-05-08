#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:18:39 2020

@author: akashkumar
"""

vov = "AEIOU"

s = "BANANA"

ks = 0
ss = 0

for i in range(len(s)):
    if s[i] in vov:
        ks += (len(s) - i)
    else:
        ss += (len(s) - i)
    
print (ks)
print (ss)