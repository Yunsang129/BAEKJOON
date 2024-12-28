def solution(quiz):
    answer = []
    for q in quiz:
        q_list = q.split()
        if operator(int(q_list[0]), int(q_list[2]), q_list[1]) == int(q_list[4]):
            answer.append("O")
        else:
            answer.append("X")
    return answer

def operator(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2