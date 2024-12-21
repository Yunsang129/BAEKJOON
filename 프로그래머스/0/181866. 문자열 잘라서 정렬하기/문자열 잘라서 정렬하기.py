def solution(myString):
    myString = myString.split("x")
    while "" in myString:
        myString.remove("")
    return sorted(myString)