#!/usr/bin/python3.8

for letter in range(122, 96, -1):
    print("{}".format(chr(letter)) if letter % 2 == 0 else
          "{}".format(chr(letter - 32)), end="")
