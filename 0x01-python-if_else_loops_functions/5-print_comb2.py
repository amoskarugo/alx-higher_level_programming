#!/usr/bin/python3.8
for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("0" + str(num) if num < 10 else num, end=", ")
