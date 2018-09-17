import random

doors = [0] * 3
goatdoor = [0] * 2

# No of swap wins
swap = 0
# No of don't swap wins
dont_swap = 0

j = 0
while j < 10:
    # xth door will comprise of BMW
    x = random.randint(0, 2)
    doors[x] = "BMW"
    for i in range(0, 3):
        if (i == x):
            continue
        else:
            doors[i] = "Goat"
            goatdoor.append(i)
    choice = int(input("Enter your choice "))

    # Open a door that comprises of goat
    door_open = random.choice(goatdoor)

    # door_open shouldn't be equal to choice made by the participant
    while (door_open == choice):
        door_open = random.choice(goatdoor)
    ch = input("Do you want to swap? y/n ")
    if (ch == 'y'):
        if (doors[choice] == 'Goat'):
            print("Player wins")
            swap = swap + 1
        else:
            print("Player lost")
    else:
        if (doors[choice] == 'Goat'):
            print("Player lost")
        else:
            print("Player wins")
            dont_swap = dont_swap + 1
    j = j + 1
print(swap)
print(dont_swap)