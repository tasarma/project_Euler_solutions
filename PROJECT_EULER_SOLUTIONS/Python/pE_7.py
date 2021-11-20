# project euler problem 7

import sys

s=0
for i in range(2, sys.maxsize):
    a = 0 
    for j in range(2,int(i**0.5) + 1):
        if (i%j == 0):
             a += 1
             break
    if a ==0:
        s += 1
    if s == 10001:
        print('answer is ',i)
        break

