from queue import PriorityQueue
A = []
S = (0, 0)
E = (0, 0)
while True:
    temp = input()
    if temp != 'q':
        A.append(list(temp))
    else:
        break

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == "S":
            S = (0, [i, j, 0])
            A[i][j] = 'a'
        if A[i][j] == 'E':
            E = (i, j)
            A[i][j] = 'z'


found = False
visited = {(S[1][0], S[1][1])}
pq = PriorityQueue()

pq.put(S)
while found is False:

    cur = pq.get()
    cur = cur[1]

    if (cur[0], cur[1]) == E:
        print(cur[2])
        break
    if cur[0]+1 < len(A):

        if ord(A[cur[0]+1][cur[1]]) <= ord(A[cur[0]][cur[1]]) + 1:
            if (cur[0]+1, cur[1]) not in visited:
                new = cur.copy()
                new[0] += 1
                new[2] += 1
                pq.put((new[2], new))
                visited.add((new[0], new[1]))
    if cur[0]-1 >= 0:
        if ord(A[cur[0]-1][cur[1]]) <= ord(A[cur[0]][cur[1]]) + 1:
            if (cur[0]-1, cur[1]) not in visited:
                new = cur.copy()
                new[0] -= 1
                new[2] += 1
                pq.put((new[2], new))
                visited.add((new[0], new[1]))

    if cur[1]+1 < len(A[0]):
        if ord(A[cur[0]][cur[1]+1]) <= ord(A[cur[0]][cur[1]]) + 1:
            if (cur[0], cur[1]+1) not in visited:
                new = cur.copy()
                new[1] += 1
                new[2] += 1
                pq.put((new[2], new))
                visited.add((new[0], new[1]))

    if cur[1]-1 >= 0:
        if ord(A[cur[0]][cur[1]-1]) <= ord(A[cur[0]][cur[1]]) + 1:
            if (cur[0], cur[1]-1) not in visited:
                new = cur.copy()
                new[1] -= 1
                new[2] += 1
                pq.put((new[2], new))
                visited.add((new[0], new[1]))

