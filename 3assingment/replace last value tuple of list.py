
#Write a Python program to replace last value of tuples in a list.
l = [(10,20,40),(20,50, 60),(10,20,50)]
n=90
for i in range(len(l)):
        l1=list(l[i])
        l1[-1]=n
        l[i]=tuple(l1)
print("replace last value :",l)
