total = 0
cycles = 20
reports = 0
X = 1
while True:
    temp = input()
    if temp == "q":
        break
    else:
        match temp.split():
            case ['q']:
                break
            case ['noop']:
                cycles += 1
                if cycles // 40 > reports:
                    total += (cycles-20)*X
                    reports +=1
            case ['addx', x]:
                x = int(x)
                if (cycles + 1) // 40 > reports:
                    total += (cycles + 1 - 20) * X
                    reports +=1
                elif (cycles + 2) // 40 > reports:
                    total += (cycles + 2 - 20) * X
                    reports += 1
                X += x
                cycles += 2
print(total)
