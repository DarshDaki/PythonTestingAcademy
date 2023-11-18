# Loops

# Repeat a block of code multiple times

print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")

# range(start,stop, step)
# for int i = 1; i< 10 ; i++
for x in range(1, 10, 1):
    print(x, end="\n")
print("without start and step", end="\n")
for x in range(10):
    print(x, end="\n")

print("without start and step", end="\n")
for x in range(1, 10, 2):
    print(x, end="\n")
