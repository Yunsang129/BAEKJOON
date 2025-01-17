import sys
input = lambda : sys.stdin.readline().strip()

n, c = map(int, input().split())
home = sorted([int(input()) for _ in range(n)])

def is_possible(k):
	bef_idx = 0
	cnt = 1
	for idx in range(1, n):
		if home[idx] - home[bef_idx] >= k:
			bef_idx = idx
			cnt += 1
	return (cnt >= c)

cur = -1
step = int(1e9) + 1

while step != 0:
	while (((cur + step) <= int(1e9)) and is_possible(step + cur)):
		cur += step
	step //= 2
print(cur) 	