a, b = map(int, input().split())
c = int(input())
if(c - 60 > 0):
    pmin = c % 60
    phour = c // 60
    a += phour
    b += pmin
else:
    b += c
if(b >= 60):
    d = b // 60
    b %= 60
    a += d
a %= 24
print(a,b)