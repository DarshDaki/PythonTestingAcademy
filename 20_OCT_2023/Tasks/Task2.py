num = int(input("Enter your number:"))
sum = 0
while num != 0 or num > 9:
    digit = num % 10
    sum = sum + digit
    num //= 10
print(sum)
