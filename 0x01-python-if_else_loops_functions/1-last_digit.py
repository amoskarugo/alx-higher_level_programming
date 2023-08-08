#!/usr/bin/python3.8
import random
number = random.randint(-10000, 10000)
num_str = str(number)
num = int(num_str[-1]) if number >= 0 else int(num_str[-1]) * -1

if num < 6 and num != 0:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
elif num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
else:
    print(f"Last digit of {number} is {num} and is 0")
