def solution(l, r):
    answer = []
    for i in range(l, r+1):
        try:
            for ch in str(i):
                if ch in "12346789":
                    raise
            answer.append(int(i))
        except:
            continue
    return answer if len(answer) != 0 else [-1]