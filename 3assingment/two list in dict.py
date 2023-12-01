# Write a Python program to map two lists into a dictionary.


a= ['rad', 'green', 'blue']
b= ['#FF0000','#008000', '#0000FF']
l= []
for i in range(len(a)):
    l.append((a[i],b[i]))
print(dict(l))
