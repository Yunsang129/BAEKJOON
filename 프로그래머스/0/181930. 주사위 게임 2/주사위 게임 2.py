def solution(a, b, c):
    answer = 1
    if a != b  and b!=c and a!=c:
        answer = (a+b+c)
    elif a == b == c:
        for n in range(3):
            answer *= (a**(n+1) + b**(n+1) + c**(n+1))
    else:
        for n in range(2):
            answer *= (a**(n+1) + b**(n+1) + c**(n+1))
    return answer