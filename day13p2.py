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




A = []
while True:
    left = input()
    if left == 'q':
        break
    else:
        left = eval(left)
        right = eval(input())
        garbage = input()
        A.append(left)
        A.append(right)

A.append([[2]])
A.append([[6]])

for i in range(len(A)):
    for j in range(len(A)-1-i):
        if compare(A[j], A[j+1]) != 0:
            A[j], A[j + 1] = A[j+1], A[j]


print((A.index([[2]])+1)*(A.index([[6]])+1))


