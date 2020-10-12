#project euler problem 6

def sum_square_difference():
    sum1 = 0
    sum2 = 0
    for i in range(1,101):
        sum1 += i
        sum2 += i**2
    return sum1**2 - sum2

print(sum_square_difference())
