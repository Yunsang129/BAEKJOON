def solution(bin1, bin2):
    answer = int(bin1,2) + int(bin2, 2)
    answer = bin(answer)
    return answer[2:]