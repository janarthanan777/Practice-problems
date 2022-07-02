i = int(input('Enter a number'))
a = 0
sum = 0
while i > 0:
    a = i % 10
    sum = sum + a
    i = i // 10
print(sum)