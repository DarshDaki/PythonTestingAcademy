fact = int(input("Enter a number to find the factorial:\n"))
result = 0
if fact >= 0:
    result = 1
    while fact >= 1:
        result *= fact
        fact = fact - 1

print(f"Factorial of {fact} is: {result}", end="\n")