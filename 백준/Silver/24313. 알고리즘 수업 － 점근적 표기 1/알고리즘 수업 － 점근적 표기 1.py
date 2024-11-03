a,b = map(int,input().split())
i = int(input())
k = int(input())
if (a - i < 0 and (a - i) * k + b <= 0) or (a-i == 0 and b <= 0) :
    print(1)
else:
    print(0)