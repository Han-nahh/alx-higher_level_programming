#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    rev = my_list.reverse()
    while i < len(my_list):
        num = my_list[i]
        print("{}".format(num))
        i += 1
