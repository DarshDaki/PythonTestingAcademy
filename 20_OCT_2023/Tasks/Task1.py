def reverse_string(input_string):
    reverse_str = ""
    for i in range(len(input_string) - 1, -1, -1):
        reverse_str += input_string[i]
    return reverse_str


user_input = input("Enter a input to find if it's a palindrome or not:\n").lower()

rev_str = reverse_string(user_input)
if user_input == rev_str:
    print("reversed string is:", rev_str)
    print("Palindrome")
else:
    print("reversed string is:", rev_str)
    print("Not a Palindrome")
