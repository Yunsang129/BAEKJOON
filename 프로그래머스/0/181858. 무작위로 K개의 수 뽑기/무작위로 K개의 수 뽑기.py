def solution(arr, k):
    result = []
    for e in arr:
        if e not in result:
            result.append(e)
    while (len(result) < k):
        result.append(-1)
    while len(result) > k:
        result.pop()
    return result       