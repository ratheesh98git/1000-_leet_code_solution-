# 27 remove  vowels using python 

# Input string from user
user = input("Enter the string: ")

# String to store the result
new_string = ""

# Tuple of vowels to check against
vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

# Iterate over each character in the input string
for char in user:
    # Check if the character is not a vowel
    if char not in vowels:
        # Append the character to the new string if it's not a vowel
        new_string += char

# Print the result
print("String without vowels:", new_string)
