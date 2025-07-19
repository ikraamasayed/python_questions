sentence = "there are to many RaceCar "

def find_pali(strng):
    pal_word = ''
    for word in strng.strip().lower().split(" "):
        if word[::-1]==word:
            pal_word = word
            print(f"{word} palindrom word")
    if pal_word=='':
        print(f"there is no palindrom word")

find_pali(sentence)