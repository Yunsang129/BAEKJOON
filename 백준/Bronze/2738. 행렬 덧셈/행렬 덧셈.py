a,b = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(a)]
li2 = [list(map(int,input().split())) for _ in range(a)]
for x in range(a):
    for y in range(b):
        print(li[x][y] + li2[x][y], end =" ")
    print("")