sum = int(input())
n = int(input())
presum = 0
for i in range(n):
    a, b = map(int, input().split())
    presum += a*b
if(presum == sum):
    print("Yes")
else:
    print("No")