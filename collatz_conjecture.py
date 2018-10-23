def checkNum(num):
    iterations = 1

    while(num != 1):
        if (num%2 == 0):
            num = int(num/2)
            iterations += 1
        else:
            num = (num*3) + 1
            iterations += 1

    print(num, iterations)

number = int(input("Enter the number to calculate number of iteration in collatz conjecture: "))

checkNum(number)