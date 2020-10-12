#project euler problem 20

import time

start = time.time()


def factorial(x):
    #Calculate factorial of 100
    if (x <= 1):
        return 1
    else:
        return x * factorial(x-1)

factorial_of_100 = str(factorial(100))

a = [ int(factorial_of_100[i]) for i in range(len(factorial_of_100))]

print(sum(a))


end = time.time()
print('time : {:.3f}'.format(end-start))

