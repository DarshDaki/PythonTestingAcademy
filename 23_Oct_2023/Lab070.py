original_str = "Darshan"
reverse_str = lambda original_str: original_str[::1]

if reverse_str == original_str:
    print("Palindrome")
else:
    print("Not a Palindrome")
