n = int(input('Enter a number to check for strong number'))
c = n
def factorial(x):
    a = 0
    if x == 1:
        return 1
    a = x * factorial(x-1)
    return a
b = 0
while n > 0:
    a = n % 10
    b += factorial(a)
    n = n // 10
if b == c:
    print('Number is a strong number')
else:
    print('Number is not a strong number')