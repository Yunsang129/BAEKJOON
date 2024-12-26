def solution(rank, attendance):
    possible_list = []
    for i in range(len(rank)):
        if attendance[i] == True:
            possible_list.append(rank[i])
    possible_list.sort()
    possible_list.reverse()
    
    return 10**4 * rank.index(possible_list.pop()) + 10**2 * rank.index(possible_list.pop()) + rank.index(possible_list.pop())