# Count vowels and consonants in a string
# aeiou

str = input("Enter a string to count the vowels and consonant:\n")
vowels_count = 0
consonant_count = 0
for char in str:
    if char == ('a' or 'e' or 'i' or 'o' or 'u'):
        vowels_count += 1
    else:
        consonant_count += 1

print(f"Count of vowels is : {vowels_count}")
print(f"Count of consonant is : {consonant_count}")
