n = int(input())
lst = list(map(int, input().split()))
result = []

for n in range(len(lst)):
    if not result:
        result.append(lst[n])
        continue
    result.append(max(result[-1] + lst[n], lst[n]))
print(max(result))    