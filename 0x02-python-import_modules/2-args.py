#!/usr/bin/python3.8

if __name__ == "__main__":
    import sys

    args_len = len(sys.argv)

    if args_len > 1:
        print("{} arguments:".format(args_len - 1))
        for arg in range(1, args_len):
            print("{}: {}".format(arg, sys.argv[arg]))
    else:
        print("0 arguments.")
