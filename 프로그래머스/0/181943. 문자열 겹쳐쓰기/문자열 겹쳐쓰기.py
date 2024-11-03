def solution(my_string, overwrite_string, s):
    st = list(my_string)
    answer = my_string[0:s] + overwrite_string + "".join(st[s + len(overwrite_string):])
    return answer