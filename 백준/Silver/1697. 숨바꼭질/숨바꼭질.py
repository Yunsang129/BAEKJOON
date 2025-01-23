from collections import deque
N, K = map(int, input().split())

q = deque()

q.append((0, N))
visited = [False] * 1000001

while q:
	time, loca = q.popleft()

	if loca == K:
		print(time)
		exit()
	
	if 0 <= loca <= 1000000 and visited[loca] == False:
		visited[loca] = True

		for i in range(3):
			if i == 0:
				q.append((time + 1, loca + 1))
			elif i == 1:
				q.append((time + 1, loca - 1))
			else:
				q.append((time + 1, 2 * loca))

