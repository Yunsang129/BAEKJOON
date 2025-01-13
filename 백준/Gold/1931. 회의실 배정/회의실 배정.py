n = int(input())
lst = []

for _ in range(n):
	lst.append(tuple(map(int, input().split())))

lst = sorted(lst, key = lambda x: (x[1],  x[0]))
result = []

for x, y in lst:
	if not result:
		result.append((x,y))
		continue
	if x >= result[-1][1]:
		result.append((x,y))

print(len(result))