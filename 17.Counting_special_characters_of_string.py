def count_sp_char(string):
    sp_characters = "!@#$%^&*()<>?:'|,[]~{`}/"
    count=0
    for i in string:
        if i in sp_characters:
            count +=1
    return count

text = "Hii there !!! where have you been ??"
result = count_sp_char(text)
print(result)