T = int(input())
for i in range(T):
    p = ""
    a,b = map(str,input().split())
    for s in b:
        p += s * int(a)
    print(p)