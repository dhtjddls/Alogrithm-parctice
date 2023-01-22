for _ in range(3):
    cnt = 0
    jjak = list(map(int, input().split()))

    cnt = jjak.count(0)
    if cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')
    else:
        print('E')
        