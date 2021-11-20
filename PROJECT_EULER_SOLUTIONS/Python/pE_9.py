#euler project problem 9

for i in range(1,1000):
    for j in range(1,1000):
        c = (i*i + j*j)**0.5
        if (i+j+c == 1000):
            print(i*j*c)
            break

