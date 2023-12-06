#!/usr/bin/python
def print_sorted_dictionary(a_dictionary):
    items_sorted = sorted(a_dictionary.items())
    for key, value in items_sorted:
        print("{}: {}".format(key, value))
