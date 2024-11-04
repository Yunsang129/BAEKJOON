def solution(numLog):
    ans = ""
    dn = {-1 : "w", 1 : "s", -10 : "d", 10 : "a"}
    for i in range(len(numLog) - 1):
        ans += dn[numLog[i] - numLog[i+1]]
    return ans