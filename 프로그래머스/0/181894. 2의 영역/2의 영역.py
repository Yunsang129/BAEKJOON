def solution(arr):
    a, b = None, None
    for i in range(0, len(arr) - 1):
        if arr[i] == 2:
            a = i
            break
    for i in range(len(arr)-1, 0, -1):
        if arr[i] == 2:
            b = i
            break
    if a is not None and b is not None:
        answer = arr[a:b+1]
    elif a is not None:
        answer = arr[a]
    elif b is not None:
        answer = arr[b]
    else:
        answer = [-1]
    return answer