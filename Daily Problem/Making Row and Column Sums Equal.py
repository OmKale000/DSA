def balanceSum(mat):
    n = len(mat)
    res = 0
    maxSum = 0
    
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += mat[i][j]
        maxSum = max(sum, maxSum)
    
    for j in range(n):
        sum = 0
        for i in range(n):
            sum += mat[i][j]
        maxSum = max(sum, maxSum)
    
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += mat[i][j]
        res += (maxSum - sum)
    
    return res


mat = [
    [1, 2, 3], 
    [4, 2, 3], 
    [3, 2, 1]
]
print(balanceSum(mat))