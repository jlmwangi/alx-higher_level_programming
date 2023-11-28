#!/usr/bin/python3
begin = ord('a')
end = ord('z')

for val_ascii in range(begin, end + 1):
    letter = chr(val_ascii)
    if (letter != 'q' and letter != 'e'):
        print("{}".format(letter), end='')
