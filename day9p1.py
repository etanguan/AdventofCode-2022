A = []
while True:
    temp = input().split(' ')
    if temp != ['q']:
        temp[1] = int(temp[1])
        A.append(temp)
    else:
        break

visited = set()
hpos = [0, 0]
tpos = [0, 0]



for move in A:
    for i in range(move[1]):
        if move[0] == 'U':
            hpos[1] += 1
        elif move[0] == 'D':
            hpos[1] -= 1
        elif move[0] == 'R':
            hpos[0] += 1
        elif move[0] == 'L':
            hpos[0] -= 1

        if abs(hpos[0] - tpos[0]) == 2 and abs(hpos[1] - tpos[1]) == 1:
            if hpos[0] - tpos[0] > 0:
                tpos[0] += hpos[0] - tpos[0] - 1
            else:
                tpos[0] += hpos[0] - tpos[0] + 1

            tpos[1] += hpos[1] - tpos[1]

        elif abs(hpos[1] - tpos[1]) == 2 and abs(hpos[0] - tpos[0]) == 1:
            if hpos[1] - tpos[1] > 0:
                tpos[1] += hpos[1] - tpos[1] - 1
            else:
                tpos[1] += hpos[1] - tpos[1] + 1

            tpos[0] += hpos[0] - tpos[0]

        elif abs(tpos[0]-hpos[0]) > 1:
            if hpos[0]-tpos[0] > 0:
                tpos[0] += 1
            else:
                tpos[0] -= 1

        elif abs(tpos[1]-hpos[1]) > 1:
            if hpos[1]-tpos[1] > 0:
                tpos[1] += 1
            else:
                tpos[1] -= 1

        visited.add((tpos[0], tpos[1]))



print(visited)
print(len(visited))

