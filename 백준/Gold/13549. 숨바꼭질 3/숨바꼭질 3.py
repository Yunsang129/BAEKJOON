import heapq
INF = int(1e9)
N, K = map(int,input().split())
distance = [INF] * 100001
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for location, time in [(now * 2, dist), (now + 1, dist + 1), (now - 1, dist + 1)]:
            if 0 <= location <= 100000 and distance[location] > time:
                distance[location] = time
                heapq.heappush(q,(time ,location))
                
                
dijkstra(N)
print(distance[K])
        