def chan(string):
    if string in "PQRS":
        return 8
    elif string in "TUV":
        return 9
    elif string in "WXYZ":
        return 10
    else:
        return (ord(string) - 62) // 3 + 2
st = input()
sum = 0
for s in st:
    sum += chan(s)
print(sum)