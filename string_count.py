#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:01:35 2020

@author: akashkumar
"""

a = "ABCDECDET"
b = "CDE"

count = 0
for i in range(len(a)):
    if(a[i:len(b)+i] == b):
        count += 1
print (count)
    