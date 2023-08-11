#!/usr/bin/python3.8

a = 1
b = 2
if __name__ == "__main__":
    from add_0 import add
    print("{} + {} = {}".format(a, b))
else:
    __import__("add_0")
