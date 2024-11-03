a,b,c = map(int,input().split())
if(a == b == c):
    print(10000 + 1000 * a)
elif(a == b or a == c or b == c):
    if(a == b):
        print(1000 + 100 * a)
    else:
        print(1000 + 100 * c)
else:
    if(a > b and a > c):
        print(100 * a)
    elif(b > a and b > c):
        print(100 * b)
    else:
        print(100 * c)