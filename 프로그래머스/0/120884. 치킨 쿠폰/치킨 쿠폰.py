def solution(chicken):
    answer = 0
    while chicken >= 10:
        answer += chicken // 10
        p = chicken % 10
        chicken //= 10
        chicken += p
    return answer