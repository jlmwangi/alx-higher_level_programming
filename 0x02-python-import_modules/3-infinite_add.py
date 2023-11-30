#!/usr/bin/python3

import sys


def main():
    args = sys.argv[1:]
    res = sum(map(int, args))
    print("{}".format(res))


if __name__ == "__main__":
    main()
