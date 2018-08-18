"""
    Fizzbuss game
"""


def fizBuzz(value):
    for i in range(1, value):
        if(i % 3 == 0 and i % 5 == 0):
            print(str(i)+" = FizzBuzz")
        else:
            if(i % 3 == 0):
                print(str(i)+" = Fizz")
            else:
                if(i % 5 == 0):
                    print(str(i)+" = Buzz")
                else:
                    print(str(i))


fizBuzz(51)

# Solution
# 1
# 2
# 3 = Fizz
# 4
# 5 = Buzz
# 6 = Fizz
# 7
# 8
# 9 = Fizz
# 10 = Buzz
# 11
# 12 = Fizz
# 13
# 14
# 15 = FizzBuzz
# 16
# 17
# 18 = Fizz
# 19
# 20 = Buzz
# 21 = Fizz
# 22
# 23
# 24 = Fizz
# 25 = Buzz
# 26
# 27 = Fizz
# 28
# 29
# 30 = FizzBuzz
# 31
# 32
# 33 = Fizz
# 34
# 35 = Buzz
# 36 = Fizz
# 37
# 38
# 39 = Fizz
# 40 = Buzz
# 41
# 42 = Fizz
# 43
# 44
# 45 = FizzBuzz
# 46
# 47
# 48 = Fizz
# 49
# 50 = Buzz
# 1
# 2
# 3 = Fizz
# 4
# 5 = Buzz
# 6 = Fizz
# 7
# 8
# 9 = Fizz
# 10 = Buzz
# 11
# 12 = Fizz
# 13
# 14
# 15 = FizzBuzz
# 16
# 17
# 18 = Fizz
# 19
# 20 = Buzz
# 21 = Fizz
# 22
# 23
# 24 = Fizz
# 25 = Buzz
# 26
# 27 = Fizz
# 28
# 29
# 30 = FizzBuzz
# 31
# 32
# 33 = Fizz
# 34
# 35 = Buzz
# 36 = Fizz
# 37
# 38
# 39 = Fizz
# 40 = Buzz
# 41
# 42 = Fizz
# 43
# 44
# 45 = FizzBuzz
# 46
# 47
# 48 = Fizz
# 49
# 50 = Buzz
