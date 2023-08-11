#!/usr/bin/python3.8

if __name__ == "__main__":
    import sys

    args_count = len(sys.argv)

    if args_count > 1:
        print("{} argument:".format(args_count - 1) if args_count == 2 else
              "{} arguments:".format(args_count - 1))
        for arg in range(1, args_count):
            print("{}: {}".format(arg, sys.argv[arg]))
    else:
        print("0 arguments.")
