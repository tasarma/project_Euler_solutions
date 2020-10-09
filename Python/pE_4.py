# euler project problem 4

b = []
for i in range(100, 1000):
    for j in range(100, 1000):
        A = str(i*j)
        if A == A[::-1] and int(A)%11 == 0:
            b.append(int(A))
print(max(b))
