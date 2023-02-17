from helperFile import *

A = []
while True:
    temp = input()
    if temp != 'q':
        temp = list(temp)
        temp = [int(x) for x in temp]
        A.append(temp)
    else:
        break
totals = 0
counted = []
for i in range(len(A)):
    temp = [False] * len(A[0])
    counted.append(temp)

#L-R
for i in range(len(A)):
    total = 0
    height = -1
    for j in range(len(A[0])):
        if A[i][j] > height:
            height = A[i][j]
            if counted[i][j] is False:
                total += 1
                counted[i][j] = True
    totals += total

#R-L
for i in range(len(A)):
    total = 0
    height = -1
    for j in range(len(A[0])-1, -1, -1):
        if A[i][j] > height:
            if counted[i][j] is False:
                total += 1
                counted[i][j] = True
            height = A[i][j]
    totals += total

#U-B
for i in range(len(A[0])):
    total = 0
    height = -1
    for j in range(len(A)):
        if A[j][i] > height:
            if counted[j][i] is False:
                total += 1
                counted[j][i] = True
            height = A[j][i]
    totals += total

#B-U
for i in range(len(A[0])):
    total = 0
    height = -1
    for j in range(len(A)-1, -1, -1):
        if A[j][i] > height:
            if counted[j][i] is False:
                total += 1
                counted[j][i] = True
            height = A[j][i]
    totals += total

print(counted)
print(totals)
