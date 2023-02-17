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

for i in A:
    mid = len(i)//2
    temp1 = i[:mid]
    temp2 = i[mid:]
    for j in range(len(temp1)):
        if temp1[j] in set(temp2):
            if temp1[j].isupper():
                total += ord(temp1[j]) - ord('A') + 27
                break
            else:
                total += ord(temp1[j])- ord('a') + 1
                break

print(total)