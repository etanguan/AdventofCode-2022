s = input()
s = list(s)
i = 0
j = 13

while j < len(s):
    if len(set(s[i:j+1])) == 14:
        print(j+1)
        break
    i+= 1
    j+= 1