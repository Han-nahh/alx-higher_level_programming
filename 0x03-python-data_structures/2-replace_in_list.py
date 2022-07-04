#!/usr/bin/python3
def replace_in_list(my_list,idx,element):
    #idx = int(input("Input to which index you need this imported"));
    #element=int(input("Enter the new number"));
    if (idx < 0 ):
        print("None");
    elif(idx>=len(my_list)):
        return my_list;

    else:
        my_list[idx]=element;
        return my_list
