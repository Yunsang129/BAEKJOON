def solution(arr):
    if len(arr) > len(arr[0]):
        for i in range(len(arr)):
            while len(arr[i]) != len(arr):
                arr[i].append(0)
    elif len(arr) < len(arr[0]):
        while len(arr[0]) != len(arr):
            arr.append([0] * len(arr[0]))
    return arr