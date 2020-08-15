#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:20:07 2020

@author: akashkumar
"""

def pallindrome(arr):
    h = int(len(arr)/2)
    j = len(arr) - 1
    i = 0
    while(i < h):
        if arr[i] != arr[j]:
            return
        i += 1
        j -= 1
    return 1

i, j = map(int, input().split())

n1 = [i,0,0,0,0,0,0]
n2 = [j,2,3,5,9,5,9]

ans = []

        