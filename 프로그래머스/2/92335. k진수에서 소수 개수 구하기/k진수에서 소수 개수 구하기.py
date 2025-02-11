import math
def trans(n, k):
    result = ""
    while True:
        result = str(n % k) + result
        if n <= k:
            return result
        n -= n % k
        n //= k

def is_divisor(n):
    if n == "" or n == "1":
        return False
    n = int(n)
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    num = trans(n, k)
    cnt = 0
    st = ""
    for n in num:
        if n == "0":
            if is_divisor(st):
                cnt += 1
            st = ""
        else:
            st += n
    if is_divisor(st):
        cnt += 1
    return cnt
