# 4. Write a Python program to multiply all numbers in a list.
#

# -------------- method 1 --------------------
numbers = [10, 20, 30, 45, 78, 60, 12, 32, 3, 59, 26, 42]
multi = 1
for i in numbers:
    multi *= i

print("The multiplication of all the element in list is: ", multi)
