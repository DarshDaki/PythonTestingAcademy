# String
# Bunch of Char
name = "Darshan"
print("Memory address of : ",name," is -> ",id(name))
name = "Daki"
print("Memory address of : ",name," is -> ",id(name))

num = 56
print("Memory address of : ",num," is -> ",id(num))
num = 62
print("Memory address of : ",num," is -> ",id(num))


# String Functions
# Python String Immutable in Nature - They can't changed!, One Created
# name[0] = "h" # TypeError: 'str' object does not support item assignment

# capitalize()
# Returns a copy of the string with its first character capitalized.
result = name.capitalize()
print(result)
print(name)

print(id(name))
print(id(result))

# Upper Case
result2 = name.upper()
print(result2)

# Lower
result3 = name.lower()
print(result3)
print(id(result3))  # Identity - Address Ref.

# Swapcase()
# Returns a copy of the string with uppercase characters converted to lowercase
# and vice versa.

name = "dArShaN"
print(name.swapcase())

# Title
# Returns a titlecased version of the string,
# where words start with an uppercase character and
# the remaining characters are lowercase.

name = "hello world"
print(name.title())

t1 = "Daki ji"
t2 = "Darshan ji"
print(t1.capitalize())
print(t2.upper())

# t1 is ref or variable name ,  "Daki ji" which is stored in memory

name = "Daki"
print(len(name))

# Replace
text = "hello world"
result_rep = text.replace("world","Python")
print(result_rep)

#index and len
name  = "Darshan"
# len -> 1
print(len(name))
# index - 0 to len-1
# p - 0, r - 1, a - 2, m - 3 , 0-4, d -5


#find()
#Returns the lowest index of a substring in the string.
# Returns -1 if the substring is not found.

text = "hello world"
index = text.find("world")
print(index)



#count() - count the char -
count = text.count("l")
print(count)


name = "p d"
print(len(name))


name = "Darshan"
print(name)
del name
#print(name)



