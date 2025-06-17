string_value = "S P A C E S"
# string_value = string_value.replace(" ","")
# print(string_value)

string2 = "".join(char for char in string_value if char != " ")
print(string2)