def solution(intStrs, k, s, l):
    answer = []
    for e in intStrs:
        num = int("".join(list(e[s : s + l])))
        if num > k:
            answer.append(num)

    return answer