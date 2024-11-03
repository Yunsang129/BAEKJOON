n = int(input())
sum = 0.0
grade = list(map(int,input().split()))
max = 0.0
for i in range(len(grade)):
    if(max < grade[i]):
        max = grade[i]
for j in range(len(grade)):
    sum += grade[j] * 100 / max
print(sum/len(grade))