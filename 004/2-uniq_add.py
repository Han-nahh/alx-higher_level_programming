def uniq_add(my_list=[]):
    s=sum(set(my_list))
    return s

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))