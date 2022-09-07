def safe_print_list(my_list=[],x=0):
    try:
        for i in range(0,x):
            print(my_list[i])
            i+=1
    except IndexError:
        print('')
    else:
        print("here")
    finally:
        print("still here")

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 3)
#print(nb_print)