def query(person, price, tree, money):
    
    price10 = price // 10
    money[person] += price - price10
    
    if price10 == 0:
        return
    
    if tree[person] == "-":
        return
    
    query(tree[person], price10, tree, money)
    
    return
    
def solution(enroll, referral, seller, amount):
    tree = dict()
    money = dict()
    
    money['-'] = 0
    for parent, child in zip(referral, enroll):
        tree[child] = parent
    
    for en_per in enroll:
        money[en_per] = 0
    
    for person, price in zip(seller, amount):
        query(person, price * 100, tree, money)
    
    result = [money[person] for person in enroll]
    return result