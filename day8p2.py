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
    temp = [1] * len(A[0])
    counted.append(temp)


#L-R
for i in range(len(A)):
    for j in range(len(A[0])):
        count = 0
        for k in range(j+1, len(A[0]), 1):
            if A[i][j] > A[i][k]:
                count += 1
            else:
                count += 1
                break

        counted[i][j] *= count


#R-L
for i in range(len(A)):
    for j in range(len(A[0])-1, -1, -1):
        count = 0
        for k in range(j -1 , -1, -1):
            if A[i][j] > A[i][k]:
                count += 1
            else:
                count += 1
                break
        counted[i][j] *= count

#U-B
for j in range(len(A[0])):
    for i in range(len(A)):
        count = 0
        for k in range(i + 1, len(A), 1):
            if A[i][j] > A[k][j]:
                count += 1
            else:
                count += 1
                break
        counted[i][j] *= count

#B-U
for j in range(len(A[0])):
    for i in range(len(A)-1, -1, -1):
        count = 0
        for k in range(i-1, -1, -1):
            if A[i][j] > A[k][j]:
                count += 1
            else:
                count += 1
                break
        counted[i][j] *= count

print(max(max(x) for x in counted))


