#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:12:49 2020

@author: akashkumar
"""

def breakingRecords(scores):
    hs = [scores[0]]
    ls = [scores[0]]
    hs_c = 0
    ls_c = 0
    for i in range(len(1,scores)):
        if scores[i]>scores[i-1]:
            hs.append(scores[i])
            ls.append(ls[i-1])
            hs_c += 1

        if scores[i] < scores[i-1]:
            ls.append(scores[i])
            hs.append(hs[i-1])
            ls_c += 1


scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
hs = [scores[0]]
ls = [scores[0]]
hs_c = 0
ls_c = 0
for i in range(1, len(scores)):
    if scores[i] > scores[i-1] and scores[i] > hs[i-1]:
        hs.append(scores[i])
        ls.append(ls[i-1])
        hs_c += 1

    elif scores[i] < scores[i-1] and scores[i] < ls[i-1]:
        ls.append(scores[i])
        hs.append(hs[i-1])
        ls_c += 1
    
    else:
        ls.append(ls[i-1])
        hs.append(hs[i-1])
        
        





















