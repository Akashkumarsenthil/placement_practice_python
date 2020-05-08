#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:50:32 2020

@author: akashkumar
"""

s = input("Enter the string: ")
#s = "akash kumar"
q = ""
li = list(s.split(" "))

for i in li:
    i = i.capitalize()
    q = q + i + " "

print(q)