# ------------------ Method 1 : to print the value at input position ---------------------------
fib = int(input("Enter a number to find the fibonacci series:\n"))


def fibonacci1(num):
    a, b = 0, 1

    for i in range(2, num + 3):
        print(a, end=" ")
        a, b = b, a + b


fibonacci1(fib)

# ---------------------- Method 2 : to print entire series ----------------------------
print(end="\n\n")
fib2 = int(input("Enter a number to find the fibonacci series:\n"))


def fibonacci2(num):
    my_list = []
    a = 0
    b = 1
    my_list.append(a)
    my_list.append(b)
    if num == 0:
        return my_list[0]
    elif num == 1:
        return my_list
    else:
        for i in range(2, num + 1):
            a, b = b, a + b
            my_list.append(b)
        return my_list


print(f"Fibonacci series for {fib} is: {fibonacci2(fib2)}", end="\n")
