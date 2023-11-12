# Compare two numbers:
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

result = "Greater than" if num1 > num2 else "Less than" if num1 < num2 else "Equal to"
print(f"{num1} is {result} {num2}")
