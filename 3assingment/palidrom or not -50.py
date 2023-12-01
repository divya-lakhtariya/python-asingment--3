# Write a Python function that checks whether a passed string is palindrome or not

def palindrome(x):
    return x ==x[::-1]
x = input('enter the word : ')
if palindrome(x):
    print('True')
else:
    print('False')

palindrome(x)
