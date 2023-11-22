user_input = input("Enter the input string:\n")


# Palindrome
# Reverse the string and match with the old string it should be same
# 1 by using a Traditional method
# 2 built-in functions
def reverse_string(input_string):
    reverse_str = ""
    for char in input_string:
        reverse_str = char + reverse_str
    return reverse_str


rev_str = reverse_string(user_input)
print(rev_str)

if user_input == rev_str:
    print("Palindrome")
else:
    print("Not a Palindrome")
