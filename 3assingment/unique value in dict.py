# Write a Python program to print all unique values in a dictionary.


d=[{"V":"1"}, {"V": "2"}, {"VI": "1"}, {"VI": "5"}, {"VII":"5"}, {"V":"9"},{"VIII":"7"}]
a=[]
for i in d:
    for j in i.values():
        a.append(j)
print(set(a))
