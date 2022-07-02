n = int(input("Enter the length of the pascal's triangle you want to print"))
a = []
for i in range(n):
    temp = []
    for j in range(i + 1):
        if j == 0 or i == j:
            temp.append(1)
        else:
            temp.append(a[i-1][j-1] + a[i-1][j])
    a.append(temp)
print(a)



