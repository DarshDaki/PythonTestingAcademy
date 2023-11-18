num = int(input("Enter a number to find the factorial:\n"))
fact = num
result = 0
if fact >= 0:
    result = 1
    while fact >= 1:
        result *= fact
        fact = fact - 1

print(f"Factorial of {num} is: {result}", end="\n")
