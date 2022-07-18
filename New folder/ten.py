def max_integer(my_list=[]):
    if len(my_list)>0:
        for i in range (len(my_list)):
            x=0
            if x>my_list[i]:
                x=my_list[i]
            else:
                i+=1
           
            return my_list[i]
    else:
        return None;

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
