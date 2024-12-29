def solution(s1, s2):
    answer = 0
    for e in s1:
        for e_s2 in s2:
            if e == e_s2:
                answer += 1
    return answer