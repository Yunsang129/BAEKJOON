n, m = 	map(int,input().split())
result_plus = []
result_minus = []
result = 0
lst = list(map(int,input().split()))
for N in lst:
	if N < 0 :
		result_minus.append(N)
	else:
		result_plus.append(N)
		
result_plus = sorted(result_plus, key = lambda x: abs(x), reverse = True)
result_minus = sorted(result_minus, key = lambda x: abs(x), reverse = True)
for i in range(0, len(result_plus), m):
	result += abs(result_plus[i])

for i in range(0, len(result_minus), m):
	result += abs(result_minus[i])

result *= 2
lst = sorted(lst, key = lambda x: abs(x))
result -= abs(lst[-1])
print(result)