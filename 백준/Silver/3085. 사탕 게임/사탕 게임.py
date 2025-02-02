import sys
input = lambda : sys.stdin.readline().rstrip()

def get_candy(y, x):
	global n
	best = 0
	# row
	bef = '-'
	value = 0
	for i in range(n):
		if bef == board[y][i]:
			value += 1
		else:
			value = 1

		bef = board[y][i]
		best = max(value, best)

	#column
	bef = '-'
	value = 0
	for j in range(n):
		if bef == board[j][x]:
			value += 1
		else:
			value = 1
		bef = board[j][x]
		best = max(value, best)


	return best

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

n = int(input())
board = [list(input()) for _ in range(n)]
ans = 0

for y in range(n):
	for x in range(n):
		if x == y:
			ans = max(ans, get_candy(y,x))
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]
			if 0 <= ny < n and 0 <= nx < n and board[y][x] != board[ny][nx]:
				board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
				ans = max(ans, get_candy(y,x))
				board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
print(ans)