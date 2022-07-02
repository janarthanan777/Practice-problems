i = int(input('Give me a divisor'))
r = int(input('Give me a range'))
def numbers(divisor, rangee):
    for i in range(rangee):
        if i % divisor == 0:
            yield i
for x in numbers(i, r):
    print(x)