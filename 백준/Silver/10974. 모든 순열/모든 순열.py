n = int(input())
lst = [n for n in range(1, n + 1)]
visited = [False] * (n + 1)
result = []
def per(level):
	if level == len(lst):
		print(" ".join(map(str,result)))
		return

	for i in range(len(lst)):
		if visited[i] == True:
			continue
		visited[i] = True
		result.append(lst[i])
		per(level + 1)
		visited[i] = False
		result.pop()

per(0)