def solution(arr, query):
    for n in range(len(query)):
        if n % 2 == 0:
            del arr[query[n] + 1:]
        else:
            del arr[:query[n]]
    return arr
