x = int(input('Enter the size of the correlation Matrix'))
for a in range(x):
    for b in range(x):
        if a == b:
            print('1', end = ' ')
        else:
            print('0', end = ' ')
    print()
