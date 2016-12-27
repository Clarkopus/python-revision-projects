import random

print("Welcome to the dice sim!")

num_of_dies = 0
usr_input = "\n"
num_of_rolls = 0
dice = [1, 2, 3, 4, 5, 6]


def roll(count, total):
    i = 1
    dice_count = 0

    for x in range(total):
        dice_count += 1

        for rolls in range(count + 1):
            print("die", dice_count, "roll", i, ":", str(dice[random.randint(0, 5)]), "\n")
            i += 1

            if i == count:
                i = 1
                print("Now rolling dice", dice_count)

        if dice_count == total:
            print("completed dice rolls")


num_of_rolls = int(input("Please enter the number of rolls you wish to perform\n"))
num_of_dies = int(input("Please enter the number of dies you wish to roll \n"))

roll(num_of_rolls, num_of_dies)
