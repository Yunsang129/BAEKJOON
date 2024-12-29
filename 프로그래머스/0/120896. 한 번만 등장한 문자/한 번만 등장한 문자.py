def solution(s):
    answer = []
    num_arr = [0 for _ in range(26)]
    for i in range(len(s)):
        num_arr[ord(s[i]) - 97] += 1
    for i in range(26):
        if num_arr[i] == 1:
            answer.append(chr(i + 97))
    return "".join(sorted(answer))