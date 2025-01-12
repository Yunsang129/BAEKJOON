n = int(input())
lst = [0] + list(map(int, input().split()))

dp = [-1 for _ in range(n + 1)]
dp2 = [-1 for _ in range(n + 1)]

def trans(arr):
	global lst
	arr[1] = 1
	for i in range(2, len(lst)):
		max_value = 0
		for j in range(1, i):
			if lst[j] < lst[i]:
				max_value = max(max_value, arr[j])
		arr[i] = max_value + 1
	return arr[1:]

dp = trans(dp)
lst = lst[::-1]
lst = [0] + lst[:-1]
dp2 = trans(dp2)[::-1]

result = 0
for i in range(n):
	if (dp[i] + dp2[i]) > result:
		result = dp[i] + dp2[i] -1 

print(result)