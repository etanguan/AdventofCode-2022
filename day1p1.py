from helperFile import *

A = []
temp2 = 0
while True:
    temp = input()
    if temp != 'q':
        if temp != '':
            temp2 += int(temp)
        else:
            A.append(int(temp2))
            temp2 = 0

    else:
        break
A.sort(reverse=True)
print(A[0]+A[1]+A[2])