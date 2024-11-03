n, m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(i+1)
for j in range(m):
    a,b = map(int,input().split())
    c = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = c
for k in range(n):
    print(arr[k], end = " ")