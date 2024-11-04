def solution(code):
    ret = ""
    mode = 0
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == "1":
                mode = 1
            elif idx % 2 == 0:
                ret += code[idx]
                
        else:
            if code[idx] == "1":
                mode = 0
            elif idx % 2 != 0:
                ret += code[idx]
                
    answer = ''.join(ret)
    if len(answer) == 0:
        answer = "EMPTY"
    return answer