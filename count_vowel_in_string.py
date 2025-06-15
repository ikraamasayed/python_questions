vowels = ["a","e","i","o","u"]
word="programming"

count=0
for alpha in word:
    if alpha in vowels:
        count +=1
print(count)