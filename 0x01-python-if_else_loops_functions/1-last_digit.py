#!/usr/bin/python3.8
import random
number = random.randint(-10000, 10000)
num_str = str(number)
if int(num_str[-1]) < 6 and int(num_str[-1]) != 0:
    print(f"Last digit of {number} is {num_str[-1]} and\
 is less than 6 and not 0")
elif int(num_str[-1]) > 5:
    print(f"Last digit of {number} is {num_str[-1]} and is greater than 5")
else:
    print(f"Last digit of {number} is {num_str[-1]} and is 0")
