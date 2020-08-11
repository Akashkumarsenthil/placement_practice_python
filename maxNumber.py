#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:35:02 2020

@author: akashkumar
"""

def findMaxPossible(arr, q):
    max_ele = arr[q]
    for i in range(q+1, len(arr)):
        if arr[i] > max_ele:
            max_ele = arr[i]
            arr[q], arr[i] = arr[i], arr[q]
    return arr
    
    

n = [int(i) for i in input()]
k = int(input())
if k > len(n):
    print("No shift possible")
else:
    for i in range(k):
        final = findMaxPossible(n, i)
    
    print("".join(map(str, final)))
            

