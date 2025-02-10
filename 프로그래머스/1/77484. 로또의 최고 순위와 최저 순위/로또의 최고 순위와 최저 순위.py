def solution(lottos, win_nums):
    dic = {
           6 : 1,
           5 : 2,
           4 : 3,
           3 : 4,
           2 : 5,
           1 : 6,
           0 : 6
          }
    correct = 0
    zero = 0
    for num in lottos:
        if num in win_nums:
            correct += 1
        elif num == 0:
            zero += 1
    return dic[correct + zero], dic[correct]