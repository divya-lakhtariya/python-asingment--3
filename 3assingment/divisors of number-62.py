
# Write a Python program to returns sum of all divisors of a number
def sd(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
print(sd(8))
print(sd(12))
