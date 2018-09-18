a = int(input())

m = []
for i in range(1, a+1):
    l = list(map(int, input().split()))
    m.append(l)

for i in range(a):
    for j in range(a):
        if(i >= j):
            if(j == a-1):
                print(m[i][j], end="")
            else:
                print(m[i][j], end=" ")
        else:
            if(j == a-1):
                print(0, end="")
            else:
                print(0, end=" ")
    if(i != a-1):
        print()
