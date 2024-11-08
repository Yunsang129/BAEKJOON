n = int(input())
lst = []
for _ in range(n):
    n, name = input().split()
    lst.append([n, name])
lst = sorted(lst, key = lambda x : int(x[0]))
for x, y in lst:
    print(x, y)