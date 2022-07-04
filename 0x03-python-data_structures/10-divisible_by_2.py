#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            print("{:d} divisible by 2".format(my_list[i]))
        else:
            print("{:d} is not divisible by 2".format(my_list[i]))
