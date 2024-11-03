d_x = []
d_y = []
for i in range(3):
    x,y = map(int,input().split())
    if d_x and x in d_x:
        d_x.remove(x)
    else:
        d_x.append(x)
    if d_y and y in d_y:
        d_y.remove(y)
    else:
        d_y.append(y)
print(d_x[0],d_y[0])
        
        