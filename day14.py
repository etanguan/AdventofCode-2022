A = set()
lowest = -999999999
while True:
    temp = input()
    if temp == 'q':
        break
    temp = temp.split(">")
    for i in range(len(temp)):
        temp[i] = temp[i].strip('-')
        temp[i] = temp[i].strip(" ")
        temp[i] = temp[i].split(',')
        temp[i] = [int(x) for x in temp[i]]

    for i in range(len(temp)-1):
        if temp[i][0] != temp[i+1][0]:
            if temp[i][0] > temp[i+1][0]:
                for j in range(temp[i+1][0], temp[i][0]+1, 1):
                    A.add((temp[i][1], j))
                    lowest = max(lowest, temp[i][1])

            else:
                for j in range(temp[i][0], temp[i+1][0] +1, 1):
                    A.add((temp[i][1], j))
                    lowest = max(lowest, temp[i][1])
        else:
            if temp[i][1] > temp[i+1][1]:
                for j in range(temp[i+1][1], temp[i][1]+1, 1):
                    A.add((j, temp[i][0]))
                    lowest = max(lowest, j)
            else:
                for j in range(temp[i][1], temp[i+1][1]+1 , 1):
                    A.add((j, temp[i][0]))
                    lowest = max(lowest, j)

print(A)
total = 0
full = False
while full is False:
    cur = [0, 500]
    while True:
        if cur[0] == lowest+1:
            A.add((cur[0], cur[1]))
            total += 1
            break
        elif (cur[0]+1, cur[1]) not in A:
            cur[0] += 1
        elif (cur[0]+1, cur[1]-1) not in A:
            cur[0] += 1
            cur[1] -= 1
        elif (cur[0]+1, cur[1]+1) not in A:
            cur[0] += 1
            cur[1] += 1
        else:
            if cur[0] == 0 and cur[1] == 500:
                total += 1
                full = True
                break
            A.add((cur[0], cur[1]))
            total += 1
            break

print(total)



