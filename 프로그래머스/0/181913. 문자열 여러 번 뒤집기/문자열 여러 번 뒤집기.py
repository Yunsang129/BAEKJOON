def solution(my_string, queries):
    for x, y in queries:
        my_string = my_string[0:x] + "".join(reversed(list(my_string[x: y+1]))) + my_string[y+1:]
    print(my_string)
    return my_string
#split으로는 문자열을 리스트로 바꿀 수 없음 list()바로 쓰기