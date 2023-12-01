#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def uniq(a):
    l = []
    for x in range(a):
        b = int(input(" element: "))
        if b not in l:
            l.append(b)
    print("Unique elements:", l)

a = int(input("enter numb is: "))
uniq(a)
