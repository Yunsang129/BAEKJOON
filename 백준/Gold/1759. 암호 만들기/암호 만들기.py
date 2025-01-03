k, n = map(int, input().split())
lst = sorted(input().split())
result = []

def com(index, level):
	if level == k:
		if any(c in "aeiou" for c in result) and sum(c not in "aeiou" for c in result) >= 2:
			print("".join(result))
		return

	for i in range(index, len(lst)):
		result.append(lst[i])
		com(i + 1, level + 1)
		result.pop()

com(0, 0)	