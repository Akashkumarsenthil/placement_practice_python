#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:45:37 2020

@author: akashkumar
"""

s = "AABCAAADA"
n = 3
a = int(len(s)/n)
k = 0
ar = []

for i in range(1,n+1):
    for j in range(a):
        ar.append(s[k+j])
    k += n
    print(list(set(ar)))
    ar = []