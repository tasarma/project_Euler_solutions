#project euler problem 1

sum_of_numbers = 0
for i in range(1000):
    if (i%3==0) or (i%5==0):
        sum_of_numbers +=i

print(sum_of_numbers)
