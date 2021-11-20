#project euler problem 18

import time


start = time.time()

triangle ="""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

triangle = triangle.split('\n')

new_triangle = []
for i in range(1,len(triangle)-1):
    #seperate all values
    new_triangle.append(triangle[i].split(' '))


allnumbers = [] # to stop recursion function
indexes = []

def sumofnumbers(x,y):
    #x is list's index
    #y is index of a number inside inner list
    #finding sum of next two number
    #whichever sum is greater is the next number
    sum1 = int(new_triangle[x+1][y]) + int(max(new_triangle[x+2][y:y+2]))
    sum2 = int(new_triangle[x+1][y+1]) + int(max(new_triangle[x+2][y+1:y+3]))
    
    
    if (sum1>sum2):
        allnumbers.append(int(new_triangle[x+1][y]))
        indexes.append((x+1,new_triangle[x+1].index(new_triangle[x+1][y])))
        
        if (len(allnumbers) == len(new_triangle)-2):
            return
        else:
            return sumofnumbers(x+1,new_triangle[x+1].index(new_triangle[x+1][y]))

    else:
        allnumbers.append(int(new_triangle[x+1][y+1]))
        indexes.append((x+1,new_triangle[x+1].index(new_triangle[x+1][y+1])))
        
        if (len(allnumbers) == len(new_triangle)-2):
            return
        else:
            return sumofnumbers(x+1,new_triangle[x+1].index(new_triangle[x+1][y+1]))

print(sumofnumbers(0,0))

#Add first and last number and find sum 
allnumbers.insert(0,int(new_triangle[0][0])) 
allnumbers.append(int(max(new_triangle[indexes[-1][0]+1][indexes[-1][1]:indexes[-1][1]+2])))

print(sum(allnumbers))


end = time.time()
print('time: ',int(end-start))


