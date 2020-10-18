#Project euler problem 22

import time 
from numpy import loadtxt
from urllib.request import urlopen

start = time.time()

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#letters = sorted(letters)

row_data = urlopen('https://projecteuler.net/project/resources/p022_names.txt')

dataset = loadtxt(row_data, dtype='str', delimiter=',')

# get rid of ""
for i in range(len(dataset)):
    dataset[i] = dataset[i].strip('""')


#calculate all name scores
def name_score(data):
    data = list(data)
    Sum = 0
    for i in data:  
        sum_of_inner_letter = 0
        for j in i:
            sum_of_inner_letter += (letters.index(j) + 1)
        Sum += ((data.index(i)+1) * (sum_of_inner_letter))
    return Sum


print(name_score(sorted(dataset)))


end = time.time()
print('time : {:.3f}'.format(end-start))

