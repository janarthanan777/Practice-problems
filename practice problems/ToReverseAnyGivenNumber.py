a = int(input('Enter First Number'))
rev = 0
b = len(str(a))
for i in range(len(str(a))):
    c = a % 10
    a = a // 10
    rev = rev + c * (10 ** (b - 1))
    b = b - 1
print(rev)