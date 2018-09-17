"""
    Jumbled Words
"""

import random


def choose():
    words = ["rainbow", "computer", "science", "programming",
             "mathematics", "player", "condition", "reverse", "water", "board"]
    pick = random.choice(words)
    return pick


def jumbled(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled


def thank(p1n, p2n, pp1, pp2):
    print(p1n, "Your score is: ", pp1)
    print(p2n, "Your score is: ", pp2)
    print("Thanks for playing")
    print("Have a nice day")


def play():
    p1Name = input("Player 1, Please enter your name\n")
    p2Name = input("Player 2, Please enter your name\n")
    pp1 = 0
    pp2 = 0
    turn = 0
    while(1):
        # Computer"s task
        picked_word = choose()
        # Create question
        qn = jumbled(picked_word)
        print(qn)
        if(turn % 2 == 0):
            # Player 1
            print(p1Name, "Your turn")
            ans = input("What is on my mind\n")
            if(ans == picked_word):
                pp1 += 1
                print("Your score is ", pp1)
            else:
                print("Better luck next time. I thought: ", picked_word)
            c = int(input("Press 1 to continue and 0 to quit: "))
            if(c == 0):
                thank(p1Name, p2Name, pp1, pp2)
                break
        else:
            # Player 2
            print(p2Name, "Your turn")
            ans = input("What is on my mind\n")
            if(ans == picked_word):
                pp2 += 1
                print("Your score is ", pp2)
            else:
                print("Better luck next time. I thought: ", picked_word)
            c = int(input("Press 1 to continue and 0 to quit: "))
            if(c == 0):
                thank(p1Name, p2Name, pp1, pp2)
                break
        turn += 1


play()


# Solution
# Player 1, Please enter your name
# Deepanshu
# Player 2, Please enter your name
# Monu
# eevsrer
# Deepanshu Your turn
# What is on my mind
# codinton
# Better luck next time. I thought:  reverse
# Press 1 to continue and 0 to quit: 1
# scincee
# Monu Your turn
# What is on my mind
# science
# Your score is  1
# Press 1 to continue and 0 to quit: 0
# Deepanshu Your score is:  0
# Monu Your score is:  1
# Thanks for playing
# Have a nice day