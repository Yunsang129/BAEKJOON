def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append("".join(list(my_string[len(my_string) - i - 1:])))
    answer.sort()
    return answer