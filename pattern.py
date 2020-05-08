#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:33:35 2020

@author: akashkumar
"""

n = int(input("Enter the number: "))



i = n
k = (n-1)*2
p = 96+n
o = 1
t = 0
u = ((n-1)*2) - 1

#top part
for q in range(n):
    #printing "-"
    for w in range(k):
        print("-", end = "")
    
    #printing alphabets (Left)
    for e in range(o):
        if q == n-1 and e == n-1:
            print("{}".format(chr(p)), end = "")
            p = p-1         
        else:
            print("{}-".format(chr(p)), end = "")
            p = p-1
    
    #printing alphabets (Right)
    l = p+2
    for r in range(t):
        if q == n-1:
            print("-{}".format(chr(l)), end = "")
            l = l+1
        else:
            print("{}-".format(chr(l)), end = "")
            l = l+1
    
    #printing "-"
    for f in range(u):
        print("-", end = "")
        
    print()
    u = u-2
    o = o+1
    k = k-2
    p = 96+i
    t = t+1

#bottom part
k = 2
c = 96+n
b = n-2
for q in range(n-1):
    #printing "-"
    for w in range(k):
        print("-", end = "")
        
    #printing alphabets (Left)
    for v in range (0,b):
        print("{}-".format(chr(c)), end = "")
        c = c-1
    #printing alphabets (Right)
    for x in range(b+1):
        print("{}-".format(chr(c)), end = "")
        c = c+1
    #printing "-"
    for w in range(k-1):
        print("-", end = "")
        
    print()
    k = k +2
    b = b-1
    c = 96+n