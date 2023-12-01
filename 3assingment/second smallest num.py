 # Write a Python program to find the second smallest number in a list.

li = [] 
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    a= int(input("Enter the elements: ")) 
    li.append(a)
    li.sort() 

print("list: ", li) 
print("second smallest : ",li[1])
