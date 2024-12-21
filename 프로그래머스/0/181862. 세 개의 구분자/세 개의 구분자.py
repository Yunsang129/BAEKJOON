def solution(myStr):
    myStr = myStr.replace("a", " ").replace("b", " ").replace("c", " ")
    myStr = myStr.split()
    if not myStr:
        return ["EMPTY"]
    return myStr
        