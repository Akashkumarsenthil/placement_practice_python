#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 20:54:48 2020

@author: akashkumar
"""

T = int(input())
for _ in range(T):
    N = int(input())
    each_array = [int(i) for i in input().split()]
    tem = []
    for ele in range(len(each_array)):
        tem.append(each_array[ele] % 3)
    total_Number_Of_Zeros = tem.count(0)
    total_Number_Of_Ones = tem.count(1)
    total_Number_Of_twos = tem.count(2)
    if total_Number_Of_Ones == 0 and total_Number_Of_twos == 0:
        print("YES")
    elif total_Number_Of_Zeros == 0 and total_Number_Of_Ones == 0:
        print("YES")
    elif total_Number_Of_Zeros == 0 and total_Number_Of_twos == 0:
        print("YES")
    elif total_Number_Of_Ones + total_Number_Of_twos - 1 <= total_Number_Of_Zeros <= total_Number_Of_Ones + total_Number_Of_twos + 1 :
        print("YES")
    else:
        print("NO")
        