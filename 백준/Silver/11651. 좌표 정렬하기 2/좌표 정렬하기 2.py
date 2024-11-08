n = int(input())
lst = []
for _ in range(n):
    x,y = map(int,input().split())
    lst.append([y,x])
lst.sort()
for dy, dx in lst:
    print(dx, dy)