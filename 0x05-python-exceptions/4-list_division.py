#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_lst = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrongtype")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        finally:
            new_lst.append(res)
    return (new_lst)
