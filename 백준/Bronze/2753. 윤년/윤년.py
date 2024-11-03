a = int(input(""))
if(((a % 4 == 0) & ((a % 100 != 0) | (a % 400 == 0))) == True):
    print("1")
else:
    print("0")