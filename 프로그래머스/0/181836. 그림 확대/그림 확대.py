def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        new_sentence = ""
        for ch in picture[i]:
            new_sentence += ch * k
            
        for _ in range(k): answer.append(new_sentence)        
    return answer