def solution(my_string, n):
    answer = ''.join(list(my_string)[len(my_string) - n:])
    return answer