import random

account = 0

for i in range(365):
    bet = random.randint(1, 10)
    lucky_draw = random.randint(1, 10)

    if bet == lucky_draw:
        account = account + 900 - 100
    else:
        account = account - 100

print("Amount in your game account: ", account)
