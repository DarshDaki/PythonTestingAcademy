num = int(input("Enter a number to find the factorial:\n"))
fact = num
result = 0
if fact >= 0:
    result = 1
    print(f"Factorial of {num} is :-")
    while fact >= 1:
        result *= fact
        if fact > 1:
            print(f"{fact} X ", end="")
        else:
            print(f"{fact} = {result}", end="")
        fact = fact - 1
