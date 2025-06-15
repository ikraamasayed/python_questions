str1= "listen"
str2= "silent"

str1 = str1.replace(" ","").upper()
str2 = str2.replace(" ","").upper()

def anagram(b,d):
    if sorted(b) == sorted(d):
        print("true")
    else:
        print("false")
anagram(str2,str1)