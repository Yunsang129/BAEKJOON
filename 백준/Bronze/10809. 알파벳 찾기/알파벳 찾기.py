string = input()
for i in "abcdefghijklmnopqrstuvwxyz":
    if i not in string:
        print(-1,end = " ")
    else:
        for s in range(len(string)):
            if i == string[s]:
                print(s, end = " ")
                break