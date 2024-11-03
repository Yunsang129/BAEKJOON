n = int(input())
room = 1
i = 0
num = 1
while(True):
    if(n <= num):
        print(room)
        break
    num += 6*(i+1)
    i +=1
    room += 1