import random
"""A number-guessing game."""

t_or_f = True
guess = 0
name = input("Howdy, enter your name please: ")
print(f"Hello {name}, welcome to the guessing game!")

random_number = random(1,100)

while t_or_f:
    
    guess = input("Please input a number between 1 and 100: ")