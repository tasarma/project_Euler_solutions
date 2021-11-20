#project euler problem 21

import time

start = time.time()

def divisor(x):
    # Find divisors of a number
    
    sum_div = 0
    for i in range(2, int(x**0.5)+1):
        if (x%i == 0):
            if (i == (x/i)):
                sum_div += i
            else:
                sum_div += (i + x/i)

    return sum_div + 1


sum_amicable_numbers = 0

for i in range(2,10001):
    number1 = divisor(i)
    number2 = divisor(number1)
    if ( i == number2) and ( i != number1):
        sum_amicable_numbers += i  

print(sum_amicable_numbers)

end = time.time()
print('time : {:.3f}'.format(end-start))

