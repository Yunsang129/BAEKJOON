st = input()
st = st.upper()
li = [0 for _ in range(26)]

for s in st:
    li[ord(s) - 65] += 1 
max = 0
for j in li:
    if(max < j):
        max = j
max_in = li.index(max)
for k in range(max):
    try:
        while(True):
            li.remove(k)
    except ValueError:
        continue
if len(li) != 1:
    print("?")
else:
    print(chr(max_in+65))