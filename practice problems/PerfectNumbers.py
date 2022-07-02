n = int(input('Enter a number to check for perfect number condition'))
c = 0
for i in range(1, int(n/2 + 1)):
    if n % i == 0:
        c += i
if c == n:
    print('Number ist perfecshlang')
else:
    print("Number is not perfect shlang")
