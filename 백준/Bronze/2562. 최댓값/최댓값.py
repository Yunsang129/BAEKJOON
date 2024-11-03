import sys
max = 0
num = None
for i in range(9):
    n = int(input())
    if n > max:
        max = n
        num = i + 1
print(max)
print(num)