#43  counting cononants in a given words


lists=["a","e","i","o","u"]

words="programming"

count=0


for character in words:
    if  character not in lists:
        count+=1
        
print(count)
