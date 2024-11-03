n = int(input())
num = 1
sum = 0
while True:
    if n <= sum:
        num -= 1
        n -= (sum - num)
        break
    sum += num
    num += 1
if(num % 2 == 0):
    print("{}/{}".format(n,num - n + 1))
else:
    print("{}/{}".format(num - n + 1, n))