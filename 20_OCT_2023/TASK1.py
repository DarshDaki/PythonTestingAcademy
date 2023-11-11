def reverse_string(input_string):
    reverse_str = ""
    for char in input_string:
        reverse_str = char + reverse_str
    return reverse_str

user_input = input("Enter a input to find if it's a palindrome or not:\n")

if user_input == reverse_string(user_input):
    print("Palindrome")
else:
    print("Not a Palindrome")
