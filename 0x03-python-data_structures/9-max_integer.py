#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) > 0:
        for i in range(len(my_list)):
            x = 0
            if x > my_list[i]:
                x = my_list[i]
            else:
                i += 1

            return my_list[i]
    else:
        return None;