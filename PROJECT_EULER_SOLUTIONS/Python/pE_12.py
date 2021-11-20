#project euler problem 12

import time

start = time.time()

s=0
for i in range(1,100000):
    s +=i
    divisor_number = 0
    for j in range(1,int(s**0.5)): #find half of divisors with sqrt n
        if (s%j==0):
            divisor_number += 1
    divisor_number *=2 # product with 2 and find all divisors
    if (divisor_number > 500):
        print(s)
        break

end = time.time()
print('time: ',int(end-start))

