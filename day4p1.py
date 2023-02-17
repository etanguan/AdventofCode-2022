from helperFile import *
import re
A = []
total = 0

while True:
    temp = re.split('-|,', input())

    if temp != ['']:
        temp = [int (x) for x in temp]
        A.append(temp)
    else:
        break

for i in A:
    if i[0] <= i[2] and i[1] >= i[3]:
        total += 1

    elif i[0] >= i[2] and i[1] <= i[3]:
        total += 1

    elif i[0] <= i[2] <= i[1] <= i[3]:
        total += 1
    elif i[2] <= i[0] <= i[3] <= i[1]:
        total += 1



print(total)