import re
A = []
cargo = ['JHPMSFNV', 'SRLMJDQ', 'NQDHCSWB', 'RSCL', 'MVTPFB', 'TRQNC', 'GVR', 'CZSPDLR', "DSJVGPBF"]

cargo = [list(i) for i in cargo]

while True:
    temp = input().split()
    if temp != []:

        A.append([int(temp[1]), int(temp[3])-1, int(temp[5])-1])
    else:
        break


for move in A:
    temp = len(cargo[move[2]])
    for i in range(move[0]):
        cargo[move[2]].insert(temp,cargo[move[1]].pop())

print(cargo)
for i in cargo:
    print(i[len(i)-1], end='')
