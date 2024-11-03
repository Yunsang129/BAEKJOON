arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
    
for j in range(10,0,-1):
    for k in range(len(arr)):
        if(j == k):
            continue
        try:
            if(arr[j] == arr[k]):
                arr.pop(k)
        except IndexError:
            continue
print(len(arr))