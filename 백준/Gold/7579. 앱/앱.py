n, m = map(int, input().split())

memory = [0] + list(map(int,input().split()))
cost = [0] + list(map(int,input().split()))

dp = [[0 for _ in range(n + 1)]for _ in range(sum(cost) + 1)]


ans = 100000001

for i in range(0, sum(cost) + 1):
	for j in range(1, n + 1):
		dp[i][j] = dp[i][j - 1]
		if cost[j] <= i:
			dp[i][j] = max(dp[i][j], dp[i - cost[j]][j - 1] + memory[j])
		if dp[i][j] >= m:
			ans = min(ans, i)

print(ans) if ans != 100000001 else print(sum(cost))