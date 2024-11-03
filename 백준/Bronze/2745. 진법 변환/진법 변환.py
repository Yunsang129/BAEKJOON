st,n = map(str,input().split())
st = list(st)
num = 0
st = st[::-1]
for i in range(len(st)):
    try:
        st[i]  = int(st[i])
    except:
        st[i] = ord(st[i]) - 55
    num += st[i] * int(n) ** (i)
print(num)