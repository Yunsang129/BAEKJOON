st = input()
st = list(st)
lst = [0 for _ in range(len(st)//2)]
for i in range((len(st) // 2)):
    if st[i] == st[len(st) - i -1]:
        lst[i] = 1
if lst.count(1) == len(lst):
    print(1)
else:
    print(0)