coin = [500, 100, 50, 10, 5, 1]

n = 1000 - int(input())
cnt = 0

for i in range(len(coin)):
	cnt += n // coin[i]
	n = n % coin[i]
print(cnt)
