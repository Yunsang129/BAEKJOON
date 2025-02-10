from collections import deque
def solution(enroll, referral, seller, amount):
    q = deque()
    dict = {}
    for i in range(len(enroll)):
        dict[enroll[i]] = i
        
    lst = [[] for _ in range(len(enroll))]
    result = [0] * len(enroll)
    
    for enroll_num in range(len(referral)):
        if referral[enroll_num] in enroll:
            lst[enroll_num].append(referral[enroll_num])
            
    q.append((dict.get(people), profit))
    
    while q:
        people_num, profit = q.popleft()
        result[people_num] += (profit - profit // 10)
        for upper in lst[people_num]:
            q.append((dict.get(upper), profit // 10))

    for seller_num in range(len(seller)):
        profit(enroll, seller[seller_num], amount[seller_num] * 100, result, lst)
        
    return result
        