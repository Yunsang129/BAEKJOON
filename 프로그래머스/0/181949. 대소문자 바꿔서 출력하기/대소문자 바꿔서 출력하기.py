str = input()
dae = [chr(i) for i in range(65,90)]
so = "abcdefghijklmnopqrstuvwxyz"
result = []
for s in str:
    if s in so:
        result.append(s.upper())
    else:
        result.append(s.lower())
print("".join(result))