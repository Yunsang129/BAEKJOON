st = input()
lst = []
sum = 0
i = 0
while i != len(st):
    if st[i] == "(":
        if(st[i + 1] == ")"):
            sum += len(lst)
            i += 1
        else:
            lst.append(st[i])
            sum += 1   
    else:
        lst.pop()
    i += 1   
print(sum)          