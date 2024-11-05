def solution(number):
    answer = 0
    for s in number:
        answer += int(s)
        
    return answer % 9