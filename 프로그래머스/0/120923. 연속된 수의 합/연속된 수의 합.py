def solution(num, total):
    if num % 2 == 1:
        middle = total // num    
        return [x for x in range(middle - num // 2, middle + num //2 + 1)]
    else:
        n = (total * 2 // num - num) // 2 + 1
        return [x for x in range(n,n+num)]