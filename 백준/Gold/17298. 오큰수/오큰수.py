n = int(input())
lst = list(map(int,input().split()))
result = [0 for _ in range(n)]
ind = []
for i in range(n):
    while ind and lst[ind[-1]] < lst[i]:
        result[ind.pop()] = lst[i]
    ind.append(i)
        
for j in range(len(ind)):
    result[ind[j]] = -1
    
print(" ".join(map(str,result)))