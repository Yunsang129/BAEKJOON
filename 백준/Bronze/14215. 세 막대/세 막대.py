a,b,c = map(int,input().split())
lst = [a,b,c]
lst.sort()
if lst[0] + lst[1] <= lst[2]:
    lst[2] = lst[0] + lst[1] -1
print(sum(lst))