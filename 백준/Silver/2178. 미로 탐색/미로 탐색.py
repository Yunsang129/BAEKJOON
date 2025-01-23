import sys
input = lambda : sys.stdin.readline().strip()
from collections import deque
n, m = map(int, input().split())

maps = ['0' * (m + 1)] + ['0' + input() for _ in range(n)]

visited = [[False for _ in range(m + 1)] for _ in range(n + 1)]

dx = [-1, 0, 1, 0]
dy = [0, -1, -0, 1]

q = deque()	

q.append((1, 1, 1))
visited[1][1] = True

while q:
	distance, y, x = q.popleft()

	if x == m and y == n:
		print(distance)
		exit()	

	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]

		if 1 <= ny <= n and 1 <= nx <= m and (not visited[ny][nx]) and (maps[ny][nx] == '1'):
			q.append((distance + 1, ny, nx))
			visited[ny][nx] = True
print(-1)