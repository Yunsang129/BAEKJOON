def solution(n):
    i = 1
    while True:
        if i ** 2 == n:
            return 1
        elif i > n:
            return 2
        else:
            i += 1
            
    return answer