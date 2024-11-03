from collections import deque
n, k = map(int, input().split())
queue = deque([i + 1 for i in range(n)])
lst = []
while len(lst) != n:
    for i in range(k-1):
        queue.append(queue.popleft())
    lst.append(queue.popleft())
print("<" + ", ".join(map(str,lst)) + ">")