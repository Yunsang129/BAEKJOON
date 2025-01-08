n = int(input())
num_lst = [0] + list(map(int,input().split()))

dp = [-1 for _ in range(n+1)]

dp[1] = 1

for i in range(2, len(num_lst)):
	best = 0
	for j in range(1,i):
		if num_lst[i] > num_lst[j]:
			best = max(best, dp[j])
	dp[i] = best + 1

print(max(dp[1:]))

""" top down

def func(n):
	global num_lst, dp

	if dp[n] != -1:
		return dp[n]

	best = 0
	for i in range(1, n):
		if arr[n] > arr[i]:
			best = max(best, func[i])

	dp[n] = best + 1
	return dp[n]
"""