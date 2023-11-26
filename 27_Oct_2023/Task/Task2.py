# 2. Write a Python program to find the smallest number in a list.
#

# -------------- method 1 --------------------
numbers = [10, 20, 30, 45, 78, 60, 12, 32, 3, 59, 26, 42]
small = numbers[0]

for ele in numbers:
    if ele < small:
        small = ele

print("The smallest number in a list using for loop is: ", small)

# -------------- method 2 --------------------
print("The smallest number in a list using min() is: ", min(numbers))

# -------------- method 3 --------------------
numbers3 = numbers.copy()
numbers3.sort()
print("The smallest number in a list using Sort() is: ", numbers3[0])

# -------------- method 4 --------------------
numbers3.reverse()
print("The smallest number in a list using reverse() is: ", numbers3[-1])
