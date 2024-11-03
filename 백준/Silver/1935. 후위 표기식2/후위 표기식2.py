n = int(input())
st = input()
lst = []
stack = []
o = [i for i in range(n)]
for _ in range(n):
    lst.append(input())
lst.reverse()
for j in range(n):
    o[j] = lst.pop()
    
for c in st:
    if c == "+":
        stack.append(float(stack.pop())+(float(stack.pop())))
    elif c == "*":
        stack.append(float(stack.pop())*(float(stack.pop())))
    elif c == "/":
        stack.append(1 / float(stack.pop())*(float(stack.pop())))
    elif c == "-":
        stack.append(-float(stack.pop())+(float(stack.pop())))
    else:
        stack.append(o[ord(c) - 65])
print("{:.2f}".format(stack[0]))