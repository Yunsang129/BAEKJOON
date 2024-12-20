def solution(myString, pat):
    if myString[-len(pat):] == pat:
            return myString[:]
    n = 1
    while True:
        if myString[-len(pat) - n : -n] == pat:
            return myString[: -n]
        n += 1