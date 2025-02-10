def solution(id_list, report, k):
    report = list(set(report))
    result = [0] * len(id_list)
    
    reported_person = dict()
    
    for id in id_list:
        reported_person[id] = []
        
    
    for r in report:
        user, reported_user = r.split(" ")
        reported_person[reported_user].append(user)
    
    for reported_user, report_user_list in reported_person.items():
        if len(report_user_list) >= k:
            for user in report_user_list:
                result[id_list.index(user)] += 1
    return result
    