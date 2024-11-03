n = int(input())

lst = list(map(int,input().split()))

count = 0

for num in lst:

    if num == 1 :

        continue

    for i in range(num - 1):

        if num == (i + 2):

            count += 1

        if num % (i + 2) == 0:

            break

print(count)  
        
            