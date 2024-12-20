def solution(str_list):
    s_index = None
    for s in str_list:
        if s == "l":
            return str_list[:str_list.index(s)]
        elif s == "r":
            return str_list[str_list.index(s) + 1:]
    return []   