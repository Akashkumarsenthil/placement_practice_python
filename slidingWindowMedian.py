#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:07:43 2020

@author: akashkumar
"""
arr = [-1, 5, 13, 8, 2, 3, 3, 1]
n = len(arr)
k = 3
window = []
ans = []

def median(arr):
    arr.sort()
    n = len(arr)
    i = int(n/2)
    j = int(n/2 - 1)
    if n % 2 == 0:
        return ((arr[i] + arr[j]) / 2)
    else:
        return(arr[i])
        
for i in range(n-k+1):
    window = arr[i:i+k]
    ans.append(median(window))
    
    
    

