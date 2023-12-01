#Write a Python program to count the number of strings where the stringlength is 2 or more and the first and last character are same from a givenlist of strings.

l1=[]
l2=[]
a=int(input("enter the number in the list: "))
for i in range(a):
    s=str(input())
    l1.append(s)
for x in l1:
    if len(x)>2 and x[0]==x[-1]:
        print(x)

