def solution(my_strings, parts):
    answer = ""
    for n in range(len(my_strings)):
        answer += "".join(my_strings[n][parts[n][0]:parts[n][1] + 1])
    return answer