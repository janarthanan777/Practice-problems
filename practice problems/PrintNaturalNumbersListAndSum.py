x = int(input("Enter a number"))
for a in range(1, x + 1):
    for i in range(1, a):
        print(i, '+', end = ' ')
    print(a, ' = ', (a * (a+1))/2)