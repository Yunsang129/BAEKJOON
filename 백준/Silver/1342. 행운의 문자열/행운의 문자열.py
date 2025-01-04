def bt(level):
	global choose, ans

	if level == len(lst):
		ans += 1
		return

	for c in chars:
		if cnt[c] == 0:
			continue

		if (not choose) or (choose[-1] != c):
			cnt[c] -=1
			choose.append(c)
			bt(level + 1)
			cnt[c] += 1
			choose.pop()

lst = sorted(input())
cnt = dict()
ans = 0
chars = set()
choose = []

for ch in lst:
	chars.add(ch)
	if ch not in cnt:
		cnt[ch] = 0
	cnt[ch] += 1

bt(0)
print(ans)