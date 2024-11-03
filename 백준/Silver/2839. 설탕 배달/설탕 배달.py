n = int(input())
lst = []
for i in range(n//5 + 1):
    if (n - 5 * i) % 3 == 0:
        lst.append(((n - 5 * i) // 3) + i)
if len(lst) == 0:
    print(-1)
else:
    print(min(lst))