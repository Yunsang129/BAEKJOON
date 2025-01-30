import heapq
import sys

input = lambda : sys.stdin.readline().strip()
INF = int(1e12)

def dijkstra(start, end):
	q = []
	dist = [INF] * (N + 1)
	heapq.heappush(q, (0, start))
	dist[start] = 0

	while q:
		cur_dist, cur_node = heapq.heappop(q)
		for adj_node, adj_dist in adj_list[cur_node]:
			if cur_dist + adj_dist < dist[adj_node]:
				dist[adj_node] = cur_dist + adj_dist
				heapq.heappush(q, (cur_dist + adj_dist, adj_node))
	return dist[end]

N, M, X = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
	start, end, dist = map(int, input().split())
	adj_list[start].append((end, dist))

result = 0

for i in range(1, N + 1):
	result = max(result, dijkstra(i, X) + dijkstra(X, i))
print(result) 