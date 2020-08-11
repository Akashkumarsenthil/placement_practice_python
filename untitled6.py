#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:13:25 2020

@author: akashkumar
"""

n = [int(i) for i in input()]
temp = []
k = int(input())
l = len(n)
for i in range(k):
    m = max(n)
    k.append(m)
    n.remove(m)
    print(int("".join(map(str, n))))
    