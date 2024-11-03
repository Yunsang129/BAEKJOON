m, n = map(int,input().split())
list = []
for j in range(m):
    list.append(0)
for i in range(n):
    a,b,c = map(int,input().split())
    for j in range(a,b+1,1):
        list[j-1] = c
for k in list:
    print(k,end = " ")