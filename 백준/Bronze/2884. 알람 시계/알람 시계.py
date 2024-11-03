a, b = map(int, input().split())
if(b - 45 < 0):
    if(a == 0):
        a = 24
    a -= 1
    b += 15
else:
    b -= 45
print(a, b)