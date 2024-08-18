#8 check  python anagram
def are_anagrams(s1, s2):
    # Check if the lengths of the two strings are the same
    if len(s1) != len(s2):
        return False
    
    # Initialize dictionaries to store character counts
    count1 = {}
    count2 = {}
    
    # Count the characters in s1
    for char in s1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    
    # Count the characters in s2
    for char in s2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
    
    # Compare the character counts
    for key in count1:
        if key not in count2 or count1[key] != count2[key]:
            return False
    
    return True

# Test the function
s1 = "listen"
s2 = "silent"
if are_anagrams(s1, s2):
    print("it's anagram")
else:
    print("no")
