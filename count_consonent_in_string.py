#Consonant is opposite of vowel

vowels = ["a","e","i","o","u"]
word="programming"

count=0
for character in word:
    if character not in vowels:
        count +=1
print(count)