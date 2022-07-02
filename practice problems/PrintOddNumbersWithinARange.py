# I am gonna try and use generators
def printOdd(n):
    i = 0
    while i < n:
        if i%2 == 0:
            i = i + 1
            continue

        else:
            yield i
            i = i + 1
f = printOdd(10000000)
for i in f:
    print(i)