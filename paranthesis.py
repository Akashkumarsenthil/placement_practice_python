#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 15:23:20 2020

@author: akashkumar
"""
#code

         
def paranthesisCheck(k):
    if len(k) % 2 != 0:
        return "not balanced"
    
    for j in k:
        if j in opening:
            stack.append(j)
        else:
            if len(stack) == 0:
                return "not balanced"
            last_open = stack.pop()
            if (last_open, j) not in matches:
                return"not balanced"
                
    if len(stack) == 0:
        return "balanced"


n = int(input())
stack = []
opening = set('[({')
matches = set([ ('(', ')'), ('[', ']'), ('{', '}') ])
for i in range(n):
    k = [i for i in input()]    
    print(paranthesisCheck(k))
        
                            
        
        