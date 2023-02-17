sensors = []
n = set()
total = 0
while True:
    temp = input()
    if temp == 'q':
        break
    else:
        temp = temp.split()
        sx = list(temp[3])
        sx = int("".join(sx[2:len(sx)-1]))
        sy = list(temp[2])
        sy = int("".join(sy[2:len(sy)-1]))
        bx = list(temp[9])
        bx = int("".join(bx[2:]))
        by = list(temp[8])
        by = int("".join(by[2:len(by) - 1]))

        dist = abs(sx-bx) + abs(sy - by)
        sensors.append((sx, sy, dist))


for xcord in range(4_000_000):
    window = []

    for s in sensors:

        if s[0] - s[2] <= xcord <= s[0] + s[2]:
            window.append([s[1] - s[2] + abs(xcord - s[0]), s[1] + s[2] - abs(xcord - s[0])])
    window.sort(key=lambda x: x[0])
    for i in range(len(window)-1):

        if window[i][0] <= window[i+1][0] and window[i][1] >= window[i+1][1]:
            window[i+1] = window[i]
        elif window[i][1] >= window[i+1][0]-1:
            window[i+1][0] = window[i][0]

    if window[-1][0] > 0 or window[-1][1] < 4_000_000:
        print(xcord, window[-1])
        print(window)
        print((window[-1][0]-1)*4_000_000+xcord)

