#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for n in names:
        if not n.startswith("__"):
            print(n)
