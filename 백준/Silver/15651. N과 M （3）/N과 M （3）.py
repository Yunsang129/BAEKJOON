n, m = map(int, input().split())

def func(n):
    global arr

    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n + 1):
        arr.append(i)
        func(n)
        arr.pop()
arr = []
func(n)