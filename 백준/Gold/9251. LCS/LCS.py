A = [0] + list(map(str,input()))
B = [0] + list(map(str,input()))

dp = [[0] * (len(B)) for _ in range(len(A))]

for n in range(1, len(A)):
	for m in range(1, len(B)):
		if A[n] == B[m]:
			dp[n][m] = dp[n-1][m-1] + 1
		else:
			dp[n][m] = max(dp[n-1][m], dp[n][m-1])

print(dp[len(A) - 1 ][len(B) - 1])
