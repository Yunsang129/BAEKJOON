n = int(input())
lst = [25,10,5,1]
for i in range(n):
    num = int(input())
    for k in lst:
        print(num // k, end = " ")
        num %= k