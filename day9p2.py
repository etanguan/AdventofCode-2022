A = []
while True:
    temp = input().split(' ')
    if temp != ['q']:
        temp[1] = int(temp[1])
        A.append(temp)
    else:
        break
grid = []
for i in range(40):
    grid.append(['.']*40)

visited = set()
npos = []
for i in range(10):
    npos.append([0,0])


past = (-1,-1)
for move in A:
    for j in range(move[1]):
        if move[0] == 'U':
            npos[0][1] += 1
        elif move[0] == 'D':
            npos[0][1] -= 1
        elif move[0] == 'R':
            npos[0][0] += 1
        elif move[0] == 'L':
            npos[0][0] -= 1
        
        for i in range(1, len(npos), 1):

            if abs(npos[i - 1][0] - npos[i][0]) == 2 and abs(npos[i - 1][1] - npos[i][1]) == 2:
                if npos[i-1][0] - npos[i][0] > 0:
                    npos[i][0] += npos[i-1][0] - npos[i][0] - 1
                else:
                    npos[i][0] += npos[i-1][0] - npos[i][0] + 1

                if npos[i - 1][1] - npos[i][1] > 0:
                    npos[i][1] += npos[i-1][1] - npos[i][1] -1
                else:
                    npos[i][1] += npos[i - 1][1] - npos[i][1] + 1

            elif abs(npos[i-1][0] - npos[i][0]) == 2 and abs(npos[i-1][1] - npos[i][1]) == 1:
                if npos[i-1][0] - npos[i][0] > 0:
                    npos[i][0] += npos[i-1][0] - npos[i][0] - 1
                else:
                    npos[i][0] += npos[i-1][0] - npos[i][0] + 1

                npos[i][1] += npos[i-1][1] - npos[i][1]

            elif abs(npos[i-1][1] - npos[i][1]) == 2 and abs(npos[i-1][0] - npos[i][0]) == 1:
                if npos[i-1][1] - npos[i][1] > 0:
                    npos[i][1] += npos[i-1][1] - npos[i][1] - 1
                else:
                    npos[i][1] += npos[i-1][1] - npos[i][1] + 1

                npos[i][0] += npos[i-1][0] - npos[i][0]
            #elif abs(npos[i][0]-npos[i-1][0]) > 2:
            #    print(npos[i-1], npos[i])
            #elif abs(npos[i][1]-npos[i-1][1]) > 2:
            #    print(npos[i-1], npos[i])
            elif abs(npos[i][0]-npos[i-1][0]) == 2:
                if npos[i-1][0]-npos[i][0] > 0:
                    npos[i][0] += 1
                else:
                    npos[i][0] -= 1

            elif abs(npos[i][1]-npos[i-1][1]) == 2:
                if npos[i-1][1]-npos[i][1] > 0:
                    npos[i][1] += 1
                else:
                    npos[i][1] -= 1
        if (npos[9][0], npos[9][1]) != past:
            print((npos[9][0], npos[9][1]))
        past = (npos[9][0], npos[9][1])

        visited.add((npos[9][0], npos[9][1]))


print(visited)
print(len(visited))

