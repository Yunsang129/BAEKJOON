num = int(input())
for i in range(1, num+1):
    k = j = i
    arr = []
    while j != 0:
        arr.append(j % 10)
        j //= 10
    for num1 in arr:
        k += num1
    if(num == k):
        print(i)
        break
    if(i == num):
        print(0)