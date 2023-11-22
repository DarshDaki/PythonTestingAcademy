num = int(input("Enter a number :\n"))

for i in range(num+1):
    for j in range(i):
        print("*",end="")
    print()
