#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:38:04 2020

@author: akashkumar
"""

from collections import defaultdict
inp = list(map(int, input().split()))
n = inp[0]
inp = inp[1:]
even, odd = [], []
for i in range(n):
    m, s = int(max(str(inp[i]))), int(min(str(inp[i])))
    temp = (m * 11) + (s * 7)
    if len(str(temp)) > 2:
        temp = str(temp)
        temp = int(temp[-2:])
    if i % 2 == 0:
        even.append(temp)
    else:
        odd.append(temp)
count = 0
d = defaultdict(lambda : 0)
odd.sort()
even.sort()
for i in range(len(even)-1):
    if even[i] == even[i+1]:
        count += 1
    elif str(even[i])[0] == str(even[i+1])[0] and d[str(even[i])[0]] < 3:
        d[str(even[i])[0]] += 1
        count += 1
d = defaultdict(lambda : 0)
for i in range(len(odd)-1):
    if odd[i] == odd[i+1]:
        count += 1
    elif str(odd[i])[0] == str(odd[i+1])[0] and d[str(odd[i])[0]] < 3:
        d[str(odd[i])[0]] += 1
        count += 1
        
print(count)