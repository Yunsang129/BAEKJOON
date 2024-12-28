def solution(n):
    answer = []
    for i in range(n):
        sentence = []
        for j in range(n):
            sentence.append(1) if i == j else sentence.append(0)
        answer.append(sentence)
    return answer