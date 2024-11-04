def solution(n, control):
    for dn in control:
        if dn == "w":
            n += 1
        elif dn == "s":
            n -= 1
        elif dn =="d":
            n += 10
        else:
            n -= 10
    return n