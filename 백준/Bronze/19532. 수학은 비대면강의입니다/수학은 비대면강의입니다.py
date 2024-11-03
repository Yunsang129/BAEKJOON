a,b,c,d,e,f = map(int,input().split())
try:
    for x in range(-999, 1000, 1):
        for y in range(-999, 1000, 1):
            if(a * x + b * y == c):
                if(d * x + e * y == f):
                    print(x,y)
                    raise
except:
    pass