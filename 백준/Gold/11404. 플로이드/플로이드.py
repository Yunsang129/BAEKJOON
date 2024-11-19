import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)] # 이차원 리스트를 만들어야함. 그니까 노드의 개수만큼의 INF n*n의 배열을 만든다고 생각하면 됨
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c) 

def floyd_washall():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0
    
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[k][b] + graph[a][k])

floyd_washall()

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            graph[a][b] = 0
        print(graph[a][b], end=" ")
    print()
