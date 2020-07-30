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
sorted(arr)
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



from collections import Counter
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print(Counter(myList).items)


def minimumAbsoluteDifference(arr):
    # com = list(combinations(arr, 2))
    return(min([abs(i[0] - i[1]) for i in list(permutations(arr, 2))]))


ord('a')

arr = set([i for i in range(8)])
arr.remove(1)





if 2 in arr:
    arr.remove(2)



print(list(input()))














































