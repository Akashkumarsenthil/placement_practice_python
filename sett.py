#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:53:57 2020

@author: akashkumar
"""


(_, A) = (int(input()),set(map(int, input().split())))
B = int(input())
for _ in range(B):
    (command, newSet) = (input().split()[0],set(map(int, input().split())))
    getattr(A, command)(newSet)

print (sum(A))