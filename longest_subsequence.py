#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 17:45:12 2020

@author: akashkumar
"""

n = 7
k = [i for i in list(map(int, input().split()))]
k.sort()
ans = 0
count = 0
for i in range(n):
    if k[i-1] + 1 == k[i] and i > 0:
        count += 1
    else:
        count = 1
    ans = max(ans, count)