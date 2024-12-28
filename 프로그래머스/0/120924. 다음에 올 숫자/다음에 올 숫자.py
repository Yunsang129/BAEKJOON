def solution(common):
    d = common[1] - common[0]
    if common[0] != 0:
        p = common[1] // common[0]
    else:
        p = None
    if common[1] + d == common[2]:
        return common[-1] + d
    elif common[1] * p == common[2]:
        return common[-1] * p