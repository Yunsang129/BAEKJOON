n, k = map(int,input().split())

lst = []

for i in range(n):

    if n % (i+1) == 0:

        lst.append(i+1)

if len(lst) < k:

    print(0)

else:

    print(lst[k-1])    