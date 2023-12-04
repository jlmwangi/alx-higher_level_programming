#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return (None)
    else:
        max_num = my_list[0]
        for n in my_list:
            if n > max_num:
                max_num = n
        return max_num
