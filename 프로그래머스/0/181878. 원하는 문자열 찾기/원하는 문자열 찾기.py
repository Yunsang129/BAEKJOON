def solution(myString, pat):
    myString = myString.upper()
    pat = pat.upper()
    n = 0
    while len(myString) >= n + len(pat):
        if myString[n:n + len(pat)] == pat[:]:
            return 1
        n += 1
    return 0
            