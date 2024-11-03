import sys
str = list(sys.stdin.readline().strip())
n = int(input())
ar = []
for i in range(n):
    p = sys.stdin.readline().strip()
    if p == "L":
        if len(str) != 0:
            ar.append(str.pop())
    elif p == 'D':
        if len(ar) != 0:
            str.append(ar.pop())
    elif p == 'B':
        if len(str) != 0:
            str.pop()
                
    elif p[0] == "P":
        str.append(p[2])
        
print("".join(str + ar[::-1]))