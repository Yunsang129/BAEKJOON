def com(arr, index, level):
	if level == 6:
		result.sort()
		print(" ".join(map(str, result)))
		return

	for i in range(index, len(arr)):
		result.append(arr[i])
		com(arr, i + 1, level + 1)
		result.pop()

while True:
	arr = list(map(int, input().split()))
	result = []
	if arr == [0]:
		break
	com(arr[1:], 0, 0)
	print()