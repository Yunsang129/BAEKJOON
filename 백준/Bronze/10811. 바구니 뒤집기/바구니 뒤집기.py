def palin(arr,i,j):
    for k in range((j - i + 1) // 2):
        c = arr[j - k]
        arr[j - k] = arr[i + k]
        arr[i + k] = c
    return arr

a,b = map(int,input().split())
arr = list(range(1, a + 1))
for i in range(b):
    x, y = map(int,input().split())
    arr = palin(arr, x - 1, y - 1)
for k in range(len(arr)):
    print(arr[k], end = " ")