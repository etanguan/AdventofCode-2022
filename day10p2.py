total = 0
cycles = 0
reports = 0
sprit = [0, 1, 2]
CRT = ['.']*240
X = 1

def draw(sprit, cycles):
    tsprit = sprit.copy()
    for i in range(6):

        if cycles in tsprit:
            CRT[cycles] = '#'
        for j in range(3):
            tsprit[j] += 40

while True:
    temp = input()
    if temp == "q":
        break
    else:
        match temp.split():
            case ['q']:
                break
            case ['noop']:
                draw(sprit, cycles)
                cycles += 1

            case ['addx', x]:
                x = int(x)
                for i in range(2):
                    draw(sprit, cycles)
                    cycles += 1
                X += x
                sprit = [X-1, X, X+1]

for i in range(1, 7, 1):
    print(CRT[i*40-40:i*40])

