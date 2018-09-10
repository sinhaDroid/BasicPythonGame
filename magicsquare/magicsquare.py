"""
    Magic Square
"""

def magicSquare(n):
    square = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        square.append(l)
    
    i = n//2
    j = n-1

    num = n*n
    count = 1

    while(count<=num):
        if(i == -1 and j == n): # Condition 4
            j = n-2
            i = 0
        else:
            if(j == n): # Column value is exceeding
                j = 0
            
            if(i < 0):  # row is becoming -1
                i = n-1
            
        if(square[i][j] != 0):
            j = j-2
            i = i+1
            continue
        else:
            square[i][j] = count
            count += 1
        
        i = i-1
        j = j+1 # Condition 2
    
    for i in range(n):
        for j in range(n):
            print(square[i][j], end=" ")
        print()
    
    print("The sum of each row/column/diagonal is: "+str(n*(n**2 + 1)/2))


magicSquare(3)

# Solution
# 2 7 6
# 9 5 1
# 4 3 8
# The sum of each row/column/diagonal is: 15.0