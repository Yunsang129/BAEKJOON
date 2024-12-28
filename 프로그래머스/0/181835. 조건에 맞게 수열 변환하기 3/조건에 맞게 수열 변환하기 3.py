def solution(arr, k):
    answer = []
    for n in arr:
        if k % 2 == 1:
            n *= k
        else:
            n += k
        answer.append(n)
    return answer