def solution(arr, queries):
    for q in range(len(queries)):
        arr[queries[q][0]], arr[queries[q][1]] = arr[queries[q][1]],  arr[queries[q][0]]
    return arr