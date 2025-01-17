n, m = map(int, input().split())

lst = list(map(int ,input().split()))

def is_possible(arr_num):
	cur_min = lst[0]
	cur_max = lst[0]
	cnt = 1

	for i in range(n):
		cur_min = min(cur_min, lst[i])
		cur_max = max(cur_max, lst[i])

		if (cur_max - cur_min) > arr_num:
			cnt += 1
			cur_min = cur_max = lst[i]

	return (m >= cnt)

cur = -1
step = 10001

while step != 0:
	while (((cur + step) <=  10000) and not is_possible(cur + step)):
		cur += step
	step //= 2

print(cur + 1)