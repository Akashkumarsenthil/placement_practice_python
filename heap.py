#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:15:05 2020

@author: akashkumar
"""

import heapq

li = [4,2,5,1,6,3]
heapq.heapify(li)
li.top
heapq.heapify(li)
heapq.heappush(li, 3)
heapq.heapify(li)
heapq.heappop(li) + heapq.heappop(li)

heapq.heappushpop(li, 9)
heapq.heapreplace(li,4)
heapq.nsmallest(3, li)
heapq.nlargest(4, li)

heapq.heapreplace(li, 3)
li.remove(4)

import heapq
li = []
heapq.heapify(li)
for _ in range(int(input())):
    arr = list(map(int, input().strip().split(' ')))
    if arr[0] == 1:
        heapq.heappush(li, arr[1])
    if arr[0] == 2:
        li.remove(arr[1])
        heapq.heapify(li)
    if arr[0] == 3:
        print(min(li))
        
        
from heapq import heappush, heappop
valheap = []
delheap = []
for _ in range(int(input().strip())):
    lst = list(map(int, input().strip().split(' ')))
    if lst[0] == 1:
        heappush(valheap, lst[1])
    elif lst[0] == 2:

        if valheap[0] == lst[1]:
            heappop(valheap)
        else:
            heappush(delheap, lst[1])
    elif lst[0] == 3:
        check = bool(delheap)
        while check:
            if delheap[0] == valheap[0]:
                heappop(delheap)
                heappop(valheap)
                check = bool(delheap)
            else:
                check = False
        print (valheap[0])
        
        

from statistics import median 
a = [6, 7, 8, 9, 10,1, 2, 3, 4, 5]
a[:8]
i = 1
while(i <= len(a)):
    tem = a[:i]
    i += 1
    print(float(median(tem)))
    

arr = [6, 7, 8, 9, 10,1, 2, 3, 4, 5]
arr.sort()
k = 4
max(arr[:k])
min(arr[(len(arr)-k):])
print((max(arr[:k]) - min(arr[(len(arr)-k):])))

def runningMedian(a):
    a.sort()
    i = 1
    arr = []
    while(i <= len(a)):
        arr.append(float(median(a[:i])))
        i += 1
    return arr

arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

for i in range(len(arr)):
    print(i)

