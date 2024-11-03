import sys
stack = []
n = int(sys.stdin.readline())
for i in range(n):
    c = sys.stdin.readline().split()
    st = c[0]
    
    if(st == 'push'):
        stack.append(c[1])
        
    elif(st == 'pop'):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif(st == 'size'):
        print(len(stack))
    elif(st == 'empty'):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(st == 'top'):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])