#project euler problem 5

def smallest_multiple():
    numbers = [*range(2,21)] # numbers from 2 to 20
    result = 1 
    for i in range(2,21):
        b = 0 #number of 
        a =1
        while a<10:
            if i not in numbers: # Check if i in list 
                break
            b +=1  
            for j in numbers:                
                if (j%i == 0):
                    numbers[numbers.index(j)] =j/i # update list               
            a +=1
            
        if (b != 0):            
            result = result*(i**b)

    return result
print(smallest_multiple())
