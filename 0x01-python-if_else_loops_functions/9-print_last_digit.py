#!/usr/bin/python3
def print_last_digit(number):
<<<<<<< HEAD
    if number < 0:
        number = number * -1
    print("{:d}".format(number % 10), end='')
    return number % 10
=======
    print(abs(number) % 10, end="")
    return abs(number) % 10
>>>>>>> 184fab7127b08b5880efa6b25a56860620201a66
