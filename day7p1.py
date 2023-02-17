from collections import defaultdict
from helperFile import *


D = defaultdict(list)
A = []
while True:
    temp = input().split()

    if temp != ['q']:
        for i in range(len(temp)):
            temp[i] = temp[i]
        A.append(temp)
    else:
        break
curh = []
cur = ''
i = 0
lsed = set()
while i < len(A)-1:

    if A[i][0] == '$':

        if A[i][1] == 'cd':

            if A[i][2] == '..':
                cur = curh.pop()
            elif A[i][2] == '/':
                cur = '/'
                curh.clear()
                curh.append(cur)
            else:
                cur = A[i][2]
                curh.append(cur)
            i += 1

        elif A[i][1] == 'ls' and cur not in lsed:
            i += 1
            while A[i][0] != '$':

                if A[i][0] == 'dir':

                    D[cur].append(A[i][1])

                else:

                    D[cur].append(int(A[i][0]))

                if i + 1 > len(A)-1:
                    i+= 1
                    break
                i += 1
            lsed.add(cur)
        else:
            i+= 1
            while A[i][0] != '$':
                if i + 1 > len(A)-1:
                    i+= 1
                    break
                i += 1
print(D)

def dfs(cur):
    if dp[cur]:
        return dp[cur]
    total = 0

    for i in D[cur]:
        if str(i).isnumeric():
            total += i
        else:
            if dp[i]:
                total += dp[i]
            else:
                total += dfs(i)
    dp[cur] = total
    return dp[cur]



def check(lst):
    count = 0
    for i in lst:
        if isinstance(i, str):
            count += 1
    return count



dp = defaultdict(int)
totals = 0
a = list(D.keys())
for i in a:
    for j in D[i]:
        if i in D[j]:
            print(i, j)

a = sorted(a, key=lambda x: check(D[x]))

for i in a:
    visited = set()
    total = 0
    dfs = [i]
    while len(dfs) > 0:

        for j in D[dfs[0]]:

            if isinstance(j, int):
                total += j
            else:
                if j not in visited:
                    dfs.append(j)
                    visited.add(j)
        dfs.pop(0)


    print(total)
    if total <= 100000:
        totals += total


print(totals)