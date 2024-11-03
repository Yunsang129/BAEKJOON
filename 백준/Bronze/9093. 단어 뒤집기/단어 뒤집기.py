import sys
n = int(input())
for i in range(n):
    st = sys.stdin.readline().split()
    new = ""
    for j in range(len(st)):
        new += st[j][::-1] 
        if j != len(st)-1:
            new += " "
    print(new)