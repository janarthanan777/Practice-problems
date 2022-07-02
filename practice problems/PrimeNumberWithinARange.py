
def prime(n):
    count = 0
    for j in range(1, n):
        count = 0
        for i in range(1, int(j/2 + 1)):
            if j % i == 0:
                count += 1
        if count == 1:
            yield j
f = prime(1000000)
for i in f:
    print(i)