#!/usr/bin/python3

import sys


def main():
    args = sys.argv[1:]

    n = len(args)

    if n == 0:
        print("0 arguments")
    elif n == 1:
        print("1 argument:")
        print("1:", args[0])
    else:
        print(n, "arguments:")
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
