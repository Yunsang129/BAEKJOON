n, m = map(int, input().split())

def func(n):
    global arr

    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n + 1):
        if arr:
            if (i in arr or arr[-1] > i) and arr:
                continue
        arr.append(i)
        func(n)
        arr.pop()
arr = []
func(n)