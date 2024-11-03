paper = [["W" for _ in range(100)]for _ in range(100)]
n = int(input())
count = 0
for i in range(n):
    a,b = map(int,input().split())
    for i in range(b,b+10,1):
        for j in range(a,a+10,1):
            paper[j][i] = "B"
for i in range(100):
    for j in range(100):
        if(paper[j][i] == "B"):
            count += 1
print(count)