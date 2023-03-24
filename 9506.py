while True:
    n = int(input())
    if n == -1 : break;
    n_list = []
    n_cnt = 0
    for i in range(1, n):
        if n % i == 0:
            n_cnt += i
            n_list.append(i)
    if n_cnt == n:
        print(f'{n} =', end=' ')
        print(*n_list, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')