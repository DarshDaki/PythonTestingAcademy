"""Using Break to exit a loop when i==51 while printing the values from 1 to 100"""
for i in range(1, 100):
    print(i, end="\t")
    if i == 51:
        break
