def solution(n):
    result = 0
    n = str(n)
    for i in range(len(n)):
        result += int(n[i])
    return result
        