import sys
input = lambda: sys.stdin.readline().rstrip()

def get_idx(arr, num):
	cur = -1
	step = len(arr)

	while step != 0:
		while cur + step < len(arr) and arr[cur + step] <= num:
			cur += step
		step //= 2

	return cur

n, m = map(int, input().split())

tops = []
bots = []

for i in range(n):
	num = int(input())

	if i % 2 == 0:
		bots.append(num)
	else:
		tops.append(m - num + 1)

tops = sorted(tops)
bots = sorted(bots)
	
mn = int(1e12)
mn_num = 0


for h in range(1, m + 1):
	cnt_bot = (n // 2) - (get_idx(bots, h - 1) + 1)
	cnt_top = get_idx(tops, h) + 1

	if mn == cnt_bot + cnt_top:
		mn_num += 1
	if mn > cnt_bot + cnt_top:
		mn_num = 1
		mn = cnt_bot + cnt_top

print(mn, mn_num)