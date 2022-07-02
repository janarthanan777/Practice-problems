def armstrong(n):
    for i in range(n):
        sum, a = 0, 0
        b = i
        c = len(str(i))
        while i > 0:
            a = i % 10
            sum += a**c
            i = i // 10
        if sum == b:
            yield b
f = armstrong(100000)
for x in f:
    print(x)


