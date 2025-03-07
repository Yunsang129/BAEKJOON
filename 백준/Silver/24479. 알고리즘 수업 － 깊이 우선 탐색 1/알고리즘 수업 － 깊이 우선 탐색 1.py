import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, start, visited):
    global count
    visited[start] = count
    for i in graph[start]:
        if visited[i] == 0:
            count += 1
            dfs(graph, i, visited)
            
n, m, r = map(int,input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n + 1):
    graph[i].sort() 
visited = [0] * (n+1)
count = 1
dfs(graph, r, visited) 

for i in range(1, n + 1):
    print(visited[i])