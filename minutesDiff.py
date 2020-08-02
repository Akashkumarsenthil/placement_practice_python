#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:46:52 2020

@author: akashkumar
"""
from timedate import timedelta
strArray = ["2:10pm", "1:30pm", "10:30am", "4:42pm", "11:45pm", "12:10am"]
minutes = []
for i in strArray:
    h = int(i.split(':')[0])
    m = int(i[:len(i)-2].split(':')[1])
    mes = i[len(i)-2:]
    x = timedel
    if h == 12 and mes == 'am':
        h = 0
    if mes == "pm":
        h += 12
    minutes.append(int(h)*60 + int(m))
    
diff = [abs(minutes[i] - minutes[i-1]) for i in range(1, len(minutes))]
print(min(diff))