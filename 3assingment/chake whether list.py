# Write a Python program to check whether a list contains a sub list

a = [2,4,3,5,7]
b = [4,3]
c = [3,7]

print(set(b).issubset(set(a)))
print(set(a).issubset(set(c)))
