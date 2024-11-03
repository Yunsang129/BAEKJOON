def rev(num):
    re_num = ""
    for i in range(len(num)):
        re_num += num[len(num) - i - 1]
    return re_num

a,b = map(str, input().split())
a = rev(a)
b = rev(b)
if(int(a) > int(b)):
    print(a)
else:
    print(b)