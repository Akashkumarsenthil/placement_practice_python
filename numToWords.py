#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:35:03 2020

@author: akashkumar
"""

n = 
ones_digit = {
        0:'',
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine"
        }
tens_digit = {
        0:'',
        2:"twenty",
        3:"thirty",
        4:"fourty",
        5:"fifty",
        6:"sixty",
        7:"seventy",
        8:"eighty",
        9:"ninety"
        }
elevenToTwenty = {
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"ninteen"
        }

s = str(n)
k = len(str(n))
if k == 1:
    print(ones_digit[n])
if k == 2:
    i = int(n / 10)
    j = int(n%10)
    if i == 1:
        print(elevenToTwenty[n])
    else:
        print(tens_digit[i],ones_digit[j],end = "")
if k == 3:
    i = int(n/100)
    j = int((n//10)%10)
    t = n % 100
    l = int(n%10)
    if j == 0 and t == 0:
        print(ones_digit[i], "hundred", end = "")
    elif j == 1:
        print(ones_digit[i],"hundred and",elevenToTwenty[t],end = "")
    else:
        print(ones_digit[i],"hundred and",tens_digit[j],ones_digit[l],end = "")
if k == 4:
    t = int(s[0])
    h = int(s[1])
    te = int(s[2])
    o  = int(s[3])
    tenplus = int(s[2] + s[3])
    
    if h == 0 and te == 0 and o == 0 :
        print(ones_digit[t],"thousand",end = "")
    elif h == 0 and te == 0:
        print(ones_digit[t],"thousand",ones_digit[o], end = "")  
    elif te == 1 and h == 0:
        print(ones_digit[t],"thousand",elevenToTwenty[tenplus])
    elif te == 1:
        print(ones_digit[t],"thousand",ones_digit[h],"hundred and",elevenToTwenty[tenplus], end = "")
    elif h == 0:
        print(ones_digit[t],"thousand",tens_digit[te],ones_digit[o], end = "") 
    else:
        print(ones_digit[t],"thousand",ones_digit[h],"hundred and",tens_digit[te], ones_digit[o], end = "")          
    
    