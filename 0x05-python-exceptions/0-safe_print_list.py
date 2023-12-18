#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    res = ""
    try:
        for i, element in enumerate(my_list):
            if i < x:
                res += str(element)
                printed += 1
            else:
                break
    except Exception as e:
        pass

    print(res)
    return (printed)
