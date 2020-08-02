#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:05:31 2020

@author: akashkumar
"""

n = int(input())
for _ in range(n):
    ans = []
    l = list(map(int, input().split()))
    arr = [int(i) for i in input().split()]
    arr.sort()
    for _ in range(l[1]):
        ans.append(arr.pop())
    print(*ans)
    