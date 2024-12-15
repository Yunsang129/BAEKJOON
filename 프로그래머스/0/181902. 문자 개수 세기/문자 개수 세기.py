def solution(my_string):
    answer = [0] * 52
    for i in range(len(my_string)):
        num = ord(my_string[i])
        if num > 91:
            num -= 6
        num -= 65
        answer[num] += 1
        
    return answer