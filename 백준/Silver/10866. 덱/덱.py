from collections import deque
import sys
queue = deque([])
n = int(input())
for i in range(n):
    s = sys.stdin.readline().strip().split()
    if s[0] == 'push_front':
        queue.appendleft(s[1])
    elif s[0] == 'push_back':
            queue.append(s[1])
    elif s[0] == 'pop_front':
        print(-1 if len(queue) == 0 else queue.popleft())
    elif s[0] == 'pop_back':
        print(-1 if len(queue) == 0 else queue.pop())
    elif s[0] == 'size':
        print(len(queue))
    elif s[0] == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif s[0] == 'front':
        print(-1 if len(queue) == 0 else queue[0])
    elif s[0] == 'back':
         print(-1 if len(queue) == 0 else queue[-1])