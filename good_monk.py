#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:16:19 2020

@author: akashkumar
"""

a = "aasdfeioahjkdfurb"

t = len(a)
for i in range(len(a)): 
    q = i
    while(t):
        for j in range(q+1):
            print(a[j],end = "")
        print()
        
        t -= 1
        
            