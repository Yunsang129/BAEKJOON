n, m = map(int,input().split())
lst = []
i = 1
while True:
    if(n == 0):
        break
    lst.append((n % (m ** i)) / m**(i-1))
    n -= n % m**i
    i += 1
lst = lst[::-1]
ch = ""
for j in range(len(lst)):
    lst[j] = int(lst[j])
    if(lst[j] >= 10):
        lst[j] = chr(lst[j] + 55)
    lst[j] = str(lst[j])
    ch += lst[j]
print(ch)