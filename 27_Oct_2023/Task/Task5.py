# 5. Write a Python program to count the number of strings in a list
# where the string length is 2 or more and the first and last character are the same.

list_string = ["add", "minimum", "abca", "zxcvbn", "asdfds", "12321"]
count = 0
for st in list_string:
    if len(st) > 2 and st[0] == st[-1]:
        count += 1

print("The count of string whose length is 2 or more and the first and last character are the same is :", count)
