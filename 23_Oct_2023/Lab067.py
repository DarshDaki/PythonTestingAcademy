user_input = input("Enter the input string:\n")


def reverse_string(input_string):
    return ''.join(reversed(input_string))


rev_str = reverse_string(user_input)
print(rev_str)
