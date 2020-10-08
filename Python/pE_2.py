#projecy euler problem 2

a=1
b=1
s=0
while a <= 4000000:
    a,b=b,a+b
    if (b%2==0):
        s +=b
        
print(s)
