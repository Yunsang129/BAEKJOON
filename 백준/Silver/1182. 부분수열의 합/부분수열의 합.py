from itertools import combinations

N, S = map(int,input().split())
lst = list(map(str,input().split()))
result = 0

for i in range(1, N + 1):
	for nums in combinations(lst, i):
		if sum(map(int,nums)) == S:
			result += 1


print(result)