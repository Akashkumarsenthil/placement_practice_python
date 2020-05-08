#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:24:58 2020

@author: akashkumar
"""


import textwrap
string = "This is a very very very very very long string."
k = 2
kiq = (textwrap.fill(string,(len(string)/k)))
