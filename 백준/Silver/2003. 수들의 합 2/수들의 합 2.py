n, m = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0
cur_sum = 0
right = -1

for left in range(n):
	while right + 1 < n and cur_sum < m:
		right += 1
		cur_sum += arr[right]
	if cur_sum == m:
		cnt += 1
	cur_sum -= arr[left]

print(cnt)