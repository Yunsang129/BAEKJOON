n, s = map(int, input().split())

arr = list(map(int, input().split()))

ans = int(1e9)

right = -1
cur_sum = 0

for left in range(n):
	while (right + 1 < n) and (cur_sum < s):
		right += 1
		cur_sum += arr[right]

	if cur_sum >= s:
		leng = (right - left + 1)
		ans = min(leng, ans)

	cur_sum -= arr[left]

print(0 if ans == int(1e9) else ans)