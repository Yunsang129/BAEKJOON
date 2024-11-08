import sys
input = sys.stdin.readline
result = []
n = int(input())
lst = list(map(int,input().split()))
set_list = list(set(lst))
set_list.sort()
dic = {}
for i in range(len(set_list)):
    dic[set_list[i]] = i 
for j in range(n):
    result.append(dic[lst[j]])
print(" ".join(map(str,result)))