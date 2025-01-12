n = int(input())
cnt = 0

queens = []
row_possible = set()
dia1 = set()
dia2 = set()

def possible(row, col):
	if col in row_possible or (row - col) in dia1 or (row + col) in dia2:
		return False
	return True

def queen(num):
	global cnt
	if num == n:
		cnt += 1
		return

	for i in range(n):
		if possible(num, i):
			queens.append((num, i))
			row_possible.add(i)
			dia1.add(num - i)
			dia2.add(num + i)
			queen(num + 1)
			queens.pop()
			row_possible.remove(i)
			dia1.remove(num - i)
			dia2.remove(num + i)
queen(0)
print(cnt)