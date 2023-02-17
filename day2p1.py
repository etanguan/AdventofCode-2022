from helperFile import *
A = strInputArraySplit(' ')
total = 0

for i in range(len(A)):
    if A[i][0] == "A":
        if A[i][1] == "X":
            total += 4
        if A[i][1] == "Y":
            total += 8
        if A[i][1] == "Z":
            total += 3
    if A[i][0] == "B":
        if A[i][1] == "X":
            total += 1
        if A[i][1] == "Y":
            total += 5
        if A[i][1] == "Z":
            total += 9
    if A[i][0] == "C":
        if A[i][1] == "X":
            total += 7
        if A[i][1] == "Y":
            total += 2
        if A[i][1] == "Z":
            total += 6

print(total)
