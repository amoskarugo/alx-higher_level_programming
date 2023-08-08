#!/usr/bin/python3.8
for alphabet in range(ord("a"), ord("z") + 1):
    if chr(alphabet) in "qe":
        continue
    print("{}".format(chr(alphabet)), end="")
