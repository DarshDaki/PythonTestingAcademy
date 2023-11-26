# 1. Write a Python program to find the largest number in a list.

# -------------- method 1 --------------------
numbers = [1, 2, 3, 4, 78, 60, 12, 32, 3, 59, 26, 42]
large = 0

for ele in numbers:
    if ele > large:
        large = ele

print("The largest number in a list using for loop is: ", large)

# -------------- method 2 --------------------
print("The largest number in a list using max() is: ", max(numbers))

# -------------- method 3 --------------------
numbers3 = numbers.copy()
numbers3.sort()
print("The largest number in a list using Sort() is: ", numbers3[-1])

# -------------- method 4 --------------------
numbers3.reverse()
print("The largest number in a list using reverse() is: ", numbers3[0])
