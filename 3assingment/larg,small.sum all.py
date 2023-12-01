#Write a Python function to get the largest number, smallest num and sum of all from a list.



l= []
num=int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    l.append(numbers)
print("Maximum :", max(l), "\nMinimum:", min(l),"\nSum:", sum(l))
