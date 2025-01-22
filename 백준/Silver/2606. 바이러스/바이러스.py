n = int(input())
m = int(input())

cnt = 0

def dfs(start):
	global cnt

	if visited[start]:
		return
	cnt += 1
	visited[start] = True

	for node in maps[start]:
		dfs(node)

maps = [[] for _ in range(n + 1)]
for _ in range(m):
	a, b = map(int, input().split())
	maps[a].append(b)
	maps[b].append(a)
visited = [False for _ in range(n + 1)]

dfs(1)

print(cnt - 1)