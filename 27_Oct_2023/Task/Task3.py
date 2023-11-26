# 3. Write a Python program to sum all numbers in a list.
#

# -------------- method 1 --------------------
numbers = [10, 20, 30, 45, 78, 60, 12, 32, 3, 59, 26, 42]
sum1 = 0
for i in numbers:
    sum1 += i

print("The sum of all the element in list is: ", sum1)

# -------------- method 2 --------------------
print(f"The sum of all the element in list is: {sum(numbers)}")
