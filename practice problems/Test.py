i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def binary(list, number):
    count = False
    min = 0
    max = len(list)
    for i in range(max):
        if list[int((min + max)/2)] == number:
            print('Yeah the number is present')
            count == True
            break
        elif number > list[int((min + max)/2)]:
            min = int((min + max)/ 2)
            continue
        if number < list[int((min + max)/2)]:
            max = int((min + max)/ 2)
            continue
    if count == False:
        print('Number not present')
binary(i, 1)