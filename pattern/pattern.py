def pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            if j == i:
                print(j, end='')
            else:
                print(j, end=' ')
        print()


n = int(input())
pattern(n)
