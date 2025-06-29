heterogeneous_list= ["ikraama",24,2021,7+3j,"sayyed","234"]
listint=[]
print(heterogeneous_list)
for i in heterogeneous_list:
    if type(i) == int:
        listint.append(i)
print(listint)