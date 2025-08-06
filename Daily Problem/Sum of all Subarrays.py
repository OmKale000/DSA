def subarraySum(arr):
    
    n = len(arr)
    result = 0

    for i in range(n):
        result += arr[i] * (i + 1) * (n - i)

    return result

arr = [1, 4, 5, 3, 2]
print(subarraySum(arr))