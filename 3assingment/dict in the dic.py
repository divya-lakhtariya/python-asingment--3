# Write a Python script to check if a given key already exists in a dictionary.

a= int(input('Enter a number: '))
d = {1: 'd', 2: 'i', 3: 'v', 4: 'y', 5: 'a'}

if a in d.keys():
    print('Key is present ')
else:
    print('Key is not present ')

