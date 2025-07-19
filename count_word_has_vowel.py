# filter only vowel words from line or sentence
# and count unique vowel words in whole sentence
newword = "i like python not html css python"
word_list = newword.split()
print(f'list of word {str(word_list)}')

def is_vowel_word(word):
    vowel = ['a','e','i','o','u']
    for alpha in word:
        if alpha in vowel:
            return True
    return False

vowel_word_list = []
for word in word_list:
    if is_vowel_word(word):
        vowel_word_list.append(word)
        
print(f'vowel list {vowel_word_list}')
print(f'total vowel word count {len(set(vowel_word_list))}')


