n = int(input())

count = n

for i in range(n):

    lst = []

    ch = input().strip()

    bef = None

    for c in ch:

        if bef != c:

            bef = c

            if c in lst:

                count -= 1

                break

            else:

                lst.append(c)

print(count)