import sys
import heapq
input = sys.stdin.readline

N, E = map(int,input().split())

graph = [[] for i in range(N + 1)]

INF = int(1e9)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a, c))
    
num1,num2 = map(int,input().split())

def dijkstra(start):
    q = []
    distance = [INF] * (N+1)
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance
        
first_distance = dijkstra(1)
second_distance = dijkstra(num1)
third_distance = dijkstra(num2)

sum_1 = first_distance[num1] + second_distance[num2] + third_distance[N]
sum_2 = first_distance[num2] + third_distance[num1] +  second_distance[N]
sum = min(sum_1, sum_2)

if sum >= INF:
    print(-1)
else:
    print(sum)