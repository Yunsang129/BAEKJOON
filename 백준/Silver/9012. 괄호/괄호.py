n = int(input())

for _ in range(n):

    lst = []

    st = input()

    for i in range(len(st)):

    

        if len(lst) == 0:

            lst.append(st[i])

        elif lst[-1] =="(" and st[i] ==")":

            lst.pop()

        

        else:

            lst.append(st[i])

            

 

    if len(lst) == 0:

        print("YES")

    else:

        print("NO")

