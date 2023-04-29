print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 10 attempts to guess the number.")
print("Let's get started!\n")

import random

att = 10
a = random.randint(1,100)

while att:
    n = int(input("Enter your guess (between 1 and 100):"))
    if n < a:
        print("The number you guessed is too small.")
        print("Try again!")
    elif n > a:
        print("The number you guessed is too large.")
        print("Try again!")
    else:
        print("Your number is", n)
        print("You won the game!")
        break
    att -= 1
else:
    print("You lose! The number was", a)
