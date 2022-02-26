n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]
dp = [1 for i in range(n)]
line.sort()

for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1

print(n - max(dp))

