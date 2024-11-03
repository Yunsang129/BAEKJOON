n = int(input())

m = int(input())

result = []

lst = [i for i in range(n, m+1)]

for num in lst:

    for j in range(1,num):

        if j + 1   == num:

            result.append(num)

        if num % (j + 1) == 0:

            break

if result:

    print(sum(result))

    print(result[0])

else:

    print(-1)