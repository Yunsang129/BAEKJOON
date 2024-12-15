def solution(n, slicer, num_list):
    answer = []
    if (n == 1):
        slicer[0] = 0
        slicer[2] = 1
        
    elif n == 2:
        slicer[1] = len(num_list) -1 
        slicer[2] = 1
        
    elif n == 3:
        slicer[2] = 1
        
        
    for i in range(slicer[0], slicer[1] + 1, slicer[2]):
            answer.append(num_list[i])
    return answer