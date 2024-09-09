# game on guessing a number

# steps

import random

value = random.randint(1, 10)
number = int(input("Enter Number :"))
while True:
    if number == value:
        print("You won the Game ")
        break
    elif number > value:
        print("entered number is to larger")
        # print(value)
        print("you loose it")
        number = int(input("Enter Number :"))

    else:
        print("enter number is to smaller")
        print("You loose it")
        # print(value)
        number = int(input("Enter Number :"))
