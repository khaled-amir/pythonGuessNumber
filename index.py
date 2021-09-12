import random

random = str(random.randint(0,10))
number = input("Please guess a number between 0 and 10: ")

if number == random:
    print("Yep, you are true")
else:
    print("Oops you are wrong the right number is "+random)