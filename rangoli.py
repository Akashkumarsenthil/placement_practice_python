#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:33:35 2020

@author: akashkumar
"""

n = int(input("Enter the number: "))

k = (n-1)*2
l = 1
r = 0

#printing top
for i in range(n):
    #print space
    for i in range(k):
        print("-", end = "")
        
    #print left star
    z = 65+n
    for j in range(l):
        if j==(l-1):
            print("*", end = "")
        else:
            print("*-", end = "")
    #print right star
    for w in range(r):
        print("-*", end = "")
    
    #print space
    for i in range(k):
        print("-", end = "")
    print()
    r = r+1
    l = l+1
    k = k-2
    

k = 2
l = n-1
r = n-1
#printing bottom
for a in range(n-1):
    #printing space
    for s in range(k):
        print("-", end = "")
    
    #printing left star
    for d in range(l):
        if a ==(n-1):
            print("*", end = "")
        if d==(l-1):
            print("*", end = "")
        else:
            print("*-", end = "")
    
    #printing right star
    for f in range(r-1):
        print("-*", end = "")
        
    #printing space
    for g in range(k):
        print("-", end = "")

    print()
    l = l-1
    r = r-1
    k = k+2
    