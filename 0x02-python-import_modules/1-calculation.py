#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    r = add(a, b)
    s = sub(a, b)
    m = mul(a, b)
    d = div(a, b)
    print("{} + {} = {}".format(a, b, r))
    print("{} - {} = {}".format(a, b, s))
    print("{} * {} = {}".format(a, b, m))
    print("{} / {} = {}".format(a, b, d))


if __name__ == "__main__":
    main()
