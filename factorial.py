k = int(input('Enter the number: '))

fac = 1
for i in range(1,k+1):
    if(k==0):
        break
    fac=fac*i

print(fac)