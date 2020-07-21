# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = int(input())

screens = {}


for i in range(0,n):
    string = input();
    arr = string.split()
    if arr[0] == "add-screen":
        add_screen(arr)
        

def add_screen(arr):
    screen_name = int(arr[1])
    rows = int(arr[2]) + 1
    cols = int(arr[3]) + 1
    screen_capacity = [[0 for i in range(cols)] for j in range(rows)]
    
    
    
arr = ["my", "name", "is", "akash", "kumar"]
for i in range(2,len(arr)):
    print(arr[i])
    
    
    
num = 1234
st = str(num)
new = st[4:1:-1]

sample = sorted([3,1,65,3,6], reverse = True)
sum(sample)/len(sample)
a = 1
b = 1
c = 2

print([[x,y,z] for x in range(0,a+1) for y in range(0,b+1) for z in range(0,c+1) if x+y+z != 3])


score = []
arr = []
for _ in range(0,3):
    name = input()
    score = float(input())
    arr.append([name,score])
    arr.sort(key = lambda x: x[1])
    
scores = list(dict.fromkeys(arr[:]))

scores = []
for _ in range(0,2):
    name = input()
    score = float(input())
    arr.append([name, score])
    scores.append(score)
second_score = sorted(list(dict.fromkeys(scores)))[1]
for name,score in sorted(arr):
    if score == second_score:
        print(name)


s = {}
s['akask'] = [2,3,5,7]
s['harsh'] = [5,3,6,1]

for ar in s:
    if ar == 'harsh':
        print(s[ar])
    

from itertools import combinations

n = int(input())
arr = list(input().split())
r = int(input())
tot_comb = list(combinations(arr,r))
req = filter(lambda x: 'a' in x,arr)
d = len(tot_comb)
n = d - len(req)
print(n/d)


ar = list(input().split())

tot_comb


ifa(tot_comb,2)

def ifa(tot_comb,r):
    for i in range(0,len(tot_comb)):
        print(tot_comb[i])



l = 0
r = 0
from itertools import product


l = list(combinations([1,2,3,4], 2))

r = list(product([1,2,3,4],[2,6,9]))


li = list(input().split())
li=0


li = [int(i) for i in range(0,len(li))]

x1 = lambda a : arr





multiply = lambda a,b : a*b

multiply(3,2)


list = [12, 65, 54, 39, 102, 339, 221, 50, 70]
result = list(filter(lambda x: (x%13 == 0), list))


s1 = "akash"
s2 = "sakah"

s1 = sorted(s1)
s2 = sorted(s2)

s=0
s = [[i,j] for i in s1 for j in s2]



print("akash ", end = "sd")



arr = 0
x = int(input())
arr = [int(input()) for _ in range(0,x)]

sums = []

def each (num):
    max = 0
    min = 0

for i in arr:


n = 75679

ar = list(n.)

from itertools import product, permutations
l = [int(x) for x in ]

import itertools

name = input().split()
letters = name[0].split()

l = input().split()
p = l[0].split()
r = int(l[1])
a = permutations(l[0], r)
for permutation in itertools.permutations(l[0], r):
    print(''.join(permutation))

s, n = input().split()
print(*[''.join(i) for i in permutations(sorted(s), int(n))], sep = "\n")
print(*[''.join(i) for i in permutations(sorted(s), int(n))])

s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')


names = ['akash', 'anish']


from itertools import combinations
s, n = input().split()
print(*[''.join(i) for j in range(1, int(n) + 1) for i in combinations(sorted(s), int(j))], sep = '\n')


from itertools import groupby


l = [char for char in input()]

for x,y in groupby(input()):
    print(x,len(list(y)))
    

from itertools import combinations, permutations, groupby
n = 2
l = input().split()

arr = list(combinations(l,n))

new = list(filter((lambda x : 'a' in x), arr))

print("{0:.3}". format(len(new) / len(arr)))

sum = 0
n = input().split()
for i in range(0,int(n[0])):
    a = [int(x) for x in input().split()]
    sum += max(a) ** 2 
print(sum % int(n[1]))

from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))




m, n = map(int, input().split())
k = (list(map(int, input().split())) for _ in range(m))
results = map(lambda x : sum(i**2 for i in x)%n, product(*k))
print(max(results))

sum = 0
n = input().split()
for i in range(0,int(n[0])):
    a = [int(x) for i in range(0,int(n[0])) for x in input().split()]
    sum += max(a) ** 2 


import itertools
k = (list(map(int, input().split())) for i in range(m))
results = map(lambda x: sum(i**2 for i in x) % n,product(*k))
print(max(results))



a = set([3,2,4,5,7,4,5,3,5,7])
a = set(set('akashkumar'))

a = set({'name': 'akash', 'roll': 'asdfa'})
a['name']


n = int(input())
s = set([input() for _ in range(n)])


print(*input().split())

n = int(input())
s = set(map(int, input().split()))
m = int(input())
arr = [input().split() for _ in range(m)]

eval('print(5)')



n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))
print(sum(s))


s = {}
s.{0}({1}) = 1



a = 2
from datetime import datetime, time

time(int('1000') // 100)


a = [3,6,4,3,6]

print(a[2])

n, d = map(int, input().split())
print(*[a[(i+d) % n] for i in range(n)])


[strings.count(q) for q in queries]


arr = [[0 for _ in range(5)] for _ in range(5)]

arr = 0
i = 0
arr = [[ for _ in range(5)] for _ in range(5)]


a = [[1,2,3],[4,5,6],[7,8,9]]
for i in a:
    print(i[2])

q = 1
w = 3

a[q:w] = range()
map(int, a)
        
b = a[:q] 

print(a[:(3-1)])
print(a[2:])

a = [5]*(4-1)


[:(a-1)] + [k]*(b-a+1) + [b:]

a = range(4,7)





    for i in range(len(queries)):
        for a,b,k in i:
            ar = arr[:(a-1)] + [k]*(b-a+1) + arr[b:]
    return max(ar)


return(max([:(a-1)] + [k]*(b-a+1) + [b:]) for i in range(len(queries)) for a,b,k in i)



a = [2,4,6,2,6,8,3,7,3,6]
print(a[(4-3):(5-1)])

s = a[]





arr = [0 for i in range(5)]
for i in queries:
    a, b, k = i[0] - 1, i[1], i[2]
    arr = arr[:a] + [x+k for x in arr[a:b]] + arr[b:]
return max(arr)

queries = [[1,2,100],[2,5,100],[3,4,100]]



arr = [0 for i in range(5)]
for i in queries:
    a, b, k = i[0] - 1, i[1], i[2]
    arr[a] += k
    arr[b] -= k
count = 0
h = 0
for i in arr:
    count += i
    if count>h:
        h = count
return h



   

















































