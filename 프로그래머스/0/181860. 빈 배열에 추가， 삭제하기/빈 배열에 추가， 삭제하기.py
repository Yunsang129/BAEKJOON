def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i] is True:
            for _ in range(2*arr[i]):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                answer.pop()
        
    return answer