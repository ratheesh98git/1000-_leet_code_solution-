#42  counting  vowels in a given words


vowels=["a","e","i","o","u"]

character="ratheesh"
count=0


for items in  character:
    if items in  vowels:
        count+=1
        
print(count)