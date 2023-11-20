# Fibonacci series
# 0,0+1, 0+1+1,
# n = 7
number = int(input("Enter a number :\n"))
a, b = 0, 1
while a <= number:
    print(a, end=" ")
    a, b = b, a + b
