#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            int_value = int(value)
            print("{:d} ".format(int_value))
            return True
    except (TypeError, ValueError):
        return False
