st = input()
count = 0
croatia_lt = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
while(True):
    if len(st) == 0:
        break
    if st[0:3] in croatia_lt:
        count += 1
        st = st[3:]
    elif st[0:2] in croatia_lt:
        count += 1
        st = st[2:]
    else:
        count += 1
        st = st[1:]
print(count)