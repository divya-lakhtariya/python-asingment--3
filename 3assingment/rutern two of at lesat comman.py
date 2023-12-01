#Write a Python function that takes two lists and returns true if they have at least one common member

n=int(input("enter numb :"))
l1=[]
l2=[]
l3=[]
count=0
print(" enter numbers :")
for i in range(n):
    a=input("enter element :")
    l1.append(a)
print("enter numbers :")
for i in range(n):
    b=input("enter element :")
    l2.append(b)
print(l1,l2)
for i in range(n):
    for j in range(n):
        if l1[j]==l2[i]:
            print(l1[j])
            count=count+1
print(" common member :")
