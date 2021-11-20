#project euler problem 19

#Solved by Zeller's congruence algorithm
#https://en.wikipedia.org/wiki/Zeller's_congruence

import time

start = time.time()

dayofmonths = { 13 : 31,
        14 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31 }


sundays = 0
for i in range(1901,2001):
    for x in range(3,15):
        for q in range(1,dayofmonths[x]+1):
            if (x == 13 or x == 14):
                t = str(i - 1)
                m = x
                K = int(t[2:])
                J = int(t[:2])
                h = (int(q) + int((13/5) * (m+1)) + K + int(K/4) + int(J/4) + 5*J)%7

                if (h == 1 and q ==1):
                    sundays += 1
            else:
                t = str(i)
                m = x
                K = int(t[2:])
                J = int(t[:2])
                h = (int(q) + int((13/5) * (m+1)) + K + int(K/4) + int(J/4) + 5*J)%7

                if (h == 1 and q ==1):
                    sundays += 1


print(sundays)


end = time.time()
print('time : {:.3f}'.format(end-start))

