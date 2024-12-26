def solution(arr):
    i = 0
    while True:
        if len(arr) <= 2 ** i:
            for _ in range(2**i - len(arr)):
                arr.append(0)
            break
        i += 1
    return arr