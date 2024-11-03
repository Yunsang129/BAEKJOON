import sys
from collections import deque
queue = deque([])
n = int(input())
for i in range(n):
    s = sys.stdin.readline().strip().split()
    if s[0] == 'push':
        queue.append(s[1])
    elif s[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif s[0] == 'size':
        print(len(queue))
    elif s[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif s[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    