#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:45:37 2020

@author: akashkumar
"""

def median(arr):
    arr.sort()
    n = len(arr)
    print(float((arr[int(n/2)-1] + arr[int(n/2)]) / 2 )) if n%2 == 0 else print(arr[int(n/2)])


arr1 = [5,3,1,6,8,12]
arr2 = [2, 4, 6]
arr = arr1 + arr2
median(arr)

