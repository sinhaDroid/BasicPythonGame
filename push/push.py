def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [i for i in num_list if i != 0]
    x.extend(a)
    return(x)


def push(a):
    res = move_zero(a)

    for i in range(len(res)):
        if i == len(res) - 1:
            print(res[i], end="")
        else:
            print(res[i], end=" ")


print("Enter the number list with single space between them: ")
a = [int(x) for x in input().split()]
push(a)
