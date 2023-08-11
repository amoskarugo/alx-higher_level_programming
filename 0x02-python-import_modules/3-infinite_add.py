#!/usr/bin/python3.8

if __name__ == "__main__":
    import sys

    total = 0

    for item in range(1, len(sys.argv)):
        total = total + int(sys.argv[item])
    print("{}".format(total))
