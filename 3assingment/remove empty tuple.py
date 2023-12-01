#Write a Python program to remove an empty tuple(s) from a list of tuples.
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
a= []
for i in L:
    if i:
        a.append(i)

print("empty tuple removed:",a)

         
