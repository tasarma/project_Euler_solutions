#project euler problem 17


numbers = { 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
        7:'seven', 8:'eight',9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
        13:'thirteen', 14:'Fourteen', 15:'fifteen', 16:'sixteen',
        17:'seventeen', 18:'eighteen', 19:'niniteen',
        20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',
        70:'seventy', 80:'eighty', 90:'ninety'
        }

def firstnumber(x):
    x = str(x)
    return int(x[0])


a = ''
for i in range(1,1000):
    remainder = 0
    dividend = 0
    remainder2 = 0
    if i in numbers:
        a += numbers[i]

    elif 20< i <=99:
        remainder = i%10
        dividend = i - remainder
        a += numbers[dividend]
        a += numbers[remainder]

    elif i>99:
        w = firstnumber(i)
        a += numbers[w]
        a += 'hundred' 

        remainder = i%100 
        if remainder == 0:
            pass
        elif remainder in numbers: 
            a += 'and'
            a += numbers[remainder]
        else:
            remainder2 = remainder%10
            dividend = remainder - remainder2
            a += 'and'
            a += numbers[dividend]
            a += numbers[remainder2]

a +='onethousand'

print(len(a))

