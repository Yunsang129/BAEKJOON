import sys
sys.setrecursionlimit(int(1e6))
def func(k,n):
	global W, V, dp

	if n == 0 or k == 0:
		return 0

	if dp[k][n] != -1:
		return dp[k][n]

	dp[k][n] = func(k, n - 1)
	if k >= W[n]:
		dp[k][n] = max(dp[k][n], func(k - W[n], n - 1) + V[n])
	return dp[k][n]

N, K = map(int, input().split())

W = [0]
V = [0]

for _ in range(N):
	w, v = map(int, input().split())
	W.append(w)
	V.append(v)

dp = [[-1 for _ in range(N + 1)] for _ in range(K + 1)]
print(func(K, N))


"""
bottom up
N, K = map(int, input().split())
W = [0]
V = [0]

for _ in range(N):
	w, v = map(int, input().split())
	W.append(w)
	V.append(v)

dp = [[0] * (N + 1) for _ in range(K + 1)]

for i in range(1, K + 1):
	for j in range(1	, N + 1):
		dp[i][j] = dp[i][j-1]
		if W[j] <= i:
			dp[i][j] = max(dp[i][j], dp[i - W[j]][j - 1] + V[j])
print(dp[K][N])
"""