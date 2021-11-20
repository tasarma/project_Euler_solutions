#project euler problem 14

import time

start = time.time()

def number(x):
    n = 0
    if (x%2==0):
        n = x/2
    else:
        n = 3*x + 1
    return n

b = 0
answer=0
for i in range(1,10**6,2):
    a=i
    s = 0
    while a>1:
        a = number(a)
        s +=1
    if (s>b):
        b=s
        answer = i
print(answer)

end = time.time()
print('time: ',int(end-start))

