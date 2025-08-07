def getLastMoment(n, left, right):
    res = 0


    for i in range(len(left)):
        res = max(res, left[i])

    for i in range(len(right)):
        res = max(res, n - right[i])

    return res

n = 4
left = [2]
right = [0, 1, 3]
print(getLastMoment(n, left, right))