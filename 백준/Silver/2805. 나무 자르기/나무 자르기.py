n, m = map(int, input().split())

lst = list(map(int, input().split()))

cur = -1
step = max(lst)

def is_possible(k):
	num = 0
	for h in lst:
		if h > k:
			num += (h - k)
	return (num >= m)


while step != 0:
	while ((cur + step)	<= max(lst)) and is_possible(cur + step):
		cur += step
	step //= 2

print(cur)