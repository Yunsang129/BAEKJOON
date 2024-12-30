def solution(array, n):
    dis_arr = []
    array.sort()
    for num in array:
        dis_arr.append(abs(n - num))
    return array[dis_arr.index(min(dis_arr))]