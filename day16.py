from collections import defaultdict

added = set()
def check(cur, m, p):
    if m == 30:
        return 0
    temp = []
    if cur not in added and psi[cur] != 0:
        added.add(cur)
        temp.append(check(cur, m + 1, p + psi[cur]) + p)

    for i in graph[cur]:
        temp.append(check(i, m+1, p) + p)
    return max(temp)


graph = defaultdict(list)
psi = defaultdict(int)
while True:
    temp = input()
    if temp == 'q':
        break
    else:
        temp = temp.split()
        vi = temp[1]
        temp[4] = temp[4].split('=')
        temp[4][1] = temp[4][1].strip(';')
        fl = int(temp[4][1])
        temp = temp[9:]
        for i in range(len(temp)):
            temp[i] = temp[i].strip(',')

        vo = temp

        for i in vo:
            graph[vi].append(i)
            psi[vi] = fl

print(check('AA', 0, 0))




