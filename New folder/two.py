#!/usr/bin/python3
def element_at(my_list, idx):
    idx=int(input("idx"));
    if (idx<0|idx>len(my_list)):
        return None;
    else:
        num=my_list[idx];
    return num;
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))


my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
