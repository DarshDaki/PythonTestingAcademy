list1 = [10, 20, 30, 40]
tuple1 = (10, 20, 30, 40)
print(list1)


def mul_by10(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10


print(list1)
mul_by10(list1)
print(list1)
mul_by10(tuple1)
print(tuple1)
