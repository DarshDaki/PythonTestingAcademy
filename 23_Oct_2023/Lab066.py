original_string = input("Enter a string:\n")


def is_palindrome(input_string):
    rev_str = input_string[::-1]
    print(rev_str)

    if original_string == rev_str:
        print("Palindrome")
    else:
        print("Not a palindrome")


is_palindrome(original_string)
