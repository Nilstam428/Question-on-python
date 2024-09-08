# game on guessing a number

# steps

import random

value = random.randint(1, 10)
number = int(input("Enter Number :"))

if number == value:
    print("You won the Game ")
elif number > value:
    print("entered number is to larger")
    print("you loose it")
else:
    print("enter number is to smaller")
    print("You loose it")
