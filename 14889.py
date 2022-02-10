import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if started[i] and started[j]:
                    start += arr[i][j]
                elif not started[i] and not started[j]:
                    link += arr[i][j]
        ans = min(ans, abs(start - link))

    for i in range(idx, n):
        if started[i]:
            continue
        started[i] = True
        dfs(i + 1, cnt + 1)
        started[i] = 0

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

started = [0 for _ in range(n)]
ans = sys.maxsize
dfs(0,0)
print(ans)