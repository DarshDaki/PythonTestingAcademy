# List
my_list = [1, 2, 3]
my_list2 = [1, True, "Darshan"]

print("Initial list:", my_list)

# Indexing
print("Element at index 0:", my_list[0])

# Changing an element
my_list[1] = 20
print("List after changing element:", my_list)

# append() used to add a element
my_list.append(4)
print("List after appending:", my_list)

# extend() used to add element from another list
my_list.extend([5, 6])
print("List after extending:", my_list)

# insert()
my_list.insert(1, 'a')
print("List after inserting 'a' at index 1: ", my_list)

# remove()
my_list.remove('a')
print("List after removing 'a':", my_list)

# clear()
my_copy_list = my_list.copy()
print(my_copy_list)

my_list.clear()
print("Initial list:", my_list)
print(my_copy_list)

# index
# print("Index of 3 in list: ", my_list.index(3))
print("Index of 3 in the copy list: ", my_copy_list.index(3))

# sort()
my_copy_list.sort()
print(my_copy_list)
my_copy_list.sort(reverse=True)
print(my_copy_list)

# reverse()
my_copy_list.reverse()
print(my_copy_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])

print("Length of copy list: ", len(my_copy_list))
