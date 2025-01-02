def kan(n):
	global arr
	if n == 0:
		return "-"
	if arr[n] == -1:
		arr[n] = kan(n-1) + " " * 3 ** (n-1) + kan(n-1)
	return arr[n]


arr = [-1] * 13
while True:
	try:
		print(kan(int(input())))
	except:
		break