import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().strip().split()))
ind = []
am = [0 for _ in range(1000001)]
res = [-1 for _ in range(n)]

for i in range(n):
    am[lst[i]] += 1
for j in range(n):
    while ind and am[lst[ind[-1]]] < am[lst[j]]:
        res[ind.pop()] = lst[j]
    ind.append(j)
print(" ".join(map(str,res)))   