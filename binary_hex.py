#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:30:46 2020

@author: akashkumar
"""

n = 17
width = len("{0:b}".format(n))
print(width)
for i in range(1,n+1):
  print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))