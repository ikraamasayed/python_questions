import re

string="Hii there where have you been ?? it's been 4 weeeks already"

digitCount= re.sub("[^0-9]","",string)
letterCount = re.sub("[^a-zA-Z]","",string)
spaceCount = re.sub("[ ]","",string)

print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))