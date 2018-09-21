def add_digits(num):
    return (num - 1) % 9 + 1 if num > 0 else 0


def repeat(n):
    res = add_digits(n)
    print(res)


num = int(input("Enter the number: "))
repeat(num)
