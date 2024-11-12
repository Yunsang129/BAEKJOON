import sys
input = sys.stdin.readline
INF = int(1e9)
def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            first_node = edges[j][0]
            second_node = edges[j][1]
            cost = edges[j][2]
            
            if dist[first_node] != INF and dist[first_node] + cost < dist[second_node]:
                dist[second_node] = dist[first_node] + cost
                if i == n-1:
                    return True
    return False
                
n, m = map(int, input().strip().split())
edges = []
dist = [INF] * (n + 1)
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a, b, c))

ford = bellman_ford(1)

if ford:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] >= INF:
            print(-1)
        else:
            print(dist[i])