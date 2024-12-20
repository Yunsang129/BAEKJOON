def cal(arr):
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            arr[i] /= 2
        elif arr[i] < 50 and arr[i] % 2 != 0:
            arr[i] *= 2
            arr[i] += 1
    return arr

def solution(arr):
    n = 0
    while arr != cal(arr[:]):
        arr = cal(arr[:])
        n += 1
    return n