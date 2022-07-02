x = int(input('Enter a number'))
rev = 0
b = x
while x > 0:
    a = x % 10
    rev = rev * 10 + a
    x = x // 10
print(rev)
if b == rev:
    print('The number entered is a palindrome')
else:
    print('Na beta palindrome nahi hai')
