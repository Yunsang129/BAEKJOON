from collections import deque
def dfs(start):
	if visited[start]:
		return
	visited[start] = True

	print(start, end = " ")
	for node in sorted(maps[start]):
		dfs(node)

def bfs(start):
	visited[start] = True
	q = deque()
	q.append(start)

	while q:
		node = q.popleft()
		print(node, end = " ")

		for nd in sorted(maps[node]):
			if visited[nd]:
				continue
			q.append(nd)
			visited[nd] = True

n, m, v = map(int, input().split())
maps = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]  
for _ in range(m):
	a, b = map(int, input().split())
	maps[a].append(b)
	maps[b].append(a)

dfs(v)
print()
visited = [False for _ in range(n + 1)]

bfs(v)