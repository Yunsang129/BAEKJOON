def num(n):
    f = 4
    for i in range(n+1):
        f +=  2 ** (2*i) + 2**(2*i+1) + 2**(i+1)
    return f
n = int(input())


print(num(n-1))