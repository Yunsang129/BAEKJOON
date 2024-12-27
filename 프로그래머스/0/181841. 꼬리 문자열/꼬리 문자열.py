def solution(str_list, ex):
    result_list = str_list[:]
    for i in range(len(str_list)):
        if ex in str_list[i]:
            result_list.remove(str_list[i])
    return "".join(result_list)