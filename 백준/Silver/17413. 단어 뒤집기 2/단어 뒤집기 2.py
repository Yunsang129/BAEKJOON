S = list(input())
lst = []

rev = []
i = 0
p = False
for ch in S:
    if ch == "<":
        lst.append("".join(rev))
        rev.clear()
        p = True
    if p == True:
        rev.append(ch)
    
    elif p == False:
        rev.append(ch)
    if ch == ">":
        lst.append("".join(rev))
        rev.clear()
        p = False
        
    if ch == " " and p == False: 
        lst.append("".join(rev))
        rev.clear()
lst.append("".join(rev))

lst = list(filter(None,lst))
        
for j in range(len(lst)):
    if lst[j][0] != "<":
        if lst[j][-1] ==  " ":
            lst[j] = lst[j][0:-1]
            lst[j] = lst[j][::-1]
            lst[j] +=  " "
        else:
            lst[j] = lst[j][::-1]

print("".join(lst)) 