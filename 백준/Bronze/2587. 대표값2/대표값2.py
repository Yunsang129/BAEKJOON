lst = []
for _ in range(5):
    n = int(input())
    lst.append(n)
lst.sort()
print(sum(lst) // len(lst))
print(lst[2])