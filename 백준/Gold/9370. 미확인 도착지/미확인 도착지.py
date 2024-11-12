import heapq
import sys
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(start, 0))
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
                
        
T = int(input())
for _ in range(T):
    result = []
    print_list = []
    input = sys.stdin.readline
    n, m, t = map(int,input().split())
    start, g, h = map(int, input().split())
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n+1)

    
    for _ in range(m):
        a,b,d = map(int,input().split())
        if (a == g and b == h) or (a == h and b == g):
            bridge = d
        graph[a].append((b,d))
        graph[b].append((a,d))
    dijkstra(start)
    for _ in range(t):
        k = int(input())
        result.append([k,distance[k]])
        
    if distance[g] > distance[h]:
        first = distance[h]
        distance = [INF] * (n+1)
        dijkstra(g)
    else:
        first = distance[g]
        distance = [INF] * (n+1)
        dijkstra(h)
    for i, j in result:
        second = distance[i] 
        result_distance = first + second + bridge
        if (result_distance >= INF) or (result_distance > j) :
            continue
        print_list.append(i)
        print_list.sort()
    print(" ".join(map(str, print_list)))