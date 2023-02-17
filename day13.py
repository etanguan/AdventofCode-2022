def compare(left, right):
    i = 0
    while i < len(left) and i < len(right):
        if isinstance(left[i], list):
            if isinstance(right[i], list):
                if compare(left[i], right[i]) == 2:
                    i += 1
                    continue
                return compare(left[i], right[i])
            else:
                if compare(left[i], [right[i]]) == 2:
                    i += 1
                    continue
                return compare(left[i], [right[i]])
        elif isinstance(right[i], list):

            if compare([left[i]], right[i]) == 2:
                i += 1
                continue
            return compare([left[i]], right[i])
        else:
            if left[i]>right[i]:
                return 1
            elif left[i]<right[i]:
                return 0

        i += 1
    if i < len(left) and i >= len(right):
        return 1
    elif i <len(right) and i >= len(left):
        return 0
    else:
        return 2




total = 0
i = 1
while True:
    left = input()
    if left == 'q':
        break
    else:
        left = eval(left)
        right = eval(input())
        garbage = input()
        if compare(left, right) == 0:
            total += i
        i+= 1
print(total)




