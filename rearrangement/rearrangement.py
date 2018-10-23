def fix(A, len):

    for i in range(0, len):

        if (A[i] != -1 and A[i] != i):
            x = A[i]

            # check if desired place
            # is not vacate
            while (A[x] != -1 and A[x] != x):
                # store the value from
                # desired place
                y = A[x]

                # place the x to its correct
                # position
                A[x] = x

                # now y will become x, now
                # search the place for x
                x = y

            # place the x to its correct
            # position
            A[x] = x

            # check if while loop hasn't
            # set the correct value at A[i]
            if (A[i] != i):

                # if not then put -1 at
                # the vacated place
                A[i] = -1


# Driver function.
A = []
A = list(map(int, input().split()))

fix(A, len(A))

for i in range(0, len(A)):
    if(i == len(A)-1):
        print(A[i], end='')
    else:
        print(A[i], end=' ')
