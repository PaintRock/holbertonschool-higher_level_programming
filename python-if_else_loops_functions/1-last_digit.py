#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
worf = str(number)[-1]
if int(worf) > 5:
    print(f"Last digit of {number} is {worf} and is greater than 5")
elif worf == 0:
    print(f"Last digit of {number} is {worf} and is 0")
elif int(worf) < 6 and int(worf) != 0:
    print(f"Last digit of {number} is {worf} and is less than 6 and not 0")