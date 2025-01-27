from collections import deque
m, n = map(int, input().split())

INF = int(1e12)
box = [list(map(int, input().split())) for _ in range(n)]
time = [[INF] * m for _ in range(n)]

q = deque()
for y in range(n):
	for x in range(m):
		if box[y][x] == 1:
			q.append((x,y))
			time[y][x] = 0


while q:
	x, y = q.popleft()
	n_arr = [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]

	for ny, nx in n_arr:

		if not(0 <= ny < n and 0 <= nx < m):
			continue
		if time[ny][nx] <= time[y][x] + 1:
			continue
		if box[ny][nx] == -1:
			continue

		q.append((nx, ny))
		time[ny][nx] = time[y][x] + 1

ans = -1
for y in range(n):
	for x in range(m):
		if box[y][x] != -1:
			ans = max(ans, time[y][x])

print(ans if ans != INF else -1)