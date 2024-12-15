def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if is_suffix == "".join(list(my_string)[len(my_string) - i - 1:]):
            return 1
    return 0