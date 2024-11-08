n = int(input())
lst = []
for _ in range(n):
    num = int(input())
    lst.append(num)
lst.sort()
lst.reverse()
for _ in range(n):
    print(lst.pop())