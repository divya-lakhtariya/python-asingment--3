#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

list1 = []

for x in range(1,31):
    list1.append(x**2)

print(list1[:5] + list1[-5:])
