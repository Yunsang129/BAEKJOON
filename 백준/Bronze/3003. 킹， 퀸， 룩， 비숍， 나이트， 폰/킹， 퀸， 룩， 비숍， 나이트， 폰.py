lst = [1,1,2,2,2,8]
rlst = list(map(int,input().split()))
for i in range(len(rlst)):
    print(lst[i] - rlst[i], end = " ")