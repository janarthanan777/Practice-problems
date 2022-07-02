n = int(input('Enter a number to check its prime factors'))
a = []
for i in range(2, int(n/2) + 3):
    if n % i == 0:
        a.append(i)
        while n % i == 0:
            n = n / i
print(a)
