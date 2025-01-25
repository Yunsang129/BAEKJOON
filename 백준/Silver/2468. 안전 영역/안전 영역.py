from collections import deque
n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]

result = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def safe_area(h):
	q = deque()
	visited = [[False] * n  for _ in range(n)]
	cnt = 0
	for i in range(n):
		for j in range(n):
			if visited[i][j] == False and maps[i][j] > h:
				visited[i][j] = True
				q.append((i, j))

				while q:
					y, x = q.popleft()
					for d in range(4):
						nx = x + dx[d]
						ny = y + dy[d]
						if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == False and maps[ny][nx] > h:
							visited[ny][nx] = True
							q.append((ny, nx))
				cnt += 1
	return cnt

max_height = max(max(row) for row in maps)
for k in range(max_height + 1):
    result = max(result, safe_area(k))

print(result)