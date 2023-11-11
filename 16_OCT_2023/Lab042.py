# Use the ternary operator to find the maximum of three numbers entered by the user.

num1 = int(input("Enter the First number : \n"))
num2 = int(input("Enter the Second number : \n"))
num3 = int(input("Enter the Third number : \n"))

max = num1 if (num1 > num2 and num1>num3) else num2 if (num2> num3 ) else num3
print(f"Max of three numbers {num1}, {num2} and {num3} is:{max}", end="\n\n")
