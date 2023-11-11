fact = int(input("Enter a number to find the factorial:\n"))
result = 0
if fact >= 0:
    result = 1
    while fact >= 1:
        result *= fact
        fact = fact - 1

print(f"Factorial of {fact} is: {result}", end="\n")

fib = int(input("Enter a number to find the fibonacci series:\n"))


def fibonacci(num):
    a = 0
    b = 1
    if num == 0:
        return a
    elif num == 1:
        return b
    else:
        for i in range(2, num + 1):
            c = a + b
            a = b
            b = c
        return b


print(f"Fibonacci series of {fib} is: {fibonacci(fib)}", end="\n")
