list = [2, 3, 99, 98, 6, 7, 8, 9]
a, b = 0, 0
for i in list:
    if i % 2 == 0:
        if i > a:
            a = i
    else:
        if i > b:
            b = i
print(a, b)