#!/usr/bin/python3.8

def uppercase(str):
    for char in str:
        print("{}".format(char) if (ord(char) -32) < 65 or
              char == " " else "{}".format(chr(ord(char) - 32)), end="")

print(uppercase("aBc fJkl"))
