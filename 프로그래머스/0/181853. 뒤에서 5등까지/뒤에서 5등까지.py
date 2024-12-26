def solution(num_list):
    answer = []
    lst = sorted(num_list, reverse = True)
    for _ in range(5): answer.append(lst.pop())
    return answer