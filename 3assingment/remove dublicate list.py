#Write a Python program to remove duplicates from a list.

l1=[12,15,11,12,8,15,3,3]  
print(l1)  
l2=[]  
for i in l1:  
    if i not in l2:  
        l2.append(i)  
 
print("duplicates ",l2) 
