dic ={"A+":4.5, "A0": 4.0,"B+": 3.5, "B0":3.0, "C+" : 2.5, "C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}

sum = 0

sum_all = 0

for i in range(20):

    x, a, b = map(str,input().split())

    if b == "P":

        continue

    else:

        sum_all += dic[b]*float(a)

        sum += float(a)

print(sum_all / sum)