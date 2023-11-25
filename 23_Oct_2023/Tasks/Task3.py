num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))


def pow_fun(x, y):
    return pow(x, y)


print(f"power of {num1} ^ {num2} is: {pow_fun(num1, num2)}")
