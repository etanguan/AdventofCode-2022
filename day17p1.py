def create1(h):
    return [[h+4, 2], [h+4, 3], [h+4, 4], [h+4, 5]]


def create2(h):
    return [[h+5, 2], [h+4, 3], [h+6, 3], [h+5, 4]]


def create3(h):
    return [[h+4, 2], [h+4, 3], [h+4, 4], [h+5, 4], [h+6, 4]]


def create4(h):
    return [[h+4, 2], [h+5, 2], [h+6, 2], [h+7, 2]]


def create5(h):
    return [[h+4, 2], [h+5, 2], [h+4, 3], [h+5, 3]]


def wallcheck(block, dir):
    if dir == '>':
        for b in block:
            if b[1] + 1 > 6 or (b[0], b[1]+1) in blocks:
                return False
    else:
        for b in block:
            if b[1] - 1 < 0 or (b[0], b[1]-1) in blocks:
                return False
    return True

def floorcheck(block):
    for b in block:
        if (b[0]-1, b[1]) in blocks:
            return False
    return True

prevh = 0
prevx = 0
a = 1000000000000
stream = list(input())
si = 0
highest = 0
blocks = set()
shape = 0
for i in range(7):
    blocks.add((0, i))

for x in range(1729):


    if shape % 5 == 0:
        block = create1(highest)
    elif shape % 5 == 1:
        block = create2(highest)
    elif shape % 5 == 2:
        block = create3(highest)
    elif shape % 5 == 3:
        block = create4(highest)
    elif shape % 5 == 4:
        block = create5(highest)

    while True:
        if si%len(stream) == 0:
            print(highest-prevh)
            print(x - prevx)
            print(x)
            prevx = x
            prevh = highest
        cur = stream[si % len(stream)]
        if wallcheck(block, cur):
            if cur == '>':
                for i in range(len(block)):
                    block[i][1] += 1
            else:
                for i in range(len(block)):
                    block[i][1] -= 1

        if floorcheck(block):
            for i in range(len(block)):
                block[i][0] -= 1
        else:
            for b in block:
                blocks.add((b[0], b[1]))
                if b[0] > highest:
                    highest = b[0]
            shape += 1
            si += 1
            break
        si += 1

thighest = highest
tthighest = highest
x = 1729

highest += ((a-x) // 1720)*2738
x += ((a-x) // 1720) * 1720

while x < a:


    if shape % 5 == 0:
        block = create1(thighest)
    elif shape % 5 == 1:
        block = create2(thighest)
    elif shape % 5 == 2:
        block = create3(thighest)
    elif shape % 5 == 3:
        block = create4(thighest)
    elif shape % 5 == 4:
        block = create5(thighest)

    while True:

        cur = stream[si % len(stream)]
        if wallcheck(block, cur):
            if cur == '>':
                for i in range(len(block)):
                    block[i][1] += 1
            else:
                for i in range(len(block)):
                    block[i][1] -= 1

        if floorcheck(block):
            for i in range(len(block)):
                block[i][0] -= 1
        else:
            for b in block:
                blocks.add((b[0], b[1]))
                if b[0] > thighest:
                    thighest = b[0]
            shape += 1
            si += 1
            break
        si += 1
    x += 1
highest += thighest-tthighest


print(highest)



