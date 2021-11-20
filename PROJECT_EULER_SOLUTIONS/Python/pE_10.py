#project euler problem 10

#sieve of eratosthenes algorithm is used
def summation_of_primes(x):
    s = 0
    sieve =  [True] * x
    for i in range(2, x):
        if sieve[i]:
            s += i            
            for j in range(i*i, x, i):
                sieve[j] = False
    return s

print (summation_of_primes(2000000))

