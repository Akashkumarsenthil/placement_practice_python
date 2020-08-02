#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 16:08:54 2020

@author: akashkumar
"""

#code
n = int(input())

def findPlatform(arr, dep, n): 
    arr.sort() 
    dep.sort() 
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while (i < n and j < n): 
        if (arr[i] <= dep[j]): 
            plat_needed+= 1
            i+= 1
        elif (arr[i] > dep[j]): 
            plat_needed-= 1
            j+= 1
        if (plat_needed > result):  
            result = plat_needed 
          
    return result

for _ in range(n):
    k = int(input())
    arraival = [int(i) for i in input().split()]
    departure = [int(i) for i in input().split()]
    print(findPlatform(arraival, departure, k))