def solution(ineq, eq, n, m):
    if eq == "=":
        if n == m:
            return 1
    
    if ineq == ">":
        return 1 if n > m else 0
    else:
        return 1 if n < m else 0