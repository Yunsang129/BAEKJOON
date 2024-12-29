def solution(num_list):
    sum = 0
    mul_sum = 1
    for num in num_list:
        mul_sum *= num
        sum += num
    return 1 if mul_sum < sum ** 2 else 0