def solution(arr, queries):
    result = []
    for a,b,c in queries:
        min = 1000000
        for i in range(a, b + 1):
            if (c < arr[i] and arr[i] < min):
                min = arr[i]
        if min == 1000000:
            min = -1
        result.append(min)
    return result