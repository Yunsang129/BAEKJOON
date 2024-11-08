n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
lst = list(set(lst))
lst.sort()
lst = sorted(lst, key = lambda x: len(x))
for w in lst:
    print(w)
