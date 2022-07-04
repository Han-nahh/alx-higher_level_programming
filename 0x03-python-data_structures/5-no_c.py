#!/usr/bin/env python3
def no_c(my_string):
    conv = list(my_string)
    index = 0
    edited = ""
    if(len(my_string)) == 0:
        return my_string
    else:
        new = conv[:]
        for i in new[:]:
            if i == 'c' or i == 'C':
                del new[index]
                index -= 1
            index += 1
        return edited.join(new)
