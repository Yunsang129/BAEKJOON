n = int(input())
nums = list(map(int,input().split()))
v = int(input())
sum = 0
for i in range(n):
    if (nums[i] == v):
        sum += 1
print(sum)