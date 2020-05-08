#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:35:23 2020

@author: akashkumar
"""

n = 9
m = 27

temp = 1
for i in range(0,n//2):
    print((".|."*temp).center(m,"-"))
    temp += 2 
print("WELCOME".center(m,"-"))
for i in range(0,n//2):
    temp -= 2
    print((".|."*temp).center(m,"-"))