squares = [1, 4, 9, 16, 25, 1]
# index    0, 1, 2,  3,  4, 5
squares2 = squares.copy()

# Remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.
print(squares.pop(1))
print(squares)

# Remove first occurrence of value.
# Raises ValueError if the value is not present.
# return none
print(squares2.remove(1))
print(squares2)
