#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
output = "Last digit of {} is ".format(number)

if (number < 0):
    output += "-{} ".format(last_digit)
else:
    output += "{} ".format(last_digit)

if (last_digit > 5):
    output += "and is greater than 5"
elif (last_digit == 0):
    output += "and is 0"
else:
    output += "and is less than 6 and not 0"

print(output)
