sentence = "python is the programming language"

char_list = list(sentence.replace(" ",""))
count_char={}

for ch in char_list:
    if ch in count_char.keys():
        count_char[ch] +=1
    else:
        count_char[ch] =1

print('\n'*3)

# print(count_char)


end_result = {ch : sentence.replace(" ","").count(ch) for ch in set(sentence.replace(" ",""))}

print(end_result)


# count vowel in dict keys
vowel= ["a","e","i","o","u"]
is_vowel = lambda char: char in vowel 
count_vowel = 0
for ch in end_result.keys():
    if is_vowel(ch):
        count_vowel+=1

print(count_vowel)
