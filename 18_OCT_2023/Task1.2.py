# ------------------ Method 1 : to print the value at input position ---------------------------
fib = int(input("Enter a number to find the fibonacci series:\n"))


def fibonacci1(num):
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


print(f"Fibonacci series of {fib} is: {fibonacci1(fib)}", end="\n")

# ---------------------- Method 2 : to print entire series ----------------------------

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
            c = a + b
            a = b
            b = c
            my_list.append(c)
        return my_list


print(f"Fibonacci series for {fib} is: {fibonacci2(fib2)}", end="\n")