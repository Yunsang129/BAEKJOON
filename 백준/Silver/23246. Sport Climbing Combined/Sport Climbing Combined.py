def cal(arr):
	return arr[1] * arr[2] * arr[3], arr[1] + arr[2] + arr[3], arr[0] 
n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
lst = sorted(lst, key = cal)
for i in range(3):
	print(lst[i][0], end = " ")
