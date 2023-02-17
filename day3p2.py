from helperFile import *

total = 0
A = []
counter = 0
while True:
    temp = input()
    if temp != '':
        temp = [c for c in temp]

        A.append(temp)
    else:
        break

for i in range(0, len(A), 3):

    for j in range(len(A[i])):
        if A[i][j] in set(A[i+1]) and A[i][j] in set(A[i+2]):
            if A[i][j].isupper():
                total += ord(A[i][j]) - ord('A') + 27
                break
            else:
                total += ord(A[i][j]) - ord('a') + 1
                break

print(total)