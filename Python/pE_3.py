#project euler problem 3

# Find first 1000 prime factor
def prime_factor():
    pf = []
    while len(pf) <= 1000:
        for i in range(2,10000):
            a = 0 
            for j in range(2,10000):
                if (i%j==0) and (i != j):
                    a += 1
                    break
            if (a==0):
                pf.append(i)

    return pf

print(max([i for i in prime_factor() if 600851475143%i == 0]))
