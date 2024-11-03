def solution(a, b):
    answer = int(str(a) + str(b)) if int(str(a) + str(b)) >= 2 * a * b else 2* a* b
    return answer