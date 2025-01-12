maps = [list(map(int,input().split())) for _ in range(9)]
pos = []

row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
square = [[set() for _ in range(3)] for _ in range(3)]

for i in range(9):
	for j in range(9):
		if maps[i][j] == 0:
			pos.append((i,j))
		else:
			row[i].add(maps[i][j])
			col[j].add(maps[i][j])
			square[i//3][j//3].add(maps[i][j])

def sudo(lev):
	if lev == len(pos):
		for i in range(9):
			for j in range(9):
				print(maps[i][j], end = " ")
			print()
		exit(0)		
		return 

	y,x = pos[lev]

	for n in range(1, 10):
		if (n not in row[y]) and (n not in col[x]) and n not in square[y//3][x//3]:
			row[y].add(n)
			col[x].add(n)
			square[y//3][x//3].add(n)
			maps[y][x] = n

			sudo(lev + 1)

			maps[y][x] = 0
			square[y//3][x//3].remove(n)
			col[x].remove(n)
			row[y].remove(n)

sudo(0)