def solution(strArr):
    result = [0 for _ in range(31)]
    for st in strArr:
        result[len(st)] += 1
    return max(result)