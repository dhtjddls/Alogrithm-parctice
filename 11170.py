t = int(input())
for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    for i in range(n, m+1):
        for i in str(i):
            if i == '0':
                cnt += 1
    print(cnt)