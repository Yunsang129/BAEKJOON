def func(n):
	global dp
	if n == 1 or n == 2:
		return n
	if dp[n] != -1:
		return dp[n]
	else:
		dp[n] = (func(n-1) + func(n-2)) % 10007
	return dp[n]


n = int(input())
dp = [-1 for _ in range(n + 1)]
print(func(n))