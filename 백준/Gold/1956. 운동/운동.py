import sys
sys = sys.stdin.readline
INF = int(1e9) 
V, E = map(int, input().split())
graph = [[INF]* (V + 1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a][b] = c
    
for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
result = INF     
for i in range(1, V + 1):
    result = min(result, graph[i][i])
if result == INF:
    print(-1)
else:
    print(result)