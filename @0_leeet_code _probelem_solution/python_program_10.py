#4 count the number of vowels in a string

def count(s):
    var="aeiou"
    return sum(1 for char in s   if char in var)
print(count("ratheesh"))
