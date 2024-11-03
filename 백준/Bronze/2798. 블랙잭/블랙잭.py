def pan(sum, recent_sum):
    if(sum > goal):
        return recent_sum
    elif(sum < recent_sum):
        return recent_sum
    else:
        return sum
sum = 0
n, goal = map(int,input().split())
num = list(map(int,input().split()))
for i in range(n):    
    for j in range(n):
        if(j == i):
            continue
        for k in range(n):
            if(k == j or k == i):
                continue
            sum = pan(num[i] + num[j] + num[k], sum)   
print(sum)