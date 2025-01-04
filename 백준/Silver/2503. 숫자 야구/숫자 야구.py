from itertools import permutations

n = int(input())
infos = [input().split() for _ in range(n)]
ans = 0

for cur in permutations(range(1,10), 3):
	ok = True

	for num, st, bl in infos:
		real_st = real_bl = 0

		for i in range(3):
			if str(cur[i]) == num[i]:
				real_st += 1
			elif str(cur[i]) in num:
				real_bl += 1

		if real_st != int(st) or real_bl != int(bl):
			ok = False
			break
	ans += ok
print(ans)