a = int(input('Enter First number of which you want to find HCM'))
b = int(input('Enter Second number of which you want to find HCM'))
c = 0
if a > b:
    for i in range(1, int(b/2 +1)):
        if b % i == 0 and a % i == 0:
            c = i
else:
    for i in range(1, int(a/2 +1)):
        if b % i == 0 and a % i == 0:
            c = i
print(c)
