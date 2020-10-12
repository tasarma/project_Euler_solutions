#project euler problem 15

#Binomial Coefficient was used 

import time

start = time.time()

def factorial(x):
    a=1
    for i in range(1,x+1):
        a *=i
    return a

answer = factorial(20+20)/(factorial(20)*factorial(20))

print(answer)

end = time.time()
print('time:',int(end-start))

