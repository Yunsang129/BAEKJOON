while True:

    n = int(input())

    sum = 0

    if n == -1:

        break

    lst = []

    for i in range(n-1):

        if n % (i+1) == 0:

            lst.append(i+1)

            sum += i+1

    if sum == n:

        print(n,"="," + ".join(map(str,lst)))

    else:
        print(n, "is NOT perfect.")