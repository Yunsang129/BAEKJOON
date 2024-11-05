def solution(a, b, c, d):
    lst = [a,b,c,d]
    count = [0,0,0,0,0,0]
    for i in lst:
        count[i - 1] += 1
    if 4 in count:
        return 1111 * (count.index(4) + 1 )
    elif 3 in count:
        return (10 * (count.index(3) + 1) + (count.index(1) + 1)) ** 2
    elif 2 in count:
        if 1 in count:
            num = count.index(1) + 1
            count[count.index(1)] = 0
            n = count.index(1) + 1
            return num * n
        else:
            num1 = count.index(2) + 1
            count[count.index(2)] = 0
            num2 = count.index(2) + 1
            return abs((num1 + num2) * (num1 - num2)) 
    else:
        return min(lst)