n = int(input())
cost = [[0,0,0]]
for _ in range(n):
	cost.append(list(map(int,input().split())))

dp = [[0,0,0] for _ in range(n + 1)]

for i in range(1, n + 1):
	dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])

	dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])

	dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n]))