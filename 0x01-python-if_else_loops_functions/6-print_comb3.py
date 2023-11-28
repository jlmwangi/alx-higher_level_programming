#!/usr/bin/python3
for digit_tens in range(10):
    for digit_ones in range(digit_tens + 1, 10):
        if (digit_tens == 8 and digit_ones == 9):
            print(f"{digit_tens}{digit_ones}", end ="")
        else:
            print(f"{digit_tens}{digit_ones}, ", end="")
