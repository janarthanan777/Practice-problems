a = int(input('Enter First number of which you want to find LCM'))
b = int(input('Enter Second number of which you want to find LCM'))
max = 0
if a > b:
    max = a
else:
    max = b
while True:
    if max % a == 0 and max % b == 0:
        print('Lcm is :', max)
        break
    else:
        max += 1
