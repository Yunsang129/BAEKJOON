def solution(A, B):
    result = 0
    while True:
        if A != B:
            result += 1
        else:
            return result
        if result >= len(A):
            return -1
        A = push_ch(A)

def push_ch(string):
    return string[-1] + string[:-1]