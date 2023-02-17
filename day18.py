import sys
sys.setrecursionlimit(10000)
def floodfill(x, y, z):
    global total
    if x + 1 <= 22:
        if (x+1, y, z) not in visited:
            if (x+0.5, y, z) in sides:
                total += 1
            else:
                visited.add((x+1, y, z))
                floodfill(x+1, y, z)

    if x - 1 >= -1:
        if (x-1, y, z) not in visited:
            if (x-0.5, y, z) in sides:
                total += 1
            else:
                visited.add((x-1, y, z))
                floodfill(x-1, y, z)

    if y + 1 <= 22:
        if (x, y+1, z) not in visited:
            if (x, y+0.5, z) in sides:
                total += 1
            else:
                visited.add((x, y+1, z))
                floodfill(x, y+1, z)

    if y - 1 >= -1:
        if (x, y-1, z) not in visited:
            if (x, y-0.5, z) in sides:
                total += 1
            else:
                visited.add((x, y-1, z))
                floodfill(x, y-1, z)

    if z + 1 <= 22:
        if (x, y, z+1) not in visited:
            if (x, y, z+0.5) in sides:
                total += 1
            else:
                visited.add((x, y, z+1))
                floodfill(x, y, z+1)

    if z - 1 >= -1:

        if (x, y, z-1) not in visited:
            if (x, y, z-0.5) in sides:
                total += 1
            else:
                visited.add((x, y, z-1))
                floodfill(x, y, z-1)


total = 0
visited = {(22, 22, 22)}
cubes = []
sides = set()

while True:
    temp = input()
    if temp == 'q':
        break
    temp = eval(temp)
    cubes.append(temp)

for cube in cubes:
    if (cube[0]+0.5, cube[1], cube[2]) in sides:
        sides.remove((cube[0]+0.5, cube[1], cube[2]))
    else:
        sides.add((cube[0]+0.5, cube[1], cube[2]))
    if (cube[0] - 0.5, cube[1], cube[2]) in sides:
        sides.remove((cube[0] - 0.5, cube[1], cube[2]))
    else:
        sides.add((cube[0] - 0.5, cube[1], cube[2]))

    if (cube[0], cube[1]+0.5, cube[2]) in sides:
        sides.remove((cube[0], cube[1]+0.5, cube[2]))
    else:
        sides.add((cube[0], cube[1]+0.5, cube[2]))

    if (cube[0], cube[1]-0.5, cube[2]) in sides:
        sides.remove((cube[0], cube[1]-0.5, cube[2]))
    else:
        sides.add((cube[0], cube[1]-0.5, cube[2]))

    if (cube[0], cube[1], cube[2]+0.5) in sides:
        sides.remove((cube[0], cube[1], cube[2]+0.5))
    else:
        sides.add((cube[0], cube[1], cube[2] + 0.5))

    if (cube[0], cube[1], cube[2]-0.5) in sides:
        sides.remove((cube[0], cube[1], cube[2]-0.5))
    else:
        sides.add((cube[0], cube[1], cube[2] - 0.5))

#floodfill(22, 22, 22)
print(len(sides))
print(total)