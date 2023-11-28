#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for char in str:
        if (char.isalpha()):
            if char.islower():
                uppercase_str += chr(ord(char) - 32)
            else:
                uppercase_str += char
        else:
            uppercase_str += char
    print(uppercase_str + '\n', end='')
